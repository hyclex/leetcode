from utills import *
from typing import List

def spiralMatrix(m:int, n:int, head:ListNode) -> List[List[int]]:
	x, y = 0, 0
	x_t, x_b = 1, m - 1
	y_l, y_r = 0, n - 1
	state = 'r'

	res = [[-1]*n for _ in range(m)]

	while head is not None:
		# print(x, y)
		cur_val = head.val
		head = head.next
		res[x][y] = cur_val
		if state == 'r':
			if y < y_r:
				y += 1
			else:
				state = 'd'
				y_r -= 1
				x += 1
		elif state == 'd':
			if x < x_b:
				x += 1
			else:
				state = 'l'
				x_b -= 1
				y -= 1
		elif state == 'l':
			if y > y_l:
				y -= 1
			else:
				state = 'u'
				x -= 1
				y_l += 1
		elif state == 'u':
			if x > x_t:
				x -= 1
			else:
				state = 'r'
				y += 1
				x_t += 1
	return res


if __name__ == "__main__":
	m, n = 3, 5
	head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
	head = ListMaster(head).head
	res = spiralMatrix(m, n, head)
	print(res)