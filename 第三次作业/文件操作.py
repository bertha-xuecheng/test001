#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @Author雪成

'''
序号 部⻔ ⼈数 平均年龄 备注
1 python 30 26 单身狗
2 Linux 26 30 没对象
3 运营部 20 24 ⼥⽣多
 .......
8 通过代码，将其构建成这种数据类型：
[{'序号':'1','部⻔':Python,'⼈数':30,'平均年龄':26,'备注':'单身狗'},......]
使⽤的知识点:
1. ⽂件读取
2. 字符串
3. 字典
4. 列表     '''

f = open('a1.txt', mode='r', encoding='utf-8')
lst = []
for line in f:
    line = line.strip()
    line_list = line.split(",")
    num = line_list[0]
    ministry = line_list[1]
    count = line_list[2]
    averageage = line_list[3]
    remark = line_list[4]
    dic = {'序号': num, '部门': ministry, '人数': count, '平均年龄': averageage, '备注': remark}
    lst.append(dic)
print(lst)
f.close()
