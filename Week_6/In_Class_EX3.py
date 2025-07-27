# #1. Exception handling (5 points)
while True:
    try:
        num = int(input("Enter a valid number: "))
    except:
        print("Number is not valid!")
    else:
        print("valid integer")
#2. File IO (5 points)
while True:
    file_name=input("Enter file name: ")
    try:
        fhandle=open(file_name,'w')
        while True:
            text=input("What do you want to write out? ")
            if text.lower()=="done":
                break
            fhandle.write(text+"\n")
    except Exception as exe:
        print(exe)
    else:
        break
    finally:
        fhandle.close()

#3. Name (5 points)
file_name=input("Enter file name: ")
try:
    fhandle=open(file_name,'r')
    for line in fhandle:
        print (line)
except :
    print("File not found")
finally:
    fhandle.close()