import os, shutil
import copy

curr_dir = os.getcwd() + f'\\task6'
shop1 = '\\shop1.txt'
shop2 = '\\shop2.txt'

if not os.path.exists(curr_dir + '\\shop_max.txt'):
    open(curr_dir + '\\shop_max.txt', 'tw').close()

with open(curr_dir + shop1, encoding='utf-8') as shop1_file, \
        open(curr_dir + shop2, encoding='utf-8') as shop2_file:
    goods = [product.split() for product in shop1_file.readlines()]
    shop1_dict = { product[0] : int(product[1]) for product in goods }
    goods = [product.split() for product in shop2_file.readlines()]
    shop2_dict = { product[0] : int(product[1]) for product in goods }
print(shop1_dict)
print(shop2_dict)

if len(shop1_dict) < len(shop2_dict):
    shop1_dict, shop2_dict = shop2_dict, shop1_dict

shop_max = {}
for product in shop1_dict:
    if shop2_dict.get(product) is not None:
        if shop1_dict[product] >= shop2_dict[product]:
            shop_max[product] = shop1_dict[product]
        else:
            shop_max[product] = shop2_dict[product]
        shop2_dict.pop(product)
    else:
         shop_max[product] = shop1_dict[product]
else:
    shop_max.update(shop2_dict)

with open(curr_dir + '\\shop_max.txt', 'w', encoding='utf-8') as shop_max_file:
    for key, item in shop_max.items():
        shop_max_file.write(f'{key} {item}\n')
