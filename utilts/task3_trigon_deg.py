def str_showcenter():
    user_string = input("Введите строку: ")
    
    if not user_string or user_string.isspace():
        print("Ошибка: пустой ввод недопустим")
        return

    user_string = user_string.strip()

    has_russian = any('а' <= char <= 'я' or 'А' <= char <= 'Я' or char in 'ёЁ' for char in user_string)
    if not has_russian:
        print("Ошибка: строка должна содержать русский текст")
        return

    terminal_width = 80
    terminal_height = 25

    centered_string = user_string.center(terminal_width)

    top_padding = (terminal_height - 1) // 2
    bottom_padding = terminal_height - 1 - top_padding

    for _ in range(top_padding):
        print()

    print(centered_string)

    for _ in range(bottom_padding):
        print()