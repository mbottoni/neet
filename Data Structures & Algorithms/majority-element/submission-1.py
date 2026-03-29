class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import defaultdict
        d = defaultdict(int)
        for n in nums:
            d[n]+=1
        d = {k:v for k,v in sorted(d.items(), key=lambda item: item[1])}
        keys = list(d.keys())
        return keys[-1]
        