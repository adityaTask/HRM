import csv
import os


def get_csv_data(file):
    print(os.getcwd())
    f = open(file, 'r')
    reader = csv.reader(f)
    next(reader)
    data = list(reader)
    f.close()
    return data


def get_proj_dir():
    cur_dir = os.path.abspath(os.curdir)
    root_dir = []
    for i in cur_dir.split('\\'):
        if i !='HRM':
            root_dir.append(i)
        else:
            break
    return '\\'.join(root_dir)

