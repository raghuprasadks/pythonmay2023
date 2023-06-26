class Node():
    def __init__(self,value):
        self.next = None
        self.value = value

class LinkedList(object):
    def __init__(self,head=None):
        self.head = head

    def append(self,new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head=new_node

    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def insert (self,new_element,position):
        count=1
        current=self.head
        if position == 1:
            new_element=self.head
            self.head=new_element
        while current:
            if count+1 == position:
                new_element.next = current.next
                current.next = new_element
                return
            else:
                count+=1
                current=current.next
        pass

    def delete(self,value):
        current=self.head
        if current.value ==value:
            self.head=current.next
        else:
            while current:
                if current.value ==value:
                    break
                prev=current
                current = current.next
            if current == None:
                return
            prev.next = current.next
            current = None



e1= Node(10)
e2= Node(12)
e3= Node(8)
e4= Node(3)


l1=LinkedList()
l1.append(e1)
l1.append(e2)
l1.append(e3)
l1.append(e4)
l1.print()

e5= Node(0)
l1.insert(e5,3)
l1.delete(12)
l1.print()
