class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    head = None
    curr = None
    while list1 and list2:
        if list1.val < list2.val:
            next = list1
            list1 = list1.next
        else:
            next = list2
            list2 = list2.next
        if not head:
            head = next
            curr = next
        else:
            curr.next = next
            curr = next
    while list1:
        if not head:
            head = list1
            curr = list1
        else:
            curr.next = list1
            curr = list1
        list1 = list1.next
    while list2:
        if not head:
            head = list2
            curr = list2
        else:
            curr.next = list2
            curr = list2
        list2 = list2.next
    return head

def printLL(node):
    while node:
        print(node.val, end=' ')
        node = node.next

list1 = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=4, next=None)))
list2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4, next=None)))
printLL(mergeTwoLists(list1, list2))
