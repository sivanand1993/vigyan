#2.1. Shapes (5 points)
shapes = ['square', 'circle']
shapes.append("traingle")
print(shapes)
shapes.insert(3,"rectangle")
print(shapes)
shapes.remove("rectangle")
print(shapes)
del shapes[2]
print(shapes)

#2.2. Sorting (5 points)
ages = [27, 60, 14, 35, 3, 76]
ages.sort()
print(ages)
names = ['Quinn', 'John', 'Amber', 'Kim']
names.sort()
print(names)
stats = [[3, 2], [1, 2], [1, 1], [3, 1]]
stats.sort()
print(stats)

#2.3. Min-Max (5 points)
numbers = [6, 10, 3, 24, 79, 24]
print("min:",min(numbers),"max:",max(numbers))