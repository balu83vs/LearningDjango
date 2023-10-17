file = "D:\\py_learning\\learning_django\\task_project\\words.txt"


def write_file(word1, word2):
    with open(file, 'a', encoding='utf-8') as words_file:
        words_file.writelines(f"{word1}-{word2}\n")
