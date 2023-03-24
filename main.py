import tkinter

import customtkinter

from GUI.window import *


customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('blue')


def main():
    root = customtkinter.CTk()
    root.geometry('350x300')
    root.title('Историчность')
    label = customtkinter.CTkLabel(master=root, text='Выбор операции',
                                   font=customtkinter.CTkFont(size=16, weight='normal'))
    label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
    label_2 = customtkinter.CTkLabel(master=root, text='version == 0.2',
                                     font=customtkinter.CTkFont(size=10, weight='normal'))
    label_2.place(relx=0.85, rely=0.92, anchor=tkinter.CENTER)
    button = customtkinter.CTkButton(master=root, text='Создать папки', command=check_dirs_info)
    button.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    button = customtkinter.CTkButton(master=root, text='Проверить файлы', command=check_files_info)
    button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    button = customtkinter.CTkButton(master=root, text='Слияние', command=merge_files_info)
    button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    root.mainloop()


if __name__ == "__main__":
    main()

