def maxProbability(n:int,
	               edges:list,
	               succProb:float,
	               start_node:int,
	               end_node:int)->float:
	pass

if __name__ == "__main__":
    n = 3
    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.2]
    start_node = 0
    end_node = 2
    res = maxProbability(n, edges, succProb, start_node, end_node)
    print(res)