# -*- coding: cp1251 -*-
import eel
import time


eel.init('web')
eel.start('index.html', size = (750, 600), mode = "firefox")

@eel.expose
def reader(speed=100, progress=0):

    enter_words = 'На старт! Внимание! Марш!'
    return enter_words
    # for word in enter_words:
    #     # for word in line.split():
    #     # print('Прочитано = ', count_read_words, end='')
    #     # progress = count_read_words * 100 / 50
    #     time.sleep(60 / speed)
    #     return word
    #     # count_read_words += 1

    # speed = int(speed)
    # progress = int(progress)
    # # file = open('text.txt', encoding="utf-8")
    # # speed = int(input())
    # file = 'Там он влюбился в дочь коменданта гарнизона. Сослуживец Гринёва уже сватался к ней, но получил отказ. Сослуживец поссорился с Гринёвым из-за девушки и на дуэли ранил его. Капитанская дочка выхаживала Гринёва и полюбила его. Гринёв хотел жениться на девушке, но его отец был против. Начался крестьянский бунт. Бунтовщики захватили гарнизон, убили капитана и хотели повесить Гринёва, но его узнал главарь бунтовщиков — как-то зимой он остался без тёплой одежды, и Гринёв подарил ему заячий тулуп. Гринёву пришлось оставить любимую и уехать. Вскоре он получил от неё письмо. Сослуживец, перешедший на сторону бунтовщиков, принуждал её к браку, и она просила о помощи.'
    # read_data = file.read()
    # per_word = read_data.split()
    # count_words = len(read_data.split())
    # count_read_words = 0
    # enter_words = 'На старт! Внимание! Марш!'
    # for word in per_word:
    #     # for word in line.split():
    #     print(word, sep='')
    #     count_read_words += 1
    #     # print('Прочитано = ', count_read_words, end='')
    #     progress = count_read_words * 100 / 50
    #     time.sleep(60 / speed)

    # eel.call_in_python("Hello from JS")

# форма
# скорость
# экран и размер экрана
# открытие файла
# размер шрифта
# цвета фона и шрифта
# прогресс
# пауза/плей
# запуск с прогресса
