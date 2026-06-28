class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr) - 1
        while r - l + 1 > k:
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1      # drop left
            else:
                r -= 1      # drop right

        return arr[l:r+1]
                

                




