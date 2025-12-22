class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force
        '''n = len(nums)
        res = [0]*n
        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue
                else:
                    prod*=nums[j]
            res[i] = prod
        return res'''
        #optimal solution
        '''2 3 4 5
        2 6 24 120
        120 60 20 5
        '''
        n = len(nums)
        res = [1]*n
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(n-1,-1,-1):
            res[i]*= postfix
            postfix *= nums[i]
        return res 
