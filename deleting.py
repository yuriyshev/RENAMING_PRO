from base import *


def deleting_from_the_beginning():
    sym = int(input('Сколько символов в начале убрать: '))
    count = 1
    files = []
    for file in listdir(path=path_to_file):
        if file == name_dir:
            continue
        else:
            new_name = file[sym:]
            point = file.rfind('.')
            if new_name in files:
                changed_new_name = file[sym:point] + ' ' + str(count) + file[point:]
                count += 1
                rename(path_to_file + file, path_to_file + changed_new_name)
                files.append(new_name)
            else:
                rename(path_to_file + file, path_to_file + new_name)
                files.append(new_name)
    completed()


def deleting_from_the_end():
    sym = int(input('Сколько символов в конце убрать: '))
    count = 1
    files = []
    for file in listdir(path=path_to_file):
        if file == name_dir:
            continue
        else:
            point = file.find('.')
            new_name = file[:len(file) - sym - len(file[point:])] + file[point:]
            if new_name in files:
                changed_new_name = file[:len(file) - sym - len(file[point:])] + ' ' + str(count) + file[point:]
                count += 1
                rename(path_to_file + file, path_to_file + changed_new_name)
                files.append(new_name)
            else:
                rename(path_to_file + file, path_to_file + new_name)
                files.append(new_name)
                print(file)
    completed()
