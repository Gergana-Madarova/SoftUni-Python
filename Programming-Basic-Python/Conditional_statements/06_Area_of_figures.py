from math import pi

fig_type = input()

if fig_type == 'square':
    a = float(input())
    s = a * a
elif fig_type == 'rectangle':
    a = float(input())
    b = float(input())
    s = a * b
elif fig_type == 'circle':
    r = float(input())
    s = r * r * pi
elif fig_type == 'triangle':
    a = float(input())
    h = float(input())
    s = (a * h) / 2

print(f'{s:.3f}')