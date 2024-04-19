from error_manager import log_error
import os.path
import operator

class query:
    def query_select(self, tokens):
        """
        query_select
        ——————–
        Entradas:
        (lista) Contiene una tupla por cada token detectado en el parser
        ——————–
        Salida:
        (None) Output: No retorna nada
        ——————–
        La funcion se encarga de guardar y comprobar informacion importante de una instruccion select
        """

        self.params = {}
        # Detectar columnas involucradas en el select
        self.params["columns"] = list()

        i = 1
        for col in tokens:
            if col.type != "FROM":
                if col.type != ",":
                    self.params["columns"].append(col.value)
                i += 1
            else:
                break

        del tokens[0:i]
        self.params["table"] = tokens.pop(0)


        if len(tokens) > 0 and tokens[0].type == "INNER":
            del tokens[0]
            del tokens[0]
            self.params["inner"] = tokens.pop(0)

        i = 1
        if len(tokens) > 0 and tokens[0].type == "WHERE":
            del tokens[0]
            self.params["where"] = list()
            for x in tokens:
                if x.type != "ORDER" and x.type != ";":
                    if x.type != "ASSIGN":
                        self.params["where"].append(x)
                    i += 1
                else:
                    break
        del tokens[0:i]

        if len(tokens) > 0 and tokens[0].type == "BY":
            del tokens[0]
            self.params["order"] = (tokens.pop(0), tokens.pop(0))

    def query_insert(self, tokens):
        """
        query_insert
        ——————–
        Entradas:
        (lista) Contiene una tupla por cada token detectado en el parser
        ——————–
        Salida:
        (None) Output: No retorna nada
        ——————–
        La funcion se encarga de guardar y comprobar informacion importante de una instruccion insert
        """
        del tokens[0]
        self.params = {}
        self.params["table"] = tokens.pop(0)

        # Detectar columnas involucradas en el insert into
        i = 1
        self.params["insert"] = list()
        for col in tokens:
            if col.type != "VALUES":
                if col.type != "LEFTPAR" and col.type != "COMMA" and col.type != "RIGHTPAR":
                    self.params["insert"].append(col)
                i += 1
            else:
                break

        del tokens[0:i]
        # Detectar valores a insertar en cada columna
        self.params["values"] = list()
        for col in tokens:
            if col.type != ";":
                if col.type != "COMMA" and col.type != "LEFTPAR" and col.type != "RIGHTPAR":
                    self.params["values"].append(col)
            else:
                break

    def query_update(self, tokens):
        """
        query_update
        ——————–
        Entradas:
        (lista) Contiene una tupla por cada token detectado en el parser
        ——————–
        Salida:
        (None) Output: No retorna nada
        ——————–
        La funcion se encarga de guardar y comprobar informacion importante de una instruccion update
        """
        self.params = {}
        self.params["table"] = tokens.pop(0)
        del tokens[0]

        i=1
        self.params["set"] = list()
        for id in tokens:
            if id.type != "WHERE":
                if id.type != "ASSIGN" and id.type != "COMMA":
                    self.params["set"].append(id.value)
                i += 1
            else:
                break

        del tokens[0:i]

        self.params["where"] = list()
        for x in tokens:
            if x.type != ";":
                if x.type != "ASSIGN":
                    self.params["where"].append(x)
            else:
                break

    def __init__(self, tokens):
        """
        __init__
        ——————–
        Entradas:
        (lista) Contiene una tupla por cada token detectado en el parser
        ——————–
        Salida:
        (None) Output: No retorna nada
        ——————–
        La funcion se encarga de indentificar que instruccion se va a ejecutar
        """
        self.operacion = tokens.pop(0).type

        if self.operacion == "SELECT":
            self.query_select(tokens)
        elif self.operacion == "INSERT":
            self.query_insert(tokens)
        elif self.operacion == "UPDATE":
            self.query_update(tokens)
        else:
            self.operacion = None
            log_error(0)
            return


