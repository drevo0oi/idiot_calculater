from utilts.task1_simple_op import calc_simple
from utilts.task2_extended_op import calc_extended
from utilts.task3_trigon_deg import str_showcenter
from utilts.task4_trigon_rad import calc_radians
from utilts.task9_dec2other import menu_logic
from utilts.task10_brackets_op import check_brackets


def menu_calc_numbers():
    number = input("""1. Простые операции;
2. Расширенные операции;
3. Тригонометрические действия с градусами;
4. Тригонометрические действия с радианами;
5. Логические операции;
6. Перевод чисел в различные СС;
7. Проверка скобок

Введите число, отражающее нужное вам:
""")
    if number == "1":
        calc_simple()
    elif number == "2":
        calc_extended()
    elif number == "3":
        str_showcenter()
    elif number == "4":
        calc_radians
    elif number == "5":
        print("logical_op") # это 5-ая задача(не сделана)
    elif number == "6":
        menu_logic()
    elif number == "7":
        check_brackets() # Он там фигню написал, с него потом выбей что-то нормальное
    else:
        print("""Можно писать число в диапозоне 1-7 и НИЧЕГО другого
Пример: 4
""")
    print("""

""")