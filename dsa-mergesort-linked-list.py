from Linked_List import LinkedList

def merge_sort(linked_list):

    """Sorts a linked list in ascending order
    -Recursively divide the linked list into sublists containing a single node
    -Repeatedly merge the sublists to produced sorted sublists until one remains

    Returns a sorted linked list
    """

    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list

    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)  #Left == 20 
    right = merge_sort(right_half) #Right == 11, 12, 20

    return merge(left, right)

def split(linked_list):
    """
    Divide the unsorted list at midpoint into sublists
    """

    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    
    else:
        size = linked_list.size()
        mid = size // 2
        
        mid_node = linked_list.node_at_index(mid-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next
        mid_node.next = None

        return left_half, right_half

def merge(left, right):
    """
    Merges two linked list sorting by data in the nodes
    Returns a new, merged list
    """

    # Create a new linked list that contains nodes from
    # merging left and right.
    merged = LinkedList()

    # Add a fake head that is discarded later
    merged.push(0)
    
    # Set current to the head of the linked list
    current = merged.head

    # Obtain head nodes from left and right linked lists
    left_head = left.head
    right_head = right.head

    # Iterate over left and right until we reach the tail of either
    while left_head or right_head:
        # If the head node of the left is None, we're past the tail
        # add the node from the right to merged linked list
        if left_head is None:
            current.next = right_head
            # Call next on right to set loop condition to False
            right_head = right_head.next 
        # If the head node of the right is None, we're past the tail
        #Add the tail node from left to merged linked list
        elif right_head is None:
            current.next = left_head
            # Call next on left to set loop condition to False
            left_head = left_head.next
        else:
            # Not at either tail node
            #Obtain node data to perform comparison operations
            left_data = left_head.data
            right_data = right_head.data 
            # If data on left is less than right, set current to left node
            if left_data < right_data:
                current.next = left_head
                #Move left head to next node
                left_head = left_head.next 
            # If data on the left is greater than right, set current to right node
            else:
                current.next = right_head
                # Move right head to next node
                right_head = right_head.next
        # Move current to next node
        current = current.next
    
    #Discard fake head and set first merged node as head
    head = merged.head.next
    merged.head = head

    return merged
    
l = LinkedList()
l.push(11)
l.push(12)
l.push(20)




print(l)
print(merge_sort(l))