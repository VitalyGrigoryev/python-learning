print("1 - сложение\n2 - вычитание\n3 - умножение\n4 - деление")

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
    



