class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        if not temp:
            print('List is empty.')
            return
        else:
            print('Start:', end=' ')
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print('end.')

    def insert(self, data):
        new_node = Node(data)

        # If the linked list is empty
        if self.head is None:
            self.head = new_node

        # If the data is smaller than the head
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node

        else:
            # Locate the node before the insertion point
            current = self.head
            while current.next and new_node.data > current.next.data:
                current = current.next

            # Insertion
            new_node.next = current.next
            current.next = new_node

    def removeDuplicates(self):
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next



if __name__=='__main__':
    # Create an object
    LL = LinkedList()
    # Print Empty List
    LL.printList()
    # Insert some nodes
    LL.insert(10)
    LL.insert(12)
    LL.insert(8)
    LL.insert(12)
    LL.insert(11)
    LL.insert(10)
    # Print the list
    LL.printList()
    print("Remove duplicate")
    LL.removeDuplicates()
    LL.printList()