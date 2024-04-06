from base import *
import datetime


for file in listdir(path=path_to_file):
    if file == name_dir:
        continue
    file = path_to_file + file
    cr_date = str(datetime.datetime.fromtimestamp(path.getctime(file)))
    point = cr_date.find('.')
    cr_date = cr_date[:point]
    cr_date = cr_date.replace('-', '').replace(':', '').replace(' ', '_')
    print(cr_date)





# def create_time(num: int):
#     file = path_to_file + files[num-1]
#     cr_date = str(datetime.datetime.fromtimestamp(path.getctime(file)))
#     point = cr_date.find('.')
#     cr_date = cr_date[:point]
#     cr_date = cr_date.replace('-', '').replace(':', '').replace(' ', '_')
#     return cr_date

# scan_files()

# nums = []
# num = 1

# for file in files:
#     nums.append(num)
#     num += 1

# print('Выберите нужный файл с помощью соответсвующих цифр\n')
# for file, num in zip(files, nums):
#     print(f'{num} - {file}')

# num = int(input('\nПисать сюда: '))

# if num in nums:
#     print(f'{nums[num-1]} - {files[num-1]}\n')
#     continuate = input('Если выбор верный, нажмите 1 и ENTER чтобы продолжить: ')

#     if continuate == '1':
#         print(create_time(num))
#         completed()
        
#     else:
#         incorrect_input()

# else:
#     incorrect_input()




