l = [3,5,1,13,9,6,7,2]
_max = l[0]
for x in l[1:]:
    if x > _max:
        _max = x
        print(x)  #longest decreasing subsequent

l = [1,2,3,4,5,6,7,89,9]
print(l[::2])

l = [1,2,3,4,5,6,7,89,9]
print(l.index(3))


l = [1,2,3,4,5,6,98,89,9]
#print(max(l))

def big(arr):
    _max = arr[0]
    for i in arr[1:]:
        if i > _max:
            _max = i
    return _max

print(big(l))


l = [1, 2, 3, 4, 5]
start, end = 0, len(l) - 1

while start < end:
    l[start], l[end] = l[end], l[start]
    start += 1
    end -= 1

print(l)


#sort a list
def bubble_sort(lst):
    """
    Sorts a list using bubble sort algorithm.
    """
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

l = [5, 2, 9, 1, 7]
print(bubble_sort(l))


#max elemnt in the list
def _max(list):
    current = list[0]
    for i in list[1:]:
        if i > current:
            current = i
    return current

print(_max([2,6,7,4,65,8,56,65]))



#reversing  a list
def reverse_list(lis):
    s, e = 0, len(lis)-1
    while s < e:
        lis[s], lis[e] = lis[e], lis[s]
        s +=1
        e -=1
    return lis

print(reverse_list([2,6,7,4,65,8,56,65]))

#sorted list
