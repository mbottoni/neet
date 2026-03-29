class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            print(stones)
            x, y = stones[-1], stones[-2]
            if x == y:
                del stones[-2]
                del stones[-1]
            elif x > y:
                stones[-2] = x-y
                del stones[-1]

        if len(stones)==0:
            return 0
        return stones[0]
        