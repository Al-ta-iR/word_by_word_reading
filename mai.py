# -*- coding: cp1251 -*-
import eel


eel.init('web')

@eel.expose
def call_in_js(x):
    print('123')
    print(x)
    return '257'

eel.call_in_python("Hello, from JS")

eel.start('ind.html', size = (750, 600), mode = "firefox")

