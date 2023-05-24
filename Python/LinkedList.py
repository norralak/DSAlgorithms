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
    
    def __repr__(self) -> str:
        nodes = []
        currentNode = self.head

        while currentNode:
            if currentNode is self.head:
                nodes.append("[Head: %s]" % currentNode.data)
            elif currentNode.nextNode is None:
                nodes.append("[Tail: %s]" % currentNode.data)
            else:
                nodes.append("[%s]" % currentNode.data)
            currentNode = currentNode.nextNode
        return '-> '.join(nodes)
    
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
    
    """
    Adds new node to head O(1)
    """
    def prepend(self, data):
        newHead = node(data)
        newHead.nextNode = self.head
        self.head = newHead
    """
    Searching is O(n)
    """
    def search(self, key):
        currentNode = self.head

        while currentNode:
            if currentNode.data == key:
                return currentNode
            else:
                currentNode = currentNode.nextNode
        return None
    """
    Insertion is O(1) but searching is O(n)
    """
    def insert(self, data, index):
        
        if index == 0:
            self.prepend(data)
        
        if index > 0:
            newNode = node(data)

            position = index
            currentNode = self.head

            while position > 1:
                currentNode = currentNode.nextNode
                position -= 1
            
            prev = currentNode
            next = currentNode.nextNode

            prev.nextNode = newNode
            newNode.nextNode = next

    def delete(self, key):
        found = False
        prev = None
        currentNode = self.head

        while currentNode and not found:
            if currentNode.data == key and currentNode is self.head:
                found = True
                self.head = currentNode.nextNode
            elif currentNode.data == key:
                found = True
                prev.nextNode = currentNode.nextNode
            else:
                prev = currentNode
                currentNode = currentNode.nextNode
        
        return currentNode

myName = linkedList()
for char in "KALARRON":
    myName.prepend(char)

print(myName.size())
print(myName.isEmpty())
print(myName)
myName.insert("THIS IS MY NAME", 8)

nodey = myName.search("A")
print(nodey)
print(myName)
myName.delete("THIS IS MY NAME")
print(myName)