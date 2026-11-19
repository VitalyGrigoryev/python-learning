def say_hello():
    print("Привет")
    print("Я учу функции")

say_hello()
say_hello()


def greet(name):
    print(f"Привет, {name}!")

greet("Виталий")
greet("Братка")

def add(a, b):
    return a+b

result = add(2, 3)
print(result)
print(add(10, 20))

def f1(n):
    print(n * 2)

def f2(n):
    return n * 2
print(f1(5), f2(5))

def show_name():
    print("Виталик из Минска)")
show_name()
show_name()
show_name()

def square(n):
    return n ** 2
print(f"{square(4)}, {square(7)}")
square(4)

def is_even(n):
    return n % 2 == 0

print(is_even(10))   
print(is_even(15))   


def average(a, b, c):
    return (a + b + c) / 3
print(average(3, 5, 10))


def greeting(hour):
    if hour < 0 or hour > 23:
        return "Ошибка: время неверное"
    elif 5 <= hour <= 11:
        return "Доброе утро!"
    elif 12 <= hour <= 17:
        return "Добрый день!"
    elif 18 <= hour <= 22:
        return "Добрый вечер!"
    else:
        return "Доброй ночи!"
print(greeting(13))
print(greeting(22))
print(greeting(28))

def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

print(max_of_two(5, 10))
print(max_of_two(11, 10))
