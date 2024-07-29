class Queue:
    
    def __init__ (self, size, queue = []):
        self.queue = queue
        self.size = int(size)
       

    def enqueue(self):
        if len(self.queue) > self.size:
            print(" Queue Overflow")
        else:
            element = int(input("Enter the element the to be enqueued:"))
            self.queue.append(element)
            
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue Underflow")
        else:
            print("Poped:",self.queue.pop())
            print("queue:", self.queue)

    def display(self):

        return self.queue

queue = Queue(input("Enter size the of the queue:"))
while(True):
    print("----------------------")
    print("1. ENQUEUE")
    print("2. DEQUEUE")
    print("3. DISPLAY")
    print("----------------------")
    
    choice = int(input("Enter the choice:"))

    if choice == 1:
        queue.enqueue()
    elif choice == 2:
        queue.dequeue()
    elif choice == 3:
        print(queue.display())
    else:
        print("Invalid choice")
        break

    
    
