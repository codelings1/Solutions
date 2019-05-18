class Node:
    def __init__(self, inp_data):
        self.data = inp_data
        self.next = None
        

class Stack:
    def __init__(self):
        self.head = None     
        
    def push(self,ele):
        createNode = Node(ele)
        createNode.next = self.head
        self.head = createNode
        print("Value ",ele," inserted")


    def pop(self):
        if(self.head is None):
            print("List is already empty")
        else:
            temp = self.head
            self.head = temp.next
            print("Value ", temp.data , " popped")
            del(temp)
            
            
if __name__ == '__main__':
    stack = Stack()
    stack.push(1);
    stack.push(2);
    stack.push(3);
    stack.push(4);
    stack.pop();
    stack.pop();
    stack.pop();
    stack.pop();
    stack.pop();

	

