# Exercise 1: (3 points)
grades = [90,100,70,45,76,84,93,21,36,99,100]
A=0
B=0
C=0
D=0
F=0
for g in grades:
    if g<60:
        F+=1
    elif g<70:
        D+=1
    elif g<80:
        C+=1
    elif g<90:
        B+=1
    elif g>90:
        A+=1
print("In the above list there are",A,"A's",B,"B's",C,"C's",D,"D's",F,"F's")

# Exercise 2: (3 points)
grades = [93, 74, 66, 98, 34, 75, 79, 83, 84, 91, 12, 69, 72]

for i in range(len(grades)):
    if grades[i]<70:
        grades[i]+=8
    elif grades[i]<80:
        grades[i]+=5
    elif grades[i]<90:
        grades[i]+=2

print(grades)

# Exercise 3: (3 points)
sales=[]
for i in range(7):
    num=int(input("Enter sales for Day #"+str(i+1)+": "))
    sales.append(num)
print("Sales for the week:",sales)

# Exercise #4: (3 points)
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

first_3=my_list[:3]
print(first_3)
specific=my_list[1:4]
print(specific)
last_4=my_list[-4:]
print(last_4)

# Exercise #5: (3 points)
products = ["apple", "pear", "peach", "banana"]
user_req=input("What product do you want? ")
if user_req.lower() in products:
    print(user_req,"is in our invertory.")
else:
    print("Product not found.")

# Exercise #6: (3 points)
a = [1,2,3,4,5]
b = [2,3,10,11,12,1]
common=[]
for e in a:
    if e in b:
        common.append(e)
print(common)

# Exercise #7: (3 points)

first_names=[]
name=input("Enter the first name or type end to stop:")
while name.lower() !="end":
    if name not in first_names:
        first_names.append(name)
    name = input("Enter the first name or type end to stop:")
print(first_names)

# Exercise #8: (3 points)
products = ["apple", "pear", "peach", "banana"]
prod=""

while len(products)>0 and prod.lower()!="end":
    prod=input("Enter the product you want: ")
    if prod.lower() in products:
        products.remove(prod.lower())
        print(products)
    elif prod.lower()=="end":
        prod=prod
    else:
        print("We do not carry such product at present.")

# Exercise #9: (3 points)
products = ['peanut butter', 'jelly', 'bread']
prices = [3.99, 2.99, 1.99]
print("Select a product from list:",products)
prod =input()
ind=products.index(prod.lower())
print("The price of",prod,"is $"+str(prices[ind]))

# Exercise #10: (3 points)

student_num=int(input("How many students are present in your class?"))
assign_num=int(input("How many assignments have been given to students?"))
for i in range(student_num):
    total=0
    for j in range(assign_num):
        score =int(input("Enter score of Student "+str(i+1)+" and assignment "+str(j+1)+": "))
        total=total+score
    avg=total/assign_num
    print("Average grade for student",(i+1),"is",avg)