class table:
    name = ""

    def __init__(self, name, separator=';'):
        """
        __init__
        ——————–
        Entradas:
        (string) Contiene una tupla por cada token detectado en el parser
        (string) Separador del archivo
        ——————–
        Salida:
        (None) Output: No retorna nada
        ——————–
        La funcion se encarga de cargar una tabla a memoria y asignar parametros basicos
        como nombre, cabeceras y verificar si es una tabla valida
        """
        self.name = name
        file = None
        self.headers = []
        self.data = {}
        self.valid = False

        if os.path.isfile(name + '.csv'):
            file = open(name + '.csv', encoding='utf-8-sig')
        else:
            log_error(6, self.name)
            return
        # Obtenemos la primera linea, la cual contiene las cabeceras
        for header in file.readline().strip().split(separator):
            self.data[header] = list()
            self.headers.append(header)

        # Obtenemos cada dato de las demas lineas y los guardamos en su
        # respectiva columna
        for line in file:
            i = 0
            for cell in line.strip().split(separator):
                if i < len(self.headers):
                    self.data[self.headers[i]].append(cell)
                    i += 1

                else:
                    log_error(8, self.name)
                    return
        self.valid = True

    def value_string(self, value):
        """
        value_string
        ——————–
        Entradas:
        (string) String o numero a verificar
        ——————–
        Salida:
        (string|numero) Output: Retorna un string o un numero
        ——————–
        La funcion se encarga de quitar las comillas de un string, en caso de
        ser un numero no hace nada. Retorna el nuevo valor del string o el mismo
        numero
        """
        if isinstance(value, str) and (value.startswith("\"") or value.startswith("'")):
            if value.startswith("\""):
                return value.strip("\"")
            else:
                return value.strip("'")
        return value

    def where(self, query):
        """
        where
        ——————–
        Entradas:
        (query) Objeto query
        ——————–
        Salida:
        (lista) Output: Retorna una lista con las filas involucradas en el where
        ——————–
        La funcion se encarga de obtener las filas involucradas en un where de
        una sentencia
        """
        table = []
        if "where" in query.params:
            where = []
            columns = []
            for i in range(0, len(query.params["where"]), 3):
                instruction = query.params["where"][i]
                if instruction.value not in self.headers:
                    log_error(9, instruction.value, self.name)
                    return
                value = self.value_string(query.params["where"][i + 1].value)
                op = ""
                if i + 2 < len(query.params["where"]):
                    op = query.params["where"][i + 2].value
                where.append((instruction.value, value, op))
                columns.append(instruction.value)
            for index in range(len(self.data[self.headers[0]])):
                valid = False
                line = []
                for header in self.headers:
                    if header in columns:
                        for condition in where:
                            if condition[0] == header:
                                value = False
                                if condition[1] == self.data[header][index]:
                                    value = True
                                if condition[2] == "AND":
                                    if not valid:
                                        break
                                elif condition[2] == "OR":
                                    if value:
                                        valid = value
                                else:
                                    if value:
                                        valid = value
                if valid:
                    for header in self.headers:
                        line.append(self.data[header][index])
                    table.append((line, index))
        else:
            for index in range(len(self.data[self.headers[0]])):
                line = []
                for header in self.headers:
                    line.append(self.data[header][index])
                table.append((line, index))
        return table

    def order(self, query, tabla):
        """
        order
        ——————–
        Entradas:
        (query) Objeto query
        (lista) Lista de tablas(filas involucradas)
        ——————–
        Salida:
        (lista) Output: Retorna lista de las filas ordenadas
        ——————–
        La funcion se encarga de ordenar las filas a partir de un
        parametro
        """
        desc = False
        if query.params["order"][1].value == "DESC":
            desc = True
        if query.params["order"][0].value not in self.headers:
            log_error(9, query.params["order"][0].value, self.name)
            return
        tabla.sort(key=operator.itemgetter(self.headers.index(query.params["order"][0].value)), reverse=desc)
        return tabla

    def select(self, query):
        """
        select
        ——————–
        Entradas:
        (query) Objeto query
        ——————–
        Salida:
        (None) Output: No retorna nada
        ——————–
        La funcion se encarga de hacer la funcion 'select' de sql.
        """
        # Verificar que todas las sentencias del where (columnas) existan en la tabla
        table = self.where(query)

        if "order" in query.params:
            table = self.order(query, table)
            if table is None:
                return

        if "*" in query.params["columns"]:
            self.print((table, self.headers))
        else:
            selected = []
            for line in table:
                temp_list = list()
                for i, data in enumerate(line[0]):
                    if self.headers[i] in query.params["columns"]:
                        temp_list.append(line[0][i])
                temp = (temp_list, line[1])
                selected.append(temp)
            cols = []
            for x in self.headers:
                if x in query.params["columns"]:
                    cols.append(x)
            self.print((selected, cols))

    def insert(self, query):
        """
        insert
        ——————–
        Entradas:
        (query) Objeto query
        ——————–
        Salida:
        (None) Output: No retorna nada
        ——————–
        La funcion se encarga de hacer la funcion 'insert' de sql.
        """
        if len(query.params["values"]) != len(query.params["insert"]):
            log_error(8)
            return

        columns = []
        for x in query.params["insert"]:
            columns.append(x.value)
        for column in columns:
            if column not in self.headers:
                log_error(9, column, self.name)
                return
        for header in self.headers:
            if header in columns:
                self.data[header].append(self.value_string(query.params["values"][columns.index(header)].value))
            else:
                self.data[header].append("")

        file = open(self.name + '.csv', "w")
        file.write(";".join(self.headers) + "\n")
        for index in range(len(self.data[self.headers[0]])):
            line = []
            for header in self.headers:
                line.append(str(self.data[header][index]))
            file.write(";".join(line) + "\n")
        print("Se ha insertado 1 fila")

    def update(self, query):
        """
        update
        ——————–
        Entradas:
        (query) Objeto query
        ——————–
        Salida:
        (None) Output: No retorna nada
        ——————–
        La funcion se encarga de hacer la funcion 'update' de sql.
        """
        columns = []
        for set in range(0, len(query.params["set"]), 2):
            if query.params["set"][set] not in self.headers:
                log_error(9, query.params["set"][set], self.name)
                return
            columns.append((query.params["set"][set], query.params["set"][set+1]))
        tabla = self.where(query)
        for data in tabla:
            for header in columns:
                self.data[header[0]][data[1]] = self.value_string(header[1])

        file = open(self.name + '.csv', "w")
        file.write(";".join(self.headers) + "\n")
        for index in range(len(self.data[self.headers[0]])):
            line = []
            for header in self.headers:
                line.append(str(self.data[header][index]))
            file.write(";".join(line) + "\n")
        if len(tabla) == 1:
            print("Se ha actualizado 1 fila")
        else:
            print("Se han actualizado {} filas".format(len(tabla)))

    def print(self, tupla):
        """
        print
        ——————–
        Entradas:
        (lista) Lista de filas a imprimir
        ——————–
        Salida:
        (None) Output: No retorna nada
        ——————–
        La funcion se encarga de imprimir (mostrar) las filas despues de una
        seleccion
        """
        data = tupla[0]
        cols = tupla[1]
        # Comprobacion de palabra mas larga
        max_length = 0
        for header in cols:
            if len(header) > max_length:
                max_length = len(header)
        for lista, num in data:
            for dato in lista:
                if len(str(dato)) > max_length:
                    max_length = len(str(dato))

        # Impresion de los datos de manera justificada
        for header in cols:
            print(header, end=" " * (max_length - len(header) + 3))
        print(" ")

        for lista, num in data:
            for dato in lista:
                print(dato, end=" " * (max_length - len(str(dato)) + 3))
            print (" ")

class database:
    def do_query(self, query):
        """
        do_query
        ——————–
        Entradas:
        (query) Objeto query
        ——————–
        Salida:
        (None) Output: No retorna nada
        ——————–
        La funcion se encarga de realizar la query.
        En simples palabras, discrimina que accion se realizara
        """
        tabla = table(query.params["table"].value)
        if tabla is None or not tabla.valid:
            log_error(0)
            return
        if query.operacion == "SELECT":
            tabla.select(query)
        elif query.operacion == "INSERT":
            tabla.insert(query)
        elif query.operacion == "UPDATE":
            tabla.update(query)
