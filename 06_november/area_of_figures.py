from math import pi

type_figure = str(input())

if type_figure == 'square':
    a = float(input())
    print(f'{a*a:.3f}')
elif type_figure == 'rectangle':
    a = float(input())
    b = float(input())
    print(f'{a*b:.3f}')
elif type_figure == 'circle':
    r = float(input())
    print(f'{(r*r)*pi:.3f}')
elif type_figure == 'triangle':
    a = float(input())
    ha = float(input())
    print(f'{a*ha/2:.3f}')
