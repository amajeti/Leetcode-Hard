class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        if n%2 == 0:
            i = int(n/2) - 1 
            j = int(n/2)
            sum1 = float(nums1[i]+nums1[j])
            median = sum1/2
        else:
            i = int(n/2)
            median = nums1[i]

        return median
