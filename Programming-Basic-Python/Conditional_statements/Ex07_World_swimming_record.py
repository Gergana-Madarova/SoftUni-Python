import math

record = float(input())
distance = float(input())
time = float(input())

time_Ivan = distance * time

if (distance >= 15):
    time_Ivan = time_Ivan + (math.floor(distance / 15) * 12.5)

if (time_Ivan < record):
    print(f"Yes, he succeeded! The new world record is {time_Ivan:.2f} seconds.")
else:
    print(f"No, he failed! He was {(time_Ivan - record):.2f} seconds slower.")