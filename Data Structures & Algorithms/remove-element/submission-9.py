class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        pointer = 0
        for i in range(len(nums)):
            if nums[i] != val:
                k += 1
            elif nums[i] == val:
                nums[i], nums[pointer] = nums[pointer], nums[i]
                pointer += 1
        print(nums)
        while True:
            if len(nums)>0 and nums[0]==val:
                del nums[0]
            else:
                break
        return k
        