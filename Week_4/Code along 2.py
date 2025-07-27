my_dict={
    "name":"Thor",
    "age": "1500"
}
print(my_dict)

example_dict={
    "animals":["Dog","Cats","Fish","Tigers"],
    "number":1,
    "a_name":"Odin",
    "a_boolean":True,
    "another_dict":{"you could":"keep going",
                    "Like this":"Forever"}
}

for key in example_dict:
    print(key)

for item in example_dict.items():
    print(item)
seasons={"Fall":["September","October","November"],
         "Spring":["March","April","May"],
         "Summer":["June","July","August"]}
print(seasons)
winter={"Winter":["December","January","February"]}
seasons.update(winter)
print(seasons)

for key,value in seasons.items():
    print(key+":",value)

# sets demo
small_primes=set()
small_primes.add(2)
small_primes.add(3)
small_primes.add(5)
print(small_primes)
small_primes.add(1)
small_primes.add(1)
small_primes.remove(1)
print(small_primes)

# tuples
t=("a","b","c","e")
print(t)
print(type(t))

