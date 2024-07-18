import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# x, y の範囲を設定
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)
Z = (1/20) * X**2 + Y**2

# グラフの作成
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 3Dの表面をプロット
ax.plot_surface(X, Y, Z, cmap='viridis')

# ラベルとタイトル
ax.set_title(r'$f(x, y) = \frac{1}{20}x^2 + y^2$')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')

plt.show()
