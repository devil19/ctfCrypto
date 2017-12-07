#encoding=utf-8
import string
letters=string.uppercase
str1='dccdcccdddcdcccddcccccccccddcdccccdccccccdcccdccdccccdccdddccdddccdcdd'
str2=''
str4=''#结果输出
list1=[]#存放初始二进制
list2=[]#存放转换后的培根密码
list3=[]#密文5个一组放入
for i in str1:
    str2+=chr(ord(i)-2)
i=0
while i<len(str2):
    str3=''
    str3=str2[i:i+5]
    list3.append(str3)
    i+=5
print list3#密文数组
#培根密码生成
def peigen(list1):
    for i in range(26):
        str4=''
        str4=bin(i)[2:]
        if len(str4)<6:
            str4='0'*(5-len(str4))+str4
            list1.append(str4)
    return list1
peigen(list1)
for i in list1:
    s=''
    l=list(i)
    for j in i:
        if j=='1':
            s+='b'
        else:
            s+='a'
    list2.append(s)
print list2
for i in range(len(list3)):
    for j in range(len(list2)):
        if list3[i]==list2[j]:
            str4+=letters[int(('0b'+list1[j]),2)]
print str4