age = int(input("Сколько тебе лет? "))

if age < 18:
    print("Ты еще не взрослый")
elif age < 65:
    print("Ты в рабочем возрасте")
else:
    print("Ты на пенсии")


x = 7
print(x > 5)            #True
print(x == 7)           #True, два знака равно: сравнение
print(x != 3)           #True, не равно
print(x < 5 and x == 7) #False, оба условия верны
print(x < 5 or x == 7)  #True, хотя бы одно верно
print(not x == 7)       #False, отрицание


num = int(input("Назови любое число "))
if num % 2 == 0:
    print("У тебя четное число ")
else:
    print("У вас нечетное число ")


num1 = int(input("Назови мне число "))
num2 = int(input("Назови еще одно "))
if num1 > num2:
    print(num1)
else:
    print(num2)


password = (input("Введите пароль "))
if password == "admin123":
    print("Доступ разрешен")
else:
    print("Отказано в доступе")


rating = int(input("Оцените наш сервис от 1 до 10 "))
if rating < 1 or rating > 10:
    print("Принимаются только числа от 1 до 10 ")
elif rating > 7:
    print("Отлично")
elif rating < 4:
    print("Плохо")
else:
    print("Нормально")