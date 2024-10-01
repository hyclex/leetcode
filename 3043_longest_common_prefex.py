from typing import List

def longestCommonPrefix(arr1:List[int], arr2:List[int]) -> int:
	# build the hash tree of arr1
	hash_tree = {}
	for num in arr1:
		head = hash_tree
		for char in list(str(num)):
			if head.get(char) is None:
				head[char] = {}
			head = head[char]
	
	largest = 0
	for num in arr2:
		head = hash_tree
		cur_depth = 0
		for char in list(str(num)):
			if head.get(char) is None:
				break
			cur_depth += 1
			head = head[char]
		if cur_depth > largest:
			largest = cur_depth
	return largest

if __name__ == "__main__":
	arr1 = [1, 10, 100]
	arr2 = [1000]

	print(longestCommonPrefix(arr1, arr2))
