prices=[1.10,0.99,5.75]

for item_price in prices:
    print("Original price:",item_price)
    item_price*=1.07
print("Original prices:",prices)

i=0
for item_price in prices:
    prices[i]*=1.07
    prices[i]=format(prices[i],".2f")
    i+=1

print(prices)

prices=[1.10,0.99,5.75]
position=0
while position<len(prices):
    prices[position]*=1.07
    prices[position]= format(prices[position],".2f")
    position+=1

print(prices)

my_numbers="10,20,30,40,50,60"
print(my_numbers)
number_list=my_numbers.split(",")
print(number_list)
print(type(number_list))
print(len(number_list))

my_string="apples,bananas,oranges"
string_list=my_string.split(",")
print(string_list)
print(string_list[1])

my_time="10:05:45, 09:45:32, 07:30:25"
time_list=my_time.split(",")
for item in time_list:
    time=item.split(":")
    print(time)
time="07:49:34"
hrs,mins,sec=time.split(":")
print(hrs,mins,sec)
