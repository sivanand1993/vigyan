# #2.1. Sum of numbers (3 points)
# def summing(a):
#     return sum(a)
#
# x=summing([1,2,3,4])
# print(x)
#
# #2.2. Number power (3 points)
# def raise_pow(a,b):
#     res=1
#     for i in range(b):
#         res*=a
#     return res
# print(raise_pow(3,2))

#2.3. Tax function (3 points)
def tax_func(price):
    return price*1.07

amt_sum=0
tax_sum=0
repeat="yes"
while(repeat.lower()=="yes"):
    price=float(input("Enter an item price: "))
    tax=0.07*price
    price=tax_func(price)
    tax_sum+=tax
    amt_sum+=price
    print("Tax on this item is",format(tax,".2f"),"; total price:",format(price,".2f"))
    repeat=input("Enter another price? (yes or no): ")
print("Total amount due:",format(amt_sum,".2f"))
print("Total tax due:",format(tax_sum,".2f"))

#2.4. Average function (3 points)
def average(num1,num2,num3):
    sum=num1+num2+num3
    avg=sum/3
    return avg
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
print("Average is",average(num1,num2,num3))