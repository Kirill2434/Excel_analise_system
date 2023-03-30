import glob
import os

import pandas as pd
import openpyxl as op

from pathlib import Path

from tqdm import tqdm

from backend.Exeptions import EmptyException
from backend.utils import record_to_excel
from settings import CHECK_REPORT_FILE, all_files


def check_directory():
    """Проверка директории на наличие папок source_data и generation_results. """
    directory_list = [fr'C:\source_data', r'C:\generation_results']
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
        return error
    return 'Все файлы прошли проверку'


def head_of_table(path, sheet_name: str = 'Лист1'):
    """Функция определяет нахождение числовой шапки и выводит ее в список

    @param path: путь к файлам
    @param sheet_name: наименование листа
    @return: шапку проверяемых файлов
    """
    result_index_dict = {}
    miss_files = []
    head_of_file = []
    none_list = []
    num_of_col = 1
    index_of_head_row = 0
    df = pd.ExcelFile(path)
    file_name = Path(df).name
    wb = op.load_workbook(path)
    # проверяем лист на его корректность
    try:
        ws = wb[sheet_name]
    # если указанного листа не существует, переходим на активный лист
    except KeyError:
        ws = wb.active
    # проверяем первый столбец по принципу, проверки первых 20 ячеек на наличие значений
    # если значения отсутствуют, значит первый столбец в файле пустой и производится сдвиг
    # на следующий столбец, до тех пор пока не будет найдене индекс столбца с данными
    while True:
        for col_empty in ws.iter_cols(min_col=num_of_col, max_col=num_of_col, max_row=20):
            for cell in col_empty:
                none_list.append(cell.value)
        if list(set(none_list))[0] is None:
            num_of_col += 1
            continue
        break
    # после полученя идекса столбца перехоим к определению начала шапки
    for col in ws.iter_cols(min_col=num_of_col, max_col=num_of_col):
        for cell in col:
            # если ячейка пустая пропускаем её
            if cell.value is None:
                pass
            else:
                try:
                    # если не пустая, пробуем привести тип данных ячейки к числовому
                    int_cell = int(cell.value)
                    # если все получилось, проверяем ячейку на наличие 1 в ней
                    if int_cell == 1:
                        # если 1 найдена, прибавляем 1 к счетчику идекса колонки,
                        # что бы перейти к следующей колонке
                        num_of_col += 1
                        # в следующей колонке повторяем операции, но теперь ищем ячейку со значеним 2
                        for col_second in ws.iter_cols(min_col=num_of_col, max_col=num_of_col):
                            for cell_second in col_second:
                                if cell_second.value is None:
                                    pass
                                else:
                                    try:
                                        # двойная проверка, на наличие в столбце значений 02
                                        int_cell = int(cell_second.value)
                                        str_cell = str(cell_second.value)
                                        # если попадется цифра 02, она будет отсеена
                                        if len(str_cell) == 1:
                                            if int_cell == 2:
                                                # пройдя все провекри и найди 1 и 2, мы можем узнать координаты шапки
                                                number_of_row = cell.row
                                                header_start_index = cell.column
                                                result_index_dict[header_start_index] = number_of_row
                                                # извлекаем индекс строки содержащей шапку,
                                                # передавая его в пустой счетчик
                                                index_of_head_row += number_of_row
                                            else:
                                                break
                                        else:
                                            pass
                                    except ValueError:
                                        pass
                # если не получилось привести тип данных ячейки к числовому,
                # получаем ошбику и пропускаем эту ячейку
                except ValueError:
                    pass
        # получаем всю строку с шапкой по полученному индексу
        for row in ws.iter_rows(min_row=index_of_head_row, max_row=index_of_head_row):
            try:
                for cell in row:
                    if cell.value is None:
                        pass
                    else:
                        # и записываем эту строчку в список
                        head_of_file.append(cell.value)
            except ValueError:
                miss_files.append(file_name)
                return miss_files
        return result_index_dict


# print(head_of_table(r'C:\Приложения регионов_исход\3_14.03.2023 после 11\7200.xlsx'))


def cheak_head_of_table(path, sum_of_head: int, *, sheet_name: str = 'Лист1'):
    final_dict = []
    sum_of_head = list(range(1, sum_of_head + 1))
    try:
        for file in tqdm(path):
            df = pd.ExcelFile(file)
            file_name = Path(df).name
            head_func = head_of_table(file, sheet_name)
            if head_func == sum_of_head:
                pass
            else:
                final_dict.append(file_name)
        record_to_excel(final_dict, 'Отчет')
    except FileNotFoundError:
        return 'Файл не найден!'
    except PermissionError as error:
        return f'Зайкроте файл: {error}'
    return f'Проверка выполнена! См отчет в {CHECK_REPORT_FILE}'


# reault = cheak_head_of_table(all_files, 36)
# print(reault)
