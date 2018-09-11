def get_intersect_node(list1, list2):
    set1 = set(list1)
    for i in list2:
        if set1.__contains__(i):
            return i
    return None

list1 = [3,7,8,10]
list2 = [99,1,8,10]
print(get_intersect_node(list1,list2))

list1 = [3,6,9,15,30]
list2 = [10,15,30]
print(get_intersect_node(list1,list2))

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def size(head, len = 0):
    if head is None:
        return len
    return size(head.next, len+1)

def traverse_upto_diff(head, diff):
    count = 0
    while head is not None:
        if count == diff:
            break
        head = head.next
        count+=1
    return head

def intersection(p_head, q_head):
    while p_head != q_head:
        p_head = p_head.next
        q_head = q_head.next
    return q_head

def travese(p_head, q_head):
    p_len = size(p_head)
    q_len = size(q_head)
    pq_abs = abs(p_len - q_len)
    if p_len > q_len:
        p_head = traverse_upto_diff(p_head, pq_abs)
    else:
        q_head = traverse_upto_diff(q_head, pq_abs)
    return intersection(p_head, q_head)



p_list = Node('a')
p_list.next = Node('b')
p_list.next.next = Node('c')
p_list.next.next.next = Node('d')
p_list.next.next.next.next = Node('e')
p_list.next.next.next.next.next = Node('f')
p_list.next.next.next.next.next.next = Node('g')

i_node = p_list.next.next.next.next

q_list = Node('m')
q_list.next = Node('n')
q_list.next.next = i_node

i_node = travese(p_list, q_list)
print(i_node.value)