recortSec = float(input())
distanceМ = float(input())
timeSecForM = float(input())

timeGeorgi = distanceМ * timeSecForM
timeGeorgi += (distanceМ // 50) * 30

if recortSec > timeGeorgi:
    print(f"Yes! The new record is {timeGeorgi:.2f} seconds.")
else:
    print(f"No! He was {timeGeorgi - recortSec:.2f} seconds slower.")
