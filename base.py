from os import listdir, rename, path

module_name = path.basename(__file__)

name_dir = __file__[:__file__.rfind('\\')]
name_dir = name_dir[-1:name_dir.rfind('\\'):-1]
name_dir = name_dir[::-1]

path_to_file = __file__.replace(name_dir+'\\', '').replace('\\', '//').replace(module_name, '') # getting path to files in current directory (without file name)

extensions = []

def printing_files():
    count = 0
    print('Имеются следующие файлы:\n')
    for file in listdir(path=path_to_file):
        if file == name_dir:
            continue
        else:
            print(file)
            count += 1
    print(f'\nВ общей сложности просканировано и отобрано для работы - {count} файлов\n')


def completed():
    print('Выполнено') 
    stop = input('ENTER for exit')


def incorrect_input():
    print('\n' + 'Некорректный ввод!' + '\n')
    stop = input('ENTER for exit')


