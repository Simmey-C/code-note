import numpy as np
import random


# 多维性
t0 = np.array(5)  #0维数组
print(t0)
print(t0.ndim)
t1 = np.array([1, 2, 3, ])  # 1维数组
print(t1)
print(t1.ndim)
print(type(t1))  # 输出数组的类型
t8 = np.array([[4, 5, 6, ],[45, 55, 65, ]])  # 2维数组
print(t8)
print(t8.ndim)


# 创建数组的其他方式
t2 = np.array(range(10))  #arange() 和 range() 用法很像
t3 = np.arange(10)  # another way to create a numpy array
print(t2)
print(t3)
t4 = np.array([random.random() for i in range(10)])
print(t4)
print(np.round(t4, 2))
# python内置的round()函数不支持numpy数组，所以用numpy的round()函数代替


# 数组的形状reshape()
t5 = np.arange(12).reshape(3, 4)
print(t5)
t7 = t5.reshape(4, 3)
print(t7)
t8 = t5.T
print('t5转置：', t8)   # 转置


# 数组的属性
t6 = np.arange(36).reshape(3, 3, 4)
print(t6)
print(t6.shape)  # 输出数组的形状
print(t6.size)  # 输出数组的元素个数
print(t6.ndim)  # 输出数组的维度
print(t6.dtype)  # 输出数组的元素类型
print(t6.T)  # 输出数组的转置
print('=============================================')


# 同质性
t9 = np.array([1, 'hello'])  # 两个都是字符串
print(t9)  # 数组中有不同数据类型，会自动转换为统一数据类型
t10 = np.array([1,2.5])   # 两个都是浮点数
print(t10)
print('=============================================')



## 数组的创建

# 基础的创建方法
arr1 = np.array([1,2,3], dtype=np.int32)
print(arr1)
# 复制数组
arr2 = np.copy(arr1)
print(arr2)   # 输出两个数组的地址不同，但是内容相同
print('=============================================')

# 预定义形状数组的创建
arr3 = np.zeros((2,3))
print(arr3)  # 输出全0数组且为小数
arr4 = np.ones(20, dtype=int )
print(arr4)  # 输出全1数组且为整数
arr5 = np.empty((7,3))
print(arr5)  # 输出未初始化的数组，内容随意,不一定为0，也不一定为1，只指定了形状
arr6 = np.full((3,3), 5)
print(arr6)  # 输出全5数组, 没有twos，threes，fours，fives等等，要用full()函数
arr7 = np.zeros_like(arr1)  # 填充0，与zeros()类似， 形状与arr1相同
arr8 = np.ones_like(arr1)   # 填充1，与ones()类似， 形状与arr1相同
arr9 = np.empty_like(arr3)  # 未初始化，与empty()类似， 形状与arr3相同
arr10 = np.full_like(arr6, 5)  # 填充5，与full()类似， 形状与arr6相同
print(arr7, arr8, arr9, arr10)  # 输出四个数组
print('=============================================')

# 等差数列的创建
array1 = np.arange(1, 10, 2)
print(array1)  # 输出[1 3 5 7 9]
array2 = np.arange(1, 50)  # 省略步长默认为1
print(array2)  # 生成指定序列 [1 2 3 ... 48 49]
# 等间隔数列的创建
array3 = np.linspace(1, 100, 25)
print(array3)  #输出[ 1.  25.  50.  75.  100. ]
array4 = np.linspace(1, 100, 25, dtype=int)
print(array4)  #输出[ 1  25  50  75  100]
# 对数间隔数列的创建（等比数列）
array5 = np.logspace(1, 2, 5)  #默认底数base=10
print(array5)  #输出[ 10.          17.7827941   31.6227766   56.23413252 100.         ]
array6 = np.logspace(0, 4, 3, base=2)  #指定底数base=2
print(array6)  #输出[ 1.  4. 16.]
print('=============================================')

# 特殊矩阵的创建
# 单位矩阵：主对角线上都是1，其他元素都是0
a1 = np.eye(3, 4,dtype=int)  # 输出3x4单位矩阵
print(a1)
# 对角矩阵：主对角线上元素为指定值，其他元素为0
a2 = np.diag([1, 2, 3, 4])  # 输出对角矩阵
print(a2)  #输出4x4对角矩阵
# 随机矩阵：元素服从指定分布
a3 = np.random.rand(3, 4)  # 输出3x4随机矩阵, 元素值在0-1之间, 服从均匀分布,
print(a3)  # 每次运行结果不同
# 随机矩阵：元素值在指定范围内的随机浮点数
a4 = np.random.uniform(1, 10, size = (2, 2))  # 输出2x2随机矩阵,  元素值在1-10之间, 服从均匀分布
print(a4)  #均匀分布：输出每个数的概率都一样
# 随机整数矩阵：元素值在指定范围内的随机整数
a5 = np.random.randint(1, 10, size = (2, 2))  # 输出2x2随机矩阵,  元素值在1-10之间, 服从均匀分布
print(a5)
# 随机数列：服从正态分布 #输出每个数的概率不一样：中间大, 两边小
a6 = np.random.randn(2, 3)  # 输出2x3随机矩阵,  元素值服从正态分布
print(a6)
# 设置随机种子
np.random.seed(50)
arr = np.random.randint(1, 10, size = (5, 4))# 设置随机种子
print(arr)  # 输出随机数列，每次运行结果相同



#数组的类型
# bool
# int
# float
# complex

arr1 = np.array([1, 0, 3], dtype = bool)
print(arr1)
arr2 = np.array([1, 127, 3], dtype = np.int8)
print(arr2)
arr3 = np.array([1, 2, 3], dtype = float)
print(arr3)
arr4 = np.array([1, 2, 3], dtype = complex)
print(arr4)
print('=============================================')

