class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap=dict()
        for i in arr:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1
        count=hashmap.values()
        if len(count)==len(set(count)):
            return True
        else:
            return False