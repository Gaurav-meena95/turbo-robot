class Node:
    def __init__(self, data):
        self.data = data  # Assign data to the node
        self.next = None  # Initialize the next node as None

class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node  # If list is empty, set head to new node
            return
        last = self.head
        while last.next:  # Traverse to the last node
            last = last.next
        last.next = new_node  # Link the new node at the end

    def display(self):
        current = self.head
        while current:  # Traverse the list and print the data
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Indicate end of the list

    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next  # If head needs to be removed
            current = None
            return
        prev = None
        while current and current.data != key:  # Find the key
            prev = current
            current = current.next
        if current is None:  # Key not found
            return
        prev.next = current.next  # Unlink the node to be deleted
        current = None

# Example usage
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.display()  # Output: 1 -> 2 -> 3 -> None

    linked_list.delete(2)
    linked_list.display()  # Output: 1 -> 3 -> None
