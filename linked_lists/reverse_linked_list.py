class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printLL(node):
    while node:
        print(node.val, end=' ')
        node = node.next
    print('')


def reverseList(head):
    if not head:
        return
    if not head.next:
        return head
    prev = head
    head = head.next
    prev.next = None
    while head.next:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    head.next = prev
    return head


def reverseList2(head):
    global new_head
    if not head:
        return
    if not head.next:
        new_head = head
        return new_head
    reverseList2(head.next)
    head.next.next = head
    head.next = None
    return new_head


new_head = ListNode()
testlist = ListNode(val=1,
                    next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=None)))))
testlist2 = ListNode(val=1,
                     next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=None)))))

testlist3 = ListNode(val=0,
                     next=None)

# printLL(testlist)
# printLL(reverseList(testlist))
# printLL(reverseList2(testlist2))
# printLL(reverseList2(testlist3))
