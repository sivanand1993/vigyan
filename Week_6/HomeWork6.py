# Exercise #1: (6 points)
try:
    fhandler=open("most_popular_words_in_english.txt",'r')
    word = input("Enter a word: ")
    for line in fhandler:
        try:
            if word.lower() == line.split("\n")[0].lower():
                print("It is one of the most popular words in English")
                break
        except:
            print("Something went wrong.")

except:
    print("File not found ")
finally:
    fhandler.close()

# Exercise #2: (6 points)
fname="security.txt"
try:
    sec_file = open(fname, 'w')
    user_name=input("Enter username: ")
    password=input("Enter password: ")
    sec_file.write(f"username:{user_name}\n")
    sec_file.write(f"password:{password}\n")

except:
    print("Something is wrong!")
finally:
    sec_file.close()

#Exercise #3: (6 points)
fname="security.txt"
try:
    fhandler=open(fname,'r')
    for line in fhandler:
        if line.startswith("username"):
            username=line.split(":")[1].split("\n")[0]
        elif line.startswith("password"):
            password=line.split(":")[1].split("\n")[0]
    while True:
        user_name=input("Enter username: ")
        if user_name!=username:
            print("No such user exists, Please try again.")
        else:
            user_password=input("Enter passowrd: ")
            if user_password!=password:
                print("Wrong Password!, Try again from first.")
            else:
                print("Access granted!")
                break
except:
    print("File not found ")
finally:
    fhandler.close()

# Exercise #4: (6 points)
fname="testscores.txt"
scores=[]
try:
    fhandler=open(fname,'r')
    for line in fhandler:
        if not line.split("\n")[0].isdecimal():
            student_name=line.split("\n")[0]
        else :
            scores.append(int(line.split("\n")[0]))
except:
    print("File not found ")
finally:
    fhandler.close()
print(f"Student {student_name} secured an average score of "+format(sum(scores)/len(scores),".2f")+".")
