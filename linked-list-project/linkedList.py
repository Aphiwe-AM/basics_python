class LinkedList:
    class Node:
        def __init__(self, element):
            self.element = element
            self.next = None

    def __init__(self):
        self.head = None
        self.length = 0

    #method to check if list is empty 
    def is_empty(self) -> bool:
        return self.length == 0 

    #method to add a node to the list
    def add(self, element) -> None:
        node = self.Node(element)

        #check if length is = to 0 and if so make head = current node
        if self.is_empty():
            self.head = node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        self.length += 1

    def remove(self, element):
        previous_node = None
        current_node = self.head
        while current_node is not None and current_node.element != element:
            previous_node = current_node
            current_node = current_node.next
        if current_node is None:
            return        
        elif previous_node is not None:
            previous_node.next = current_node.next
        else:
            self.head = current_node.next
        self.length -= 1

        


my_list = LinkedList()
my_list.add(1)
my_list.add(3)
my_list.remove(1)
print(my_list.length)
print(my_list.is_empty())
