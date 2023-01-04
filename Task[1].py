# Задайте список из n чисел 
# последовательности (1+1/n)^n и выведите на экран их сумму.
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06


def Sequence(num):
    
    my_list = []
    for i in range(1, num+1):
        my_list.append(round((1 + 1 / i)**i, 2))
    return my_list 

num = int(input("Введите число: "))       
print(Sequence(num))
print(sum(Sequence(num)))
