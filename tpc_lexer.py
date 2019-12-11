# -*- coding:utf-8 -*-

import ply.lex as lex
import re

tokens = (
    'UPALPHA',
    'LOALPHA',
    'DIGIT',
    'CTL',
    'CR',
    'LF',
    'CRLF',
    'SP',
    'HT',
    'MI',
    'QUOTATION',
    'COLON'
)

states = (
    ('alpha', 'inclusive'),
    ('digit', 'inclusive'),
    ('notation', 'inclusive')
)

types = {
        '\x3A': 'COLON',
         '\x22': 'QUOTATION',
         '\x20': 'SP',
         "\x0D": 'CR',
         '\x0A': 'LF',
         '\x0D\x0A': 'CRLF',
         '\x2D': 'MI'
}

pattern = re.compile(r'[\x22|\x3A|\x0A|\x0D\x0A|\x20|\x09|\x2D]')

def t_begin_alpha(t):
    r'[\x41-\x5A|\x61-\x7A]'
    t.lexer.begin('alpha')
    t.value = lexer.lexdata[t.lexer.lexpos-1]
    if re.match(r'\x41-\x5A', t.value):
        t.type = "UPALPHA"
    else:
        t.type = "LOALPHA"
    return t


def t_alpha_end(t):
    r'[^\x41-\x5A|\x61-\x7A]'
    t.value = lexer.lexdata[t.lexer.lexpos - 1]
    if re.match(r'[\x30-\x39]', t.value):
        t.lexer.begin('INITIAL')
        t.type = 'DIGIT'
        return t
    else:
        match = pattern.match(t.value)
        if match:
            t.lexer.begin('INITIAL')
            t.type = types[match.group()]
            return t
        else:
            t.lexer.begin('INITIAL')
            t_error(t)


def t_begin_digit(t):
    r'[\x30-\x39]'
    t.lexer.begin('digit')
    t.value = lexer.lexdata[t.lexer.lexpos-1]
    t.type = "DIGIT"
    return t

def t_digit_end(t):
    r'[^\x30-\x39]'
    t.value = lexer.lexdata[t.lexer.lexpos - 1]
    if re.match(r'[\x41-\x5A]', t.value):
        t.lexer.begin('INITIAL')
        t.type = "UPALPHA"
        return t
    elif re.match(r'[\x61-\x7A]', t.value):
        t.lexer.begin('INITIAL')
        t.type = "LOALPHA"
        return t
    else:
        match = pattern.match(t.value)
        if match:
            t.lexer.begin('INITIAL')
            t.type = types[match.group()]
            return t
        else:
            t.lexer.begin('INITIAL')
            t_error(t)

def t_begin_notation(t):
    r'[\x22|\x3A|\x0A|\x0D\x0A|\x20|\x09|\x2D]'
    t.lexer.begin('notation')
    t.value = t.lexer.lexdata[t.lexer.lexpos-1]
    match = pattern.match(t.value)
    if match:
        t.type = types[match.group()]
        return t

def t_notation_end(t):
    r'[^\x22|\x3A|\x0A|\x0D\x0A|\x20|\x09|\x2D]'
    t.value = t.lexer.lexdata[t.lexer.lexpos - 1]
    if re.match(r'[\x41-\x5A]', t.value):
        t.lexer.begin('INITIAL')
        t.type = "UPALPHA"
        return t
    elif re.match(r'[\x61-\x7A]', t.value):
        t.lexer.begin('INITIAL')
        t.type = "LOALPHA"
        return t
    elif re.match(r'[\x30-\x39]', t.value):
        t.lexer.begin('INITIAL')
        t.type = 'DIGIT'
        return t
    else:
        t.lexer.begin('INITIAL')
        t_error(t)

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(0)

def t_notation_error(t):
    print "Illegal notation '%s'" % t.value[0]
    t.lexer.skip(0)

t_notation_COLON = r'\x3A'
t_notation_QUOTATION = r'\x22'
t_notation_CR = r'\x0D'
t_notation_LF = r'\x0A'
t_notation_CRLF = r'\x0D\x0A'
t_notation_SP = r'\x20'
t_notation_HT = r'\x09'
t_notation_MI = r'\x2D'
t_INITIAL_CTL = r'[\x00-\x1F|7F]'
t_digit_DIGIT = r'[\x30-\x39]'
t_alpha_UPALPHA = r'[\x41-\x5A]'
t_alpha_LOALPHA = r'[\x61-\x7A]'

lexer = lex.lex()

data = '''request\r\nusername:test\r\n'''

lexer.input(data)

    # Tokenize
while True:
    tok = lexer.token()
    if not tok: break      # No more input
    print tok