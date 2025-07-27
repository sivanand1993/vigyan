#1. Change Calculator (2.5 points)
pennies=int(input("How many pennies do you have? "))
nickels=int(input("How many nickels do you have? "))
dimes=int(input("How many dimes do you have? "))
quarters=int(input("How many quarters do you have? "))

total=pennies*.01+nickels*.05+dimes*.1+quarters*.25
amount=format(total,".2f")
print("You have $",amount,"in change.")

#2. Currency Exchange

exchange_rate=input("Enter exchange rate: ")
exchange_rate=float(exchange_rate)

amount=float(input("How much would you like to convert? "))

#calculate values
us_dollars=exchange_rate*amount
amount=format(amount,".2f")
print(amount,"of this currency is equal to","$",us_dollars,"USD.")