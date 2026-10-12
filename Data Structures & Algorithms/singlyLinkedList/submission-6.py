class Node:

    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        current = self.head.next
        i = 0
        while current:
            if i == index:
                return current.val
            i += 1
            current = current.next
        return -1  # Index out of bounds or list is empty
        

    def insertHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node
        

    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        i = 0
        head = self.head
        while i < index and head:
            i += 1
            head = head.next
        
        if head and head.next:
            if head.next == self.tail:
                self.tail = head
            head.next = head.next.next
            return True
        return False
        

    def getValues(self) -> List[int]:
        array = []
        head = self.head.next
        while head:
            array.append(head.val)
            head = head.next
        return array
        
