score = int(input())

if score <= 100:
    bonus_score = 5;
elif score >1000:
    bonus_score = 0.1 * score
else:
    bonus_score = 0.2 * score

if score % 2 == 0:
    bonus_score +=1
elif score % 10 == 5:
    bonus_score +=2

print(bonus_score)
print(bonus_score+score)