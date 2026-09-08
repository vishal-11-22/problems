class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      
        hashmap = {}

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)

            if key not in hashmap:
                hashmap[key] = []

            hashmap[key].append(s)
        print(hashmap)
        return list(hashmap.values())

        # hashmap=dict()
        # for i in strs:
        #     sorted_str=''.join(sorted(i))
        #     if sorted_str in hashmap:
        #         hashmap[sorted_str].append(i)
        #     else:
        #         hashmap[sorted_str]=[i]
        # return list(hashmap.values())
        