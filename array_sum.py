class Solution:

    def twoSum(self,nums,target):
        self.nums = nums
        self.target = target
        for i in range(len(self.nums)):
            for j in range(i+1,len(self.nums)):
                if nums[j] == self.target - self.nums[i]:
                    #print([i,j])
                    return [i,j]

nums = [3,2,4]
target = 6
out_index = Solution().twoSum(nums,target)
print(out_index)