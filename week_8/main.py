class X:
    def __init__(self,name,mood):
        self.name=name
        self.mood=mood

    def __str__(self):
        state = "     I'm " + self.name + ". "
        state += " I feel " + self.mood + ". "
        state += self.__str__()
        return state
y=X("Sivanand","Good")
print(y)