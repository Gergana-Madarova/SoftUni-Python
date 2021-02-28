lenght_cm = int(input())
width_cm = int(input())
hight_cm = int(input())
percent = float(input())

v = lenght_cm * width_cm * hight_cm
l = (v * 0.001) * (1-(percent*0.01))

print(l)