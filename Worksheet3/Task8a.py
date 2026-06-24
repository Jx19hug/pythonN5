print("What is your name?")
name = input()
print("How many times would you like your name to be displayed?")
times = int(input())
for counter in range(0, times):
    print(name)