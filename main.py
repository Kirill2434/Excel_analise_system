from GUI.window import *


def main():
    root = Tk()
    root.title('Историчность')
    root.geometry('250x200')
    label = ttk.Label(text='План выполнения программы', font=("Arial", 10))
    label.pack(anchor='n')
    btn = ttk.Button(text='1) Создать папки', command=check_dirs_info)
    btn.pack(anchor='nw', padx=50, pady=15, ipadx=30)
    btn = ttk.Button(text='2) Проверка файлов', command=check_files_info)
    btn.pack(anchor='nw', padx=50, pady=15, ipadx=30)
    btn = ttk.Button(text='3) Слияние', command=merge_files_info)
    btn.pack(anchor='nw', padx=50, pady=20, ipadx=38)
    root.mainloop()


if __name__ == "__main__":
    main()

