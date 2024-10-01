from typing import List

def sumPrefixScores(words:List[str]) -> List[int]:
    # build trie with count
    trie = {'next':{},
            'count': 0}
    for w in words:
        head = trie
        for char in list(w):
            if head['next'].get(char) is None:
                head['next'][char] = {'next':{},
                                      'count': 0}
            head['next'][char]['count'] += 1
            head = head['next'][char]
    # get the result
    res = []
    for w in words:
        cur_res = 0
        head = trie
        for char in list(w):
            cur_res += head['next'][char]['count']
            head = head['next'][char]
        res.append(cur_res)
    return res
    
if __name__ == "__main__":
    words = ["abc","ab","bc","b"]
    print(sumPrefixScores(words))