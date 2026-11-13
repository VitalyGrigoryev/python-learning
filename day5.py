# Проверка пароля
password = input("Введите пароль ")
bad_pass = "password"
bad_pass2 = "12345678"
if len(password) < 8:
    print("Пароль должен содержать не меньше 8 символов")
elif password in [bad_pass, bad_pass2]:
    print("Пароль слабый")
else:
    print("Пароль принят")


hour = int(input("Какое сейчас время? "))
if hour < 0 or hour > 23:
    print("Ошибка: время не верное")
elif 5 <= hour <= 11:
    print("Доброе утро!")
elif 12 <= hour <= 17:
    print("Добрый день!")
elif 18 <= hour <= 22:
    print("Добрый вечер!")
else:
    print("Доброй ночи!")

name = input("Укажите ваше имя ").strip().capitalize()
surname = input("Укажите вашу фамилию ").strip().capitalize()
city = input("Укажите ваш город ").strip().capitalize()
print(f"Имя: {name}\nФамилия: {surname}\nГород: {city}\nИнициалы: {name[0]}.{surname[0]}.")

