# Exercise 2.1: (2.5 points)
coin_in=int(input("Enter a coin value: "))
if coin_in==1:
    print("That’s a penny!")
elif coin_in==5:
    print("That’s a nickle!")
elif coin_in==10:
    print("That’s a dime!")
elif coin_in==25:
    print("That’s a quarter!")
elif coin_in==50:
    print("That’s a half dollar!")
else:
    print("That’s not a valid coin!")

# Exercise 2.2: (2.5 points)
num=int(input("Enter a number between 1 and 10: "))
if num>=1 and num<=10:
    if num%2==0:
        print(num,"is even number.")
    else:
        print(num,"is odd number.")
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count+=1
    if count>2 :
        print(num,"is not prime number.")
    elif count==2 and num!=1:
        print(num,"is prime number.")
else:
    print(num, "is not in between 1 and 10, ending the program.")

# Exercise 2.3: (2.5 points)

price=float(input("Enter the price of item: "))
while price<=0:
    price=float(input("Price should be positive, Enter the price of item again: "))
if price<=10:
    print("No discount.")
elif price<=50:
    print("10% discount.")
elif price >50:
    print("20% discount.")

# Exercise #2.4: (2.5 points)

start_num=int(input("Enter starting number: "))
end_num=int(input("Enter ending number: "))
type=input("Enter even or odd for customization: ")

while (start_num<=end_num):
    if type.lower()=="even":
        if start_num%2==0:
            print(start_num)
    elif type.lower()=="odd":
        if start_num%2==1:
            print(start_num)
    start_num+=1

# Exercise #2.5: (3 points)

num_prod=int(input("Enter number of products: "))
count=1
sum=0
while (count<=num_prod):
    price=float(input("Enter price of #"+str(count)+": "))
    sum=sum+price
    count+=1
print("Total cost:",sum)

# Exercise #2.6: (3 points)

repeat="yes"
while(repeat.lower()=="yes"):
    price=float(input("Enter an item price: "))
    print("Tax on this item is",format((0.07*price),".2f"),"; total price:",format(1.07*price,".2f"))
    repeat=input("Enter another price? (yes or no): ")

# Exercise #2.7: (3 points)
amt_sum=0
tax_sum=0
repeat="yes"
while(repeat.lower()=="yes"):
    price=float(input("Enter an item price: "))
    tax=0.07*price
    price=1.07*price
    tax_sum+=tax
    amt_sum+=price
    print("Tax on this item is",format(tax,".2f"),"; total price:",format(price,".2f"))
    repeat=input("Enter another price? (yes or no): ")
print("Total amount due:",format(amt_sum,".2f"))
print("Total tax due:",format(tax_sum,".2f"))

# Exercise #2.8: (3 points)
ans=0
while(2+2!=ans):
    ans=int(input("What is 2+2?"))
    if ans==(2+2):
        print("Correct!")
    else:
        print("Wrong, try again.")

# Exercise #2.9: (3 points)

import random
num1=random.randint(0,10)
num2=random.randint(0,10)
ans=num1+num2-1
while((num1+num2)!=ans):
    ans=int(input("What is "+str(num1)+"+"+str(num2)+"?"))
    if ans==(num1+num2):
        print("Correct!")
    else:
        print("Wrong, try again.")