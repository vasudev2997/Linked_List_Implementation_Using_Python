class Node():
    def __init__(self, data=None, next=None, prev=None):
        self.data=data
        self.next=next
        self.prev=prev

class Clinkedlist():
    def __init__(self):
        self.head=None
        self.last=None
        
    def insertbeg(self, newdata):
        node=Node(newdata)
        if(self.head==None):
            self.head=node
            self.last=self.head
        else:
            node.next=self.head
            self.head.prev=node
            self.head=node
            self.last.next=self.head
            self.head.prev=self.last

    def insertmid(self, newdata, position):
        node=Node(newdata)
        if(self.head is not None and 1<position<=self.length()):
                i=0
                current=self.head
                while(i<position-2):
                    current=current.next
                    i+=1
                node.next=current.next
                current.next.prev=node
                node.prev=current
                current.next=node
        elif(position==1):
            self.insertbeg(newdata)
        elif(position==self.length()+1):
            self.insertend(newdata)
        else:
            print("Invalid Entry or list not created")
    
    def insertend(self, newdata):
        node=Node(newdata)
        if(self.last==None):
            self.head=node
            self.last=self.head
        else:
            self.last.next=node
            node.next=self.head
            node.prev=self.last
            self.last=node
            self.head.prev=self.last
    
    def length(self):
        if(self.head is not None and self.last==self.head):
            return 1
        elif(self.head!=self.last):
            l=0
            current=self.head
            while(True):
                l+=1
                current=current.next
                if(current==self.head):
                    break
            return l
        else:
            return 0
        
    def delete(self, position):
        if(self.last!=self.head):
            if(1<position<self.length()):
                i=0
                current=self.head
                while (i<position-1):
                    current=current.next
                    i+=1
                current.next.prev=current.prev
                current.prev.next=current.next
            elif(position==1):
                self.head=self.head.next
                self.last.next=self.head
                self.head.prev=self.last
            elif(position==self.length()):
                self.last=self.last.prev
                self.last.next=self.head
                self.head.prev=self.last
        elif(self.head==self.last and position==1 and self.head is not None):
            self.head=self.last=None
        else:
            print("Invalid Entry or list not created")
                
    def printfrombeg(self):
        if(self.length()==1):
            print(self.head.data)
        elif(self.head!=self.last):
            current=self.head
            while(True):
                print(current.data,end=" ")
                current=current.next
                if(current==self.head):
                    break
            print()
        else:
            print("List is not created or empty")

    def printfromend(self):
        if(self.length()==1):
            print(self.head.data)
        elif(self.head!=self.last):
            current=self.last
            while current:
                print(current.data,end=" ")
                current=current.prev
                if(current==self.last):
                    break
            print()
        else:
            print("List is not created or empty")
        
def Operations():
    n=int(input("1. Insert  2. Delete   3. Update   4. Length   5. Print Form Beginnig  6. Print From End\n"))
    
    if(n==1):
        m=int(input("1. Beginning   2.End\n"))
        if(m==1):
            numberofnodes=int(input("Enter the number of nodes - "))
            for i in range(numberofnodes):
                l1.insertbeg(input())
        elif(m==2):
            numberofnodes=int(input("Enter the number of nodes - "))
            for i in range(numberofnodes):
                l1.insertend(input())
        else:
            print("Invalid Entry")
            
    elif(n==2):
        position=int(input("Enter the position of node - "))
        l1.delete(position)
        
    elif(n==3):
        data=input("Enter the data for the new node - ")
        position=int(input("Enter the position for the new node - "))
        l1.insertmid(data, position)
        
    elif(n==4):
        print(l1.length())
        
    elif(n==5):
        l1.printfrombeg()

    elif(n==6):
        l1.printfromend()
        
    else:
        print("Invalid Entry")

print("Doubly Circular Linked List.")
l1=Clinkedlist()
Operations()
while(True):
    c=input("Continue Y/N - ")
    if(c=="Y" or c=="y"):
        Operations()
    elif(c=="N" or c=="n"):
        break
    else:
        print("Invalid Entry")
