def print_red(msg):
    print(f'\033[31m{msg}\033[0m')

def print_yellow(msg):
    print(f'\033[33m{msg}\033[0m')

from pygments.lexers import get_lexer_by_name
from pygments.styles import get_style_by_name


def test_custom_pygments():
    try:
        lexer = get_lexer_by_name('custompython')
        print('Lexer registrado com sucesso!')
    except Exception as e:
        print_red(f'Erro ao registrar o lexer: {e}')

    try:
        style = get_style_by_name('pycharm')
        print('Style registrado com sucesso!')
    except Exception as e:
        print_red(f'Erro ao registrar o style: {e}')


if __name__ == '__main__':
    test_custom_pygments()