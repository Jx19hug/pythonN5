
name= input("What is your name? ")
gender= input("What is your gender? ")
while gender != "male" and gender != "female":
    print("error, wrong gender ")
    gender = input("What is your gender? ")
age= int(input("What is your age? "))
while age < 0 or age > 120:
    print("error, wrong age ")
    age = int(input("What is your age? "))