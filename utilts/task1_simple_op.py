def calc_simple():
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    operation = input("Введите операцию: ")
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Ошибка: Деление на ноль невозможно!")
            return
        result = num1 / num2
    else:
        print("Ошибка: Неизвестная операция!")
        return
    print(f"Результат: {result}")

if __name__ == "__main__":
    calc_simple()