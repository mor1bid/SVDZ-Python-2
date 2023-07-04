from sys import getsizeof

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

data = [42, 4.2, "Сорок два", True, 42, True]
for i in range(len(data)):
    check = ''
    if type(data[i]) is int:
        check = 'целое'
    elif type(data[i]) is str:
        check = 'строка'
    print(i + 1, "-", data[i], "адрес:", id(data[i]), ", размер:", getsizeof(data[i]), ", хэш:", hash(data[i]), ",", check)