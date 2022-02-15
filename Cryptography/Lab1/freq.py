#!/usr/bin/env python3
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
# print(char_frequency('google.com'))
# 2. Дурын тоог оруулахад 1-26 дотор хөрвүүлэх функц нэмж бич
# Дурын тоог mod 26 хийхэд 1-26дотор хариу гарна
def xmod26(num):
        return num % 26
