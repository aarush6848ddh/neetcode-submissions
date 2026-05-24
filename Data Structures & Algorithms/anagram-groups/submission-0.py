class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_hashmap = {}
        for i, s in enumerate(strs):
           s_sort = "".join(sorted(s))
           if s_sort in my_hashmap:
                my_hashmap[s_sort].append(s)
           else:
                my_hashmap[s_sort] = [s]
        
        return list(my_hashmap.values())