class Node():
#Creation of node
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next
        
class Linkedlist():
#Head declaration
    def __init__(self):
        self.head=None
        self.last=None
        
#Insert at the end of the list
    def insertend(self, newdata):
        if(self.last==None):
            self.head=Node(newdata)
            self.last=self.head
        else:
            self.last.next=Node(newdata)
            self.last=self.last.next
            
#Insert in the beginning of the list          
    def insertbeg(self, newdata):
        if(self.head is None):
            self.head=Node(newdata)
        else:
            node=Node(newdata)
            node.next=self.head
            self.head=node
            
#Insert in the middle of two nodes
    def insertmid(self, newdata, position):
        node=Node(newdata)
        i=0
        current=self.head
        if(position>1 and position<=self.length()+1):
            while(current and i<position-2):
                current=current.next
                i+=1
            node.next=current.next
            current.next=node
        elif(position==1):
            self.insertbeg(newdata)
        else:
            print("Invalid Entry or List Not Created")

#Delete node from the list
    def delete(self,position):
        current=self.head
        if(position<=self.length() and position>1):
            i=0
            while(current and i<position-2):
                current=current.next
                i+=1
            current.next=current.next.next
        elif(position==1):
            self.head=self.head.next
        else:
            print("Invalid Entry or List not Created.")

#Length of List Function
    def length(self):
        if(self.head is not None):
            current=self.head
            l=0
            while(current):
                current=current.next
                l+=1
            return l
        else:
            return 0
        
#Print Function
    def print(self):
        if(self.head is not None):
            current=self.head
            while current:
                print(current.data,end=" ")
                current=current.next
            print()
        else:
            print("List is not created or empty.")

def Operations():
    n=int(input("1. Insert  2. Delete   3. Update   4. Length   5. Print\n"))
    
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
        l1.insertmid(data,position)
        
    elif(n==4):
        print(l1.length())
        
    elif(n==5):
        l1.print()
        
    else:
        print("Invalid Entry")

l1=Linkedlist()
print("Singly Linked List")
Operations()
while(True):
    c=input("Continue Y/N - ")
    if(c=="Y" or c=="y"):
        Operations()
    elif(c=="N" or c=="n"):
        break
    else:
        print("Invalid Entry")
