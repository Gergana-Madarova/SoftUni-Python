n = int(input())
l = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(ord('a'), l+97):
            for m in range(ord('a'), l+97):
                p = 0
                if i >= j:
                    p = i + 1
                elif j > i:
                    p = j + 1

                while p <= n:
                    password = str(i) + str(j) + chr(k) + chr(m) + str(p)
                    print(password, end=" ")
                    p += 1