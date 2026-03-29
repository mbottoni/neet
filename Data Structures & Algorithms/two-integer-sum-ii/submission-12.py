class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer1 = 0
        pointer2 = len(numbers) - 1
        while True:
            print(numbers[pointer1], numbers[pointer2])
            if numbers[pointer1]+numbers[pointer2]   > target:
                pointer2 = pointer2 - 1
            elif numbers[pointer1]+numbers[pointer2] < target:
                pointer1 = pointer1 + 1
            elif numbers[pointer1]+numbers[pointer2] == target:
                break

        return [pointer1+1, pointer2+1]
        