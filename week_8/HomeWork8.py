# Exercise #1 : (10 points)
class Spell:
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation

    def __str__(self):
        return self.name + " " + self.incantation + "\n" + self.get_description()

    def get_description(self):
        return "No description"

    def execute(self):
        print(self.incantation)

class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, "Accio", "Summoning Charm")

    def get_description(self):
        return "Summons object towards the invoker."

class Confundo(Spell):

    def __init__(self):
        Spell.__init__(self, "Confundo", "Confundus Charm")

def get_description(self):
    return "Causes the victim to become confused and befuddled."

def study_spell(spell):
        print(spell)

spell = Accio()
spell.execute()
study_spell(spell)
study_spell(Confundo())

## 1 Accio and Confundo are the child classes of Class Spell
## 2 Prints
# line1: Accio
# line2: Summoning Charm Accio
# line3: No description
# line4: Confundus Charm Confundo
# line5: No description

## 3 get_description method in Class Spell is executed when study_spell(Confundo()) is called since get_description in Class Confundo
# is out of indentation
## 4
print (Accio())
## added a get_description method inside the Accio class

#Exercise #2: (10 points)

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self):
        return "Vehicle Name: "+self.name+" Speed: "+str(self.max_speed)+" Mileage: "+str(self.mileage)

# creating a bus object
bus=Vehicle("School Volvo",180,12)
print(bus)

# Exercise #3: (10 points)

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(Vehicle):

    def fare(self):
        return (self.capacity * 100)*1.1

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

# Exercise #4: (10 points)
class Numbers:
    MULTIPLIER=100
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def multiply(self, a):
        return self.MULTIPLIER * a

    @staticmethod
    def subtract(b, c):
        return b-c

    @property
    def value(self):
        return self.x, self.y

    @value.setter
    def value(self,x,y):
        self.x=x
        self.y=y

    @value.deleter
    def value(self):
        del self.value
    # TODO: Create a setter and a deleter for value.


# test the class.
num = Numbers(5, 6)
print(num.add())
print(num.multiply(2))
print(num.subtract(4, 4))

# Exercise #5 “Abstract classes” (10 points)
class Box:
    def add(self, *items):
        raise NotImplementedError()

    def empty(self):
        raise NotImplementedError()

    def count(self):
        raise NotImplementedError()


class Item:
    def __init__(self, name, value):
        self.name=name
        self.value=value


class ListBox(Box):
    def __init__(self):
        self._items = []

    def add(self, *items):
        self._items.extend(items)

    def empty(self):
        self.items=self._items
        self._items=[]
        return self.items

    # TODO: create a new variable called items and set it equal to _items.
    # TODO: set the private variable _items to a new list, this will make _items empty again.
    # TODO: return the new items variable.

    def count(self):
        return len(self.items)
        # TODO: Create a return statement to return the length of the items.


class DictBox(Box):
    def __init__(self):
        self._items = {}

    def add(self, *items):
        self._items.update(dict((i, i) for i in items))

    def empty(self):
        self.items=self._items
        self._items={}
        return self.items

    # TODO: create a new variable and set it equal to the dictionary values.
    # TODO: set the private variable _items to a new dictionary to make it empty.
    # TODO: return the new variable.

    def count(self):
        return len(self.items)


# TODO: Create a return statement to return the length of the items.


def repack_boxes(*boxes):
    items = []

    # get all the items from each box, save it to a new variable called items, then empty the boxes.
    for box in boxes:
        items.extend(box.empty())

    # now we have all of the items in each box inside one list, traverse the list of items.

    while items:

        # for each box passed in, add an item to box, remove the item from the item list as its added to the box.
        # if we pass in 3 boxes to this function, that means we'll add 3 items to the boxes and remove those items from the list on each pass within the for loop.

        for box in boxes:
            try:
                box.add(items.pop())
            # TODO: for each box in boxes: box.add(items.pop())
            except IndexError:
                break

box1 = ListBox()
for i in range(20):
    item = Item(str(i), i)
    box1.add(item)


box2 = ListBox()
for i in range(9):
    item = Item(str(i), i)
    box2.add(item)


box3 = DictBox()
for i in range(5):
    item = Item(str(i), i)
    box3.add(item)


repack_boxes(box1, box2, box3)

print(box1.count())
print(box2.count())
print(box3.count())