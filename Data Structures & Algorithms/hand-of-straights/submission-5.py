class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize > 0:
            return False

        from collections import defaultdict
        group = defaultdict(int)
        for h in hand:
            group[h] += 1

        for _ in range(len(hand)//groupSize):
            min_val = min(group.keys())
            for i in range(min_val, min_val+groupSize):
                group[i] -= 1
                if group[i]==0:
                    del group[i]

        if len(group)>0:
            return False
        return True



        