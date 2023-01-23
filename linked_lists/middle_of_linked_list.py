class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printLL(node):
    while node:
        print(node.val, end=' ')
        node = node.next
    print('')

def middleNode(head):
    if not head:
        return
    cnt = 1
    orig = head
    while head.next:
        head = head.next
        cnt += 1
    place = (cnt // 2)
    print(cnt, place)
    while place > 0:
        orig = orig.next
        place -= 1
    return orig.val


test = ListNode(val=1,
                    next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5, next=None)))))
test2 = ListNode(val=1,
                    next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=None))))

test3 = ListNode(val=1,
                     next=None)

print(middleNode(test))
print(middleNode(test2))
print(middleNode(test3))

