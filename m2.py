import lex
import yacc


keywords = ('IF','ELSE')        
tokens = keywords +  (
    'CIO',
    'CIC',
    'CUO',
    'CUC',
    'SQO',
    'SQC',
    'STR',
    'NUM',
    'COMMA',
    'SP',
    'VAR',
    'LOG',
    'DOT'
)

t_IF = r'if'
t_ELSE = r'else'

t_NUM = r'([0-9]+\.[0-9]*)|([0-9]+)'
t_CIO = r'\('
t_CIC = r'\)'
t_CUO = r'\{'
t_CUC = r'\}'
t_SQO = r'\['
t_SQC = r'\]'
t_STR = r'(\'.+\')|(\".+\")'
t_COMMA = r'\,'
t_LOG = r'&&|\|\||\<\=|>=|<|>|==|!='
t_DOT = r'\.'

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
    | func
    | STR
    | dotaccess
    | arridx"""

def p_args(p):
    """args : expr
    | expr COMMA args
    | empty"""

def p_arridx(p):
    """arridx : expr SQO expr SQC"""

def p_dotaccess(p):
    """dotaccess : expr DOT VAR"""

def p_func(p):
    """func : expr CIO args CIC"""

def p_term(p):
    """term : term LOG term
    | expr
    | CIO term CIC"""

def p_if(p):
    """if : IF CIO term CIC CUO body CUC"""

def p_ifelse(p):
    """ifelse : if ELSE CUO body CUC"""

def p_empty(p):
    """empty : """
    pass

def p_error(p):
    print("Syntax error at ", p)
    raise(SyntaxError())
    pass


lexer = lex.lex()
yacc = yacc.yacc(start='body')
def validate_str(s):
    try:
        res = yacc.parse(s, debug=False)
    except Exception as  e:
        pass
    else:
        print("Valid string")


def main():
    while (1):
        buf = input()
        if (buf == "quit"):
            return
        print(buf)
        validate_str(buf)

main()

