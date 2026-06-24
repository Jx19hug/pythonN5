print("What is the captal of UK?")
print("A London")
print("B Paris")
print("C Berlin")
print("D Madrid")

answer = input("Enter your answer (A/B/C/D): ")

while answer != "A" and answer != "B" and answer != "C" and answer != "D":
    print("error, wrong answer ")
    answer = input("Enter your answer (A/B/C/D): ")
print("your answer was, " + answer)