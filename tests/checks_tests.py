# m={}
# n=9
# for i in range(n):
#     m[i]=True
# for j in m:
#     print(j)
#
# print(m)


nums=[2,2,1,4,4]

# nums=[4,1,2,1,2]
m = {}
for i in nums:
    if i not in m:
        m[i] = 1
    else:
        m[i] = 2
print(m)
for i in m:
    print('m[i] = ',m[i])
    print('i = ',i)
    if m[i] == 1:
        print('inside if',i)

