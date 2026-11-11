a = 10     # int, целое число
b = 3.5    # float, дробное число
c = "Привет" # str, строка
d = True     # bool, истина/ложь
print(type(a), type(b), type(c), type(d))
print(a + b)
print(a / b)      # обчное деление
print(a // 3)     # целая часть
print(a % 3)      # остаток
print(a ** 2)     # степень

name = input("Как тебя зовут? ")
age = int(input("Сколько тебе лет?"))
print(f"Привет, {name}! Через 5 лет тебе будет {age + 5}")

num1 = int(input("Назови число любое "))
num2 = int(input("И еще одно число) "))
print(f"Сумма твоих чисел {num1 + num2}! Разность твоих чисел состовляет {num1 - num2}! А произведение чисел {num1 * num2} ") 

price_product = int(input("Сколько стоит твой товар? "))
count_product = int(input("Какое его количество? "))
print(f"За все товары ты заплатишь {price_product * count_product}")

circle_radius = int(input("Какой радиус круга? "))
pi_num = 3.14
print(f"Площадь твоего круга ровна {pi_num * circle_radius ** 2}")

date_now = int(input("Какой сейчас год? "))
birth_day = int(input("Год твоего рождения? "))
print(f"Тебе полных {date_now - birth_day} лет!")

distance_mile = int(input("Какова дистанция в милях?"))
print(f"Ваше расстояние в километрах равна {distance_mile * 1.6}")
