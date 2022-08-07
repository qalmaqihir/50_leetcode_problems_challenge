from typing import List


def valid_mountain(nums:List[int])-> bool:
    i=1
    if len(nums)<3:
        return False

    while i<len(nums) and nums[i]>nums[i-1]:
        i+=1
    if i == len(nums) or i ==1:
        return False
    while i< len(nums) and nums[i]<nums[i-1]:
        i +=1
    return i == len(nums)



print(f"Output True: {valid_mountain([2,3,4,0,-2,-3,-4])}")
print(f"Output False: {valid_mountain([2,3,4,0,2,5,6,9])}")
print(f"Output True: {valid_mountain([2,3,4,0])}")
print(f"Output False: {valid_mountain([2,3,4])}")

