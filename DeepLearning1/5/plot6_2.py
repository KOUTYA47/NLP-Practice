import numpy as np
import matplotlib.pyplot as plt

# x, y の範囲を設定
x = np.linspace(-10, 10, 20)
y = np.linspace(-10, 10, 20)
X, Y = np.meshgrid(x, y)

# 勾配ベクトルの計算
Fx = X / 10  # ∂f/∂x = x / 10
Fy = 2 * Y   # ∂f/∂y = 2y

# グラフの作成
plt.figure(figsize=(10, 8))
plt.quiver(X, Y, Fx, Fy, color='red')

# ラベルとタイトル
plt.title(r'Gradient of $f(x, y) = \frac{1}{20}x^2 + y^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
