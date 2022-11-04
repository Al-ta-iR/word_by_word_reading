# -*- coding: cp1251 -*-
import eel


eel.init('web')

@eel.expose
def call_in_js(x):
    print('123')
    return '257'

eel.start('ind.html', size = (750, 600), mode = "firefox")

