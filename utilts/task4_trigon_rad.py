import math

def calc_radians():
    op = input('Введите номер действия (1 - sin, 2 - cos): ')
    
    if op not in ('1', '2'):
        print('Ошибка: неверное действие')
        return

    try:
        angle = float(input('Введите вещественное число (угол в радианах): '))
    except ValueError:
        print('Ошибка: введено не число')
        return

    if op == '1':
        res = math.sin(angle)
        print(f'Результат: sin({angle}) = {res}')
    elif op == '2':
        res = math.cos(angle)
        print(f'Результат: cos({angle}) = {res}')