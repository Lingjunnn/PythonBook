'''
输入年份判断是不是闰年。
'''

# 输入年份
year = int(input('请输入年份：'))

# 验证
temp = abs(year - 2024)/4

# 结论
if temp==0:
    print('YES')
else:
    print('NO')