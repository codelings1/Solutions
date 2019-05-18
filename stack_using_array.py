# push pop

class Stack:
    def __init__(self,maxSize):
        self.maxs = maxSize     
        self.top = -1
        self.arr = [None]*maxSize
    def push(self,ele):
        if(self.top < self.maxs - 1):
            self.top += 1
            self.arr[self.top] = ele
            print("Value ",ele," inserted")
        else:
            print("Cannot insert more values as Stack is already full")


    def pop(self):
        if(self.top == -1):
            print("List is already empty")
        else:
            print("Value ", self.arr[self.top] , " popped")
            del(self.arr[self.top])
            self.top -= 1
            
if __name__ == '__main__':
    stack = Stack(2)			# Max size can be taken as anything as passed
    stack.push(1);
    stack.push(2);
    stack.push(3);
    stack.push(4);
    stack.pop();
    stack.pop();
    stack.pop();
    stack.pop();
    stack.pop();
    