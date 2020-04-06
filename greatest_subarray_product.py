from typing import List

class Solution:
    def maxProduct_On2(self, nums: List[int]) -> int:
      N = len(nums)
      max_prod = max(nums)  # Max across diagonal here.
      for i in range(N):
        p = 1
        for j in range(i,N):
          p *= nums[j]
          max_prod = max(p, max_prod)
      return max_prod
    
    # Do for just + numbers first, then generalized
    def maxProductNonNegative(self, nums: List[int]) -> int:
      max_product = nums[0]
      p = 1
      for num in nums:
        if num == 0:
          p = 1  # reset the product tracker
        else:
          p *= num   # max product since last 0
          max_product = max(max_product, p)
      return max_product
    
    # Do for just + numbers first, then generalized
    def maxProduct(self, nums: List[int]) -> int:
      max_product = nums[0]
      p_min = nums[0]
      p_max = nums[0]
      for num in nums[1:]:
        previous_p_max = p_max
        previous_p_min = p_min
        if num < 0:
          p_max = max(num, previous_p_min* num);
          p_min = min(num, previous_p_max* num);
        else:
          p_max = max(num, previous_p_max * num);
          p_min = min(num, previous_p_min * num);

        max_product = max(p_max, max_product)

      return max_product

s = Solution()
s.maxProduct([1,2,-3,0,1,2,3])
