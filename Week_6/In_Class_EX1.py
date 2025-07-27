#1. Name function (5 points)
def fullname(fname,lname,minit):
    return f"{fname} {minit} {lname}"
name=fullname("Sivanand","Sista","K")

print(name)

#2. String function practice (5 points)
#.1
print('Welcome to O\'Neil\'s Boat Rentals!')
#.2
string="Hello there!\nHow are you?\nI\'m doing fine."
print(string)
#.3
string="hello python".upper()
print(string)
#.4
cond=True
while(cond):
    age=input("Enter your age: ")
    if age.isdecimal():
        cond=False
#.5
fname="Sivanand"
lname="Sista"
full_name=f"{fname} {lname}"
print(full_name.center(25,"*"))
