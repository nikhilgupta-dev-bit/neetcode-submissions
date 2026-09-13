class Solution:
    def reverseBits(self, n: int) -> int:
        bin_no=bin(n)[2:].zfill(32)
        new_bin=bin_no[::-1]
        num=int(new_bin,2)
        return num 
