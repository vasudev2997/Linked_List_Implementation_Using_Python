class Node():
#Node creation function
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next

class Clinkedlist():
#Head declaration
    def __init__(self):
        self.head=None
        self.last=None

#Insertbeg function is used to insert node at the beginning of the list
    def insertbeg(self, newdata):
        node=Node(newdata)
        if(self.head==None):
            self.head=node
            self.last=self.head
        else:
            node.next=self.head
            self.head=node
            self.last.next=self.head

#Insertmid function is used to insert node at any specified location in the list
    def insertmid(self, newdata, position):
        node=Node(newdata)
        current=self.head
        if(self.head is not None and 1<position<=self.length()):
                i=0
                while(i<position-2):
                    current=current.next
                    i+=1
                node.next=current.next
                current.next=node
        elif(position==1):
            self.insertbeg(newdata)
        elif(position==self.length()+1):
            self.insertend(newdata)
        else:
            print("Invalid Entry or List is not Created")

#Insertend function is used to insert node at the end of the list
    def insertend(self, newdata):
        if(self.last==None):
            self.head=Node(newdata)
            self.last=self.head
        else:
            node=Node(newdata)
            self.last.next=node
            node.next=self.head
            self.last=node

#Length function returns the length of the list          
    def length(self):
        l=0
        if(self.last==self.head and self.head is not None):
            return 1
        elif(self.head!=self.last):
            current=self.head
            while(True):
                l+=1
                current=current.next
                if(current==self.head):
                    break
            return l
        else:
            return 0

#Delete functionis used to delete the user defined node from the list
    def delete(self, position):
        if(self.head!=self.last):
            i=0
            current=self.head
            #When the list has more than 1 node and the user wants to delete the first node
            if(position==1):
                self.head=self.head.next
                self.last.next=self.head
            #When the list has more than 1 node and the user wants to delete the last node
            elif(position==self.length()):
                while(i<position-2):
                    current=current.next
                    i+=1
                current.next=self.head
                self.last=current
            #When the list has more than 1 node and the user wants to delete any node between the first and the last node
            else:
                if(1<position<self.length()):
                    while(i<position-2):
                        current=current.next
                        i+=1
                    current.next=current.next.next
        #When there is only one node and the user wants to delete the node
        elif(self.head==self.last and position==1 and self.head is not None):
            self.head=self.last=None
        else:
            print("Invalid Entry or List not Created")
            
    def print(self):
        current=self.head
        if(self.length()==1):
            print(current.data)
        elif(self.length()>1):
            while(True):
                print(current.data,end=" ")
                current=current.next
                if(current==self.head):
                    break
            print()
        else:
            print("List not created or empty.")

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
        newdata=input("Enter the data for the new node - ")
        position=int(input("Enter the position for the new node - "))
        l1.insertmid(newdata, position)
        
    elif(n==4):
        print(l1.length())
        
    elif(n==5):
        l1.print()
        
    else:
        print("Invalid Entry")

l1=Clinkedlist()
print("Circular Singly Linked List.")
Operations()
while(True):
    c=input("Continue Y/N - ")
    if(c=="Y" or c=="y"):
        Operations()
    elif(c=="N" or c=="n"):
        break
    else:
        print("Invalid Entry")
