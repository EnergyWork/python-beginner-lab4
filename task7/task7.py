import os
import json

# add country product weight
# list
# export -country name
# export -product name
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
        
EXPORTS_FILE = os.getcwd() + '\\task7\\input-json.txt'
exports = read_file(EXPORTS_FILE, isjson=True)
print(exports)

while True:
    cmd = input('Введите команду > ')
    if cmd == 'exit':
        exit(0)
    
    