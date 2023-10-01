class Node:
    """An object for string a single node for a lined list.
        Models two attributes - data and the link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" %self.data
class LinkedList:
    """
    Singly linked list
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        """
        Returns the number of nodes in the list
        Take 0(n) time - linear time
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count
    
    # Ends at 2:36:29

    def add(self, data):
        """
        Adds new Node containing data at head of the list
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node contai0ning data that matches the key
        Returns the node or None if not found

        Takes O(n) or linear time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
            return None
        
    def insert(self, data, index):
        """
        Inserts a new node containing data at index position
        Insertion takes O(1) - constant time but finding the node 
        at the insertion point takes O(n) - linear time.

        Takes overall O(n) - linear time
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = current.next_node # Error in this line 
                position -= 1
            
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Removes Node containing data that matches the key
        Returns the node of None if key doesn't exist
        Takes O(n)
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

    def __repr__(self):
        """
        Return a string representation of the list
        Takes O(n) time - linear time
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return '-> '.join(nodes)
    
    # Search - Ended at 2:48:35



