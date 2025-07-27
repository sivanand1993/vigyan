# Exercise #1: (5 points)

import datetime

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):

        self.name = name

        self.surname = surname

        self.birthdate = birthdate

        self.address = address

        self.telephone = telephone

        self.email = email

        self.age_calculated_on=None


    def age(self):

        today = datetime.date.today()

        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):

            age -= 1

        return age

    def age_last_calculated(self):
        self.age_calculated_on=datetime.date.today()
        return self.age_calculated_on

person = Person(

    "Jane",

    "Doe",

    datetime.date(1992, 3, 12), # year, month, day

    "No. 12 Short Street, Greenville",

    "555 456 0987",

    "jane.doe@example.com"

)


print(person.name)

print(person.email)

print(person.age())

#1 Person: Person is a class and scope is global
#2 person: person is an instance and scope is outside the class
#3 surname: surname is an object passed as an argument passed to instructor init
#4 self: self is an instance of the class through which we can access attributes and methods in class
#5 age (the function name): age is a method which can accessed by class Person or a defined capability in a class
#6 age (the variable used inside the function): A bit od data in a class
#7 self.email: it is a variable whose scope is local within the class it is different from the arument email defined in __init__
#8 person.email: It refers to variable defined inside Person class

# Exercise #2: (5 points)
print(person.age_last_calculated())

# Exercise #3: (5 points)

class Square:
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side**2

square=Square(4)
print(square.area())

# Exercise #4: (5 points)

person2=Person(
    "Sivanand",

    "Sista",

    datetime.date(1993, 1, 10), # year, month, day

    "Liberty Crest Apt",

    "555 456 0987",

    "anand1993@gmail.com"
)

print(dir(person))
print(dir(Person))
#i)
print(person.__str__())
#ii)
print(type(person2))
#iii)
print(type(Person))
#iv)
def fun(val):
    lis=dir(val)
    i=0
    while i<len(lis):
        if "__"in lis[i]:
            lis.remove(lis[i])
        else:
            i+=1
    return lis

print(fun(person2))
print(fun(Person))

# Exercise #5: (5 points)
class Reversestring:
    def __init__(self,sentence):
        self.sentence=sentence

    def reverse_str(self):
        return " ".join(self.sentence.split()[::-1])

str="The quick brown fox jumps"

rev_str=Reversestring(str)
print(rev_str.reverse_str())

# Exercise #6: (5 points)
import math
class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi*self.radius**2

    def perimeter(self):
        return 2*math.pi*self.radius

circle=Circle(10)
print(circle.area())
print(circle.perimeter())

# Exercise #7: (5 points)
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

rectangle=Rectangle(5,10)
print(rectangle.area())

# Exercise #8: (5 points)
import math
class Line:

    def __init__(self, coor1, coor2):
        self.coor1=coor1
        self.coor2=coor2

    def distance(self):
        total=0
        for i in range(len(self.coor1)):
            total=total+(self.coor1[i]-self.coor2[i])**2

        return math.sqrt(total)

    def slope(self):
        return (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)
print(li.distance())
#9.433981132056603

print(li.slope())
#1.6

# Exercise #9: (5 points)
# Step 1
def collatz(num):
    if (num%2) == 0:
        print(num//2)
        return (num//2)
    else:
        print(3*num+1)
        return (3*num+1)

# Step 2
user_num=int(input("Enter a number: "))

while user_num!=1:
    user_num=collatz(user_num)

