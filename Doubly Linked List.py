class Node():
#Creation of node
    def __init__(self, data=None, prev=None, next=None):
        self.data=data
        self.prev=prev
        self.next=next

class Linkedlist():
#Head Declaration
    def __init__(self):
        self.head=None
        self.last=None

#Insertbeg function for the insertion of node at the beginning of the list
    def insertbeg(self, newdata):
        node=Node(newdata)
        if(self.head==None):
            self.head=node
            self.last=self.head
        else:
            node.next=self.head
            self.head.prev=node
            self.head=node

#Insertmid function for the insertion of node at a specified location in the list
    def insertmid(self, newdata, position):
        node=Node(newdata)
        i=0
        if(1 < position <= self.Length()):
            current=self.head
            while i<position-2:
                current=current.next
                i+=1
            node.next=current.next
            current.next.prev=node
            node.prev=current
            current.next=node
        elif(position==1):
            self.insertbeg(newdata)
        elif(position==self.Length()+1):
            self.insertend(newdata)
        else:
            print("Invalid Entry or List not Created")

#Insertend function for the insertion of node at the end of the list
    def insertend(self, newdata):
        node=Node(newdata)
        if(self.last is None):
            self.head=node
            self.last=self.head
        else:
            node.prev=self.last
            self.last.next=node
            self.last=node

#Delete function for the deletion of the specified node
    def delete(self, position):
        current=self.head
        i=0
        if(1 < position < self.Length()):
            while current and i<position-1:
                current=current.next
                i+=1
            current.next.prev=current.prev
            current.prev.next=current.next
        elif(position==1 and self.Length()>1):
            self.head=self.head.next
            self.head.next.prev=None
        elif(position==1 and self.Length()==1):
            self.head=None
        elif(position==self.Length()):
            self.last.prev.next=None
            self.last=self.last.prev
        else:
            print("Invalid Entry or List not Created")

#Length function which returns ths length of the list
    def Length(self):
        if(self.head):
            l=0
            current=self.head
            while current:
                current=current.next
                l+=1
            return l
        else:
            return 0

#Print function for printing the node's data from the beginning of the list
    def printfrombeg(self):
        if(self.head):
            current=self.head
            while current:
                print(current.data,end=" ")
                current=current.next
            print()
        else:
            print("List is not created or empty.")

#Print function for printing the node's data from the end of the list
    def printfromend(self):
        if(self.head):    
            current=self.last
            while current:
                print(current.data,end=" ")
                current=current.prev
            print()
        else:
            print("List is not created or empty.")

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
        print(l1.Length())
        
    elif(n==5):
        l1.printfrombeg()

    elif(n==6):
        l1.printfromend()
        
    else:
        print("Invalid Entry")

l1=Linkedlist()
Operations()
while(True):
    c=input("Continue Y/N - ")
    if(c=="Y" or c=="y"):
        Operations()
    elif(c=="N" or c=="n"):
        break
    else:
        print("Invalid Entry")
