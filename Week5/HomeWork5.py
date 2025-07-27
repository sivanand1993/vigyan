#Exercise #1: (5 points)
def topOrBottom():
    print ("#####")
topOrBottom()
print("#   #")
print(" # # ")
print("  #")
print(" # # ")
print("#   #")
topOrBottom()

#Exercise #2: (5 points)
def feet_to_inch(num):
    print("...",format(12*num),"inches")
def feet_to_meter(num):
    print("...",(format(0.3048*num,".4f")),"meters")

for i in range(10):
    print(i,"ft:")
    feet_to_inch(i)
    feet_to_meter(i)

# Exercise #3: (5 points)
import random
def roll(num):
    num1=random.randint(1,num+1)
    num2=random.randint(1,num+1)
    if num1<=num2:
        string=str(num)+" sided dice roll: "+str(num1)+" & "+str(num2)
    else:
        string = str(num) + " sided dice roll: " + str(num2) + " & " + str(num2)
    print(string)
for i in range(6,11):
    roll(i)

#Exercise #4: (5 points)
secretNumber = random.randint(1, 20)
print(secretNumber)
print("I am thinking of a number between 1 and 20.")
def guess(num,guesses):
    if guesses<=6:
        if num==secretNumber:
            print("Good job! You guessed my number in",guesses,"guesses!")
            return True
        elif num<secretNumber:
            print("Your guess is too low.")
            return False
        elif num>secretNumber:
            print("Your guess is too high.")
            return False
x=False
for guessesTaken in range(1,8):
    if guessesTaken>6:
        print("Nope. The number I was thinking of was",secretNumber)
    else:
        print("Take a guess.")
        num = int(input())
        x=guess(num,guessesTaken)
        if x==True:
            break





