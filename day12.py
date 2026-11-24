try:
    nubmer = int(input("Введи число: "))
    print(f"Ты ввел {nubmer}")
except ValueError:
    print("Это не число!")

print("Программа продолжила работу")


try:
    a = int(input("Число a: "))
    b = int(input("Чмсло b: "))
    print(a / b)
except ValueError:
    print("Нужно вводить числа")
except ZeroDivisionError:
    print("На ноль делить нельзя")


try:
    n = int(input("Число: "))
except ValueError:
    print("Не число")
else:
    print("Ошибки не было", n)
finally:
    print("Это выполниться всегда")

# Задачи

def ask_int(prompt):
    while True:
        try: n = int(input(prompt))
        except ValueError:
            print("Ошибка!")
        else:
            return n
ask_int("Укажи число ")


def ask_hour():
    while True:
        hour = int(input("Который час (0-23)? "))
        if 0 <= hour <= 23:
            return hour
        print("Введите число от 0 до 23")

def greeting(hour):
    if 5 <= hour <= 11:
        return "Доброе утро!"
    elif 12 <= hour <= 17:
        return "Добрый день!"
    elif 18 <= hour <= 22:
        return "Добрый вечер!"
    else:
        return "Доброй ночи!"

print(greeting(ask_hour()))



def division(prompt_a, prompt_b):
    while True:
        try:
            n = int(input(prompt_a))
            b = int(input(prompt_b))
            return n / b
        except ValueError:
            print("Введите целые числа!")
        except ZeroDivisionError:
            print("На ноль делить нельзя!")

print(division("Введите первое число: ", "Введите второе число: "))


servers = {"web1": "ok", "web2": "error"}
def ask_server(prompt):
    while True:
        try: n = servers[(input(prompt))]
        except KeyError:
            print("Нет такого сервера")
        else:
            return n

print(ask_server("Введите имя сервера "))



