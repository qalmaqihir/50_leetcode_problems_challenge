# a more optimized version of the previous problem


def max_sum_optimized(arr,k):
    if k>len(arr):
        return -1

    #max_sum = -1000000000000000000
    window_sum=sum([arr[i] for i in range(0,k)])
    max_sum=window_sum
    n=len(arr)

    for i in range(0,n-k):
        window_sum= window_sum-arr[i]+arr[i+k]
        max_sum=max(window_sum,max_sum)

    return max_sum



arr=[2,3,4,2,-1,1,0,3,8,7,9]
print(max_sum_optimized(arr,3))

