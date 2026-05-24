class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = []
        freq=Counter(nums)
        for el, frequency in freq.most_common(k):
            out.append(el)
        return out