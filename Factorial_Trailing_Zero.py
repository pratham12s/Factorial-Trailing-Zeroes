class Solution:
    def trailingZeroes(self, n: int) -> int:
        count=0
        multiple=5
        while (n//multiple)>0:
            count+=(n//multiple)
            multiple*=5
        return count