import os

from backend.Exeptions import EmptyException


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
