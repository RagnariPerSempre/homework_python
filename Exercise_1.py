"""
1) Сумму ряда 0 - 88888888
2) Среднее арифметическое ряда [3, 4, 56, 100, 2, 2, 3]
3) Заменить в строке "asdxfghyxyx" все буквы "х" на "у"
4) Сосчитать произведение чисел [3, 4, 56, 100, 15, 2, 20, 30],
кратных и 3 и 5.
5) Заменить все буквы "х" на "у" в исходной строке
без использования дополнительной строки.
"""
big_number = 88888888
result = 0


for i in range(big_number + 1):
    if i < 1 or i > 88888887:
        print(i)
    result += i


print(f"Суммa ряда 0 - 88888888 = ",result)