# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Node:
    def __init__(self,data):
        self.data=data
        self.previous_node=None

    def get(self,x):
        if self.data==x:
            return self.previous_node











class linked_L:
    def __init__(self):
        self.current_node=None



    def insert(self,data):
        self.new_node = Node(data)
        if not self.current_node:
            self.current_node = self.new_node
        else:
            self.new_node.previous_node = self.current_node
            self.current_node = self.new_node

    def get_node(self,x):
        return self.new_node.get(x)








l=linked_L()
l.insert(4)
l.insert(3)
l.insert(5)
l.get_node(5)





