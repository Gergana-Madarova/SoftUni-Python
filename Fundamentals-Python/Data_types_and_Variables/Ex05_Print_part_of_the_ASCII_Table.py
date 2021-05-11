char_start_index = int(input())
char_end_index = int(input())

for i in range(char_start_index, char_end_index + 1):
    print(f"{chr(i)}", end=" ")
