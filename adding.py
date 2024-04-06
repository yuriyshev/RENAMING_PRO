from base import *



def adding_to_the_beginning():
    text = (input('Какой текст в начале добавить: '))
    for file in files:
        rename(path_to_file + file, path_to_file + text + file)
    scan_files()
    printing(files)
    completed()


def adding_to_the_end():
    text = (input('Какой текст в конце добавить: '))
    for file in files:
        point = file.find('.')
        rename(path_to_file + file, path_to_file + file[:point] + text + file[point:])
    scan_files()
    printing(files)
    completed()