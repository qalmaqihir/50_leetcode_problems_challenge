from typing import List


def missing_number(nums:List[int])-> int:
    nums.sort()
    n=nums[-1]
    if nums[0]!=0:
        return 0
    for i in range(n-1):
       # print(f"at index {i} the number is {nums[i]} and next number is {nums[i+1]}")
        if nums[i+1]> nums[i]+1:
            return nums[i]+1
        # else:
        # #    print("All fine till here")
    return -1




l=[0,1,2,3,5]
print(missing_number(l))
