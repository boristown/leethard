class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right, pre_sum, ret = 0, 1, 0, 1
        while right < len(nums):
            pre_sum += (right - left) * (nums[right] - nums[right - 1])
            while pre_sum > k:
                pre_sum -= nums[right] - nums[left]
                left += 1
            ret = max(ret, right - left + 1)
            right += 1
        return ret
      
#https://leetcode-cn.com/problems/frequency-of-the-most-frequent-element/solution/zui-gao-pin-yuan-su-de-pin-shu-by-leetco-q5g9/
