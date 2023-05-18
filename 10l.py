import json
file = "eda.json"
try:
    with open(file) as f:
        data = json.load(f)
except FileExistsError:
    data = {"eda": []}
    edda = {}
    edda['name'] = input("Введите название продукта: ")
    edda['price'] = int(input("Введите цену продукта: "))
    edda['available'] = input(" Есть ли продукт в наличии? (да или нет): ").lower() == 'да'
    edda['weight'] = int(input("Введите вес продукта: "))
    data['eda'].append(edda)
    with open(file, 'w') as f:
        json.dump(data, f)
    eda = data['products']
    for edda in eda:
        print("Название:", edda['name'])
        print("Цена:", edda['price'])
        print("Вес:", edda['weight'])
        if edda['available']:
            print("Есть наличии")
        else:
            print("Нет в наличии")
        print()

def lab1():
    with open("en-ru.txt", "r") as file:
        lines = file.readlines()
    w = {}
    for line in lines:
        key_value = line.strip().split(" - ")
        key = key_value[1]
        values = key_value[0].split(" , ")
        w[key] = values
    sorted_keys = sorted(w.keys())
    sorted_values = []
    for key in sorted_keys:
        values = w[key]
        for value in values:
            sorted_values.append(value)
    with open("ru-en.txt", "w") as file:
        for key in sorted_keys:
            values = w[key]
            for value in values:
                file.write(key + " - " + value + "\n")


lab1()



