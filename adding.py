from base import *


def adding_to_the_beginning():
    text = (input('Какой текст в начале добавить: '))
    for file in listdir(path=path_to_file):
        if file == name_dir:
            continue
        else:
            rename(path_to_file + file, path_to_file + text + file)
    completed()


def adding_to_the_end():
    text = (input('Какой текст в конце добавить: '))
    for file in listdir(path=path_to_file):
        if file == name_dir:
            continue
        else:
            point = file.find('.')
            rename(path_to_file + file, path_to_file + file[:point] + text + file[point:])
    completed()