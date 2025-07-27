# append example
my_list=["Calvin","Caleb","Sergio","Jason","Dhanya"]
my_list.append("Steen")
my_list.append("Coleman")
print(my_list)

location=my_list.index("Jason")
print(location)

#del example
del my_list[1]
print(my_list)

#pop example
my_list=[4,3,5]
print(my_list)
item=my_list.pop(1)
print(my_list)
print(item)

# reverse example
my_list.reverse()
print(my_list)

# min & max functions
prices=[3.99,2.99,1.99,1.98,4.99,0.99,0.99]
max_price=max(prices)
min_price=min(prices)
print(min_price,"up to",max_price)

prices.insert(1,6.99)
prices.remove(0.99)
prices.sort()
print(prices)
prices.sort(reverse=True)
print(prices)
max_price=max(prices)
min_price=min(prices)
print(min_price,"up to",max_price)