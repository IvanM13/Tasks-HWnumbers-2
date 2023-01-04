# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

def GetNumb(message):
    
    isCorrect = False
    while isCorrect == False:
        try:
            number = int(input(message))
            isCorrect = True
        except ValueError:
            print("Введено не число. Повторите!")
    return number

def Sigma(numb):

    sum = 0
    number = str(numb)
    for i in (number):
        if i.isdigit():
            sum+=int(i)
    return sum

number = GetNumb("Введите число ")
print(f'{number} -> {Sigma(number)}')