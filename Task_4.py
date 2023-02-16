'''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
'''


def encode_rle(string):
    encode = ""
    i = 0
    while i < len(string):
        count = 1
        while i + 1 < len(string) and string[i] == string[i + 1]:
            count += 1
            i += 1
        encode += str(count) + string[i]
        i += 1
    return encode


def decode_rle(data):
    decode = ""
    count = ""
    for symbol in data:
        if symbol.isdigit():
            count += symbol
        else:
            decode += symbol * int(count)
            count = ""
    return decode


string = input("Введите строку для кодирования RLE: ")
s = encode_rle(string)
print(f"Закодированная строка: -> {s}")

print(f"Декодированная строка: -> {decode_rle(s)}")
