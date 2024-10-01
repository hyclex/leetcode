from typing import List

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printAll(self):
        cur = self
        while cur is not None:
            print(cur.val)
            cur = cur.next

def modifiedList(nums:List[int], head:ListNode) -> ListNode:
    hashed_nums = set(nums)
    dummy_head = ListNode(-1, head)
    p1 = dummy_head
    p0 = head

    while p0 is not None:
        if p0.val in hashed_nums:
            p1.next = p0.next
        else:
            p1 = p1.next
        p0 = p0.next
    return dummy_head.next

if __name__ == "__main__":
    nums = [1,2,3]
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head.printAll()
    print("-----")
    res = modifiedList(nums, head)
    res.printAll()