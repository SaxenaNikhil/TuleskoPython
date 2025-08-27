from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = dict()

        for i, elem in enumerate(nums):
            complement = target - elem

            if complement in values:
                return [values[complement], i] # To find the complement index inside the values array and i is the current index value.

            values[elem] = i # Storing the current element from nums inside the values dictionary for the current index where elem is key and i is values.

        return []


if __name__ == "__main__":
    sol = Solution()

    nums1 = [2, 7, 11, 15]
    target1 = 9
    print("Result:", sol.twoSum(nums1, target1))  # [0, 1]

    nums2 = [3, 2, 4]
    target2 = 6
    print("Result:", sol.twoSum(nums2, target2))  # [1, 2]

    nums3 = [3, 3]
    target3 = 6
    print("Result:", sol.twoSum(nums3, target3))  # [0, 1]