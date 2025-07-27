import pandas as pd
# file=pd.read_csv(r'C:\Users\anand\Desktop\Expenses.txt')
# print(file.head())
df=pd.DataFrame( columns=['Date','Location','Cost'])
with open(r'C:\Users\anand\Desktop\Expenses.txt') as f:

    for l in f:
        l.replace("\n","")
        d,c=l.split(" ")[0],l.split(" ")[-1]
        df_dum = pd.DataFrame([[d, l, c]],columns=['Date', 'Location', 'Cost'])
        df=pd.concat([df_dum, df])

df.to_csv(r'C:\Users\anand\Desktop\Expenses.csv',sep='|')