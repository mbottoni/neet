class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        triplets = [t for t in triplets if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]]

        merged = (0, 0, 0)
        for t in triplets:
            merged = (max(merged[0], t[0]), max(merged[1], t[1]), max(merged[2], t[2]))

        return merged == tuple(target)