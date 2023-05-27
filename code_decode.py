import tkinter as tk
from tkinter import ttk

# Обозначение алфавита
alphabet_RU = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet_EN = 'abcdefghijklmnopqrstuvwxyz'


# функция шифрования
def encoding(lang, step, message):
    result = ''
    if lang == 'RU':
        for i in message:
            if i in alphabet_RU:
                place = alphabet_RU.find(i)
                new_place = (place + step) % len(alphabet_RU)
                result += alphabet_RU[new_place]
            else:
                result += i
    else:
        for i in message:
            if i in alphabet_EN:
                place = alphabet_EN.find(i)
                new_place = (place + step) % len(alphabet_EN)
                result += alphabet_EN[new_place]
            else:
                result += i
    return result


# Функция дешифрования
def decoding(lang, step, message):
    result = ''
    if lang == 'RU':
        for i in message:
            if i in alphabet_RU:
                place = alphabet_RU.find(i)
                new_place = (place - step) % len(alphabet_RU)
                result += alphabet_RU[new_place]
            else:
                result += i
    else:
        for i in message:
            if i in alphabet_EN:
                place = alphabet_EN.find(i)
                new_place = (place - step) % len(alphabet_EN)
                result += alphabet_EN[new_place]
            else:
                result += i
    return result


# mode = input('Выберите: шифрование/дешифрование ')
# lang = input('Выберите язык EN или RU - ')
# step = int(input('Шаг шифровки: '))
# message = input('Введите сообщение - ')
#
# encoding_code = encoding(lang, step, message)
# decoding_code = decoding(lang, step, message)
# if mode == 'шифрование':
#     print('Готовый текст: ', encoding_code)
# else:
#     print('Готовый текст: ', decoding_code)

# Функция для отображения функций в tkinter
def encrypt_decrypt():
    mode = mode_var.get()
    lang = lang_var.get()
    step = int(step_entry.get())
    message = message_entry.get()

    if mode == 'encryption':
        result = encoding(lang, step, message)
    else:
        result = decoding(lang, step, message)

    result_label.config(text=result)


# Создание главного окна
window = tk.Tk()
window.title('Шифр Цезаря')
window.geometry('1000x700+200+300')

# Настройка цветов
bg_color = '#D6D6D6'
fg_color = '#333333'

# Установка иконки для приложения
photo = tk.PhotoImage(file='code.png')
window.iconphoto(False, photo)

# Установка фона и переднего плана
window.configure(bg=bg_color)
window.config(bg=bg_color)
window.option_add('*Background', bg_color)
window.option_add('*Foreground', fg_color)

# Создание рамок для группировки элементов
mode_frame = ttk.LabelFrame(window, text='Режим')
mode_frame.pack(pady=10, padx=20, anchor='w')
lang_frame = ttk.LabelFrame(window, text='Язык')
lang_frame.pack(pady=10, padx=20, anchor='w')
step_frame = ttk.LabelFrame(window, text='Шаг шифровки')
step_frame.pack(pady=10, padx=20, anchor='center')
message_frame = ttk.LabelFrame(window, text='Сообщение')
message_frame.pack(pady=10, padx=20, anchor='center')
result_frame = ttk.LabelFrame(window, text='Результат')
result_frame.pack(pady=10, padx=20, anchor='center')

# Переключатель для выбора режима
mode_var = tk.StringVar(value='encryption')  # Значение по умолчанию - шифрование
encryption_radio = ttk.Radiobutton(mode_frame, text='Шифрование', variable=mode_var, value='encryption')
encryption_radio.pack(padx=5, pady=5, anchor='w')
decryption_radio = ttk.Radiobutton(mode_frame, text='Дешифрование', variable=mode_var, value='decryption')
decryption_radio.pack(padx=5, pady=5, anchor='w')

# Переключатель для выбора языка
lang_var = tk.StringVar(value='RU')  # Значение по умолчанию - русский язык
ru_lang_radio = ttk.Radiobutton(lang_frame, text='RU', variable=lang_var, value='RU')
ru_lang_radio.pack(padx=5, pady=5, anchor='w')
en_lang_radio = ttk.Radiobutton(lang_frame, text='EN', variable=lang_var, value='EN')
en_lang_radio.pack(padx=5, pady=5, anchor='w')

# Поле ввода для шага шифровки
step_entry = ttk.Entry(step_frame, width=30)
step_entry.pack(padx=5, pady=5)

# Поле ввода для сообщения
message_entry = ttk.Entry(message_frame, width=30)
message_entry.pack(padx=5, pady=5)

# Кнопка для запуска шифрования/дешифрования
process_button = ttk.Button(window, text='Выполнить', command=encrypt_decrypt)
process_button.pack(pady=10)

# Метка для вывода результата
result_label = ttk.Label(result_frame)
result_label.pack(padx=5, pady=5)

# Стиль для кнопки "Выполнить"
style = ttk.Style()
style.configure('TButton', foreground='white', background='blue')

# Запуск главного цикла обработки событий
window.mainloop()
