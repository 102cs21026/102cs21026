class Node:
    def __init__(self,value=None):
          self.value=value
          self.next=None
class SinglyLinkedList:
    def __init__(self):
          self.head=None
    def atFront(self,value):
        new_Node=Node(value)
        new_Node.next=self.head
        self.head=new_Node
    def __iter__(shift):
        Node=self.head
        while Node:
             yield Node
        Node=Node.next
   
    def search (self_key):
        for Node in sll:
            if Node.value==key:
                print("key found")
                return
                print("key not found")

sll=SinglyLinkedList()
sll.atFront(1)
sll.atFront(2)
sll.atFront(3)
   
