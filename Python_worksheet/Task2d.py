#percentage calculator
print("What is the price of the product?")
price= int(input(""))

#calculation
discount= price*0.2
final= price-discount

print("Your new price is", final)
print("You saved", discount)