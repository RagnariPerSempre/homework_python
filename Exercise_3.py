#3) Заменить в строке "asdxfghyxyx" все буквы "х" на "у"

str = 'asdxfghyxyx'


def replacement(str):
    new_str = ''
    for i in str:
        if i != 'x':
            new_str += i
        else:
            new_str += 'y'
    return new_str


print(replacement(str))