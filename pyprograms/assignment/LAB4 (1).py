# LAB4
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

class Node: # You are not allowed to modify this class
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return f"Node({self.value})"

    __repr__ = __str__
                        
                          
class SortedLinkedList:
    '''
        >>> x=SortedLinkedList()
        >>> x.add(8.76)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(5)
        >>> x.add(3)
        >>> x.add(-7.5)
        >>> x.add(4)
        >>> x.add(9.78)
        >>> x.add(4)
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 1 -> 1 -> 3 -> 4 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.removeDuplicates()
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 3 -> 4 -> 5 -> 8.76 -> 9.78
        >>> sub1, sub2 = x.split()
        >>> sub1
        Head:Node(-7.5)
        Tail:Node(4)
        List:-7.5 -> 1 -> 3 -> 4
        >>> sub2
        Head:Node(5)
        Tail:Node(9.78)
        List:5 -> 8.76 -> 9.78
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 -> 1 -> 3 -> 4 -> 5 -> 8.76 -> 9.78
        >>> x.add(1)
        >>> x.intersection(sub1)
        Head:Node(-7.5)
        Tail:Node(4)
        List:-7.5 -> 1 -> 3 -> 4
    '''

    def __init__(self):   # You are not allowed to modify the constructor
        self.head=None
        self.tail=None

    def __str__(self):   # You are not allowed to modify this method
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' -> '.join(out) 
        return f'Head:{self.head}\nTail:{self.tail}\nList:{out}'

    __repr__=__str__


    def isEmpty(self):
        return self.head == None

    def __len__(self):
        count=0
        current=self.head
        while current:
            current=current.next
            count+=1
        return count

                
    def add(self, value):
        # --- YOUR CODE STARTS HERE
        #pass
        new_node = Node(value)

        # If the linked list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node

        # If the data is smaller than the head
        elif self.head.value >= new_node.value:
            new_node.next = self.head
            self.tail = self.head
            self.head = new_node

        else:
            # Locate the node before the insertion point
            current = self.head
            #self.tail=current
            #counter =0
            while current.next and new_node.value > current.next.value:
                current = current.next

            # Insertion
            new_node.next = current.next
            current.next = new_node
            curr=self.head
            while curr.next!=None:
                curr = curr.next
            self.tail = curr

    def split(self):
        # --- YOUR CODE STARTS HERE
        #pass
        current = self.head
        if current is None:
            return
        breakpoint=0
        length=self.__len__()
        if(self.__len__()%2==0):
            breakpoint=length//2
        else:
            breakpoint = (length // 2)+1
        sortedlist1=SortedLinkedList()
        sortedlist2 = SortedLinkedList()
        #current = self.head
        counter = 1
        while current.next:
            if(counter<=breakpoint):
                value = current.value
                sortedlist1.add(value)
            else:
                value =current.value
                sortedlist2.add(value)
            current=current.next
            counter = counter+1
            if(counter==length):
                sortedlist2.add(current.value)

        return sortedlist1,sortedlist2



    def removeDuplicates(self):
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.value == temp.next.value:
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next

    def intersection(self, other):
        # --- YOUR CODE STARTS HERE
        #pass
        intersectionlist=SortedLinkedList()
        lenlist1 = self.__len__()
        lenlist2 = other.__len__()
        current1 = self.head
        other1 = other.head
        if (lenlist1>=lenlist2):
            while(other1.next):
                valueother = other1.value
                while (current1.next):
                    valuecurrent = current1.value
                    if (valuecurrent ==valueother):
                        intersectionlist.add(valuecurrent)
                        break
                    current1 = current1.next
                other1=other1.next
        return intersectionlist





def run_tests():
    import doctest
    doctest.testmod(verbose=True)
    
if __name__ == "__main__":
    run_tests()