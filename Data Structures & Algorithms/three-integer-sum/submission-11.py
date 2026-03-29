class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        possible_sums = []
        for i in range(n):
            for j in range(i + 1, n):
                soma = -(nums[i] + nums[j])
                if soma in nums[j+1:]:
                    possible_sums.append([nums[i], nums[j], soma])
        
        for combo in range(len(possible_sums)):
            possible_sums[combo] = sorted(possible_sums[combo])
        
        return [list(t) for t in set(tuple(c) for c in possible_sums)]