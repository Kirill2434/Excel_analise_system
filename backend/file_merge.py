import glob
import os

import pandas as pd
import openpyxl as op

from pathlib import Path

from tqdm import tqdm

from backend.check_system import head_of_table


file_path = glob.glob(r'C:\Сгруппированные файлы\xlsx файлы\*.xlsx')


def file_merge_new(path, sheet_name: str = 'Лист1'):
    """

    :param path:
    :param sheet_name:
    :return:
    """
    lis = []
    lis_2 = []
    dic = {}
    for file in tqdm(path):
        df = pd.ExcelFile(file)
        file_name = Path(df).name
        head = head_of_table(file)
        for k, v in head.items():
            wb = op.load_workbook(file)
            # проверяем лист на его корректность
            try:
                ws = wb[sheet_name]
            # если указанного листа не существует, переходим на активный лист
            except KeyError:
                ws = wb.active
            for col in ws.iter_rows(min_col=k, min_row=v+1, values_only=True):
                dic[k] = col
                for cell_k, cell_v in dic.items():
                    dic[k] = cell_v
                    mer = pd.DataFrame.from_dict(dic, orient='index')
                    mer['Файл источник'] = file_name
                    lis.append(mer)

    mer = pd.concat(lis, ignore_index=True)
    lis_2.append(mer)
    final_mer = pd.concat(lis_2, ignore_index=True)
    final_mer.to_excel(r'C:\generation_results\НБО_свод.xlsx',
                       sheet_name='Финал',
                       index=False)


print(file_merge_new(file_path))
