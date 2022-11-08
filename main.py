# -*- coding:utf-8 -*-
import eel
# import tkinter 
# import tkinter.filedialog as filedialog



eel.init('web')

speed = 400
progress = 0
text_data = ''

# @eel.expose
# def selectFolder():
#     print("Here")
#     root = tkinter.Tk()
#     root.attributes("-topmost", True)
#     root.withdraw()
#     directory_path = filedialog.askdirectory()
#     print(directory_path)

def open_file():
    '''Open file'''
    global text_data
    try:
        file = open('text.txt', encoding="utf-8")
        text = file.read()
        text_data = text.split()
    except:
        eel.sleep(0.5)
        eel.showWords('Добавьте файл `text.txt` в текущий репозиторий')
        eel.sleep(9.5)
        open_file()

@eel.expose
def play_reading(flag):
    if flag == 1:
        return 1
    else:
        eel.sleep(1)

@eel.expose
def set_values(speed_val=100, progress_val=0):
    '''Set speed and progress'''
    if speed_val == '' or speed_val == '0' or speed_val == 0:
        speed_val = 400
    if progress_val == '':
        progress_val = 0
    global speed, progress
    speed = 60 / int(speed_val)
    progress = int(progress_val)
    open_file()
    # text_word_counter = len(text_data)
    reader_python()

def word_chooser(text, speed_ratio=1):
    '''Read in HTML'''
    global speed, progress, text_data
    text_words_counter = len(text)
    start_progress = int(progress / 100 * text_words_counter)
    for word_id in range(start_progress, text_words_counter):

        latest_symbol = text[word_id][-1]
        if latest_symbol in '.!?;':
            eel.showWords(text[word_id])
            eel.sleep(speed * 1.8 * speed_ratio * 0.88)
            progress = 100 / text_words_counter * (word_id + 1)
            eel.showProgress(round(progress, 1))
            continue
        eel.showWords(text[word_id])
        eel.sleep(speed)
        eel.showWords('') # данные 2 строки добавлены для мерцания слов при смене
        eel.sleep(speed * 0.12)

@eel.expose
def reader_python():
    '''Logic router'''
    global speed, progress, text_data
    start_words = '► Приготовиться! Внимание! Марш!'.split()
    for word in start_words:
        eel.showWords(word)
        eel.sleep(1)
    word_chooser(text_data)

    
# if __name__ == '__main__':
#     reader(speed, progress)

eel.start('index.html', size = (750, 600), mode = "firefox")

# паузы предложений и абзацев
# форма
# экран и размер экрана
# размер шрифта
# цвета фона и шрифта
# прогресс
# пауза/плей
# запуск с прогресса