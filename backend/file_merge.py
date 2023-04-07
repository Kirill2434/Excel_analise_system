import glob
import os

import pandas as pd
import openpyxl as op

from pathlib import Path

from tqdm import tqdm

from backend.check_system import head_of_table
from backend.utils import record_to_excel

file_path = glob.glob(r'C:\Сгруппированные файлы\xlsx файлы\*.xlsx')


def file_merge_new(path, sheet_name: str = 'Лист1'):
    """Функция объединяет файлы ориентируясб на числовую шапку файла.

    :param path: путь к файлам
    :param sheet_name: имя лста
    :return: 'текст'
    """
    single_file_list = []
    all_files_list = []
    single_file_dictionary = {}
    for file in tqdm(path):
        df = pd.ExcelFile(file)
        file_name = Path(df).name
        head = head_of_table(file, sheet_name)
        for row_col_ind, head in head.items():
            wb = op.load_workbook(file)
            # проверяем лист на его корректность
            try:
                ws = wb[sheet_name]
            # если указанного листа не существует, переходим на активный лист
            except KeyError:
                ws = wb.active
            for row in ws.iter_rows(min_col=row_col_ind[1], min_row=row_col_ind[0] + 1, values_only=True):
                single_file_dictionary[row_col_ind[1]] = row
                for cell_k, cell_v in single_file_dictionary.items():
                    single_file_dictionary[row_col_ind[1]] = cell_v
                    df = pd.DataFrame.from_dict(single_file_dictionary, orient='index')
                    df['Файл источник'] = file_name
                    # формируем список с данными одного файла
                    single_file_list.append(df)
    # объединяем данные одного файла в один DataFrame
    df = pd.concat(single_file_list)
    # добавляем каждый целостный DataFrame в общий список
    all_files_list.append(df)
    # сливаем все DataFrame-мы общего списка в один DataFrame
    final_mer = pd.concat(all_files_list)
    final_mer.to_excel(r'C:\generation_results\НБО_свод.xlsx',
                       sheet_name='Финал',
                       index=False)
    return 'Слияние выполнено'


print(file_merge_new(file_path))
