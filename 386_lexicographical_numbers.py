from typing import List

def lexicalOrder(n:int) -> List[int]:
	res = []
	state_stack = [(0, 0, 0)]
	cur_depth = 1
	cur_digit = 1
	cur_num = 1
	while cur_depth != 0:
		if cur_num <= n and cur_digit <= 9:
			res.append(cur_num)
			state_stack.append((cur_depth, cur_digit, cur_num))
			cur_depth += 1
			cur_digit = 0
			cur_num = cur_num * 10 + cur_digit
		else:
			cur_depth, cur_digit, cur_num = state_stack.pop()
			cur_digit += 1
			cur_num += 1
	return res


if __name__ == "__main__":
	n = 13
	print(lexicalOrder(13))