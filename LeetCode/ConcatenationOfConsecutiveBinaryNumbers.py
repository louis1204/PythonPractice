class Solution:
    def concatenatedBinary(self, n: int) -> int:
        binString = ""
        for i in range(n + 1):
            binString = binString + "{0:b}".format(i)
        return int(binString, 2) % 1000000007
