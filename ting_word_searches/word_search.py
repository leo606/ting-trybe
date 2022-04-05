import re
# from ting_file_management.file_process import process
# from ting_file_management.queue import Queue


def word_occurrences(word, lines, return_content):
    matched = []
    reg_pattern = re.compile(word, re.IGNORECASE)

    for index, line in enumerate(lines):
        if re.search(reg_pattern, line):
            if return_content:
                matched.append({'linha': index + 1, 'conteudo': line})
            else:
                matched.append({'linha': index + 1})
    return matched


def exists_word(word, instance):
    exists_word_report = []
    for file in instance:
        ocurrences = word_occurrences(word, file['linhas_do_arquivo'], False)
        if len(ocurrences):
            exists_word_report.append({
                "palavra": word,
                "arquivo": file['nome_do_arquivo'],
                "ocorrencias": ocurrences,
            })
    return exists_word_report


def search_by_word(word, instance):
    search_word_report = []
    for file in instance:
        ocurrences = word_occurrences(word, file['linhas_do_arquivo'], True)
        if len(ocurrences):
            search_word_report.append({
                "palavra": word,
                "arquivo": file['nome_do_arquivo'],
                "ocorrencias": ocurrences,
            })
    return search_word_report
