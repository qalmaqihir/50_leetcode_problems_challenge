m={}
n=[2,3,4,0,0,3,3]
for i in range(len(n)):
    if n[i] in m:
        m[n[i]]+=1
    m[n[i]]=1
print(m)


# nums=[2,2,1,4,4]
#
# # nums=[4,1,2,1,2]
# m = {}
# for i in nums:
#     if i not in m:
#         m[i] = 1
#     else:
#         m[i] = 2
# print(m)
# for i in m:
#     print('m[i] = ',m[i])
#     print('i = ',i)
#     if m[i] == 1:
#         print('inside if',i)
#

# s1="12"
# s2='34'
# print(s1+s2)
# print(s2+s1)
