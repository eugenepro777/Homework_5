'''
Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
'''

import random

def get_random_string(length):
    letters = 'бабвер рабаа аввба абвбав абв абырвалг вабабв вава абва абба баобаб бобабв'
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def cheking_string(string):
    words = string.split(' ')
    search = 'абв'
    new_words = []
    for word in words:
        if search not in word:
            new_words.append(word)
    string_out = ' '.join(new_words)   
    return string_out

string_in = get_random_string(128)
print(f"Генерируем текст:\n {string_in}\n")
print(f"Новый текст:\n {cheking_string(string_in)}")