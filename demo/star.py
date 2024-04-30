#打印星星阵
# num1=int(input('Please input row number'))
# num2=int(input('Please input colume number'))
# for i in range(1,num1):
#     for i2 in range(1,num2):
#         print('*', end='')
#     print()#

#冒泡
# arr=[7,3,8,2,5,1]
# for i in range(len(arr)-1):
#     for n in range(len(arr)-1-i):
#         if arr[n]>arr[n+1]:
#             temp=arr[n]
#             arr[n]=arr[n+1]
#             arr[n+1]=temp
#         n-=1
# print(arr)
#
#倒输出测试
# for i in range(10,0,-1):
#     print('*'*i)

#打印金字塔
# n=9
# k=n-1
# for i in range(0, n):
#     # 内部循环处理根据要求更改的数字空间值
#     for j in range(0, k):
#         print('k',end=" ")
#     # 每次循环后递减 k
#     k = k - 1
#     # 内循环处理列值更改为外循环
#     for j in range(0, i + 1):
#         # 打印星号
#         print("* ", end="")
#     # 每行之后的结束行
#     print()
#空心金字塔
# n=9
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if j==1 or j==i:
#             print('*',end='')
#         elif i==n:
#             print('*', end='')
#         else:
#             print(' ',end='')
#     print()
#提取系统日期
# from datetime import *
# somedate=date(2022,2,12)
# today=date.today()
# today=today+timedelta(2)
# print(somedate)
# print(today)
#13章课后1
# for i in range(30):
#     print('%d盎司是%d克'%(i,i * 28.35))
#13章课后2
# userid=input('请出入字符串')
# di_list=['0','1','2','3','4','5','6','7','8','9']
# str_list=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# if userid[0] in di_list and userid[1] in di_list and userid[2] in di_list:
#     print('数字对')
# else:
#     print('数字不对')
# if userid[3] in str_list and userid[4] in str_list and userid[5] in str_list and userid[6] in str_list:
#     print('字母对')
# else:
#     print('字母不对')
#13章课后2
# list_hobby=[0,0,0,0,0]
# while True:
#     num_list=int(input('输入1至5的序号，0退出'))
#     if num_list==1:
#         list_hobby[0]+=1
#     elif num_list==2:
#         list_hobby[1]+=1
#     elif num_list==3:
#         list_hobby[2]+=1
#     elif num_list==4:
#         list_hobby[3]+=1
#     elif num_list == 5:
#         list_hobby[4] += 1
#     elif num_list==0:
#         break
# print('reading books','\\'*(list_hobby[0]))
# print('computer games','\\'*(list_hobby[1]))
# print('sport','\\'*(list_hobby[2]))
# print('programming','\\'*(list_hobby[3]))
# print('watching tv','\\'*(list_hobby[4]))

#用FOR写
list_hobby=['reading books',0,'computer game',0,'sport',0,'programming',0,'watching tv',0]
while True:
    num_list=int(input('输入1至5的序号，0退出'))
    if num_list==1:
        list_hobby[1]+=1
    elif num_list==2:
        list_hobby[3]+=1
    elif num_list==3:
        list_hobby[5]+=1
    elif num_list==4:
        list_hobby[7]+=1
    elif num_list == 5:
        list_hobby[9] += 1
    elif num_list==0:
        break
for items in list_hobby:

    print(items)






