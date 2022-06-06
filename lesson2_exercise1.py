lst = ["Пригоршня","Химик", "Курильщик", "Меченый", "Сидорович"]
dictc = {1:"Пригоршня", 2:"Химик", 3:"Курильщик", 4:"Меченый", 5:"Сидорович"}
setc = ["Пригоршня","Химик", "Курильщик", "Меченый", "Сидорович", "Курильщик"]


lst.append("Воронков")


print(lst) # Широкий функционал методов для работы со списками
print(dictc[1])  # Удобно получать значение по ключу, не важно местоположение в словаре
print(set(setc)) # С помощью множества можно избавиться от дубликатов



# Поиск элемента
searched = "Меченый"
for i in lst: #setc
    if i == searched:
        print("Yes")
        break

if searched in setc: #lst
    print("Yess")

for i in range(5):
    if dictc[i+1] == searched:
        print("Ye")

if searched in dictc.values():
    print("Ey")