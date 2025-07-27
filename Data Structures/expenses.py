import pandas as pd

file=pd.read_csv(r"C:\Users\anand\Desktop\Expenses.txt",sep="|",header=None)
file["data"]=file
new_file=pd.DataFrame({"date" : [],"data" : [],"price" : []})
c=0
for i in file["data"]:
    temp_file = pd.DataFrame({"date": [i.split(" ")[0]],
                        "data": [i],
                       "price":[i.split(" ")[-1]]}
                    )
    new_file=pd.concat([new_file,temp_file],ignore_index=True)

new_file.to_excel(r"C:\Users\anand\Desktop\Expenses.xlsx",engine="openpyxl")