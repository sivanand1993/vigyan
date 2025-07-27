# part1 boolean values
print(True)
print(type(True))
print(False)
print(1==1)
print(1==2)
print(1!=1)
print(1<2)
print(1>2 and 2<5)
print(1<3>5-3)
print(1>2 or 2<5)
print(not 1>2 and not 2<5)

# part2
# one way condition
x=5
if x>0:
    print("X is positive")
elif x==0:
    print("X is zero")
else:
    print("X is negative")

print("This line will always print")

x=int(input("Enter a number: "))
if x>0:
    print("X is positive")
    if x%2==0:
        print("Number is even!")
    else:
        print("Number is odd!")
else:
    print("X is not a positive number")