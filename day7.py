# for: повторить заданное число раз
for i in range(5):
    print("Шаг", i)     # 0, 1, 2, 3, 4

for i in range(1,6):
    print(i)            # 1, 2, 3, 4, 5(первая граница не входит)

# for по строке

for letter in "Python":
    print(letter)

# while: повторять, пока условие истинно
count = 0
while count < 3:
    print("count =", count)
    count = count + 1   # без этой строки цикл будет бесконечен

# Задачи
for i in range(1, 11):
    print(i)

for i in range(2, 21, 2):
    print(i)

total = 0 
for number in range(1, 101):
   total += number
print(total)

num = int(input("Введите число "))
count = 1
while count < 11:
    print(num * count)
    count = count + 1


while True:
    hour = int(input("Который час (0-23)? "))
    if hour < 0 or hour > 23:
        print("Ошибка: введите число от 0 до 23")
    else:
        print("Принято:", hour)
        break

print("1 - сложение\n2 - вычитание\n3 - умножение\n4 - деление")

while True:
    num_operation = int(input("Выберите номер операции "))
    if num_operation < 1 or num_operation > 4:
        print("Ошибка! Выберите варианты от 1 до 4")
    else:
        num1 = float(input("Введите первое число "))
        num2 = float(input("Введите второе число "))
        if num_operation == 1:
            print(f"{num1} + {num2} = {num1 + num2}")
        elif num_operation == 2:
            print(f"{num1} - {num2} = {num1 - num2}")
        elif num_operation == 3:
            print(f"{num1} * {num2} = {num1 * num2}")
        elif num_operation == 4:
            if num2 == 0:
                print("На ноль делить нельзя")
            else:
                print(f"{num1} / {num2} = {num1 / num2}")

    question = input("Желаете продолжить? yes/no ")
    if question != "yes":
        break