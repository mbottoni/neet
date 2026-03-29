class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        d = defaultdict(int)
        for n in nums:
            d[n] = d[n] + 1

        d2 = defaultdict(list) # key -> freq, value [n1,n2,...]
        for key, value in d.items():
            d2[value] = d2[value] + [key]

        final = []
        most_freq = sorted(list(d2.keys()), reverse=True)
        for freq in most_freq:
            final.extend(d2[freq])
            if len(final) >= k:
                break
        return final[:k]




        