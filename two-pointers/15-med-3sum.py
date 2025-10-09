# Leetcode 15: 3Sum
# Link: https://leetcode.com/problems/3sum/

from typing import List

class Solution:
    '''
    Time Complexity: O(n^2): O(n^2). twoSumII is O(n), and we call it n times.
                        Sorting the array takes O(nlogn), so overall complexity is O(nlogn+n^2). This is asymptotically equivalent to O(n^2).
    Space Complexity: from O(logn) to O(n), depending on the implementation of the sorting algorithm. For the purpose of complexity analysis, we ignore the memory required for the output.
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):

            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start, end = i+1, len(nums)-1

            while start < end:
                total = nums[i] + nums[start] + nums[end]
                if total > 0:
                    end -= 1
                elif total < 0:
                    start += 1
                else:
                    res.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1

                    # Skip duplicates for left and right
                    while nums[start] == nums[start-1] and start < end:
                        start += 1
                    while nums[end] == nums[end+1] and start < end:
                        end -= 1             
        
        return res