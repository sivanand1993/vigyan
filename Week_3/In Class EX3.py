#1 Input with a for-loop (4.5 points)
length=int(input("How many numbers you want to enter:"))
sum=0
for i in range(length):
    num=float(input("Enter num #"+str(i+1)+": "))
    sum=sum+num
print("Total :",sum)

#2 Find the vowels – for loop (4.5 points)

word=input("Type the word: ")
total=0
vowels_found=[]
for i in word:
    if i.lower() in ["a","e","i","o","u"]:
        total+=1
        vowels_found.append(i)
print("Number of vowels in",word,"are",total)
print("Vowels found:",vowels_found)