from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, INFO, OK, showerror


from backend.check_system import check_source_data, check_directory
from backend.row_counter import row_merger
from settings import resurs_path, main_path


def check_dirs_info():
    text = str(check_directory())
    if check_directory() == 'Все необходимые папки - созданы!':
        showinfo(title='Отчет о выполнении', message=text)
    else:
        showerror(title='Отчет о выполнении', message=text)


def check_files_info():
    text = str(check_source_data())
    if check_source_data() == 'Все файлы прошли проверку':
        showinfo(title='Отчет о выполнении', message=text,
                 icon=INFO, default=OK)
    else:
        showerror(title='Отчет о выполнении', message=text)


def merge_files_info():
    text = str(row_merger(resurs_path, main_path, 'СВОД'))
    if row_merger(resurs_path, main_path, 'СВОД') == 'Программа выполнена':
        showinfo(title='Отчет о выполнении', message=text,
                 icon=INFO, default=OK)
    else:
        showerror(title='Отчет о выполнении', message=text)


# root = Tk()
# root.title('Историчность')
# root.geometry('250x200')
# label = ttk.Label(text='План выполнения программы', font=("Arial", 10))
# label.pack(anchor='n')
# btn = ttk.Button(text='1) Создать папки', command=check_dirs_info)
# btn.pack(anchor='nw', padx=50, pady=15, ipadx=30)
# btn = ttk.Button(text='2) Проверка файлов', command=check_files_info)
# btn.pack(anchor='nw', padx=50, pady=15, ipadx=30)
# btn = ttk.Button(text='3) Слияние', command=merge_files_info)
# btn.pack(anchor='nw', padx=50, pady=20, ipadx=38)
#
# root.mainloop()
