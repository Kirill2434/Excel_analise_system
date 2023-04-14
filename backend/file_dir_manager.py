import os
import shutil
from pathlib import Path
from collections import Counter

from settings import file_path_regions, group_dir, xlsx_file, xls_files


def add_hyphen(path):
    """Функция добавляет деффис в начале имени файла.

    @param path: путь до папки с файлами
    """
    try:
        # вывод наименование папок в директории
        for file_dir in os.listdir(path):
            # вывод наименование файлов в папках
            for file_name in os.listdir(fr'{file_path_regions}\{file_dir}'):
                try:
                    # если '_' отсутвует в начале наименования файла, добавляем '_'
                    if file_name.split('.')[-1] == 'xlsx':
                        if file_name[0] != '_':
                            os.rename(fr'{file_path_regions}\{file_dir}\{file_name}',
                                      fr'{file_path_regions}\{file_dir}\_{file_name}')
                        else:
                            pass
                except Exception as error:
                    return error
    except Exception as error:
        return f'Ошибка {error} в функции {add_hyphen.__name__}'


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
            for file_name in os.listdir(fr'{file_path_regions}\{file_dir}'):
                try:
                    # если после '.' расширение файла xlsx, то добавляем к имени файл, имя папки
                    if file_name.split('.')[-1] == 'xlsx':
                        os.rename(fr'{file_path_regions}\{file_dir}\{file_name}',
                                  fr"{file_path_regions}\{file_dir}\{file_name.split('.')[0]}_{file_dir}.xlsx")
                    # если после '.' расширение файла xls, то добавляем к имени файл, имя папки
                    if file_name.split('.')[-1] == 'xls':
                        os.rename(fr'{file_path_regions}\{file_dir}\{file_name}',
                                  fr"{file_path_regions}\{file_dir}\{file_name.split('.')[0]}_{file_dir}.xls")
                # если в папке лежит подпапка, то ловим ошибку и добавляем ее в соварь
                except IndexError as error:
                    miss_files[file_name] = error
                    pass
    except Exception as error:
        return f'Ошибка {error} в функции {rename_file_by_folder_name.__name__}'
    if len(miss_files) == 0:
        pass
    else:
        print(miss_files)
    return 'Файлы переименованы.'


# def duplicate_region_number():
#     """Функция находит повторы файлов в итоговой папке
#     и возвращает наименование повторяющихся регионов
#
#     @return: список из наименований файлов
#     """
#
#     duplicate_files = []
#     all_files_duplicate = []
#     try:
#         for value_double in os.listdir(fr'C:\{group_dir}\{xlsx_file}'):
#             region_number = value_double.split('_')[1]
#
#             all_files_duplicate.append(region_number)
#         duplicate = Counter(all_files_duplicate)
#         for reg_num, count_of_repeats in duplicate.items():
#             if count_of_repeats > 1:
#                 duplicate_files.append(reg_num)
#     except Exception as error:
#         return f'Ошибка {error} в функции {duplicate_region_number.__name__}'
#     return duplicate_files


def replace_files(path):
    """ Функция копирует файлы расширения xlsx и xls из нескольких папок
    с учетом возможного дублирования файлов в разных папках, при наличие дубликатов программа
    останавливает свое выполнение.

    @param path: путь к папкам с файлами
    @return: возвращает сообщение -> 'Файлы скопированы.' или 'Есть повторы! Нельзя копировать файлы.'
    """
    all_files = []
    duplicate_files = []
    all_files_duplicate = []
    try:
        for file_dir in os.listdir(path):
            # вывод наименование файлов в папках
            for file_name in os.listdir(fr'{file_path_regions}\{file_dir}'):
                if file_name.split('.')[-1] == 'xlsx':
                    all_files.append(file_name)
    except Exception as error:
        return f'Ошибка чтении файлов {error} в функции {replace_files.__name__}'
    for excel_path in Path(path).glob(r'**\*.xlsx'):
        shutil.copy(excel_path, fr'C:\{group_dir}\{xlsx_file}')
    for excel_path in Path(path).glob(r'**\*.xls'):
        shutil.copy(excel_path, fr'C:\{group_dir}\{xls_files}')
    # в итоговой папке удаляем все дубликаты файлов со статусом 'после'
    try:
        for value_double in os.listdir(fr'C:\{group_dir}\{xlsx_file}'):
            region_number = value_double.split('_')[1]
            all_files_duplicate.append(region_number)
        duplicate = Counter(all_files_duplicate)
        for reg_num, count_of_repeats in duplicate.items():
            if count_of_repeats > 1:
                duplicate_files.append(reg_num)
    except Exception as error:
        return f'Ошибка дублях {error} в функции {replace_files.__name__}'
    try:
        for file in os.listdir(fr'C:\{group_dir}\{xlsx_file}'):
            date_status_file = file.split('_')[3].split(' ')
            if file.split('_')[1] in duplicate_files:
                if date_status_file[1] == 'после':
                    os.remove(fr'C:\{group_dir}\{xlsx_file}\{file}')
    except Exception as error:
        return f'Ошибка в удалении дублей {error} в функции {replace_files.__name__}'
    return fr'Файлы скопированы в "C:\{group_dir}".'


# print(rename_file_by_folder_name(file_path_regions))
# print(replace_files(file_path_regions))

def rename_and_replace(path):
    for file in os.listdir(fr'C:\{group_dir}\{xlsx_file}'):
        if ('после' or 'до') in file.split(' ')[1]:
            return 'Файлы уже переименованы'
    rename_file_by_folder_name(path)
    replace_files(path)
    for file in os.listdir(fr'C:\{group_dir}\{xls_files}'):
        if len(file) != 0:
            return fr'Файлы скопированы в "C:\{group_dir}".' \
                   fr' ' \
                   fr'Есть файлы в fr"C:\{group_dir}\{xls_files}"'
        else:
            pass
    return fr'Файлы скопированы в "C:\{group_dir}".'


def clean_dirs():
    try:
        for file_dir in os.listdir(fr'{file_path_regions}'):
            os.rmdir(fr'{file_path_regions}\{file_dir}')
        for file in os.listdir(fr'C:\{group_dir}\{xlsx_file}'):
            os.remove(fr'C:\{group_dir}\{xlsx_file}\{file}')
        for file in os.listdir(fr'C:\{group_dir}\{xls_files}'):
            os.remove(fr'C:\{group_dir}\{xls_files}\{file}')
    except FileNotFoundError:
        return 'Все файлы и папки удалены!'
    except OSError:
        for file_dir in os.listdir(fr'{file_path_regions}'):
            for file_name in os.listdir(fr'{file_path_regions}\{file_dir}'):
                os.remove(fr'{file_path_regions}\{file_dir}\{file_name}')
            os.rmdir(fr'{file_path_regions}\{file_dir}')
        for file in os.listdir(fr'C:\{group_dir}\{xlsx_file}'):
            os.remove(fr'C:\{group_dir}\{xlsx_file}\{file}')
        for file in os.listdir(fr'C:\{group_dir}\{xls_files}'):
            os.remove(fr'C:\{group_dir}\{xls_files}\{file}')
        return 'Все файлы и папки удалены!'
    return 'Все файлы и папки удалены!'


# print(rename_and_replace(file_path_regions))
# print(clean_dirs())
