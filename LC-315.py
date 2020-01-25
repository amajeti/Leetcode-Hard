class Solution(object):
    def countSmaller(self, nums):
        res = []
        count = 0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            res.append(count)
            count =0
        return res


        

