class dll:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    # Initializing by setting the head, tail, hash table, capacity and length.
    def __init__(self, capacity: int):
        self.head = dll(-1, -1)
        self.tail = self.head
        self.hash = {}
        self.capacity = capacity
        self.length = 0

    # Function to get an element.
    def get(self, key: int) -> int:

        # Check if the key is not in the hash table.
        if key not in self.hash:
            return -1

        # If it is not there we create an entry in the dictionary.
        else:
            node = self.hash[key]
            val = node.val

            # Moving the node to the end of the linked list.
            while node.next:

                # Connecting the nodes before and after the current node.
                node.prev.next = node.next
                node.next.prev = node.prev

                # Setting the current tail's next to the node and the node's previous to the current tail.
                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = node

            return val

    # Function to put an element.
    def put(self, key: int, value: int) -> None:

        # Check if the element is in the hash table.
        if key in self.hash:

            node = self.hash[key]
            node.val = value

            # Moving the node to the end of the linked list.
            while node.next:

                # Connecting the nodes before and after the current node.
                node.prev.next = node.next
                node.next.prev = node.prev

                # Setting the current tail's next to the node and the node's previous to the current tail.
                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = node

        # If the element is not in the hash table.
        else:

            # Set up the node.
            node = dll(key, value)
            self.hash[key] = node

            # Changing the references at the tail to account for the new node.
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

            # Increasing the length by one.
            self.length += 1

            # Check if we have reached above capacity.
            if self.length > self.capacity:

                # Finding the node to remove, changing the references and deleting it.
                remove = self.head.next
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                del self.hash[remove.key]
                self.length -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
