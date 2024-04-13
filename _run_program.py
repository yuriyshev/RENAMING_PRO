from base import *
from extension import *
from choise import *


print(f'\n Приветствую в главном меню программы - {name_dir}\n')
continuation = input('ENTER для продолжения\n')

scan_extensions()


if len(extensions) > 1:

    show_extension()
    choose_an_extension = input('Введите расширение, с которым нужно работать\n1 - чтобы изменить расширение: ')

    if choose_an_extension == '1':
        change_extension()

    elif choose_an_extension in extensions:
        scan_files_with_extension(choose_an_extension)
        printing(files)
        choose(choose_an_extension)

    else:
        incorrect_input()
else:
    printing_files()
    choose(extensions[0])













            
        




        

