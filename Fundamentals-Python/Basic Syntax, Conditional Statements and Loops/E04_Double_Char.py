word = input()
new_word = ""

for i in range(len(word)):
    new_word += 2 * word[i]

print(new_word)