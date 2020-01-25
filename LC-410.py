class Solution:
    def splitArray(self, nums, m):
        l = max(nums)
        r = sum(nums)
        while l<r:
            mid = l + (r-l)/2
            if(self.no_of_partitions(nums,mid)>m):
                l=mid+1
            else:
                r=mid
        ans=l
        for i in range(l,r+1):
            if(self.no_of_partitions(nums,i)==m):
                ans=i
                break
        return ans
    
    def no_of_partitions(self,nums,max_sum):
        curr_sum=0
        partitions=1
        for i in range(len(nums)):
            if(curr_sum+nums[i]<=max_sum):
                curr_sum+=nums[i]
            else:
                curr_sum = nums[i]
                partitions+=1
        return partitions
