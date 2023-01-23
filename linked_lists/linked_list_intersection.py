class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next


def printLL(node):
    while node:
        print(node.val, end=' ')
        node = node.next
    print('')


def getIntersectionNode(headA, headB):
    myset = set()
    while headA and headB:
        if headA in myset:
            return headA
        else:
            myset.add(headA)
            headA = headA.next
        if headB in myset:
            return headB
        else:
            myset.add(headB)
            headB = headB.next
    while headA:
        if headA in myset:
            return headA
        else:
            myset.add(headA)
            headA = headA.next
    while headB:
        if headB in myset:
            return headB
        else:
            myset.add(headB)
            headB = headB.next



headA = ListNode(x=4,
                 next=ListNode(x=1,
                               next=ListNode(x=8,
                                             next=ListNode(x=4,
                                                           next=ListNode(x=5,
                                                                         next=None)))))
headB = ListNode(x=5,
                 next=ListNode(x=6,
                               next=ListNode(x=1,
                                             next=ListNode(x=8,
                                                           next=ListNode(x=4,
                                                                         next=ListNode(x=5,
                                                                                       next=None))))))
printLL(headA)
printLL(headB)
printLL(getIntersectionNode(headA, headB))




