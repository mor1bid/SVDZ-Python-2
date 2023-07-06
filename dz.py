from fractions import Fraction
import smn

# 2. Напишите программу, которая получает целое число 
# и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

number = int(input("2. Здравствуйте, введите число\n: "))
print("Результат А\n:", hex(number))
hexre = ''
while number > 0:
    hexre = str(number % 16) + hexre
    match hexre:
        case '10':
            hexre = 'a'
        case '11':
            hexre = 'b'
        case '12':
            hexre = 'c'
        case '13':
            hexre = 'd'
        case '14':
            hexre = 'e'
        case '15':
            hexre = 'd'
    number //= 16
print(f"Результат Б\n: 0x{hexre}")

# 3. Напишите программу, которая принимает две строки вида 
# "a/b" - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
# Для проверки своего кода используйте модуль fractions.

fracta = input("\n3.\nВведите через пробел числитель и знаменатель первой дроби\n: ").split()
fractb = input("Введите через пробел числитель и знаменатель второй дроби\n: ").split()
print("Результат А")
print("Сумма дробей\n:", Fraction(int(fracta[0]), int(fracta[1])) + Fraction(int(fractb[0]), int(fractb[1])))
print("Произведение дробей\n:", Fraction(int(fracta[0]), int(fracta[1])) * Fraction(int(fractb[0]), int(fractb[1])))
print("\nРезультат Б")

print("Произведение дробей\n:", int(fracta[0]) * int(fractb[0]), '/', int(fracta[1]) * int(fractb[1]))


