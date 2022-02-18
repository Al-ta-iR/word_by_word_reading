import eel
import time


eel.init('web')
eel.start('index.html', size = (750, 600))

@eel.expose
def call_in_js(x):
    print(x)

file = open('text.txt', encoding="utf-8")
speed = int(input())
read_data = file.read()
per_word = read_data.split()
count_words = len(read_data.split())
progress = 0
count_read_words = 0
for word in per_word:
    # for word in line.split():
    print(word, sep='')
    count_read_words += 1
    # print('Прочитано = ', count_read_words, end='')
    progress = count_read_words * 100 / 50
    time.sleep(60 / speed)

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
