print("What is your name? And what year of high school are you currently in?")
name = input("What is your name? ")
year = input("What year of high school are you currently in? ")
while year != "1st" and year != "2nd" and year != "3rd" and year != "4th" and year != "5th" and year != "6th":
    print("error, wrong year ")
    year = input("What year of high school are you currently in? ")