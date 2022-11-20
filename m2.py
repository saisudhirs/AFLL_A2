import lex
import yacc


keywords = ('IF','ELSE')        
tokens = keywords +  (
    'CIO',
    'CIC',
    'CUO',
    'CUC',
    'NUM',
    'COMMA',
    'SP',
    'VAR',
    'LOG'
)

t_IF = r'if'
t_ELSE = r'else'

t_NUM = r'([0-9]*\.[0-9]*)|([0-9]+)'
t_CIO = r'\('
t_CIC = r'\)'
t_CUO = r'\{'
t_CUC = r'\}'
t_COMMA = r'\,'
t_LOG = r'&&|\|\||<|>|<=|>=|==|!='


def t_VAR(s):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if s.value.upper() in keywords:
        s.type = s.value.upper()
    return s


def t_SP(s):
    r"""\s"""
    pass

def p_body(p):
    """body : if 
    | ifelse
    | empty"""
    p[0] = p[1]

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def p_expr(p):
    """expr : NUM
    | VAR
    | func"""

def p_args(p):
    """args : expr
    | expr COMMA args"""

def p_func(p):
    """func : VAR CIO args  CIC"""
    p[0] = p[1]

def p_term(p):
    """term : expr LOG expr 
    | expr
    | CIO term CIC"""
    p[0] = ''

def p_if(p):
    """if : IF CIO term CIC CUO body CUC"""
    p[0] = p[3]

def p_ifelse(p):
    """ifelse : if ELSE CUO body CUC"""

def p_empty(p):
    """empty : """
    pass

def p_error(p):
    print("Syntax error at ", p)
    pass


lexer = lex.lex()
yacc = yacc.yacc(start='body')
try:
    res = yacc.parse("if (f(g(x), 1) && 1) {}", debug=False)
except Exception as  e:
    print("Syntax Error")
