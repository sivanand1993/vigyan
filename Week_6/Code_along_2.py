number_of_scores=int(input("enter how many scores: "))
scores=[]
for x in range(0,number_of_scores):
    while True:
        try:
            score=int(input("What is score #: "+str(x+1)+" "))
            scores.append(score)
        except:
            print("invalid score value. Please try again.")
        else:
            break
try:
    print(sum(scores)/0)
except ValueError:
    print("You entered wrong value")
except TypeError:
    print("You might have entered a string")
except:
    print("Something went wrong")

while True:
    try:
        email_address=input("Enter email address: ")
        parts=email_address.split("@")
        name=parts[0]
        domain=parts[1].split(".")
        print("The email address is:",name,domain[0],domain[1])
        break
    except:
        print("Not valid address, please try again")
