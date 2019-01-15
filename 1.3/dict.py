# -*- coding:utf-8 -*-

Dict = {'Name':'Zara', 'Age':7, 'Class':'First'}

print("Dict['Name']:", Dict['Name'])
print("Dict['Age']:", Dict['Age'])

print("\n")

#访问不存在的key
#print(Dict['xunhun'])


#修改值

print("修改前:", Dict['Age'])
Dict['Age'] = 8 # update existing entry
print("修改后:", Dict['Age'])

print('\n')

#删除
del Dict['Age']#删除键是'Name'的条目
#print("Dict['Age']:", Dict['Age'])#引发异常
Dict.clear() #清空词典所有条目
print(Dict)
del Dict #删除词典

#print(Dict)
