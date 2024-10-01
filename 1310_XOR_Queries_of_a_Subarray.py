from typing import List
def xorQueries(arr:List[int], queries:List[List[int]]) -> List[int]:
	prefix_sum = [0]
	for num in arr:
		prefix_sum.append(prefix_sum[-1] ^ num)
	res = []
	for i, j in queries:
		res.append(prefix_sum[j+1] ^ prefix_sum[i])
	return res


if __name__ == "__main__":
	arr = [1,3,4,8]
	queries = [[0,1],[1,2],[0,3],[3,3]]
	# print([i for i in queries])
	res = xorQueries(arr, queries)
	print(res)
