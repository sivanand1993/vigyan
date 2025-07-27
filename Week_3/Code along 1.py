empty_list=[]

# mix of data types
my_list=[95,3.2,"Marvel",17,-4]
print(my_list[2])
print("list contents:",my_list)

# create a second list
second_list=[100,101]
print("Second list:",second_list)

second_list=second_list*2
print("Second list repeated:",second_list)

big_list=my_list+second_list
print(big_list)

# List of Marvel Characters
characters=["Thor","Thanos","Black Panther","Ironman","Hulk","Batman","Captain America"]
print(characters)
print(len(characters))
print(characters[2])
print(characters[1:3])
print(characters[1:5])
print(characters[-3])
print(characters[-4:])
print(characters*2)
print(characters[::3])
print(characters[2][-1])
