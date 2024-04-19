from error_manager import log_error
import collections
import re


Token = collections.namedtuple('Token', ['type', 'value', 'column'])


class TokenNode:
    Start = []
    End = []
    Values = []
    From = []
    To = []

    def __init__(self, start, end, values, From, to):
        """
        __init__
        ——————–
        Entradas:
        (lista) Hoja con la que el Token debe partir en el parser
        (lista) Hoja con la que debe terminar el Token en el parser
        (lista) Hojas que son admitidas en el Token
        (lista) Tokens del cual el actual token puede venir
        (lista) Tokens que le siguen al actual token
        ——————–
        Salida:
        (lista) Output: Retorna los mismos tokens, en caso de error retorna None
        ——————–
        Se encarga de verificar la sintaxis siguiendo un seudo arbol sintactico.
        """
        self.Start = start
        self.End = end
        self.Values = values
        self.From = From
        self.To = to


def is_valid(token, space):
    """
    is_valid
    ——————–
    Entradas:
    (Token) Token el cual sera buscado en el espacio dado
    (diccionario) Espacio donde debe ser buscado el 'token'
    ——————–
    Salida:
    (lista) Output: Retorna los mismos tokens, en caso de error retorna None
    ——————–
    Se encarga de verificar la sintaxis siguiendo un seudo arbol sintactico.
    """
    return token.type != "" and token.type in space


def parser(tokens):
    """
    parser
    ——————–
    Entradas:
    (lista) lista con objetos 'Tokens' los cuales contienen informacion
    para ser procesada
    ——————–
    Salida:
    (lista) Output: Retorna los mismos tokens, en caso de error retorna None
    ——————–
    Se encarga de verificar la sintaxis siguiendo un seudo arbol sintactico.
    """
    # RESUMEN: Arbol sintactico para el reconocimiento de instrucciones validas.
    # Los nodos corresponden a sentencias no terminales, denominados CONTEXTOS,
    # mientras que las hojas corresponden a sentencias terminales. Cada contexto
    # admite tokens especificos, dispuestos necesariamente al comienzo ("START"),
    # necesariamente al final ("END") o en otra posicion ("VALUES"); y tambien
    # contextos vecinos especificos, donde "TO" simboliza los contextos que pueden
    # suceder al contexto actual, y "FROM" especifica los contextos de los cuales
    # el actual puede proceder. Similarmente, cada hoja dispone una relacion de
    # tokens disponibles que antecedan o sucedan al actual
    # INPUT: tokens = string enviado por tokenizer()
    # RETURN: Nada. En caso de error, lo imprime.

    # TOKEN NODE ('START', 'END', 'VALUES', 'FROM', 'TO')
    nodos = {
        "SELECT": TokenNode(["ID", "AST"], ["ID", "AST"], ["ID", "COMMA", "AST"], [""], ["FROM"]),
        "FROM": TokenNode(["ID"], ["ID"], ["ID"], ["SELECT"], ["INNER", "WHERE", "ORDER", ";"]),
        "INNER": TokenNode([""], [""], [""], ["FROM"], ["JOIN"]),
        "JOIN": TokenNode(["ID"], ["ID"], ["ID"], ["INNER"], ["WHERE"]),
        "WHERE": TokenNode(["ID"], ["STRING", "NUMBER", "IDVALUE"], ["ID", "IDVALUE", "ASSIGN", "STRING", "NUMBER"], ["FROM", "JOIN", "SET"], ["ORDER", "AND", "OR", ";"]),
        "AND": TokenNode(["ID"], ["STRING", "NUMBER", "IDVALUE"], ["ID", "IDVALUE", "ASSIGN", "STRING", "NUMBER"], ["WHERE", "AND", "OR"], ["OR", "AND", "ORDER", ";"]),
        "OR": TokenNode(["ID"], ["STRING", "NUMBER", "IDVALUE"], ["ID", "IDVALUE", "ASSIGN", "STRING", "NUMBER"], ["WHERE", "AND", "OR"], ["OR", "AND", "ORDER", ";"]),
        "ORDER": TokenNode([""], [""], [""], ["FROM", "WHERE", "AND", "OR"], ["BY"]),
        "BY": TokenNode(["ID"], ["ID"], ["ID"], ["ORDER"], ["ASC", "DESC"]),
        "ASC": TokenNode([""], [""], [""], ["BY"], [";"]),
        "DESC": TokenNode([""], [""], [""], ["BY"], [";"]),


        "INSERT": TokenNode([""], [""], [""], [""], ["INTO"]),
        "INTO": TokenNode(["ID"], ["RIGHTPAR"], ["ID", "LEFTPAR", "COMMA", "RIGHTPAR"], ["INSERT"], ["VALUES"]),
        "VALUES": TokenNode(["LEFTPAR"], ["RIGHTPAR"], ["LEFTPAR", "STRING", "NUMBER", "COMMA", "RIGHTPAR"], ["INTO"], [";"]),


        "UPDATE": TokenNode(["ID"], ["ID"], ["ID"], [""], ["SET"]),
        "SET": TokenNode(["IDSET"], ["STRING", "NUMBER"], ["IDSET", "ASSIGN", "STRING", "NUMBER", "COMMA"], ["UPDATE"], ["WHERE"]),

        ";": TokenNode([""], [";"], [""], ["FROM", "WHERE", "AND", "OR", "ASC", "DESC", "VALUES"], [""])
    }

    hojas = {
        "ID": {"LVALUES": ["COMMA", "LEFTPAR"], "RVALUES": ["COMMA", "ASSIGN", "LEFTPAR", "RIGHTPAR"]},
        "AST": {"LVALUES": [""], "RVALUES": [""]},
        "COMMA": {"LVALUES": ["ID", "STRING", "NUMBER"], "RVALUES": ["ID", "STRING", "NUMBER", "IDSET"]},
        "ASSIGN": {"LVALUES": ["ID", "IDSET"], "RVALUES": ["STRING", "NUMBER", "IDVALUE"]},
        "STRING": {"LVALUES": ["COMMA", "ASSIGN", "LEFTPAR"], "RVALUES": ["COMMA", "RIGHTPAR"]},
        "NUMBER": {"LVALUES": ["COMMA", "ASSIGN", "LEFTPAR"], "RVALUES": ["COMMA", "RIGHTPAR"]},

        "IDSET": {"LVALUES": ["COMMA"], "RVALUES": ["ASSIGN"]},
        "IDVALUE": {"LVALUES": ["ASSIGN"], "RVALUES": [""]},

        "LEFTPAR": {"LVALUES": ["ID"], "RVALUES": ["ID", "STRING", "NUMBER"]},
        "RIGHTPAR": {"LVALUES": ["ID", "STRING", "NUMBER"], "RVALUES": [""]},
    }

    context = Token("", "", "")
    last_token = Token("", "", "")
    for token in tokens:
        type = token.type
        if type in nodos:
            condition1 = last_token == Token("", "", "") and "" in nodos[type].From
            condition2 = context != Token("", "", "") and type in nodos[context.type].To and context.type in nodos[type].From
            condition3 = (last_token.type in hojas and last_token.type in nodos[context.type].End) or (context != Token("", "", "") and "" in nodos[context.type].End) # (last_token.type in nodos)

            if condition1 or (condition2 and condition3):
                context = token
            else:
                if not condition2 or not condition3:
                    log_error(1, token.value, context.value)
                elif not condition1:
                    log_error(4, token.value)
                return
        else:
            condition1 = context != Token("", "", "")
            condition2 = last_token != Token("", "", "")
            condition3 = (condition1 and condition2 and last_token.type == context.type and type in nodos[context.type].Start) or (condition1 and condition2 and last_token.type != context.type)
            condition4 = condition1 and type in nodos[context.type].Values
            condition5 = (condition2 and last_token.type in hojas and type in hojas[last_token.type]["RVALUES"] and last_token.type in hojas[type]["LVALUES"]) or (condition2 and last_token.type in nodos)

            if not(condition1 and condition2 and condition3 and condition4 and condition5):
                log_error(1, token.value, last_token.value)
                return
        last_token = token

    valid_context = is_valid(context, nodos)
    context_can_end = valid_context and "" in nodos[context.type].To
    valid_last_token = is_valid(last_token, hojas) or is_valid(last_token, nodos)
    last_token_is_keyword = valid_last_token and last_token.type in nodos
    last_token_can_end = valid_last_token and valid_context and last_token.type in nodos[context.type].End

    if not valid_context or not context_can_end or not last_token_can_end:
        if valid_context and valid_last_token and last_token_is_keyword and not last_token.type in nodos[context.type].Start:
            log_error(3, ", ".join('%s' % key for key in nodos[last_token.type].Start), last_token.value)
        elif not last_token_can_end and valid_last_token:
            log_error(3, ", ".join('%s' % key for key in list(set(hojas[last_token.type]["RVALUES"]) & set(nodos[context.type].Values))), last_token.value)
        elif valid_context and not context_can_end:
            log_error(3, ", ".join('%s' % key for key in nodos[context.type].To), last_token.value)
        else:
            log_error(0)
        return
    return tokens


