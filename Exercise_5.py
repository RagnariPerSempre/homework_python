#5) Заменить все буквы "х" на "у" в исходной строке без использования дополнительной строки.

str = 'asdxfghyxyx'


def replacement(str):
    str = str.replace('x','y')
    return str


print(replacement(str))