
# binary search in python.
''' we can do binary search only when the list is sorted. '''
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    
    for i in range(len(arr)):
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
print(binary_search([1,2,3,4,5,6,7,8,9], 3)) 



#what if the list is unsorted.
def linear(arr, target):
    for i in range(len(arr)):
        if target == arr[i]:
            return i
    return -1
    
#print(linear([2,5,3,4,8,9,2],4))