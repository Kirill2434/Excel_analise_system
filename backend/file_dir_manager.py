import os
import shutil
from pathlib import Path
from collections import Counter


file_path = r'C:\Приложения регионов'
group_dir = 'Сгруппированные файлы'
xlsx_file = 'xlsx файлы'
xls_files = 'xls файлы'


def add_hyphen(path):
    # вывод наименование папок в директории
    for file_dir in os.listdir(path):
        # вывод наименование файлов в папках
        for file_name in os.listdir(fr'{file_path}\{file_dir}'):
            try:
                # если '_' отсутвует в начале наименования файла, добавляем '_'
                if file_name.split('.')[-1] == 'xlsx':
                    if file_name[0] != '_':
                        os.rename(fr'{file_path}\{file_dir}\{file_name}',
                                  fr'{file_path}\{file_dir}\_{file_name}')
                    else:
                        pass
            except Exception as error:
                return error


def rename_file_by_folder_name(path):
    """ Функция принимает путь к директории в которой лежат папки с файлами.
    Далее функция заходит в каждую папку, считывает имя папки и переименовывает файлы внутри
    активной папки добавляя к имени файла, имя папки.

    @param path: путь к папкам с файлами
    @return: возвращает сообщение -> 'Файлы переименованы.'
    """
    miss_files = {}
    add_hyphen(path)
    try:
        # вывод наименование папок в директории
        for file_dir in os.listdir(path):
            # вывод наименование файлов в папках
            for file_name in os.listdir(fr'{file_path}\{file_dir}'):
                try:
                    # если после '.' расширение файла xlsx, то добавляем к имени файл, имя папки
                    if file_name.split('.')[-1] == 'xlsx':
                        os.rename(fr'{file_path}\{file_dir}\{file_name}',
                                  fr"{file_path}\{file_dir}\{file_name.split('.')[0]}_{file_dir}.xlsx")
                    # если после '.' расширение файла xls, то добавляем к имени файл, имя папки
                    if file_name.split('.')[-1] == 'xls':
                        os.rename(fr'{file_path}\{file_dir}\{file_name}',
                                  fr"{file_path}\{file_dir}\{file_name.split('.')[0]}_{file_dir}.xls")
                # если в папке лежит подпапка, то ловим ошибку и добавляем ее в соварь
                except IndexError as error:
                    print('Есть ошибка!')
                    miss_files[file_name] = error
                    pass
    except Exception as error:
        return error
    if len(miss_files) == 0:
        pass
    else:
        print(miss_files)
    return 'Файлы переименованы.'


def duplicate_region_number():
    """Функция находит повторы файлов в итоговой папке
    и возвращает наименование повторяющихсярегионов

    :return: список
    """

    duplicate_files = []
    all_files_duplicate = []
    try:
        for value_double in os.listdir(fr'C:\{group_dir}\{xlsx_file}'):
            region_number = value_double.split('_')[1]

            all_files_duplicate.append(region_number)
        duplicate = Counter(all_files_duplicate)
        for reg_num, count_of_repeats in duplicate.items():
            if count_of_repeats > 1:
                duplicate_files.append(reg_num)
    except Exception as error:
        return error
    return duplicate_files


def replace_files(path):
    """ Функция копирует файлы расширения xlsx и xls из нескольких папок
    с учетом возможного дублирования файлов в разных папках, при наличие дубликатов программа
    останавливает свое выполнение.

    @param path: путь к папкам с файлами
    @return: возвращает сообщение -> 'Файлы скопированы.' или 'Есть повторы! Нельзя копировать файлы.'
    """

    all_files = []
    try:
        if os.path.exists(fr'C:\{group_dir}') is False:
            os.makedirs(fr'C:\{group_dir}\{xlsx_file}')
            os.makedirs(fr'C:\{group_dir}\{xls_files}')
        else:
            pass
        for file_dir in os.listdir(path):
            # вывод наименование файлов в папках
            for file_name in os.listdir(fr'{file_path}\{file_dir}'):
                if file_name.split('.')[-1] == 'xlsx':
                    all_files.append(file_name)
        for excel_path in Path(path).glob(r'**\*.xlsx'):
            shutil.copy2(excel_path, fr'C:\{group_dir}\{xlsx_file}')
        for excel_path in Path(path).glob(r'**\*.xls'):
            shutil.copy2(excel_path, fr'C:\{group_dir}\{xls_files}')
        # в итоговой папке удаляем все дубликаты файлов со статусом 'после'
        for file in os.listdir(fr'C:\{group_dir}\{xlsx_file}'):
            date_status_file = file.split('_')[3].split(' ')
            if file.split('_')[1] in duplicate_region_number():
                if date_status_file[1] == 'после':
                    os.remove(fr'C:{group_dir}\{xlsx_file}\{file}')
    except Exception as error:
        return error
    return 'Файлы скопированы.'


# print(rename_file_by_folder_name(file_path))
# print(replace_files(file_path))
