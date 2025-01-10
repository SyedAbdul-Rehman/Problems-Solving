from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j

# Test case code
if __name__ == "__main__":
    # Create a Solution object
    solution = Solution()

    # Test case 1: Example input
    nums = [1, 1, 2, 2, 3, 4, 4, 5]
    print(f"Original List: {nums}")

    # Call the method and get the new length
    length = solution.removeDuplicates(nums)
    print(f"Updated List: {nums[:length]}")
    print(f"New Length: {length}")

    # Test case 2: Edge case with all elements the same
    nums = [7, 7, 7, 7, 7]
    print(f"\nOriginal List: {nums}")
    length = solution.removeDuplicates(nums)
    print(f"Updated List: {nums[:length]}")
    print(f"New Length: {length}")

    # Test case 3: Edge case with no duplicates
    nums = [1, 2, 3, 4, 5]
    print(f"\nOriginal List: {nums}")
    length = solution.removeDuplicates(nums)
    print(f"Updated List: {nums[:length]}")
    print(f"New Length: {length}")

    # Test case 4: Empty list
    nums = []
    print(f"\nOriginal List: {nums}")
    length = solution.removeDuplicates(nums)
    print(f"Updated List: {nums[:length]}")
    print(f"New Length: {length}")
