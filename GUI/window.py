# import tkinter.messagebox
# import customtkinter
# from tkinter.messagebox import showinfo, INFO, OK, showerror
#
# from backend.check_system import check_source_data, check_directory, check_sheets, cheak_head_of_table
# from backend.file_dir_manager import rename_file_by_folder_name, replace_files
# from backend.file_merge import file_dir_merge
# from backend.row_counter import row_merger
# from settings import resurs_path, main_path, all_files, LEN_OF_HEAD, file_path_regions, group_dir, file_path
#
# customtkinter.set_appearance_mode("System")
# customtkinter.set_default_color_theme("blue")
#
#
# class App(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()
#
#         self.title('Мониторинг НБО')
#         self.geometry(f"{410}x{400}")
#         self.label = customtkinter.CTkLabel(self, text='Основное меню',
#                                             font=customtkinter.CTkFont(size=16, weight='normal'))
#         self.label.place(relx=0.5, rely=0.05, anchor=tkinter.CENTER)
#         self.label_version = customtkinter.CTkLabel(self, text='version 0.3',
#                                                     font=customtkinter.CTkFont(size=12, weight='normal'))
#         self.label_version.place(relx=0.85, rely=0.92, anchor=tkinter.CENTER)
#         self.tabview = customtkinter.CTkTabview(self, width=350)
#         self.tabview.grid(row=1, column=3, padx=(30, 0), pady=(30, 0), sticky="nsew")
#         self.tabview.add('Проверка')
#         self.tabview.add('Историчность')
#         self.tabview.add('Менеджер файлов')
#         self.tabview.tab('Проверка').grid_columnconfigure(0, weight=1)
#         self.tabview.tab('Историчность').grid_columnconfigure(0, weight=1)
#         self.tabview.tab('Менеджер файлов').grid_columnconfigure(0, weight=1)
#
#         self.first_check_button = customtkinter.CTkButton(self.tabview.tab('Проверка'),
#                                                           text='Проверить папки',
#                                                           command=self.check_dirs_info,
#                                                           fg_color='green')
#         self.first_check_button.grid(row=0, column=0, padx=20, pady=(20, 10))
#         self.first_history_button = customtkinter.CTkButton(self.tabview.tab('Историчность'),
#                                                             text='Проверить файлы',
#                                                             command=self.check_files_info,
#                                                             fg_color='green')
#         self.first_history_button.grid(row=0, column=0, padx=20, pady=(10, 10))
#         self.seccond_history_button = customtkinter.CTkButton(self.tabview.tab('Историчность'),
#                                                               text='Слияние на историчность',
#                                                               command=self.merge_files_info,
#                                                               fg_color='green')
#         self.seccond_history_button.grid(row=1, column=0, padx=20, pady=(10, 10))
#         self.first_file_manager_button = customtkinter.CTkButton(self.tabview.tab('Менеджер файлов'),
#                                                                  text='Переместить файлы',
#                                                                  command=self.replace_files_info)
#         self.first_file_manager_button.grid(row=0, column=0, padx=20, pady=(10, 10))
#         self.seccond_file_manager_button = customtkinter.CTkButton(self.tabview.tab('Менеджер файлов'),
#                                                                    text='Проверить листы файла',
#                                                                    command=self.check_sheets_info)
#         self.seccond_file_manager_button.grid(row=1, column=0, padx=20, pady=(10, 10))
#         self.third_file_manager_button = customtkinter.CTkButton(self.tabview.tab('Менеджер файлов'),
#                                                                  text='Проверить шапку файла',
#                                                                  command=self.cheak_head_of_table_info)
#         self.third_file_manager_button.grid(row=2, column=0, padx=20, pady=(10, 10))
#         self.fourth_file_manager_button = customtkinter.CTkButton(self.tabview.tab('Менеджер файлов'),
#                                                                   text='Слияние файлов',
#                                                                   command=self.file_dir_merge_info)
#         self.fourth_file_manager_button.grid(row=4, column=0, padx=20, pady=(10, 10))
#
#     def check_dirs_info(self):
#         text = str(check_directory())
#         if text == 'Все необходимые папки - созданы!':
#             showinfo(title='Отчет о выполнении', message=text)
#         else:
#             showerror(title='Отчет о выполнении', message=text)
#
#     def check_files_info(self):
#         text = str(check_source_data())
#         if text == 'Все файлы прошли проверку':
#             showinfo(title='Отчет о выполнении', message=text,
#                      icon=INFO, default=OK)
#         else:
#             showerror(title='Отчет о выполнении', message=text)
#
#     def check_sheets_info(self):
#         text = str(check_sheets(all_files))
#         if text == 'Проверка листов, выполнена. Ошибки не обнаружены!':
#             showinfo(title='Отчет о выполнении', message=text,
#                      icon=INFO, default=OK)
#         else:
#             showerror(title='Отчет о выполнении', message=text)
#
#     def cheak_head_of_table_info(self):
#         text = str(cheak_head_of_table(all_files, LEN_OF_HEAD))
#         if text == f'Проверка выполнена! Ошибок нет.':
#             showinfo(title='Отчет о выполнении', message=text,
#                      icon=INFO, default=OK)
#         else:
#             showerror(title='Отчет о выполнении', message=text)
#
#     def merge_files_info(self):
#         text = str(row_merger(resurs_path, main_path, 'СВОД'))
#         if text == 'Программа выполнена':
#             showinfo(title='Отчет о выполнении', message=text,
#                      icon=INFO, default=OK)
#         else:
#             showerror(title='Отчет о выполнении', message=text)
#
#     def replace_files_info(self):
#         rename_file_by_folder_name(file_path_regions)
#         text = str(replace_files(file_path_regions))
#         if text == fr'Файлы скопированы в "C:\{group_dir}".':
#             showinfo(title='Отчет о выполнении', message=text,
#                      icon=INFO, default=OK)
#         else:
#             showerror(title='Отчет о выполнении', message=text)
#
#     def file_dir_merge_info(self):
#         text = str(file_dir_merge(file_path))
#         if text == 'Слияние выполнено!':
#             showinfo(title='Отчет о выполнении', message=text,
#                      icon=INFO, default=OK)
#         else:
#             showerror(title='Отчет о выполнении', message=text)
