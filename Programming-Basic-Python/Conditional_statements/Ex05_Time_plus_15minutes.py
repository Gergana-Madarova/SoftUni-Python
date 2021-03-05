hour = int(input())
minutes = int(input())

if (minutes + 15 <= 59):
    minutes = minutes + 15
elif (minutes + 15 > 59):
    minutes = minutes + 15 - 60
    if(hour == 23):
        hour = 0
    else:
        hour +=1

print(f'{hour}:{minutes:02d}')