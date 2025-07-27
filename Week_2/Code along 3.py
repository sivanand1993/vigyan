import random
"""
generate 2 random numbers
ask the user what the sum of generated numbers are
add the sum together
begin loop, while the answer does not equal the sum
if correct , print correct and end loop
else, print incorrect and prompt the user to try again.
"""

num1=random.randint(0,10)
num2=random.randint(0,10)
answer=int(input("What is the sum of "+str(num1)+"+"+str(num2)+": "))
num_sum=num1+num2
if answer==num_sum:
    print("Correct")

while answer!=num_sum:
    print("Incorrect, try again")
    answer = int(input("What is the sum of " + str(num1) + "+" + str(num2) + ": "))
    if answer == num_sum:
        print("Correct")

number=int(input("Enter number: "))

while number>=0:
    print(number)
    number-=1
else:
    print("Done!")

quantity=int(input("How many random numbers would you like to generate? "))
while quantity>0:
    number=random.randint(1,100)
    print(number)
    quantity=quantity-1