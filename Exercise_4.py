#4) Сосчитать произведение чисел [3, 4, 56, 100, 15, 2, 20, 30],кратных и 3 и 5.

lst = [3, 4, 56, 100, 15, 2, 20, 30]

def multiplication_of_multiples(lst: lst):
    result = 1
    for i in lst:
        if i % 3 == 0 and i % 5 == 0:
            result *= i
    return result


print(multiplication_of_multiples(lst))
