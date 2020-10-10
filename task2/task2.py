import random
import os

def lets_play(guys):
    print('Поиграем в игру! Угадай друга!')
    print('Я тебе его любимую вещь, ты мне как его зовут')
    guy = random.choice(list(guys.keys()))
    categories = list(guys[guy].keys())
    while True:
        category = random.choice(categories)
        categories.remove(category)
        print('-' * 30)
        print(category,': ', guys[guy][category], sep='', end='\n')
        answer = input('Кто это? > ')
        if answer != guy:
            if len(categories) == 0:
                print('-' * 30)
                print(f'Ты не смог угадать. Это был {guy}, твой друг...')
                break
            else:
                print('Неверно')
                continue
        else:
            print('-' * 30)
            print(f'Верно! Это тот самый {guy}!')
            break


def main():
    txt_files = list(filter(lambda file: file.endswith('.txt'), os.listdir('./task2')))
    guys = {}
    for file in txt_files:
        dude = {}
        with open(f'./task2/{file}', encoding='utf-8') as f:
            rows = [row.rstrip('\n') for row in f.readlines()]
        i = 0
        while i < len(rows):
            if i == 0:
                guy = f'{rows[i+1]} {rows[i+3]}'
                i += 4
                continue
            dude[rows[i]] = rows[i+1]
            i += 2
        guys[guy] = dude
    print(guys)
    lets_play(guys)


if __name__ == "__main__":
    main()
