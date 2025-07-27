class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.numofNodes=0

    def insert_start(self,data):
        self.numofNodes+=1
        new_node=Node(data)
        if not self.head:
            self.head = new_node
            print(data)
        else:
            print(data)
            new_node.nextNode = self.head
            self.head = new_node



    def insert_end(self,data):
        self.numofNodes += 1
        new_node=Node(data)
        actual_node=self.head

        while actual_node.nextNode is not None:
            actual_node=actual_node.nextNode

        actual_node.nextNode=new_node

    def traverse(self):
        while self.head.nextNode:
            print(self.head)
            self.head=self.head.nextNode


l=LinkedList()
l.insert_start(1)
l.insert_start(2)
l.insert_start(3)




