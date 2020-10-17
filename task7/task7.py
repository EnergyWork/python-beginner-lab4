import os
import json

# add country product weight
# list -> список всех стран и их экспорта
# export -country name -> выведет список товаров, экспортируемых страной name
# export -product name -> выведет список стран, экспортирующих товар name
# exit

def read_file(file, isjson=False):
    if isjson:
        with open(file, encoding='utf-8') as json_file:
            return json.load(json_file)

    data = {}
    with open(file, encoding='utf-8') as f:
        rows = f.readlines()
        for row in rows:
            info = row.split() # country product weight
            if data.get(info[0]) is None:
                data[info[0]] = { info[1] : info[2] }
            else:
                 data[info[0]].update({ info[1] : info[2] })
    return data

def save_exports(isjson=False):
    if isjson:
        with open(EXPORTS_FILE, 'w', encoding='utf-8') as f:
            json.dump(exports, f, ensure_ascii=False)

def print_country_and_products(country, products):
    print(f'{country}:')
    for product, weight in products.items():
        print(f'   {product} - {weight}')

def print_exports():
    for country, products in exports.items():
        print_country_and_products(country, products)
        print('-' * 40)

def print_products_of_country(country, splt):
    for country, products in exports.items():
        if country == splt[2]:
            print_country_and_products(country, products)

def print_countries_of_product(product):
    print(f'{product}:')
    for country, products in exports.items():
        for product_, weight in products.items():
            if product_ == product:
                print(f'   {country} - {weight}')

def add_export(country, product, weight):
    if exports.get(country) is not None: # если такая страна уже есть в экспорте
        if exports[country].get(product) is not None: # и есть такой продукт
            exports[country][product] += int(weight) # то добавить экспорта
        else: # а если нет такого продукта
            exports[country].update({ product : int(weight) }) # то добавить новый экспорт
    else: # иначе такой страны нет и её надо добавить вместе с её экспортом
        exports.update({ country : { product : int(weight) } })

EXPORTS_FILE = os.getcwd() + '\\task7\\input.json'
exports = read_file(EXPORTS_FILE, isjson=True)

def main():
    print(exports)
    while True:
        cmd = input('Введите команду > ')
        if cmd == 'exit':
            save_exports(isjson=True)
            exit(0)
        splt = cmd.split()
        if splt[0] not in ['add', 'list', 'export']:
            print('Неверная команда')
            continue 
        # вывод полного списка экспорта
        if splt[0] == 'list':
            if len(splt) == 1:
                print_exports()
            else:
                print('Неверный формат команды list')
        # вывод нужного экспорта по стране или продукту
        elif splt[0] == 'export':
            if splt[1] == '-country':
                print_products_of_country(splt[2], splt)
            elif splt[1] == '-product':
                print_countries_of_product(splt[2])
            else:
                print('Неверный формат команды export')
                continue
        # добавление нового экспорта
        elif splt[0] == 'add':
            if 4 > len(splt) > 5:
                print('Неверный формат команды add')
                continue
            else:
                add_export(splt[1], splt[2], splt[3])

if __name__ == "__main__":
    main()
