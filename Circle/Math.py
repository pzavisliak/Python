import math

print("Вычисление длины круга")

def bugsa():
    if a != "R" or a != "D":
        print("Нужно было ввести R или D , в следуйщий раз читай внимательнее")
        exit()

a = input("С помощью чего ты хочешь найти длину? Радиус - R, Диаметр - D\n")

bugsa()

rad = ""
diam = ""

def bugsradius():
    if rad <= str(0):
        print("Число не может быть меньше или равно нулю, ничего не значить, а также оно не должно быть буквой!\n\n")
        exit()
    else:
        return

def bugsdiametr():
    if diam <= str(0):
        print("Число не может быть меньше или равно нулю, ничего не значить, а также оно не должно быть буквой!\n\n")
        exit()
    else:
        return

if a == "R":
    rad = input("Введите радиус: ")
    bugsradius()
    radius = (float(2) * math.pi * float(rad))
    okr = round(radius, 2)
    print("Длина круга равна: " + str(okr))
elif a == "D":
    diam = input("Введите диаметр: ")
    bugsdiametr()
    diametr = (float(diam) * math.pi)
    okr = round(diametr, 2)
    print("Длина круга равна: " + str(okr))
