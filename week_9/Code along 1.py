# # Week 9
# # Code along lab - composition & Properties
#
class Person:
    def __init__(self,first_name,last_name,uNID,
                 student=None,teacher=None):
        self._first_name=first_name
        self._last_name=last_name
        self._uNID=uNID
        self.student=student
        self.teacher=teacher

    @property
    def firstName(self):
        return self._first_name

    @firstName.setter
    def firstName(self,value):
        self._first_name=value

    @property
    def lastName(self):
        if self._last_name!=None:
            return self._last_name
        else:
            return "Not set"

    @lastName.setter
    def lastName(self,value):
        self._last_name=value
#
# a_person=Person()
# a_person.firstName="Sivanand"
# a_person.lastName="Sista"
# print(a_person.lastName,a_person.firstName)

class Student:

    def __init__(self):
        self.classes=[]

    def enroll(self,course):
        self.classes.append(course)

    def schedule(self):
        return self.classes

class Teacher:
    def __init__(self):
        self.courses_taught=[]

    def assign_teaching(self,course):
        self.courses_taught.append(course)


obj=Person("Sivanand","Sista","u1304335",Student(),Teacher())
obj.student.enroll("Python 6850")
obj.student.enroll("Economics 6000")
obj.teacher.assign_teaching("History")
print(obj.student.schedule())


#2.2. Properties Exercise: (5 points)

class Person():

    def __init__(self, firstname, lastname):
        self._first=firstname
        self._last=lastname


    @property
    def firstName(self):
        return self._first

    @firstName.setter
    def firstName(self, value):
        self._first = value

    @property
    def lastName(self):
        return self._last


    @lastName.setter
    def lastName(self, value):
        self._last = value

    @property
    def fullname(self):
        return self._first+" "+self._last

    @fullname.setter
    def fullname(self,value):
        name=value.split()
        self._first=name[0]
        self._last=name[1]

    def email(self):
        return '{}.{}@email.com'.format(self._first, self._last)

siva = Person("Sivanand", "Sista")
siva.fullname="Sivanand Sista"
print(siva.fullname)


