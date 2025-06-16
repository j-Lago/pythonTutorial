import subprocess
import sys
import os
import glob
import shutil


def print_red(msg): print(f'\033[31m{msg}\033[0m')
def print_yellow(msg): print(f'\033[33m{msg}\033[0m')


def remove_minted_dirs():
    for path in glob.glob(os.path.join('..', 'out', '_minted*')):
        if os.path.isdir(path):
            print_yellow(f'Removendo pasta: {path}')
            shutil.rmtree(path)


def ensure_pygments():
    try:
        import pygments
        print('Pygments já está instalado.')
    except ImportError:
        print('Pygments não encontrado. Instalando...')
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pygments'])


def run_pip_install():
    setup_dir = os.path.dirname(os.path.abspath(__file__))
    print('Instalando o pacote com pip...')
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', setup_dir])
    except subprocess.CalledProcessError as e:
        print_red(f'Erro ao instalar o pacote: {e}')
        sys.exit(1)


if __name__ == '__main__':
    ensure_pygments()
    run_pip_install()
    remove_minted_dirs()
    print()
    from test_installation import test_custom_pygments
    test_custom_pygments()
