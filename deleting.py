from base import *


def deleting_from_the_beginning():
    sym=int(input('Сколько символов в начале убрать: '))
    for file in files: 
        rename(path_to_file + file, path_to_file + file[sym:])
    scan_files()
    printing(files)
    completed()


def deleting_from_the_end():
    sym=int(input('Сколько символов в конце убрать: '))
    for file in files:               
        point = file.find('.')
        rename(path_to_file + file, path_to_file + file[:len(file)-sym-len(file[point:])] + file[point:])
    scan_files()
    printing(files)
    completed()