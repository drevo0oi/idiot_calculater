def calc_10_2(n):
    a = bin(n)
    return(a[2:])

def calc_10_8(a):
    numb = (oct(a))[2:]
    return(numb)


def calc_10_16(a):
    return(hex(a)[2:])


def menu_logic():
    print("1. Перевод 10 СИ -> 2 СИ;")
    print("2. Перевод 10 СИ -> 8 СИ;")
    print("3. Перевод 10 СИ -> 16 CИ;")
    try:
        nomber = int(input())
        if nomber == 1:
            print("dec2bin_op:")
            a = int(input())
            print(calc_10_2(a))

        if nomber == 2:
            print("dec2oct_op:")
            a = int(input())
            print(calc_10_8(a))

        if nomber == 3:
            print("dec2hex_op:")
            a = int(input())
            print(calc_10_16(a))
    except ValueError:
        print("ПИШИ ЦИФРЫ А НЕ БУКВЫ")
        print()
        print("Пример: 2")
        menu_logic()