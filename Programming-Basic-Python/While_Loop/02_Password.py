name = input()
password = input()

given_pass = input()

while given_pass != password:
    given_pass = input()

print(f"Welcome {name}!")