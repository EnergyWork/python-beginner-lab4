import os, shutil

TASK4 = '\\task4'
NEW_DIR = '\\X-copy'
DIR = '\\X'

def main():
    curr_dir = os.getcwd() + TASK4
    print(curr_dir)
    if not os.path.exists(curr_dir + NEW_DIR):
        shutil.copytree(curr_dir + DIR, curr_dir + NEW_DIR)

    lvl = 1
    for root, dirs, files in os.walk(curr_dir + NEW_DIR):
        print(f'Level {lvl}', root, dirs, files)
        for file in list(filter(lambda ext: ext.endswith('.txt'), files)):
            with open(root + f'\\{file}', 'r') as fr:
                strs = fr.readlines()
            with open(root + f'\\{file}', 'w') as f:
                f.write(str(len(strs)) + '\n')
                f.writelines(strs)
                f.write('\n' + str(lvl))
        lvl += 1

if __name__ == "__main__":
    main()
