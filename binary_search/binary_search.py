def binary_search(array, target):
    left = 0
    right=len(array)-1

    while left<=right:
        mid = left+right//2
        if target<array[mid]:
            right=mid-1
        elif target>array[mid]:
            left=mid + 1
        else:
            return mid
    return -1



arr=[1,2,3,4,4,3,3,2,5,6,7,0,9,-1]
index=binary_search(arr,90)
if index==-1:
    print("Element not found")
else:
    print("Element is found at index %d" %index)


