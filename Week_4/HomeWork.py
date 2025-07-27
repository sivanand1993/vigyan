# Exercise #1: (10 points)
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12,'map fragments':3}
sum=0
print("Inventory:")
for key,value in stuff.items():
    print(value,key)
    sum=sum+value
print("Total number of items :",sum)

# Exercise #2: (10 points)
characters = ["Thor", "Thanos", "Black Panther", "Iron Man", "Hulk", "Batman", "Captain America"]
i=0;string=""
while(i<len(characters)):
    if i==len(characters)-1:
        string=string+" and "+characters[i]
    else:
        string = string + ", " + characters[i]
    i+=1
string=string[2:]
print(string)

# Exercise #3: (10 points)
definitions={'dict':"stores a key/value pair", 'list':"stores a value at each index", 'map':"see dict",
             'set':"stores unordered unique elements",'exit':"**Ending the program**"}
user_input=""
while(user_input!="exit"):
    user_input=input("Type dict/list/map/set to know their definition or type exit to end program: ").lower()
    print(definitions[user_input])

