from fractions import Fraction

# 2. Напишите программу, которая получает целое число 
# и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

number = int(input("2. Здравствуйте, введите число\n: "))
print("Результат А\n:", hex(number))
hexn = '0x'
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
# code = [int(i) for i in str(hexre)]
# hec = [int(i) for i in str(hexre)]
# for d in range(len(code)):
#     if d != 0:
#         if code[d] == 0 and code[d-1] > 0:
#             hec[d] = "a"
#         elif code[d] == 1 and code[d-1] > 0:
#             hec[d] = "b"
#         elif code[d] == 2 and code[d-1] > 0:
#             hec[d] = "c"
#         elif code[d] == 3 and code[d-1] > 0:
#             hec[d] = "d"
#         elif code[d] == 4 and code[d-1] > 0:
#             hec[d] = "e"
#         elif code[d] == 5 and code[d-1] > 0:
#             hec[d] = "f"
#         hexn += str(hec[d])
#     elif len(code) == 1:
#         hexn += str(hec[d])
print(f"Результат Б\n: 0x{hexre}")
# print("Результат Б\n:", hexn)

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


