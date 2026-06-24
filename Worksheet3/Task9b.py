
# Task9b.py

SECRET_NUMBER = 98

print("I'm thinking of a number. Try to guess it!")

attempts = 0
while True:
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("enter a whole number.")
        continue
    attempts += 1
    if guess < SECRET_NUMBER:
        print("Too low. Guess higher!")
    elif guess > SECRET_NUMBER:
        print("Too high. Guess lower!")
    else:
        print(f"Congrats! You got it in {attempts} tries. Good job!")
        

