while True:
    file_name=input("Enter file name: ")
    try:
        fhandle=open(file_name,'r')
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