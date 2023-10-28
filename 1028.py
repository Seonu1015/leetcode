# 268. Missing Number - 퀵 정렬

class Solution(object):
    def missingNumber(self, nums):
        def quick_sort(nums):
            if len(nums)<=1:
                return nums
            
            pivot = nums[len(nums)//2]

            left = [x for x in nums if x < pivot]
            middle = [x for x in nums if x == pivot]
            right = [x for x in nums if x > pivot]

            return quick_sort(left) + middle + quick_sort(right)
        
        nums = quick_sort(nums)

        for i in range(len(nums)+1):
            if i not in nums:
                return i
            
# 35. Search Insert Position - 이진탐색

class Solution(object):
    def searchInsert(self, nums, target):
        low, high = 0, len(nums)-1

        while low <= high:
            mid = low + (high - low) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return low

sol = Solution()
print(sol.searchInsert([1,3,5,6], 5))
        