def tokenizer(code):
    """
    tokenizer
    ——————–
    Entradas:
    (string) string ingresado por el usuario
    ——————–
    Salida:
    (None) Output: No retorna nada
    ——————–
    Reconocedor de tokens. Analiza cada palabra de la instruccion
    enviada por el usuario y lo clasifica en funcion de la expresion regular
    coincidente. Las palabras reservadas por el lenguaje son almacenadas en
    el diccionario keywords
    """
    keywords = {'SELECT', 'FROM', 'INNER', 'JOIN', 'WHERE', 'ORDER', 'BY',
    'INSERT', 'INTO', 'VALUES', 'UPDATE', 'SET', 'AND', 'OR', 'ASC', 'DESC', ';'}

    tokens = {
    'NUMBER':       r'\d+(\.\d*)?',                 # Int o float
    'STRING':       r'[\'"][\- a-zA-Z0-9_]+[\'"]',  # String
    'ASSIGN':       r'=',                           # Asignacion
    'ID':           r'[\-a-zA-Z0-9_\.]+|;',         # Identificador
    'AST':          r'\*',                          # Caracter 'todas las columnas'
    'SKIP':         r'[ \t]+',                      # Espacios y/o tabulaciones
    'COMMA':        r',',                           # Coma
    'LEFTPAR':      r'\(',                          # Parentesis izquierdo
    'RIGHTPAR':     r'\)',                          # Parentesis derecho
    'MISMATCH':     r'.'                            # Cualquier otro caracter
    }

    tok_regex = ""
    for key in tokens:
        if tok_regex != "":
            tok_regex += '|'
        tok_regex += '(?P<{}>{})'.format(key, tokens[key])

    tokens = []
    keyword = ''
    last_token = Token('', '', '')
    line_start = 0
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        column = mo.start() - line_start
        if kind == 'NUMBER':
            value = float(value) if '.' in value else int(value)
        elif kind == 'ID' and value in keywords:
            kind = value
            keyword = kind
        elif kind == 'SKIP':
            continue
        elif kind == 'ID' and keyword == 'SET':
            kind = 'IDSET'
        elif kind == 'ID' and keyword == 'WHERE' and last_token.type == 'ASSIGN':
            kind = 'IDVALUE'

        last_token = Token(kind, value, column)
        tokens.append(last_token)
    return tokens
