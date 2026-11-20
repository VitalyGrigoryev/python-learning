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
    return float(input(prompt))

def show_menu():
    print("1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n5. Степень")

while True:
    show_menu()
    operation = int(input("Выберите пожалуйста номер операции "))
    if operation < 1 or operation > 5:
        print("Ошибка! Выберите варианты от 1 до 5")
    else:
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
            print("На 0 делить нельзя!")
        else:
            print(f"Результат вашей операции: {result}")
    question = input("Желаете продолжить? yes/no ")
    if question != "yes":
        break
        
