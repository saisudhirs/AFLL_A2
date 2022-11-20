import lex
import yacc

tokens = (
    'CIO',
    'CIC',
    'CUO',
    'CUC',
    'NUM',
    'VAR',
    'COMMA',
    'SP',
    'IF',
    'ELSE'
)

t_NUM = r'([0-9]*\.[0-9]*)|([0-9]+)'
t_VAR = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_CIO = r'\('
t_CIC = r'\)'
t_CUO = r'\{'
t_CUC = r'\}'
t_COMMA = r'\,'
t_IF = 'if'
t_ELSE = 'else'


def t_SP(s):
    r"""\s"""
    pass


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


start = 'if'

lexer = lex.lex()
yacc = yacc.yacc()

res = yacc.parse("if (func()) {}")
print(res)
