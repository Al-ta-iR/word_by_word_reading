import eel


eel.init('web')
eel.start('index.html', size = (750, 600))

@eel.expose
def call_in_js(x):
    print(x)

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
