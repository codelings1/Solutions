class Node:
    def __init__(self,ele):
        self.data = ele
        self.next = None
    
class CircularList:
    def __init__(self):
        self.tail = None
        
    def insert(self,ele):
        createNode = Node(ele)
        if(self.tail is None):
            createNode.next = createNode
            self.tail = createNode
        else:
            createNode.next = self.tail.next
            self.tail.next = createNode
            self.tail = createNode
            
        print("Inserted Node ", ele)
    
    def delete(self):
        if(self.tail is None):
            print("List is already empty")
        elif(self.tail.next == self.tail):
            print("Deleted node ", self.tail.data)
            del(self.tail)
            self.tail = None
        else:
            print("Deleted node ", self.tail.next.data)
            temp = self.tail.next
            self.tail.next = self.tail.next.next    
            del(temp)
            
            
if __name__ == '__main__':
    cList = CircularList()
    cList.insert(1)
    cList.insert(2)
    cList.insert(3)
    cList.insert(4)
    cList.delete()
    cList.delete()
    cList.delete()
    cList.delete()
    cList.delete()
    cList.delete()