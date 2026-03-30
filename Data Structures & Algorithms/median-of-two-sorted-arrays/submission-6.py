class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        total = len(A)+len(B)
        half = total // 2
        if len(B)<len(A):
            A,B = B,A

        l, r = 0, len(A)-1
        while True:
            i = (l+r) // 2 # A
            j = half - i - 2

            Aleft = A[i] if i >= 0 else -99999999999
            Aright = A[i+1] if i+1<len(A) else 99999999999

            Bleft = B[j] if j >= 0 else -99999999999
            Bright = B[j+1] if j+1<len(B) else 99999999999  # Fix 1: i+1 -> j+1

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft)+min(Aright, Bright))/2  # Fix 2: added parentheses
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1