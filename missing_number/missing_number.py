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

def missing_number_sumtrick(nums:List[int])->int:
    n=len(nums)
    sum_all=n*(n+1)//2
    sum_actual=sum(nums)
    # for i in nums:
    #     sum_actual+=i
    return sum_all-sum_actual
def missing_number_dict(nums:List[int])->int:
    dic={}
    nums.sort()
    n = nums[-1]
    for i in range(n):
        if dic[i]!=nums[i]:
            dic[i]=0
        else:
            dic[i]+=1

    for i in range(nums):
        if dic[i]==1 or dic[i]==0:
            return i



l=[0,1,2,3,5]
print(missing_number(l))

# print(missing_number_dict(l))
print(missing_number_sumtrick(l))