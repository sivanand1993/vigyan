#1. Password verification
password="python123"
user_entry=input("Enter password: ")
if user_entry==password:
    print("Access granted")
else:
    print("Access denied")

#2. Voting Age
voting_age=18
user_age=int(input("Please enter your age: "))
if user_age>=voting_age:
    print("You are eligible to vote")
else:
    print("You are eligible to vote after",voting_age-user_age,"years.")

#3. Dress for Weather
temp=int(input("Enter temperature: "))
if temp<40:
    print("Wear a warm coat.")
elif temp<70:
    print("Wear a light jacket.")
elif temp<100:
    print("Wear something cool.")
elif temp>=100:
    AC=input("Do you have air conditioning at home? (yes/no): ").upper()
    if AC=="YES":
        print("Stay at home.")
    elif AC=="NO":
        print("Bummer, try a swimming pool.")