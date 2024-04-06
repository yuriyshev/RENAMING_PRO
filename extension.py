from base import *


def extension(file):
    point = file.rfind('.')
    ex = file[point+1:]
    return ex
    

def scan_extensions():
    for file in listdir(path=path_to_file):
        if file == name_dir:
             continue
        else:
            ex = extension(file)
            if ex in extensions:
                continue
            else:
                extensions.append(ex)


def scan_files_with_extension(extn: str):
    for file in listdir(path=path_to_file):
        if file == name_dir:
            continue       
        elif extension(file) == extn:
             files.append(file)
    print('\nСканирование файлов, выбранного расширения, выполнено!\n')


def show_extension():
    scan_extensions()
    print('В папке имеются файлы со следующими расширениями:')
    for i in extensions:
        print(i)
    print()


def change_extension():
    for i in listdir(path='..'):
        if i == name_dir:
            continue
        else:
            files.append(i)
    print()        
    old_extansion = input('Введите расширение без точки, которое хотите изменить: ')
    new_extansion = input('Введите расширение без точки, которое хотите получить: ')

    for i in files:
            point = i.find('.')
            if i[point+1:] == old_extansion:
                    rename(path_to_file+i[:point+1]+old_extansion,path_to_file+i[:point+1]+new_extansion)
            else:
                    continue
    scan_files()
    printing(files)
    completed()


    

