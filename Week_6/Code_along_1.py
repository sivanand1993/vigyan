# Week 6
# Lab 1
print("The {} {} {}".format("Fox","Brown","Quick"))
# Index name
print("The {2} {1} {0}".format("Fox","Brown","Quick"))
# Key
print("The {q} {b} {f}".format(f="Fox",b="Brown",q="Quick"))

# float format
#{value:width.precision f}
result=100/777
print(result)
print("The result {r:1.3f}".format(r=result))

name="john"
age=25
name1=f"Hello, my name is {name}"
print(name1)
print(f"Hello, my name is {name}, my age is {age}")