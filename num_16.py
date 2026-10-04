def str_simple(s):
    if s == '+':
        print("Введите 2 строки")
        s2 = input().strip()
        s3 = input().strip()
        result0 = s2+s3
        print(result0)
    elif s == '*':
        print("Введите строку и число")
        s4 = input().strip()
        n = int(input())
        result = s4*n
        print(result)

def str_showcenter():
    user_string = input("Введите строку: ")

    terminal_width = 80
    terminal_height = 25
    
    centered_string = user_string.center(terminal_width)
    
    top_padding = (terminal_height - 1) // 2
    
    for _ in range(top_padding):
        print()

    print(centered_string)
    
    bottom_padding = terminal_height - 1 - top_padding
    for _ in range(bottom_padding):
        print()
    
def str_words():
    text = input("Введите строку: ").split()
    size1 = len(text)
    size2 = len(set(text))
    print("Количество слов: ", size1,"\n Количество уникальных слов: ", size2)

def str_stat():
    text = input("Введите строку: ")
    size = len(text)

    count1 = 0#количество цифр
    for char in text:
        if char.isdigit():
            count1 += 1
    
    count2 = 0 #количество заглавных букв
    count2 = sum(1 for ch in text if ch.isupper())

    count3 = 0 #количество маленьких букв
    count3 = sum(1 for ch in text if ch.islower())

    count4 = 0 #количество "пробельных" символов
    count4 = sum(1 for ch in text if ch.isspace())
    print("Размер строки:", size, "\nКоличество чисел:", count1, "\nКоличество заглавных букв:", count2, "\nКоличество строчных букв:", count3, "\nКоличество 'пробельных' символов:", count4)

def menu_strings():
    print("Меню калькулятора строк:")
    print("1. Простые операции со строками")
    print("2. Вывод строки по центру экран")
    print("3. Количество слов и количество уникальных слов")
    print("4. Статистика по символам строк")

    print("Введите число от 1 до 4")
    user_input = int(input())

    if user_input == 1:
        operation = input("Введите '*' или '+' : ")
        str_simple(operation)
    elif user_input == 2:
        str_showcenter()
    elif user_input == 3:
        str_words()
    elif user_input == 4:
        str_stat()
    else:
        print("Введите число от 1 до 4")

