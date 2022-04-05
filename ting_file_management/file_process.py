import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    file_content = txt_importer(path_file)

    if instance.is_file_in_queue(path_file):
        print('file already in queue', file=sys.stderr)
    else:
        file_processed = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file_content),
            "linhas_do_arquivo": file_content
        }
        instance.enqueue(file_processed)
        print(file_processed)


def remove(instance):
    if len(instance):
        removed = instance.dequeue()
        print(f"Arquivo {removed['nome_do_arquivo']} removido com sucesso\n")
    else:
        print('Não há elementos')


def file_metadata(instance, position):
    try:
        file_data = instance.search(position)
        print(file_data)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
