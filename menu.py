import os
from num_16 import menu_strings
from menu_calculete_nums import menu_calc_numbers
#import    

class NotCalculaterFunction(Exception):
    pass
class Nothing(Exception):
    pass

def menu():
    while True:
        error=""
        print("введите желаемую функцию (цифрой от 1 до 3):")
        print("    1. Калькулятор чисел") 
        print("    2. Калькулятор строк")
        print("    3. Длинная арифметик")
        try:
            a=int(input())
            if a<1 or a>3:
                raise NotCalculaterFunction
            if a==1:
                menu_calc_numbers()
            if a==2:
                menu_strings()
            if a==3:
                raise Nothing
        except TypeError:
            error="ошибка: неверный тип данных\nесли вы желаете воспользоваться калькулятором то"
        except ValueError:
            error="ошибка: неверный тип данных\nесли вы желаете воспользоваться калькулятором то"
        except NotCalculaterFunction:
            error="ошибка: несушествующая функция калкулятора\nесли вы желаете воспользоваться калькулятором то"
        except Nothing:
            error="никто не сделал эту функцию, но спасибо за оплату"
        finally:
            if error:
                print("произошла ошибка (вернитесь чтобы узнать подробнее)")
            t=input("нажмите enter что бы вернуться")
            os.system('cls' if os.name == 'nt' else 'clear')
            print(error)
        
