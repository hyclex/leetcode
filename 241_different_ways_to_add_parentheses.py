from typing import List

def diffWaysToCompute(expression:str) -> List[int]:
	def pairOps(num1, num2, opt_char):
		if opt_char == '+':
			res = num1 + num2
		elif opt_char == "-":
			res = num1 - num2
		elif opt_char == '*':
			res = num1 * num2
		return res

	# parse the string
	nums = []
	ops = []
	cur_num_str = ""
	idx = 0
	l = len(expression)
	while idx < l:
		if expression[idx] in ['+', '-', '*']:
			nums.append(int(cur_num_str))
			cur_num_str = ""
			ops.append(expression[idx])
		else:
			cur_num_str += expression[idx]
		idx += 1
	if len(cur_num_str) > 0:
		nums.append(int(cur_num_str))
	print(nums, ops)

	dp_cache = []
	dp_cache.append([[i] for i in nums])
	for i in range(1, len(nums)):
		cur_row = []
		for j in range(len(nums) - i):
			cur_res = []
			for k in range(i):
				nums1 = dp_cache[k][j]
				nums2 = dp_cache[i-1-k][j+k+1]
				op = ops[j+k]
				cur_res += [pairOps(a, b, op) for a in nums1 for b in nums2]
			cur_row.append(cur_res)
		dp_cache.append(cur_row)
	return dp_cache[-1][0]

if __name__ == "__main__":
	expression = "2*3-4*5"
	res = diffWaysToCompute(expression)
	print(res)