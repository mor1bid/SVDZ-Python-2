from sys import getsizeof
import math

# 1

print("1. ")
data1 = 42
data2 = 4.2
data3 = "Сорок два"
data4 = True
print(data1, "это", type(data1))
print(data2, "это", type(data2))
print(data3, "это", type(data3))
print(data4, "это", type(data4))

# 2
print("\n2.")
data = [42, 4.2, "Сорок два", True, 42, True]
for i in range(len(data)):
    check = ''
    if type(data[i]) is int:
        check = 'целое'
    elif type(data[i]) is str:
        check = 'строка'
    print(i + 1, "-", data[i], "адрес:", id(data[i]), ", размер:", getsizeof(data[i]), ", хэш:", hash(data[i]), check)

# 3

numa = int(input("\n3. Введите число: "))
numb = numa
binau = bin(numa)
octau = oct(numa)

binre = ''
while numa > 0:
    binre = str(numa % 2) + binre
    numa //= 2
octre = ''
while numb > 0:
    octre = str(numb % 8) + octre
    numb //= 8

print("Двоичный вид\nРезультат А:", binau)
print("Результат Б:", binre)
print("Восьмеричный вид\nРезультат А:", octau)
print("Результат Б:", octre)

# 4
print("\n4.")
compute = True
while (compute):
    d = float(input("Введите желаемое значение диаметра (до 1000)\n: "))
    if d < 1000:
        r = d / 2
        s = math.pi * math.sqrt(r)
        l = 2 * math.pi * r
        print("Площадь данного круга\n: ", f'{s:.50g}')
        print("Длина данного круга\n: ", f'{l:.50g}')
        compute = False

# 5

# 6
print("\n6.")
perc1 = 1.5
perc2 = 3
sum = 0
compute = True
round = 0
while (compute):
    move = input("Выберите желаемое действие:\n(1) Пополнить баланс\n(2) Снять сумму\n(3) Показать счёт\n(q) Выйти\n: ")
    if move == "1":
        money = int(input("Введите желаемую сумму\n: "))
        if money % 50 == 0:
            sum += money
            print("Вы пополнили ваш счёт на\n:", money, "кредитов.\nВаш счёт теперь составляет\n:", sum, "кредитов.")
            round += 1
            if round % 3 == 0:
                sum += sum * perc2 / 100
    elif move == "2":
        money = int(input("Введите желаемую сумму\n: "))
        if money % 50 == 0 and money <= sum:
            procent = money * perc1 / 100
            sum -= money + procent
            print("Вы сняли со счёта сумму в размере\n:", money, "кредитов.\nВаш счёт теперь составляет\n:", sum, "кредитов.\nС учётом ставки в 1.5% процентов, с вашего счёта также было снято\n:", procent, "кредитов.")
            round += 1
            if round % 3 == 0:
                sum += sum * perc2 / 100
    elif move == "3":
        print("Ваш счёт составляет\n:", sum, "кредитов.")
    elif move == "q":
        print("\nДо свидания.")
        compute = False