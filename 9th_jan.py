# 1. Binary search.
def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

print(binary_search([2,5,8,12,16,23,38,56,72,91],23))

# 2. Search in Rotated Sorted Array
def search_rotated(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        if nums[l] <= nums[mid]:  # left half sorted
            if nums[l] <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:  # right half sorted
            if nums[mid] < target <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1


print(search_rotated([5,6,7,8,9,10,1,2,3],8))