from pathlib import Path


base_dir = Path(__file__).resolve().parent.parent.parent
data_dir = base_dir / 'data'
figs_dir = base_dir / 'src' / 'figs'


if __name__ == '__main__':
    print(f"{base_dir = }")
    print(f"{data_dir = }")
    print(f"{figs_dir = }")
