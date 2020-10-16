import os, shutil
import datetime as dt

curr_dir = os.getcwd() + '\\task5'
files = list(filter(lambda x: x != __file__.split('\\')[-1], os.listdir(curr_dir)))

for file in files:
    path_to_file = curr_dir + f'\\{file}'
    date = dt.datetime.fromtimestamp(os.path.getmtime(path_to_file))
    date = '.'.join(reversed(str(date).split()[0].split('-')))
    try:
        os.mkdir(curr_dir + f'\\{date}')
    except OSError:
        pass
    finally:
        new_path = shutil.move(curr_dir + f'\\{file}', curr_dir + f'\\{date}')
