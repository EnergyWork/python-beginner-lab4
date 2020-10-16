import os, shutil

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

shop_max = {}
for product in shop1_dict if len(shop1_dict) > len(shop2_dict) else shop2_dict:
    pass