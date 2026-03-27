print("How much money do you want to borrow from the bank?")
amount= int(input(""))
print("Enter how much months you would like to repay the loan in")
months= int(input(""))
#calculation
intrest=amount*0.15
total=intrest+amount
per_month= total/months
print("Your payment per month will be", per_month)