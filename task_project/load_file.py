file = "D:\\py_learning\\learning_django\\task_project\\words.txt"


def read_file():
    words_list = []
    with open(file, 'r', encoding='utf-8') as words_file:
        for word in words_file.readlines():
            or_word, tr_word = word.strip('\n').split('-')
            words_list.append((or_word.strip(' '), tr_word.strip(' ')))
    return words_list
