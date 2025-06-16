
from pygments.token import Operator, Name
from pygments.lexers import PythonLexer
import re

__all__ = ['CustompythonLexer']


class CustompythonLexer(PythonLexer):
    aliases = ['custompython']

    def get_tokens_unprocessed(self, text):
        tokens = list(super().get_tokens_unprocessed(text))

        for i, (index, token, value) in enumerate(tokens):
            if token is Name and i + 1 < len(tokens):
                next_token, next_value = tokens[i + 1][1], tokens[i + 1][2]

                if next_token is Operator and next_value == "=":
                    yield index, Name.Argument, value
                else:
                    yield index, token, value
            else:
                yield index, token, value



