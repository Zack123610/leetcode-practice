# Leetcode 4: Median of Two Sorted Arrays
# Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Optimal binary search solution (O(log(min(m, n))))
        A, B = nums1, nums2
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m
        imin, imax, half_len = 0, m, (m + n + 1) // 2
        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                imax = i - 1
            else:
                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])
                if (m + n) % 2 == 1:
                    return max_of_left
                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])
                return (max_of_left + min_of_right) / 2.0

    # Naive merge solution (O(m + n))
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     merged = []
    #     i = j = 0
    #     while i < len(nums1) and j < len(nums2):
    #         if nums1[i] < nums2[j]:
    #             merged.append(nums1[i])
    #             i += 1
    #         else:
    #             merged.append(nums2[j])
    #             j += 1
    #     merged.extend(nums1[i:])
    #     merged.extend(nums2[j:])
    #     n = len(merged)
    #     if n % 2 == 1:
    #         return float(merged[n // 2])
    #     else:
    #         return (merged[n // 2 - 1] + merged[n // 2]) / 2.0