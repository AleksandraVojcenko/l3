def xz():

    class IceCreamStand:
        def __init__(self, name, flavors):
            self.name = name
            self.flavors = flavors
        def show_flavors(self):
            print("Список  сортов мороженого:")
            for flavor in self.flavors:
                print("- " + flavor)
    my_stand = IceCreamStand("Кафе-мороженное", ['пломбир', 'шоколадное', 'клубничное', 'с шоколадной крошкой'])
    my_stand.show_flavors()

def xz1():

    class IceCreamStand:
        def __init__(self, name, flavors, location, working_hours, type_flavors):
            self.name = name
            self.flavors = flavors
            self.location = location
            self.working_hours = working_hours
            self.type_flavors = type_flavors
        def show_flavors(self):
            print("Список сортов мороженого:")
            for flavor in self.flavors:
                print("- " + flavor)
        def add_flavor(self, flavor):
            self.flavors.append(flavor)
            print(f'Сорт {flavor} в списке')
        def remove_flavor(self, flavor):
            if flavor in self.flavors:
                self.flavors.remove(flavor)
                print(f'Сорт {flavor} удален из списка')
            else:
                print(f'Сорта {flavor} нет в списке')
        def check_flavor(self, flavor):
            if flavor in self.flavors:
                print(f'Сорт {flavor} в списке')
            else:
                print(f'Сорта {flavor} нет в списке')
        def describe_stand(self):
            print(f"Стенд мороженого: {self.name}")
            print(f"Место: {self.location}")
            print(f"Время работы: {self.working_hours}")
        def show_Typesflavors(self):
            print("Список типов мороженого:")
            for types in self.type_flavors:
                print("- " + types)
    my_stand = IceCreamStand("Лучшее, что было и есть в твоей жизни", ['ванильное', 'шоколадное', 'клубничное', 'пломбир'], 'Проспект Ветеранов', '08.00 - 15.00', ['нв палочке', 'в стаканчике', 'в креманке', '18+'])
    my_stand.describe_stand()
    my_stand.show_flavors()
    my_stand.show_Typesflavors()
    my_stand.check_flavor("клубничное")
    my_stand.check_flavor("с шоколадной крошкой")
    my_stand.add_flavor("с шоколадной крошкой")
    my_stand.check_flavor("с шоколадной крошкой")
    my_stand.remove_flavor("клубничное")
    my_stand.check_flavor("клубничное")

def xz2():

    class IceCreamStand:
        def __init__(self, name, flavors):
            self.name = name
            self.flavors = flavors
        def get_menu(self):
            menu = "Вкусное мороженое " + self.name + "\n"
            menu += "У нас есть  сорта:\n"
            for flavor in self.flavors:
                menu += "- " + flavor + "\n"
            return menu
    import tkinter as tk
    my_stand = IceCreamStand("Натуральное мороженое", ["пломбир", "шоколад", "банан"])
    root = tk.Tk()
    root.title("Натуральное мороженое")
    menu_label = tk.Label(root, text=my_stand.get_menu())
    menu_label.pack()
    root.mainloop()

xz(),xz1(),xz2()