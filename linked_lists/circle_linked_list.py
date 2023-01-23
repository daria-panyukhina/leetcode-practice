class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printLL(node):
    while node:
        print(node.val, end=' ')
        node = node.next
    print('')


def hasCycle(head):
    visited = set()
    if not head:
        return False
    while head.next:
        if head in visited:
            return True
        visited.add(head)
        head = head.next
    return False

def hasCycle2(head):
    if not head or not head.next:
        return False
    ptr1 = head
    ptr2 = head.next
    while ptr1.next and ptr2.next and ptr2.next.next:
        if ptr1 == ptr2:
            return True
        ptr1 = ptr1.next
        ptr2 = ptr2.next.next
    return False


test = ListNode(val=1,
                    next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=None)))))

test2 = ListNode(val=1,
                    next=ListNode(val=2, next=None))

test.next.next = test
print(hasCycle(test2))
print(hasCycle2(test2))