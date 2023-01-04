# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int

def GetRandom():

    import random
    
    n = int(input("Введите количество элементов в списке: "))

    my_list = []

    for i in range(n):
        my_list.append(random.randint(0,100))

    print(f'Исходный список: {my_list}')

    result = my_list[:]
    for i in range(n):
        index = random.randint(0, n-1)
        temp = result[i]
        result[i] = result[index]
        result[index] = temp

    print(f'Результат перемешивания: {result}') 

GetRandom()
   