# Currencies с окном просмотра

import tkinter as tk
from tkinter.scrolledtext import ScrolledText as st
from tkinter import messagebox as mb
from tkinter import  filedialog as fd

# Создание главного окна
window = tk.Tk()
window.geometry("600x550")
window.title("Окно курсов валют")

# Создание меток вывода
label_00 = tk.Label(text = "Веб-сервис:")
label_00.grid(row=0, column=0, padx=10, pady=10, sticky="e")

label_01 = tk.Label(text = "")
label_01.grid(row=0, column=1, sticky="w")

# Создание текстового вывода c прокруткой
output_text = st(height = 25, width = 50)
output_text.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Диалог открытия файла
def do_dialog():
    name= fd.askopenfilename()
    return name

# Обработчик нажатия кнопки
def process_button():
    do_dialog()
    mb.showinfo(title=None, message="Готово")

# Создание кнопки
button=tk.Button(window, text="Просмотреть данные", command=process_button)
button.grid(row=4, column=1)

# Запуск цикла mainloop
window.mainloop()
