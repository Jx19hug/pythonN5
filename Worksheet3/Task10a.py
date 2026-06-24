
print("This program calculates the total calories for 5 pupils.")
total_calories=0
for index in range (1,6):
    total_calories=0
    print("Pupil", index)
    for meal in ["breakfast", "lunch", "dinner"]:
        calories = int(input(meal + " calories: "))
        total_calories += calories
    print("Total calories for pupil", index, "=", total_calories)
    print()