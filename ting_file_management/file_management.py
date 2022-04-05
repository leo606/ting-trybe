import sys

TXT_EXTENSION = 'txt'


def txt_importer(path_file):
    file_extension = path_file.split('.')[-1].lower()
    if file_extension != TXT_EXTENSION:
        return print("Formato inválido", file=sys.stderr)

    try:
        with open(path_file) as file:
            lines = file.read()
            return lines.split('\n')
    except Exception:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
