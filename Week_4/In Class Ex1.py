#3.1. Split Number List (2.5 points)
num_string='10 67 123 46 20 18 36 250'
num_list=num_string.split()
print(num_list)

num_string='10,67,123,46,20,18,36,250'
num_list=num_string.split(",")
print(num_list)

#3.2 Split Data into List (2.5 points)

num_string='90,67,87,102,77,80'
num_list=num_string.split(",")
total=0
for num in num_list:
    total+=float(num)
print("Total: ",total)

#3.3 Slice Lists (2.5 points)

num_list=[1,2,3,4,5,6,7,8,9]
print(num_list[:4])

#3.4 Slice Lists with Increment (2.5 points)

alphabet_list=['a','b','c','d','e','f','g']
print(alphabet_list[::2])
