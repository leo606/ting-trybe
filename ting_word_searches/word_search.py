import re
# from ting_file_management.file_process import process
# from ting_file_management.queue import Queue


def word_occurrences(word, lines):
    matched = []
    reg_pattern = re.compile(word, re.IGNORECASE)

    for index, line in enumerate(lines):
        if re.search(reg_pattern, line):
            matched.append({'linha': index + 1})
    return matched


def exists_word(word, instance):
    exists_word_report = []
    for file in instance:
        ocurrences = word_occurrences(word, file['linhas_do_arquivo'])
        if len(ocurrences):
            exists_word_report.append({
                "palavra": word,
                "arquivo": file['nome_do_arquivo'],
                "ocorrencias": ocurrences,
            })
    return exists_word_report


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
