from base import *
from extension import *

hours = []
others = []
# dates = []

def spec_printing(lst: list):
    for file in lst:
        print(file)


def special_renaming():
    print('Добро пожаловать в специальное переименование\n')

    for file in files:
        border = file.find('_')
        point = file.rfind('.')

        hour = file[border+1:border+3]
        hours.append(hour)

        other = file[border+7:point]
        others.append(len(other))

    if len(set(others)) == 1:
        changing = int(input('На сколько часов изменить время съемки, откинув лишнее: '))

        for file in files:
            border = file.find('_')
            point = file.rfind('.')
            
            hour = file[border+1:border+3]
            rename(path_to_file + file, path_to_file + file[:border+1] + str(int(hour)+changing) + file[border+3:border+7] + file[point:])
    
    elif len(set(others)) > 1:
        print('\nОперация невозможна, так как остаток после времени съемки у файлов разный\n')

    else:
        print('Какая то еще ошибка')





 
    


    # for file in files:
    #     border = file.find('_')
    #     date = file[:border]
    #     dates.append(date)

        




