class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n=len(arr)
        max_len = 1
        curr = 1
        #a > b < c > d < e ... OR a < b > c < d > e ...
        # actully jo chaiye woh alternating signs hain +-+- or -+-+
        for i in range(1,n):
            if arr[i]==arr[i-1]:
                curr=1
            elif (i==1) or ((arr[i] > arr[i-1]) != (arr[i-1] > arr[i-2])):
                curr+=1
            else :
                curr=2
            max_len=max(max_len,curr)
        return max_len

            
