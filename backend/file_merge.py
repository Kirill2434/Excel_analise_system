import glob
import os

import pandas as pd
import openpyxl as op

from pathlib import Path

from tqdm import tqdm

from backend.check_system import head_of_table
from settings import all_files


def file_merge_new(path, sheet_name: str = 'Лист1'):
    """

    :param path:
    :param sheet_name:
    :return:
    """
    lis = []
    head = head_of_table(path)
    for k, v in head.items():
        wb = op.load_workbook(path)
        # проверяем лист на его корректность
        try:
            ws = wb[sheet_name]
        # если указанного листа не существует, переходим на активный лист
        except KeyError:
            ws = wb.active
        for col in ws.iter_rows(min_col=k, min_row=v):
            for cell in col:
                lis.append(cell.value)

    print(lis)


print(file_merge_new(r'C:\Приложения регионов_исход\3_14.03.2023 после 11\7200.xlsx'))
