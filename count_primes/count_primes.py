import math


def count_primes(n:int)->int:
    if n <2:
        return 0
    is_prime=[True for i in range(n+1)]
    is_prime[0]=is_prime[1]=False
    for i in range(2,math.ceil(math.sqrt(n))):
        if is_prime[i]:
            for multiples_of_i in range(i*i,n,i):
                is_prime[multiples_of_i]=False
    return sum(is_prime)

    # m={}
    # primes = 0
    # for i in range(1,n+1):
    #     m[i]=True
    # print(f"our dict after setting all True \n {m}")
    # root = int(math.sqrt(n+1))
    # print(f"root = {root}")
    # for j in range(2,root+1):
    #     print(f"Checking {j}th index at dic == {m[j]}")
    #     if m[j]==True:
    #         for j in range(j*j,n,j):
    #             m[j]=False
    # print(f"Our dic after Falsing all non-primes \n {m}")
    # for k in m:
    #     print(f"Checking {k} in our dic")
    #     if m[k]==False:
    #         primes+=1
    # return primes


print(count_primes(110))

