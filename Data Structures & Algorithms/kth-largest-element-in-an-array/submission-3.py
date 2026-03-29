class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        while k>0:
            maxi = heapq.heappop(nums)
            heapq.heapify_max(nums)
            print(maxi)
            k-=1

        return maxi
        