## 索引
# 切片
# 一维数组
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr[0])  # 输出1
print(arr[1:3])  # 输出[2 3] 左包含右不包含
print(arr[slice(1, 3)])  # 输出[2 3] 步长为2  # 等价于上式
print(arr[:])   # 输出全部：[1 2 3 4 5]
print(arr[(arr > 2)& (arr < 5)] )# 输出[3 4 ]
print('=============================================')
# 二维数组
arr2 = np.random.randint(1, 10, size = (6, 7))
print(arr2)
print(arr2[0, 0])  # 输出1
print(arr2[5])
print(arr2[1:3])
print(arr2[2, 2:4])
print(arr[2] [arr[2] > 1])  # 输出[3 4 5]



#  数组的运算
#  数组的加法 //二维数组也可以
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)  # 输出[5 7 9]
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)
print(arr1 // arr2)
print(arr1 ** 2)
#区分
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)  # 输出[1, 2, 3, 4, 5, 6]
# 形状不一样的数组不能进行运算 // 但是可以用reshape()函数进行转换
# 广播机制：当两个数组形状不同时，会自动进行广播，使得两个数组的形状相同

## 矩阵的运算
# 矩阵的乘法
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print(arr1 * arr2)  # 输出[[5 12] [21 32]]
print(arr1 @ arr2)  # 输出[[19 22] [43 50]]
print('=============================================')


### numpy的常用函数
# numpy的基本函数 sqrt() exp() log() sin() cos() tan() abs() power() round() ceil() floor() isnan()
print(np.sqrt([1, 4, 9]))  # 开方 返回浮点数
print(np.exp(1))  # e的指数 返回浮点数 e^x e^1
print(np.log(10))  # 自然对数 返回浮点数 ln(x) ln(10)
print(np.sin(np.pi/2))  # 正弦 返回浮点数 sin(x)
print(np.cos(np.pi/2))  # 余弦 返回浮点数 cos(x)
print(np.tan(np.pi/4))  # 正切 返回浮点数 tan(x)
print(np.abs(-3.14))  # 绝对值 返回浮点数 |x|
print(np.power(2, 3))  # 幂 返回浮点数 x^y 输出2^3=8
print(np.round(3.1415926, 2))  # 四舍五入 返回浮点数 round(x, n) n为保留小数位数
print(np.ceil(3.14))  # 向上取整 返回浮点数数 ceil(x) 返回4.0
print(np.floor(3.14))  # 向下取整 返回浮点数 floor(x) 返回3.0
print(np.isnan([np.nan, 1, 2]))  # 判断是否为nan 返回布尔值 True False False
print('=============================================')

# 统计函数 sum() mean() std() var() min() max() argmin() argmax() median() percentile()
a7 = np.array([1, 2, 3])
print(np.sum(a7))  #求和
print(np.mean(a7))  #求平均值
print(np.std(a7))  #求标准差
print(np.var(a7))  #求方差
print(np.min(a7))  #求最小值
print(np.max(a7))  #求最大值
print(np.argmin(a7))  #求最小值的索引
print(np.argmax(a7))  #求最大值的索引
print(np.median(a7))  #求中位数
print(np.percentile(a7, 60))  #求百分位数
print(np.cumsum(a7))   #求累加和
print(np.cumprod(a7))  #求累乘积
print('=============================================')

# 排序函数 sort() argsort() lexsort()
np.random.seed(0)
a1 = np.random.randint(1, 100, 10)
a2 = np. random.randint(1, 100, 10)
a1.sort()  #python内置sort()会在原数组上进行排序
print(a1)
print(np.sort(a2))  # 而numpy的sort()不会改变原数组，而是返回一个排序后的新数组
print(np.argsort(a2))  # 返回排序后的索引
print(a2)
print('=============================================')

# 比较函数 greater() less() equal() logical_and() logical_or() logical_not() where()
print(np.greater([1, 2, 3, 4, 5], 4))  # 是否大于
print(np.less([1, 2, 3, 4, 5], 4))  # 是否小于
print(np.equal([1, 2, 3, 4, 5], 4))  # 是否等于(数组与值）
print(np.equal([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))  # 是否等于(数组与数组）
print(np.logical_and([1, 0, 4, 0], [1, 2, 0, 1]))
print(np.logical_not([1, 0, 4, 0]))
print(np.logical_or([1, 0, 0, 0], [1, 2, 0, 1]))
print('=============================================')

# 检查元素是否存在一个元素为True的数组 any() all()
print(np.any([1, 0, 0, 0]))  # 是否存在一个元素为True
print(np.all([1, 0, 0, 0]))  # 是否全部元素为True
print('=============================================')

# 去重函数 unique()
np.random.seed(1)
a3 = np.random.randint(1, 100, 10)
print(a3)
print(np.unique(a3)) #去掉重复元素，且排序，并返回新数组, 不改变原数组
print(a3)
print('=============================================')

# 数组的拼接 concatenate()
a4 = a1.copy()
a5 = a2.copy()
print(np.concatenate((a1, a2)))  # 按行拼接
print('=============================================')

# 数组的分割 split()
print(np.split(a4, 5))
print(np.split(a5, [3,7]))
print('=============================================')

# 自定义函数 where(条件， 符合条件， 不符合条件)
np.random.seed(3)
a6 = np.random.randint(50, 100, 10)
print(np.where(a6 >= 60,"及格", "不及格"))
print(np.where(a6 < 60, "不及格",(np.where(a6 <= 80, "良好", "优秀"))))  # where()函数嵌套使用
# select("条件123， 返回结果123, default=默认值"))
print(np.select([a6  < 60, (60 <= a6) & (a6< 80), a6 > 80],["不及格", "良好", "优秀"], default="不在范围内"))
print('=============================================')



