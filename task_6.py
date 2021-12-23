# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

word = 'small'


def int_func(w):
    return w.capitalize()


# Вывод слова
print(int_func(word))


words = 'little big planet'

words_arr = words.split()

result_arr = (int_func(w) for w in words_arr)

# Вывод строки
print(" ".join(str(a) for a in result_arr))
