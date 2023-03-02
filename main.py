f = input()
c = input()
if f == 'красный' and 'красный':
    print("красный")
else:
    if f == 'синий' and c == 'красный' or f == 'красный' and c == 'синий':
        print("Фиолетовый")
    else:
        if f == 'красный' and c == 'желтый' or f == 'желтый' and c == 'красный':
            print("оранжевый")
        else:
            if c == 'синий' and 'синий':
                print("синий")
            else:
                if c == 'синий' and f == 'желтый' or c == 'желтый' and f == 'синий':
                    print("зеленый")
                else:
                    if c == 'желтый' and 'желтый':
                        print("желтый")
                    else:
                        print("нет такого цвета")

def q2():
    "проверка пароля"
    a = input()
    b = input()
    if a == b:
        print('пароль совпадает')
    else:
        print('пароль не совпадает')

def q3():
    n = int(input("Введите номер места в плацкартном вагоне:"))
    print()
    if n > 36:
        print('боковое место')
    elif n % 2:
        print('нижнее место')
    else:
        print('верхнее место')

def q4():
    age = int(input('Введите год'))
    print()
    if age % 4 == 0 and age % 100 != 0 and age % 400:
        print(age, 'год високосный')
    else:
        print('год не високосный')


q2(), q3(), q4()