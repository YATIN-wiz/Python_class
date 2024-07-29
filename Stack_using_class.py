class Stack:
    satck = []
    def __init__ (self, size, stack = []):
        self.stack = stack
        self.size = int(size)
       

    def push(self):
        if len(self.stack) > self.size:
            print("Stck Overflow")
        else:
            element = int(input("Enter the element the to be pushed"))
            self.stack.append(element)
            
    def pop(self):
        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            print("Poped:",self.stack.pop())
            print("Stack:", self.stack)

    def peek(self):

        return self.stack[-1]

stack = Stack(input("Enter size the of the stack"))
while(True):
    print("----------------------")
    print("1. PUSH")
    print("2. POP")
    print("3. PEEK")
    print("----------------------")
    
    choice = int(input("Enter the choice"))

    if choice == 1:
        stack.push()
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        print(stack.peek())
    else:
        print("Invalid choice")
        break

    
    
