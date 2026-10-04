import math

def calc_extended():
    print("Выберите операцию:")
    print("1 - Возведение в степень")
    print("2 - Остаток от деления")
    print("3 - Нахождение квадратного корня")

    operation = int(input("Введите номер операции (1, 2 или 3): "))

    if operation == 1:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число (степень): "))
        result = num1**num2
        print(f"Результат: {result}")

    elif operation == 2:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число (делитель): "))
        if num2 == 0:
            print("Ошибка: Деление на ноль невозможно!")
            return
        result = num1 % num2
        print(f"Результат: {result}")

    elif operation == 3:
        num1 = float(input("Введите число: "))
        if num1 < 0:
            print(
                "Ошибка: Нельзя извлечь квадратный корень из отрицательного числа!"
            )
            return
        result = math.sqrt(num1)
        print(f"Результат: {result}")

    else:
        print("Ошибка: Неверный номер операции!")

if __name__ == "__main__":
    calc_extended()