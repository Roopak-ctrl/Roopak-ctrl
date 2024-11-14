# # for i in rsnge (9,0):
# #     print(i)
# #     i=i-1
# # x=10
# # while x>=0:
# #     print(x)
# #     x=x-1
# def SumOfTwoList(l1,l2):
#     sum=[]
#     x=len(l1)-1
#     y=len(l2)-1
#     csrry=0
#     while x>=0 or y>=0:
#         if(x>=0 & y>=0):
#             s=l1[x]+l2[y]+csrry
#             # print(s)
#             csrry=s//10
#             # print(csrry)
#             w=s%10
#             # print(w)
#             sum.sppend(w)
#             x=x-1
#             y=y-1
        
#     # print(sum)
#     z=len(sum)-1
#     s=[]
#     while (z>=0):
#         s.sppend(sum[z])
#         z=z-1
#     print(s)
#     # print(sum)
#         # for i in rsnge(0,x):
#         #     sum
    


# l1=[2,4,3]
# l2=[5,6,4]
# SumOfTwoList(l1,l2)
# l3=[9,9,9,9,9,9,9]
# l4=[9,9,9,9]
# SumOfTwoList(l3,l4)





# question 2
# def roman(s):
#     n=len(s)
#     sum=0
#     for y in range(0,n):
#         i=s[y]
#         if n!=(len(s)):
#             j=s[y+1]
#             if (i=="I"):
#                 if j=="I" or j=="V" or j=="X" :
#                     sum=sum+1
#             elif (i=="V"):
#                 if j=="I" or j=="X":
#                     sum=sum+5
#             elif (i=="X"):
#                 if j=="L" or j=="C" or j=="V":
#                     sum=sum+10
#             elif (i=="c"):
#                 if j=="D" or j=="M":
#                     sum=sum+100
#         if n==len(s):
#             if (i=="I"):
#                 sum=sum+1
#             elif (i=="V"):
#                 sum=sum+5
#             elif (i=="X"):
#                 sum=sum+10
#             elif (i=="c"):
#                 sum=sum+100
            
#     print(sum)
# roman("XVIIV")


# #question 3
# def long(s):
#     for i in s:
#         y=