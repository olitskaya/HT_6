# Програма-світлофор.
# Створити програму-емулятор світлофора для авто і пішоходів.
# Після запуска програми на екран виводиться в лівій половині -
# колір автомобільного, а в правій - пішохідного світлофора.
# Кожну секунду виводиться поточні кольори. Через декілька ітерацій
# - відбувається зміна кольорів - логіка така сама як і в звичайних
# світлофорах.
# Приблизний результат роботи наступний:
# Red      Green
# Red      Green
# Red      Green
# Red      Green
# Yellow   Green
# Yellow   Green
# Green    Red
# Green    Red
# Green    Red
# Green    Red
# Yellow   Red
# Yellow   Red
# Red      Green
# .......

import time

def lights_test(a):
    while True:
        for elem in a:
            print(f'{elem[0].title()}{elem[1].title()}')
            time.sleep(1)
    return elem
    
lights = [('red', '      green'), ('red', '      green'), ('red', '      green'), ('red', '      green'), ('yellow', '   green'), ('yellow', '   green'), ('green', '    red'), ('green', '    red'), ('green', '    red'), ('green', '    red'), ('green', '    red'), ('yellow', '   red'), ('yellow', '   red')]
lights_test(lights)
