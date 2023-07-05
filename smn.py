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
compute = True
while (compute):
    d = float(input("\n4. Введите желаемое значение диаметра (до 1000)\n: "))
    if d < 1000:
        r = d / 2
        s = math.pi * math.sqrt(r)
        l = 2 * math.pi * r
        print("Площадь данного круга\n: ", f'{s:.50g}')
        print("Длина данного круга\n: ", f'{l:.50g}')
        compute = False

# 5

