class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The previous node has to actually exist.")
            return
        
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
            
        last = self.head
        while (last.next):
            last = last.next
        last.next = new_node

    def deleteNode(self, key):
        temp = self.head 

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp == None:
            return

        prev.next = temp.next
        temp = None

    
    def size(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count



    def search(self, key):
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next
        return None

    def insert(self, new_data, index):
        if index == 0:
            self.push(new_data)
        
        if index > 0:
            new_node = Node(new_data)
            position = index 
            current = self.head

            while position > 1:
                current = current.next
                position -= 1
            
            prev = current
            next = current.next

            prev.next = new_node
            new_node.next = next

    def delete(self, key):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next
            elif current.data == key:
                found = True
                previous.next = current.next
            else:
                previous = current
                current = current.next
        return current

    def deleteIndex(self, index):
        if self.head is None:
            return

        position = index
        current = self.head

        if position == 0:
            self.head = current.next
        
        while position > 1:          
            current = current.next
            position -= 1 
        
        if current.next is not None:
            previous = current
            current = current.next
            next_node = current.next
            previous.next = next_node
            current = None
            return current
        else:
            return


    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0
            while position < index:
                current = current.next
                position += 1
                return current


    def __repr__(self):
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: {}]".format(current.data))
            elif current.next is None:
                nodes.append("[Tail: {}]".format(current.data))
            else:
                nodes.append("[{}]".format(current.data))

            current = current.next
        return '-> '.join(nodes)


    def printlist(self):
        temp = self.head
        print("Linked list:", end = " ")
        while temp:
            print(temp.data, end= " ")
            temp = temp.next

l1 = LinkedList()
l1.push(1)
l1.push(2)
l1.push(3)
l1.push(4)
l1.append(6)











