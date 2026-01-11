
'''from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
        Find two indices of numbers in the array that add up to the target sum.
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List containing two indices [i, j] where nums[i] + nums[j] == target
        """
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i  # Store the number (not the list!) with its index
        
        return []


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Basic case
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Test 1: nums = {nums1}, target = {target1}")
    print(f"Output: {solution.two_sum(nums1, target1)}")
    print(f"Expected: [0, 1]\n")
    
    # Test case 2: Array with 2 elements (your code would skip this!)
    nums2 = [3, 3]
    target2 = 6
    print(f"Test 2: nums = {nums2}, target = {target2}")
    print(f"Output: {solution.two_sum(nums2, target2)}")
    print(f"Expected: [0, 1]\n")
    
    # Test case 3: Solution not at beginning
    nums3 = [3, 2, 4]
    target3 = 6
    print(f"Test 3: nums = {nums3}, target = {target3}")
    print(f"Output: {solution.two_sum(nums3, target3)}")
    print(f"Expected: [1, 2]\n")
    
    # Test case 4: Negative numbers
    nums4 = [-1, -2, -3, -4, -5]
    target4 = -8
    print(f"Test 4: nums = {nums4}, target = {target4}")
    print(f"Output: {solution.two_sum(nums4, target4)}")
    print(f"Expected: [2, 4]\n")
    
    # Test case 5: With zero
    nums5 = [0, 4, 3, 0]
    target5 = 0
    print(f"Test 5: nums = {nums5}, target = {target5}")
    print(f"Output: {solution.two_sum(nums5, target5)}")
    print(f"Expected: [0, 3]")  '''


# # two pointer approach.
# def two_sum(nums,target):
#     l=0
#     n = len(nums)
#     r = n-1
#     while l < r:
#         summ = nums[l] + nums[r]
#         if summ == target:
#             return [l+1,r+1]
#         elif summ < target:
#             l+=1
#         else:
#             r-=1
# nums = [2,5,7,8,9,6,4,2]
# target = 8
# print(two_sum(nums,target))


def twoSum(n, target):
    n1 = sorted(n)
    l, r = 0, len(n1)-1
    while l < r:
        s = n1[l] + n1[r]
        if s == target:
            return (l,r)
        elif s < target:
            l += 1
        else:
            r -=1
    return None

n = [2,5,7,8,9,6,4,2]
target = 8
print(twoSum(n,target))


# valid palindrome.
#3sum
''' palindrome is some'''
def isPalindrome(s:str) -> bool:
    if not isinstance(s, str):
        return False
    filtered = [ch.lower() for ch in s if ch.isalnum()]
    return filtered == filtered[::-1]

s= "kamalamal"
print(isPalindrome(s))

#3sum
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: sort the array
        res = []
        
        for i in range(len(nums)):
            # Step 2: skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            
            # Step 3: two-pointer search
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # Move inward
                    left += 1
                    right -= 1
                
                elif total < 0:
                    left += 1  # need a bigger sum
                else:
                    right -= 1  # need a smaller sum
        
        return res
