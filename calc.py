def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return None
    return a / b
def power(a, b):
    return a ** b

def get_number(prompt):
    while True:
        try:
            n = float(input(prompt))
            return n
        except ValueError:
            print("Введите только числа")

def ask_operation():
    print("1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n5. Степень")
    while True:
        try:
            n = int(input("Выберите операцию от 1 до 5 "))
            if n < 1 or n > 5:
                print("Выберите число от 1 до 5")
            else:
                return n
        except ValueError:
            print("Введите только числа!")

while True:
    operation = ask_operation()
    num1 = get_number("Введите первое число ")
    num2 = get_number("Введите второе число ")

    if operation == 1:
        result = add(num1, num2)
    elif operation == 2:
        result = subtract(num1, num2)
    elif operation == 3:
        result = multiply(num1, num2)
    elif operation == 4:
        result = divide(num1, num2)
    elif operation == 5:
        result = power(num1, num2)

    if result is None:
        print("На 0 делить нельзя")
    else:
        print(f"Результат вашей операции: {result}")
    question = input("Желаете продолжить? yes/no ").strip().lower()
    if question != "yes":
        break

def test():
    for i in range(5):
        if i == 2:
            break
        print(i)
    print("конец")

print(test())