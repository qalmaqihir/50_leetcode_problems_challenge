from orca.punctuation_settings import infinity


def max_sum(arr,k):
    max_sum=-1000000000000000
    n = len(arr)
    for i in range(0,n-k+1):
        current_sum=0
        for j in range(0,k):
            current_sum+=arr[i+j]

        max_sum=max(current_sum,max_sum)

    return max_sum



arr=[2,3,4,2,-1,1,0,3,8,7,9]
print(max_sum(arr,3))