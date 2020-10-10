import re

def main():
    with open('.\\task1\\input.txt') as file:
        lines = [re.findall(r'\w+', line) for line in file.readlines()]
    mydict = {}
    for line in lines:
        for i in range(1, len(line)):
            if line[i] not in mydict:
                mydict[line[i]] = [line[0]]
            else:
                mydict[line[i]].append(line[0])
    with open('.\\task1\\output.txt', 'w') as file:
        sep = ', '
        for key, value in mydict.items():
            out = f'{key} - {sep.join(sorted(value))}\n'
            file.write(out)

if __name__ == "__main__":
    main()
