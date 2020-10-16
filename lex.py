import re
from typing import NamedTuple, Iterable


class Token(NamedTuple):
    kind: str
    value: str


def lex(code: str) -> Iterable[Token]:
    """
    Retorna sequência de objetos do tipo token correspondendo à análise léxica
    da string de código fornecida.
    """

    token_specification = [
        ('NUMBER', r'(\+|\-)?\d+(\.\d*)?'),
        ('STRING', r'\".*\"'),
        ('BOOL', r'#[t|f]'), 
        ('CHAR', r'#\\[a-zA-Z]*'),
        ('QUOTE', r'\''),
        ('LPAR', r'\('), #open parenthesis
        ('RPAR', r'\)'), #close parenthesis
        ('NAME', r'([^;()\"\#\n ]+)'),
    ]

    # Remove comments from entry
    code = re.sub(r';;.*', '', code)
    
    token_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

    for mo in re.finditer(token_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        yield Token (kind, value)

    return [Token('INVALIDA', 'valor inválido')]