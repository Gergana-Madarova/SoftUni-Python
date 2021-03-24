n = int(input())

for i in range(1, 10):
    if n % i == 0:
        for j in range(1, 10):
            if n % j == 0:
                for k in range(1, 10):
                    if n % k == 0:
                        for l in range(1, 10):
                            if n % l == 0:
                                special_num = str(i) + str(j) + str(k) + str(l)
                                print(special_num, end=' ')