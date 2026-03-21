## json学习  

>以后学了再补充(  
![Screenshot_20260321_113555.jpg](Screenshot_20260321_113555.jpg)

**json语法规则**   

1. 名称必须被双引号（“”）包括   
2. 数据间用逗号分隔  
3. 花括号保存对象   
4. 方括号保存数组   

**json数据类型**   

1. 字符串: "Simmey"   
- 必须用双引号，不能用单引号
2. 数字: 19    
- 不区分 int /float，统一叫数字
- 不能加引号（加了就变成字符串了）   
3. 布尔: true/false   
- 小写，不加引号
4. 空值: null    
- 小写，不加引号
5. 对象: {"name":"Simmey", "age":19}
- 用 {} 包裹，存放键值对  
- 键必须是双引号字符串  
- 键值之间用冒号 :
- 多个键值对用逗号 , 分隔
6. 数组: [1, 2, 3]   
- 用 [] 包裹，存放有序列表
- 里面可以放任意类型：字符串、数字、对象、数组都行
- 元素之间用逗号分隔   
    
**json常见错误类型**  

> 以后遇到了再补充
1. 字符串、键名用双引号
2. 最后不要多余逗号
3. 不能写注释
4. true/false/null 全小写
5. 数字不加引号

**json常用函数**

1. json.dumps()   
   
```python

#将Python对象编码成json字符串
import json
data = {'name':'nanbei','age':18}
print(json.dumps(data))   

#结果：
{"name": "nanbei", "age": 18}

```
2. json.loads()   

```python

#将json字符串解码成Python对象
import json
json_str = '{"name": "nanbei", "age": 18}'
print(json.loads(json_str))    

#结果：
{'name': 'nanbei', 'age': 18}

```  

> Python中的list和tuple都被转化成json的数组，
而解码后，json的数组最终被转化成Python的list的，无论是原来是list还是tuple。   

```python 

import json
data = (1,2,3,4)
data_json = [1,2,3,4]
#将Python对象编码成json字符串
print(json.dumps(data))
print(json.dumps(data_json))
a = json.dumps(data)
b = json.dumps(data_json)
#将json字符串编码成Python对象
print(json.loads(a))
print(json.loads(b))  

#结果：
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]
[1, 2, 3, 4]

```

3. json.dump()  

```python

#将Python内置类型序列化为json对象后写入文件：
import json
data = {
    'nanbei':'haha',
    'a':[1,2,3,4],
    'b':(1,2,3)
}
with open('json_test.txt','w+') as f:
    json.dump(data,f)
   
```

4. json.load()  

```python

#从文件中读取json对象，并反序列化为Python内置类型：
import json
with open('json_test.txt','r') as f:
    data = json.load(f)
    print(data)

#结果：
{'nanbei': 'haha', 'a': [1, 2, 3, 4], 'b': [1, 2, 3]}

```


     


     

