
#2) Среднее арифметическое ряда [3, 4, 56, 100, 2, 2, 3]

lst = [3, 4, 56, 100, 2, 2, 3]

def arithmetic_mean(lst):
    result = 0
    for i in lst:
        result += i
    return result / len(lst)


print(arithmetic_mean(lst))

#24.285714285714285