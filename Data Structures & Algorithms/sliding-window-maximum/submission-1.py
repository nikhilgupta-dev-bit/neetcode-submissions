from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = deque()   # stores indices
        ans = []

        for right in range(len(nums)):

            # Remove smaller elements from the back
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            # Add current element
            dq.append(right)

            # Remove elements outside the window
            left = right - k + 1

            if dq[0] < left:
                dq.popleft()

            # Window has reached size k
            if right >= k - 1:
                ans.append(nums[dq[0]])

        return ans
            
