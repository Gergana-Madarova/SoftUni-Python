year = input()

happy_year = year
is_happy_year = False

while(True):
    happy_year = int(happy_year) + 1
    happy_year = str(happy_year)

    for i in range(len(year) - 1):
        for j in range(i + 1, len(year)):
            if(happy_year[i] != happy_year[j]):
                is_happy_year = True
            elif (happy_year[i] == happy_year[j]):
                is_happy_year = False
                break
        if (is_happy_year == False):
            break

    if(is_happy_year):
        break

if (is_happy_year):
    print(happy_year)