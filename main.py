import lex
import yacc

tokens = (
    'IF',
    'THEN',
    'FI',
    'VARIABLE',
    'BRACE_OPEN_SQ',
    'BRACE_CLOSE_SQ',
    'NUMBER',
    'SPACE',
    'EQUAL',
    'NOT_EQUAL',
    'GREATER',
    'LESSER',
    'EQUAL_GREATER',
    'EQUAL_LESSER',
    'BRACE_OPEN_CI',
    'BRACE_CLOSE_CI',
    'COMMA',
    'LOGICAND',
    'LOGICOR',
    'BRACE_OPEN_CU',
    'BRACE_CLOSE_CU',

)

t_NUMBER = r'([0-9]*\.[0-9]*)|([0-9]+)'
t_BRACE_OPEN_SQ = r'\['
t_BRACE_CLOSE_SQ = r'\]'
t_VARIABLE = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_IF = r'if'
t_EQUAL = r'=='
t_NOT_EQUAL = r'!='
t_GREATER = r'>'
t_LESSER = r'<'
t_EQUAL_GREATER = r'>='
t_EQUAL_LESSER = r'<='
t_LOGICOR = r'\|\|'
t_LOGICAND = r'\&\&'
t_BRACE_OPEN_CI = r'\('
t_BRACE_CLOSE_CI = r'\)'
t_COMMA = r'\,'
t_BRACE_OPEN_CU = r'\{'
t_BRACE_CLOSE_CU = r'\}'


def t_SPACE(t):
    r"""\s"""
    pass


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
lexer.input("")


def p_empty(p):
    """empty :"""
    pass


def p_body(p):
    """body : if
    | empty"""
    p[0] = p[1]


def p_if(p):
    """if : IF BRACE_OPEN_CI expr BRACE_CLOSE_CI BRACE_OPEN_CU body BRACE_CLOSE_CU"""
    p[0] = p[2]


def p_item(p):
    """item : NUMBER
            | VARIABLE
            | functioncall
            | BRACE_OPEN_CI term BRACE_CLOSE_CI"""
    p[0] = p[1] if not len(p) > 2 else p[1] + p[2] + p[3]


def p_term(p):
    """term : item connector item
    | item"""
    p[0] = p[1] + p[2] + p[3] if len(p) > 3 else p[1]


def p_args(p):
    """args : item
    | item COMMA args
    | empty"""
    p[0] = p[1] if len(p) < 3 else p[1] + p[2] + p[3]


def p_functioncall(p):
    """functioncall : VARIABLE BRACE_OPEN_CI args BRACE_CLOSE_CI """
    p[0] = p[1] + p[2] + p[3] + p[4]


def p_connector(p):
    """connector : EQUAL
                 | NOT_EQUAL
                 | GREATER
                 | LESSER
                 | EQUAL_GREATER
                 | EQUAL_LESSER"""
    p[0] = p[1]


def p_expr(p):
    """expr : BRACE_OPEN_SQ term BRACE_CLOSE_SQ"""
    p[0] = p[1] + p[2] + p[3]


def p_error(p):
    print("Syntax error in input!")


start = 'body'

parser = yacc.yacc()
result = parser.parse('if ( f(x) ) {}', debug=True)
print(result)
