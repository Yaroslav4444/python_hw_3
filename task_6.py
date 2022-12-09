"""
Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
 возвращающую его же, но с прописной первой буквой.
 Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной
буквы. Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(string):
    """replacing a capital letter with a capital letter"""
    return string.title()


print(int_func(input("Введите текст прописью : \n")))


def replacing_letters(string):
    """replacing a capital letter with a capital letter"""
    capital_letters = []
    cap = string.split()
    for el in cap:
        capital_letters.append(int_func(el))
    print(*capital_letters)
