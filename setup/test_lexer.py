
from pygments.lexers import get_lexer_by_name
from pygments import lex
import re

if __name__ == '__main__':
    code = r"func(52, b=45)"

    lexer = get_lexer_by_name('custompython')
    tokens = lex(code, lexer)

    for token_type, value in tokens:
        print(f"{token_type}: {value}")

    def f(a, b):
        return a,b

    f(1, b=0)