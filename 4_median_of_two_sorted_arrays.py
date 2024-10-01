from typing import List

def swap_all(p_up, p_down, up, down):
    return p_down, p_up, down, up

def findMedianSortedAarrays(nums1:List[int], nums2:List[int]) -> float:
	left, right = [], []
	up, down = nums1, nums2
	total_size = len(nums1) + len(nums2)
	ref_size = total_size // 2
	while len(up) > 0 and len(down) > 0:
		# print(left, right)
		is_equal = False
		p_up = len(up) // 2
		p_down = len(down) // 2
		if up[p_up] > down[p_down]:
			p_up, p_down, up, down = swap_all(p_up, p_down, up, down)
		elif up[p_up] == down[p_down]:
			is_equal = True
		l_size = len(left) + p_up + p_down + 1
		if l_size < ref_size:
			if is_equal and up[0] > down[0]:
				p_up, p_down, up, down = swap_all(p_up, p_down, up, down)
			down_id = 0
			while down[down_id] < up[p_up]:
				down_id += 1
			left = left + down[:down_id]
			down = down[down_id:]
			left = left + up[:p_up+1]
			up = up[p_up+1:]
		else:
			if is_equal and up[-1] > down[-1]:
				p_up, p_down, up, down = swap_all(p_up, p_down, up, down)
			up_id = len(up) - 1
			while up[up_id] > down[p_down]:
				up_id -= 1
			right = up[up_id+1:]
			up = up[:up_id+1]
			right = down[p_down:] + right
			down = down[:p_down]
	if len(down) > 0:
		up = down
	left = left + up + right
	if total_size % 2 == 0:
		return float(left[ref_size] + left[ref_size-1]) / 2
	else:
		return float(left[ref_size])