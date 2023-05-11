import os

import pandas as pd

from pathlib import Path

from backend.exeptions import EmptyException
from backend.utils import record_to_excel, head_of_table
from settings import group_dir, xlsx_file


def check_directory():
    """Проверка директории на наличие папок source_data и generation_results. """

    directory_list = [r'C:\source_data', r'C:\generation_results',
                      r'C:\Приложения регионов', r'C:\Сгруппированные файлы',
                      r'C:\Сгруппированные файлы\xlsx файлы', r'C:\Сгруппированные файлы\xls файлы']
    result = []
    for directory in directory_list:
        if os.path.exists(directory):
            print(f'Папка {directory}- уже есть!')
            continue
        else:
            try:
                if directory not in os.getcwd():
                    while True:
                        print(f'Папка {directory} - отсутсвует!')
                        print(f'Создаю папку >>> {directory}\n')
                        os.mkdir(directory)
                        break
                else:
                    result.append(f'Папка {directory} в директори {os.getcwd()} - найдена!')
            except (FileNotFoundError, FileExistsError):
                continue
    return 'Все необходимые папки - созданы!'


# print(check_directory())


def check_source_data():
    """Проверка директории "source_data" на наличие исходных файлов. """

    directory = r'C:\source_data'
    source_files = ['re.xlsx', 'main.xlsx']
    list_of_dir = []
    list_of_ideal = []
    files = os.listdir(directory)
    for file_in_dir in files:
        list_of_dir.append(file_in_dir)
    for file_need in source_files:
        list_of_ideal.append(file_need)
    try:
        if len(files) == 0:
            raise EmptyException(f'В папку {directory} необходимо добавить файлы!')
        else:
            result = list(set(list_of_dir) ^ set(list_of_ideal))
            if not result:
                pass
            else:
                return f'Нужно исправить: \n{result}'
    except Exception as error:
        return f'Ошибка {error} в функции {check_source_data.__name__}'
    return 'Все файлы прошли проверку'


def check_sheets(*, sheet_name: str = 'Лист1'):
    """Функция по провекре листов, на несоответсвие наименованию листа по умолчанию
    выводит отчет с именем неккоректного файла и наименованиями его листов.

    :param sheet_name: наименование листа по умолчанию
    :return: 'текст' или сообщение об ошибке
    """

    incorrect_files = {}
    for file in os.listdir(fr'C:\{group_dir}\{xlsx_file}'):
        df = pd.ExcelFile(fr'C:\{group_dir}\{xlsx_file}\{file}')
        file_name = Path(df).name
        sheet = df.sheet_names
        if len(sheet) > 1:
            incorrect_files[file_name] = sheet
        if len(sheet) < 2 and sheet != [sheet_name]:
            incorrect_files[file_name] = sheet
    if len(incorrect_files) == 0:
        return 'Проверка листов, выполнена. Ошибки не обнаружены!'
    else:
        record_to_excel(incorrect_files, 'Sheet_check_report', 'Отчет о листах')
        return f'Проверка выполнена! Есть ошибки, см. отчет в Sheet_check_report.xlsx'


# print(check_sheets(all_files))


# @timemometr
def cheak_head_of_table(sum_of_head: int, *, sheet_name: str = 'Лист1'):
    """Функция проверяет шапку таблицы на соответсвие заданным параметрам, в аргументах мы указываем путь до файлов
    и численный диапазон, который представляет из себя эталанную численную шапку, с которой мы сравниваем шапки
    входящих файлов.

    :param paths: путь к файлам
    :param sum_of_head: сумма столбцов, должна совпсть с суммой шапки файлов
    :param sheet_name: имя проверяемого листа, по умолчанию Лист1
    :return: 'текст'
    """
    final_dict = {}
    unreadable_file = []
    sum_of_head = list(range(1, sum_of_head + 1))
    try:
        for file in os.listdir(fr'C:\{group_dir}\{xlsx_file}'):
            df = pd.ExcelFile(fr'C:\{group_dir}\{xlsx_file}\{file}')
            file_name = Path(df).name
            try:
                for row_col_ind, head in head_of_table(fr'C:\{group_dir}\{xlsx_file}\{file}', sheet_name).items():
                    if head != sum_of_head:
                        final_dict[file_name] = head
                    elif row_col_ind != (10, 1):
                        final_dict[file_name] = row_col_ind
                    else:
                        pass
            except ValueError:
                unreadable_file.append(fr'C:\{group_dir}\{xlsx_file}\{file}')
                record_to_excel(unreadable_file, 'НЕ ЧИТИЕМЫЕ ФАЙЛЫ', 'Не читаемые файлы')
                pass
    except FileNotFoundError:
        return 'Файл не найден!'
    except PermissionError as error:
        return f'Зайкроте файл: {error}'
    if len(unreadable_file) != 0:
        return 'Есть не читаеые файлы!'
    if len(final_dict) != 0:
        record_to_excel(final_dict, 'Head_check_report', 'Ошибка в шапке')
        return f'Проверка выполнена, есть ошибки! См отчет в Head_check_report'
    else:
        return f'Проверка выполнена! Ошибок нет.'


# print(head_of_table(36))
