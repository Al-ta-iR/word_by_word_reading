# -*- coding: cp1251 -*-
import eel


eel.init('web')


speed = 100
progress = 0
text_data = ''

def open_file():
    global text_data
    # file = open('text.txt', encoding="utf-8")
    # read_data = file.read() # Считывает и возвращает указанное количество данных из файла (size)
    read_data = 'Там он влюбился в дочь коменданта гарнизона. Сослуживец Гринёва уже сватался к ней, но получил отказ. Сослуживец поссорился с Гринёвым из-за девушки и на дуэли ранил его. Капитанская дочка выхаживала Гринёва и полюбила его. Гринёв хотел жениться на девушке, но его отец был против. Начался крестьянский бунт. Бунтовщики захватили гарнизон, убили капитана и хотели повесить Гринёва, но его узнал главарь бунтовщиков — как-то зимой он остался без тёплой одежды, и Гринёв подарил ему заячий тулуп. Гринёву пришлось оставить любимую и уехать. Вскоре он получил от неё письмо. Сослуживец, перешедший на сторону бунтовщиков, принуждал её к браку, и она просила о помощи.'
    return read_data

@eel.expose
def set_values(speed_val=100, progress_val=0):
    global speed, progress
    speed = int(speed_val)
    progress = int(progress_val)

def word_chooser(text):
    for word in text:
        # for word in line.split():
        # print('Прочитано = ', count_read_words, end='')
        # progress = count_read_words * 100 / 50
        eel.sleep(60 / speed)
        # count_read_words += 1
    

def reader_python(speed, progress):
    print(speed, progress)
    start_words = 'На старт! Внимание! Марш!'
    read_data = open_file()
    per_word = read_data.split()
    count_words = len(per_word)
    count_read_words = 0

    # 

    # for word in per_word:
    #     # for word in line.split():
    #     print(word, sep='')
    #     count_read_words += 1
    #     # print('Прочитано = ', count_read_words, end='')
    #     progress = count_read_words * 100 / 50
    #     eel.sleep(60 / speed)

    # eel.call_in_python("Hello from JS")
    return word

    
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
