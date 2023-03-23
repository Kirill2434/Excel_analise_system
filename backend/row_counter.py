import pandas as pd


def row_merger(main_path, resurse_path, sheet_name, *, indx_colomn: int = 5):
    """Функция проверяет и объединяет два файла с учетом повторения выбранного элемента
    по которому она находит развличия между двумя файлами и дозаписывает эти различия в актуальный файл

    :param main_path: Файл источник из которого берем данные
    :param resurse_path: Основной файл в который добовляем данны
    :param sheet_name: Имя листа
    :param indx_colomn: Колонка с уникальными значениями по которой будут отбираться повторы при слиянии
    :return: "текст"
    """

    unresolved_inn = []
    try:
        # читаем данные из двух файлов эксель
        resurse_df = pd.read_excel(resurse_path, header=8, sheet_name=sheet_name, dtype=str)
        main_df = pd.read_excel(main_path, header=8, sheet_name=sheet_name, dtype=str)
        # записываем данные стобцов indx_colomn 1 и 2 файлов в списки
        list_resurse_df = resurse_df[indx_colomn].tolist()
        list_main_df = main_df[indx_colomn].tolist()
        for inn in list_resurse_df:
            # проверяем отсутсвие ИНН в списке
            if inn not in list_main_df:
                # записываем в список не совпавшие значения ИНН
                unresolved_inn.append(inn)
        match_cell = resurse_df.loc[resurse_df[5].isin(unresolved_inn)]
        main_df['Статус'] = '-'
        main_df = main_df.append(match_cell, ignore_index=True)
        main_df['Статус'] = main_df['Статус'].fillna('Новый')
        main_df.to_excel(r'C:\generation_results\fin.xlsx',
                         index=False)
    except Exception as error:
        return 'Нет файлов для слияния!'
    return 'Программа выполнена'

# Работа с несколькими файлами
# files = 'rC:\source_data\*.xlsx'
# main_df = pd.read_excel(path_2,  header=8, sheet_name='Лист1', dtype=str)
# unresolved_inn = []
#
# for file in files:
#     df = pd.read_excel(file,
#                        header=8,
#                        sheet_name='Лист1',
#                        dtype=str)
#     list_of_inn = df[3].tolist()
#     for inn in list_of_inn:
#         if inn not in main_df:
#             unresolved_inn.append(inn)
#
#     match_cell = df.loc[df[3].isin(unresolved_inn)]
#     main_df = main_df.append(match_cell, ignore_index=True)
#     main_df.to_excel(r'C:\generation_results\fin.xlsx',
#                      index=False)
