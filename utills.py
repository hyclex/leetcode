from typing import List

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListMaster(object):
	def __init__(self, vals:List):
		self.head = self.create(vals)

	def create(self, vals:List) -> ListNode:
		head = None
		for each in reversed(vals):
			head = ListNode(val = each, next = head)
		return head

	def get_all(self):
		head = self.head
		res = []
		while head is not None:
			res.append(head.val)
			head = head.next
		return res

class TreeMater(object):
	pass

if __name__ == "__main__":
	# test the list master
	head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
	head_master = ListMaster(head)
	print(head_master.get_all())