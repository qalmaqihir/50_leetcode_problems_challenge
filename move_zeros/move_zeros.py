from typing import List


def move_zeros(nums:List[int])-> None:
    j = 0
    for num in nums:
        if num!=0:
            nums[j]=num
            j+=1
    for x in range(j,len(nums)):
        nums[x]=0
    return nums


print(move_zeros([0,1,0,3,12,3,0]))
