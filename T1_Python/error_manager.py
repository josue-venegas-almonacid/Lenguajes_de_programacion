def log_error(id, *par):
    """
    log_error
    ——————–
    Entradas:
    (entero) numero de error
    (lista) contiene una tupla con las palabras involucradas
    ——————–
    Salida:
    (None) Output: No retorna nada
    ——————–
    La funcion se encarga de mostrar un codigo de error junto con una breve
    descripcion
    """
    # RESUMEN: Funcion auxiliar. Imprime el error encontrado
    # INPUT: id = Numero del error,
    #       *par = Parametros del error. determinados solo en ejecucion
    # RETURN: Nada. Imprime el error encontrado

    errors = {0: "[Error 0] Instruccion invalida",
              1: "[Error 1] Elemento '{}' no esperado despues de '{}'",
              2: "[Error 2] Elemento '{}' no esperado",
              3: "[Error 3] Se esperaba '{}' despues de '{}'",
              4: "[Error 4] Una sentencia no puede iniciar con '{}'",
              5: "[Error 5] La tabla '{}' ya existe",
              6: "[Error 6] La tabla '{}' no existe",
              7: "[Error 7] La tabla no es valida",
              8: "[Error 8] La cantidad de datos no corresponde a la cantidad de columnas",
              9: "[Error 9] No existe la columna '{}' en la tabla '{}'",
    }
    if id in errors:
        print(errors[id].format(*par))
