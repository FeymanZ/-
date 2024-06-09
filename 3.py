import numpy as np
import matplotlib.pyplot as plt

# 模拟时间t，从0到10，步长为0.1
t = np.arange(0, 10, 0.1)

# 使用piecewise函数定义兔子的位移函数
rabbit_position = np.piecewise(t, [t < 2, (t >= 2) & (t < 5), t >= 5], [lambda t: t * 10, 20, lambda t: 20 + 10 * (t - 5)])

# 乌龟的位移函数，乌龟以恒定速度爬行
turtle_position = 2 * t

# 绘制图像
plt.figure(figsize=(10, 6))

# 绘制兔子的轨迹
plt.plot(t, rabbit_position, label='兔子', linewidth=2)

# 绘制乌龟的轨迹
plt.plot(t, turtle_position, label='乌龟', linewidth=2)

# 添加标题和标签
plt.title('龟兔赛跑')
plt.xlabel('时间 (秒)')
plt.ylabel('位移 (米)')

# 添加图例
plt.legend()

# 显示网格
plt.grid(True)

# 显示图像
plt.show()
