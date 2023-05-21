"""
Nodes to put into linked list
Has data and a reference to the next node
"""
class node:
    data = None
    nextNode = None

    def __init__(self, data) -> None:
        self.data = data

    def __repr__(self) -> str:
        return self.data
    
"""
Single linked list
"""
class linkedList:
    
    def __init__(self) -> None:
        self.head = None
    
    def isEmpty(self) -> bool:
        return self.head == None
    
    """
    Returns the number of node. Takes O(n) time since it goes thru the entirety of the list
    """
    def size(self) -> int:
        currentNode = self.head
        count = 0
        while currentNode:
            count += 1
            currentNode = currentNode.nextNode
        
        return count
    
    def prepend(self, newHead):
        newHead.nextNode = self.head
        self.head = newHead
        

n1 = node("N")
n2 = node("O")
n3 = node("R")
n4 = node("R")
n5 = node("A")
n6 = node("L")
n7 = node("A")
n8 = node("K")
n1.nextNode = n2
n2.nextNode = n3
n3.nextNode = n4
n4.nextNode = n5
n5.nextNode = n6
n6.nextNode = n7
n7.nextNode = n8

n0 = "SUKARAM"
myName = linkedList()
myName.head = n1
print(myName.size())
print(myName.isEmpty())

myName.prepend(n0)