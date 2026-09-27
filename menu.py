#import
#import
#import
class NotCalculaterFunction(Exception):
    pass
class Nothing(Exception):
    pass

def menu():
    while True:
        print("введите желаемую функцию (цифрой от 1 до 3):")
        print("    1. Калькулятор чисел") 
        print("    2. Калькулятор строк")
        print("    3. Длинная арифметик")
        try:
            a=int(input())
            if a<1 or a>3:
                raise NotCalculaterFunction
            if a==1:
                raise Nothing
            if a==2:
                raise Nothing
            if a==3:
                raise Nothing
        except TypeError:
            print("ошибка: неверный тип данных\nесли вы желаете воспользоваться калькулятором то")
        except ValueError:
            print("ошибка: неверный тип данных\nесли вы желаете воспользоваться калькулятором то")
        except NotCalculaterFunction:
            print("ошибка: несушествующая функция калкулятора\nесли вы желаете воспользоваться калькулятором то")
        except Nothing:
            print("никто не сделал эту функцию, но спасибо за оплату")