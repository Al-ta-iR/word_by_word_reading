# -*- coding: cp1251 -*-
import eel
import time


eel.init('web')


speed = 60
progress = 0
text_data = 'Там он влюбился в дочь коменданта гарнизона. Сослуживец Гринёва уже сватался к ней, но получил отказ'

def open_file():
    global text_data
    # file = open('text.txt', encoding="utf-8")
    # read_data = file.read() # Считывает и возвращает указанное количество данных из файла (size)
    text_data = ''
    # return read_data

@eel.expose
def set_values(speed_val=100, progress_val=0):
    if speed_val == '' or speed_val == '0' or speed_val == 0:
        speed_val = 200
    if progress_val == '':
        progress_val = 0
    global speed, progress
    speed = 60 / int(speed_val)
    progress = int(progress_val)
    reader_python()

def word_chooser(text):
    global speed, progress, text_data
    per_word = text.split()
    for word in per_word:
        eel.sleep(speed)
        print(word)
        eel.showJs(word)
    
@eel.expose
def reader_python():
    global speed, progress, text_data
    start_words = 'На старт! Внимание! Марш!'
    word_chooser(start_words)
    word_chooser(text_data)

    # for word in per_word:
    #     # for word in line.split():
    #     print(word, sep='')
    #     count_read_words += 1
    #     # print('Прочитано = ', count_read_words, end='')
    #     progress = count_read_words * 100 / 50
    #     print(int(speed), type(speed))
    #     eel.sleep(60 / speed)
    #     return word

    # eel.call_in_python("Hello from JS")

    
# if __name__ == '__main__':
#     reader(speed, progress)

eel.start('index.html', size = (750, 600), mode = "firefox")

# паузы предложений и абзацев
# на старт, внимание, марш
# форма
# скорость
# экран и размер экрана
# открытие файла
# размер шрифта
# цвета фона и шрифта
# прогресс
# пауза/плей
# запуск с прогресса
