#1 Countdown
number=int(input("Enter number: "))

while number>=1:
    print(number)
    number-=1
else:
    print("Done!")

#2 Shopping Total
total=0
tax=8.875
price=input("Enter the price of the item: ")
while price.upper()!="DONE":
    price=float(price)
    while price<0:
        price = float(input("Enter again, price should be greater than 0: "))
    else:
        total=total+price
        price = input("Enter the price of the next item or type done to stop: ")
amount=format(total+(total*tax/100),".2f")
print("Prices of all items after including tax is $"+str(amount))


