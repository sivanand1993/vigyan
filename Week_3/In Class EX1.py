#1.1. Color List (2.5 points)
colors=["blue","red","yellow","green","orange","black","white"]
print("Colors:",colors)
print("Length of colors:",len(colors))
print("Position 4:",colors[4])
print(colors[1:5])
print(colors[-3:])
print(colors*2)

#1.2. Color List Mutation (2.5 points)
colors[5]="indigo"
print("Position 5:",colors[5])
colors[2]=colors[4]
print(colors[2],colors[4])

new_colors=["violet","pink","brown"]
big_list=colors+new_colors
print(big_list)

big_list[5]=colors
print(big_list)
