
'''文件的打开方式：r,w,a必须选一个,这个是在github修改的
再测试下,分布的下载和合并
r文件必须存在
w文件不存在就得创建，有就清空
a文件不存在就得创建，有就继续写
+对原有权限加成，例如r+w
b以二进制字节串打开


文件打开方式的训练

try:
    #fd=open('text.py','r')#以只读的方式打开,文件必须存在
    #fd=open('text.py','w')#以写的方式打开,如果有文件就是空的
    fd=open('text.py','a')#以写的方式打开,如果有文件就保留原样

    #普通的文本文件既可以使用文本方式打开，也可以使用二进制打开。。二进制文件只能二进制方式打开
    #fd=open('text.py','rb')#以二进制的方式打开,文件必须存在

    print(fd)
except Exception as e:
    print(e)
fd.close()#关闭文件，fd不可用了


#文件读取演示
#打开文件
f=open('demo','r')#打印字符串
f=open('demo','rb')#打印字节串
date=f.read(10)#读取前10个字符串
print(date)
print(date.decode())#转换为了字符串
f.close()

#打开二进制图像
f=open('text_pic.jpeg','rb')#打印字节串
date=f.read()
print(date)#很长的字节串
f=open('demo','r')


#一、一行一行的打印
while True:#读到文本结尾
    date=f.read(10)
    if not date:#读到结尾跳出循环
        break
    print(date)
'''

#二、读取一行的内容
# f=open('word_list4.txt','r')
# date=f.readline()#如果有参数就读取第一行中第4个字符
# print('一行内容',date)
# date=f.readline()#读完第一行剩余的内容
# print('一行内容',date)


#三、readlines，读取文件中每一行作为列表中的一项
# f=open('demo','r')
# # date=f.readlines()#列表中每一项就是一行
# # print('多行内容',date)
# # date=f.readlines(20)#前20个字节所在的行作为读取对象
# # print('多行内容',date)
#
# #文件本身是可迭代对象，可用for 打开
# for i in f:
#     print(i)
# f.close()

# 在单词本(word_list4)中，从终端输入一个单词，从单词本中找到该单词，打印解释内容
# 如果找不到打印‘找不到’
fd=open('word_list4.txt','r')
word=input('word:')
for line in fd:
    w=line.split(' ')[0]#通过空格分割字符串，空格前面的是要找的单词
    if w>word:#如果遍历到的单词大于word,就结束查找
        print('没有这个单词')
        break
    elif w==word:
        print(line)
        break
else:
    print('没有')
fd.close()
