class Solution:
    def countBits(self, num: int):
        result = [0] # initialize at zero
        for i in range(1, num+1):
            result.append(result[i>>1] + int(i&1)) # int(i&1) tells us whether i is odd or even
        return result

s = Solution()
print(s.countBits(2) == [0,1,1])
print(s.countBits(5) == [0,1,1,2,1,2])
