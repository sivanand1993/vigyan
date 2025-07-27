#1. Divide by zero exception (5 points)
def divide(num1,num2):
    try:
        num=num1/num2
        return num
    except:
        return "invalid argument"

print(divide(3,0))

#2. Basic exception handling (5 points)
try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except :
    print("There is a string in the list")

#3. try-except-finally (5 points)

x = 5
y = 0
try:
    z = x/y
except:
    print("Seems like problem with division")
finally:
    print("All Done.")

4. try-except-else-finally (5 points)

def ask():
    while True:
        try:
            num = int(input("Input an Integer: "))
            print(f"Thank you, your number squared is: {num**2}")
        except:
            print("An error occurred! Please try again!")
        else:
            break
ask()