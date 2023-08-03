'''
输入圆的半径计算计算周长和面积。
'''

import math

R = float(input('请输入半径：'))
print('C = %.1f' % (2*R*math.pi))
print('S = %.1f' % (R*R*math.pi))

'''
debug记录：

1.
input()返回的是字符串类型的值，需要类型转换。
'''