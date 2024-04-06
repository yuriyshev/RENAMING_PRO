from base import *
from exif import Image


def renaming_with_exif():
    warning = input('Вы выбрали переименование с помощью метаданных.\nНажмите ENTER для продолжения')
    dates = [] # сюда попадут имена, основанные на дате съемки снимка  
    count = 1

    for i in files:
        i = path_to_file + i

        with open(i, 'rb') as file:
            file = Image(file)

            if file.has_exif:
                datetime = file.datetime_original
                datetime = str(datetime).replace(':', '').replace(' ', '_')

                if datetime in dates:
                    datetime = datetime[:9] + (str(int(datetime[9:]) + count)) # есть переменная счетчик, которая гарантирует что не будет одинаковых имен (если такие попадаютс, то увеличивает каждый следующий на 1)
                    print(datetime)
                    dates.append(str(datetime))
                    count += 1

                else:
                    dates.append(datetime)

    
    for i in range(len(files)):
        rename(path_to_file + files[i], path_to_file + dates[i] + '.jpg')
    completed()