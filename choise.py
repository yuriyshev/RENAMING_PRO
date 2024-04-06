from deleting import *
from adding import *
from witn_exif import *
from extension import *
from special import *

def choose(extension: str):
    print(f'\nРаботаем с расширением: {extension}\n')

    if extension == 'jpg' or extension == 'jpeg':
        choise = input('''Введите: 
        1 - если хотите убрать текст из названия, 
        2 - если хотите добавить текст в название, 
        3 - чтобы изменить расширение
        4 - чтобы переименовать фото в соответсвии с датой и временем съемки,
        : ''')

    elif extension == 'mp4':
        choise = input('''Введите: 
        1 - если хотите убрать текст из названия, 
        2 - если хотите добавить текст в название,
                        
        3 - чтобы изменить расширение,
                       
        0 - для специального переименования (нужно знать как работает чтобы использовать)
        : ''')

    else:
        choise = input('''Введите: 
        1 - если хотите убрать текст из названия, 
        2 - если хотите добавить текст в название,
                        
        3 - чтобы изменить расширение
        : ''')


    if choise == '1':
        removing = input('\n' + '1 - чтобы убрать текст в начале,\n2 - чтобы убрать в конце: ')
        if removing == '1':
            deleting_from_the_beginning()         
        elif int(removing) == 2:
            deleting_from_the_end()
        else:
            incorrect_input()
    
    elif choise == '2':
        adding = input('\n' + '1 - чтобы добавить в начале названия,\n2 - чтобы добавить в конце: ')
        if adding == '1':
            adding_to_the_beginning()     
        elif adding == '2':
            adding_to_the_end()
        else:
            incorrect_input()

    elif choise == '3':
        change_extension()

    elif choise == '4':
        renaming_with_exif()
    
    elif choise == '0':
        special_renaming()

    else:
        incorrect_input()