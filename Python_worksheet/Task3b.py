print("Enter the number of people having a meal")
number= int(input(""))
print("Enter the total price of the meal")
total_1= int(input(""))
#tip
tip= total_1*0.1
total_2= tip+total_1
#each person
person= total_2/number
print("Each person has to pay", person)