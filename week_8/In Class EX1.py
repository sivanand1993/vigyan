#1.1. Ice Cream Shop inherits from Restaurant (5 points)
class Restaurant:

    def __init__(self, name, cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type

    def describe_restaurant(self):
        print( self.name+" has cuisine type "+ self.cuisine_type)

    def open_restaurant(self):
        print(self.name + " is open for business")

class Ice_Cream_Stand(Restaurant):
    def __init__(self,name, cuisine_type,flavors):
        Restaurant.__init__(self, name, cuisine_type)
        self.flavors=flavors

    def get_flavors(self):
        print("Flavors available are",",".join(self.flavors))

ice_cream = Ice_Cream_Stand("My Ice Cream Shoppe", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry"])
ice_cream.describe_restaurant()
ice_cream.open_restaurant()
ice_cream.get_flavors()

#1.2. Admin inherits from User (5 points)
class User:
    def __init__(self,first_name,last_name,mobile,state):
        self.first_name=first_name
        self.last_name=last_name
        self.mobile=mobile
        self.state=state

    def describe_user(self):
        print("User",self.first_name,self.last_name,"has mobile",self.mobile,"and lives in",self.state)

    def greet_user(self):
        print("Greetings",self.first_name,self.last_name)

user1=User("Sivanand","Sista",9999,"Utah")
user2=User("Soumith","M",888,"California")
user3=User("Sharath","P",777,"Washington")

user1.greet_user()
user1.describe_user()

user2.greet_user()
user2.describe_user()

user3.greet_user()
user3.describe_user()

class Admin(User):
    def __init__(self,first_name,last_name,mobile,state,privileges):
        User.__init__(self,first_name,last_name,mobile,state)
        self.privileges=privileges

    def show_privileges(self):
       print("User",self.first_name,self.last_name,"has privileges",",".join(self.privileges))



user4=Admin("Siddharth","H",111,"Texas",["can add post","can delete post","can ban user"])
user4.greet_user()
user4.describe_user()
user4.show_privileges()