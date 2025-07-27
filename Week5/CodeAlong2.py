def format_name(first_name,last_name):
    return first_name+" "+last_name
first_name=input("What is your first name? ")
last_name=input("What is your last name? ")
print("Hello",format_name(first_name,last_name))

def average(num1,num2,num3):
    sum=num1+num2+num3
    avg=sum/3
    print(avg)

average(5,18,25)

def func(num1,num2):
    if num1<0:
        return
    else:
        retval=num1+num2
        return retval
print(func(-1,20))

def print_dict(dictionary):
    keys=list(dictionary.keys())
    values=list(dictionary.values())

    for i in range(0,len(keys)):
        k=keys[i]
        v=values[i]
        print(str(k),str(v))

example_dict={
    "name":"Thor",
    "age":"25"
}

print_dict(example_dict)

def sum_two_numbers(a,b):
    return a+b
num1=int(input("Enter a number: "))
num2=int(input("Enter another number: "))
print(sum_two_numbers(num1,num2))

def multiply(a,b=2):
    return a*b

print(multiply(2,3))
print(multiply(2))

def func(*args):
    print(type(args))
    print(args)

func(1,2,3,4,5,6,7,8,9,10)

def func(**kwargs):
    print(kwargs)

func(a=1,b=2,c=3)

def db_connect(**options):
    conn_string={
        "host":options.get("host","127.0.0.1"),
        "port":options.get("port",5432),
        "user":options.get("user","admin"),
        "pwd":options.get("pwd",""),
        "catalog":options.get("catalog","default_name")
    }
    print(conn_string)

db_connect(host="192.0.0.1",port=12202,user="Admin",pwd="gandalf",catalog="SafeUT")

def db_connect(host,port,user,pwd,catalog):
    print(host,port,user,pwd,catalog)

db_connect("192.0.0.1","12202","Admin","ItsASecrect")