import glob
import os

import pandas as pd
from pandas import ExcelWriter

from settings import CHECK_REPORT_FILE, CHECK_REPORT_N_FILE


def record_to_excel(obj, sheet_name):
    """Универсальная функция записи результатов выполнения различных
    проверок и действий в других модулях проекта.

    @param obj: датафрейм который необходимо записать в файл формата xlsx
    @param sheet_name: имя листа на который будут записаны данные
    """

    # если файл-отчет отсувует в папке, то записываем первый файл-отчет
    if os.path.exists(CHECK_REPORT_FILE) is False:
        with ExcelWriter(CHECK_REPORT_FILE,
                         engine='openpyxl') as writer:
            # проверяем тип объекта
            # либо список
            if isinstance(obj, list):
                df = pd.DataFrame(obj).transpose()
                df.to_excel(writer, sheet_name=sheet_name)
            # либо словарь
            if isinstance(obj, dict):
                df = pd.DataFrame.from_dict(obj)
                df.to_excel(writer, sheet_name=sheet_name)
    # когда файл уже есть:
    else:
        # счиаем кол-во файлов-отчетов в папке
        sum_of_files = len(list(glob.glob(r'C:\generation_results\check_report_file??.xlsx')))
        num = sum_of_files + 1
        # создаем новое имя файла с учетом нового номера
        new_file_name = CHECK_REPORT_N_FILE + '_' + str(num) + '.xlsx'
        with ExcelWriter(new_file_name,
                         engine='openpyxl') as writer:
            # проверяем тип объекта
            # либо список
            if isinstance(obj, list):
                df = pd.DataFrame(obj).transpose()
                df.to_excel(writer, sheet_name=sheet_name)
            # либо словарь
            if isinstance(obj, dict):
                df = pd.DataFrame.from_dict(obj)
                df.to_excel(writer, sheet_name=sheet_name)
