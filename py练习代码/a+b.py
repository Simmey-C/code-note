#  学习·练习Python

# a=10
# b=3
# print(type(a))
# print(a)
# print('a')
# print(a/b)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a**b)
# print(a//b)
# print(a%b)
import turtle

# try:
#     a=input("请输入a的值：")
#     b=input("请输入b的值：")
#     c=float(a)/float(b)
# except ZeroDivisionError:
#     print("除数不能为0！")
# except ValueError:
#     print("请输入数字！")
# else: # 无异常发生时执行
#     print(c)
# finally: # 无论是否有异常发生都会执行
#     print("程序结束")


# 打印乘法口诀表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,"*",i,"=",j*i,end="\t")
#     print()


### 列表
# list=[1,2,3,4,5,6,"hello","world"]
## 打印列表
# print(list[1])
# print(list[-2])
# print(list[1:4])
# print(list[::2])
# print(list[1::2])
# print(list[:4:])
## 修改列表 直接修改
# list[1]=100
# list[2]=200
# print(list)
## 添加元素
# list.append(7) # 在列表末尾添加单个元素
# list.insert(3,8) # 在指定位置插入元素
# list.extend([9,10]) #在列表末尾添加多个元素
## 合并列表
# list1=[10,20,30]
# list.extend(list1)
# print(list)
## 删除元素
# list.pop(3) # 删除指定位置元素
# print(list)
# list.pop() # 删除列表末尾元素
# print(list.pop()) # 删除列表末尾元素并返回该元素
# print(list)
# list.remove("hello") # 删除指定元素
# print(list)
# del list[0] # 删除指定位置元素
# print(list)
# list.clear() # 清空列表
# print(list)
# 列表元素类型
# print(type(list))
# # 列表元素个数
# print(len(list))
# # 列表元素是否存在
#  print(1 in list)
# print(100 in list)
# # 列表元素是否为空；
# print(list)
# if list:
#     print("列表不为空！")
# else:
#     print("列表为空！")
# list1=[1,2,8,6,3,4,5]
# print(sum(list1)) # 求和
# print(max(list1)) # 最大值
# print(min(list1)) # 最小值
# list1.sort() # 排序（默认升序）
# list1.sort(reverse=True) # 排序（降序）
# print(sorted(list1)) # 排序并返回新列表
# print(sorted(list1,reverse=True)) # 排序（降序）并返回新列表
# print(list1)
# list1.reverse() # 反转列表
# print(list1)


###for循环
# 示例1：循环5次，打印0-4
# for i in range(5):
#     print(i)  # 输出：0 1 2 3 4
#
# # 示例2：循环打印1-5
# for i in range(1, 6):
#     print(i)  # 输出：1 2 3 4 5
#
# # 示例3：步长为2，打印1,3,5
# for i in range(1, 7, 2):
#     print(i)  # 输出：1 3 5


### 元组
# tuple1=(1,2,3,4,5)
# tuple2=(6,7,8,9,10)
# # tup=tuple1+tuple2
# tuple=() # 空元组
# tuple=(1,) # 只有一个元素的元组 tuple=(1)的类型是int
# print(tuple1)
# print(tuple1[1])
# print(tuple1[-2])
# print(tuple1[1:4])
# print(tuple1[::2])
# print(tup)
# #元组不可以修改 删除
# print(max(tuple1))
# print(min(tuple1))
# print(sum(tuple1))
# print(tuple1.count(2)) # 统计元组中元素出现的次数
# print(tuple1.index(2)) # 找出元组中第一个指定元素的索引
# print(tuple1.index(2,0)) # 找出指定元素的索引，从指定位置开始搜索
# print(tuple1.index(2,0,4))
# print(len(tuple1)) # 元组长度


###字典
# dict1={"name":"张三","age":20,"gender":"男"}
# print(dict1)
# print(dict1["name"])
# dict1["age"]=18 # 修改键值对
# dict1["city"]="guangzhou"
# print(dict1)
# del dict1["age"] # 删除键值对
# print(dict1)
# dict1.clear() # 清空字典中所有键值对
# print(dict1)
# del dict1

# dict2=dict.fromkeys(dict1.keys())
# dict3=dict.fromkeys(dict1,"undefined")
# print(dict1.keys())
# print(dict2)
# print(dict3)

# number=[1,2,3,4,5]
# squares=map(lambda x:x**2,number)
# print(list(squares))

# a=int(input())
# b=int(input())
# print(a)
# print(b)

