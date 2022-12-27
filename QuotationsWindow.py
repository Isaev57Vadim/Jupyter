# Котировки с окном просмотра

import tkinter as tk
from tkinter.scrolledtext import ScrolledText as st
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import os
import requests
import xmltodict

# Создание главного окна
window = tk.Tk()
window.geometry("780x550")
window.title("Окно курсов валют")

# Создание меток вывода
label_00 = tk.Label(text = "Веб-сервис:")
label_00.grid(row=0, column=0, padx=10, pady=10, sticky="e")

label_01 = tk.Label(text = "http://www.cbr.ru/scripts/xml_metall.asp?date_req1=01/07/2001&date_req2=13/07/2001")
label_01.grid(row=0, column=1, sticky="w")

# Создание текстового вывода c прокруткой
output_text = st(height = 25, width = 68)
output_text.grid(row=3, column=1, padx=10, pady=10, sticky="w")

url = "http://www.cbr.ru/scripts/xml_metall.asp?date_req1=01/07/2001&date_req2=13/07/2001" 
response = requests.get(url)
data = xmltodict.parse(response.content)
print(data)

my_array = []
for item in data['Metall']['Record']:
    my_set = [item['@Date'], item['@Code'], item['Buy'], item['Sell']];
    my_array.append(my_set)
    print(my_set)

# - print(my_array)

# Диалог открытия файла
def do_dialog():
    for i in my_array:
        output_text.insert(tk.END, str(i) + os.linesep)

# Обработчик нажатия кнопки
def process_button():
    do_dialog()
    mb.showinfo(title=None, message="Готово")

# Создание кнопки
button=tk.Button(window, text="Просмотреть данные", command=process_button)
button.grid(row=4, column=1)

# Запуск цикла mainloop
window.mainloop()
