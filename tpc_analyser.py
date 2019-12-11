import ply.yacc as yacc

from tpc_lexer import tokens

precedence = (
    ('left', 'DIGIT','MI'),
    ('left', 'LOALPHA', 'UPALPHA')
)

def p_message_term(p):
    '''message : message statement
               | statement
               '''
    if len(p) is 2:
        p[0] = []
        p[0].append(p[1])
    elif len(p) is 3:
        p[0] = p[1]
        if not p[0]:
            p[0] = []
        if p[2]:
            p[0].append(p[2])


def p_statement_term(p):
    '''statement : expression COLON expression crlf
                  | expression SP expression crlf
                  | expression crlf
                  | crlf
                  '''
    if len(p) > 4:
        p[0] = [p[1],p[3]]
    elif p[1]=="\r\n":
        pass
    else:
        p[0] = [p[1]]

def p_expression_string(p):
    '''expression : expression alpha
                  | expression DIGIT'''
    p[0] = p[1]+p[2]

def p_expression_uuid(p):
    '''expression : expression MI expression'''
    p[0] = p[1]+p[2]+p[3]

def p_expression_term(p):
    '''expression : alpha alpha
                  | alpha DIGIT
                  | DIGIT
                  '''
    if len(p) is 3:
        p[0] = str(p[1])+str(p[2])
    else:
        p[0] = str(p[1])

def p_alpha_term(p):
    '''alpha : LOALPHA
            | UPALPHA'''
    p[0] = p[1]

def p_crlf_term(p):
    '''crlf : CR LF
            | CRLF'''
    p[0] = "\r\n"

def p_error(p):
    parser.restart()
parser = yacc.yacc()
if __name__ == "__main__":
    parser = yacc.yacc()

    s = '''request\r\nusername:test\r\nuuid:00000000-00000-0000000-0000000000000\r\ntype:unichat\r\nmsglen:20\r\ndstuser:admin\r\n\r\n2345676435367432242536\r\n'''
    result = parser.parse(s)
    print result