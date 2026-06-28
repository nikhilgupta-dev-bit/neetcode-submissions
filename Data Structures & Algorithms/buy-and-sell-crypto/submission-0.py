class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # how do u get max profit the answer is by minimising the loss 
        #that is max(r-l,max)
        n=len(prices)
        l=0 
        max_profit=0 
        for r in range(n):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                max_profit=max(profit,max_profit)
            else:
                l=r
        return max_profit