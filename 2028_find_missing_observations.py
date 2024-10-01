from typing import List
def missingRolls(rolls:List[int], mean:int, n:int)->List[int]:
	# get the sum of the list
	return_sum = mean * (n+len(rolls)) - sum(rolls)
	return_mean = return_sum / n
	print(return_mean)
	if return_mean < 1 or return_mean > 6:
		return [] 
	less_mean = int(return_mean)
	less_sum = less_mean * n
	remain = return_sum - less_sum
	return [less_mean] * (n-remain) + [less_mean+1] * remain

if __name__ == "__main__":
	rolls = [3,5,3]
	mean = 5
	n = 3
	print(missingRolls(rolls, mean, n))