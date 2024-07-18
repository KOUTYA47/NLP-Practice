import numpy as np
import matplotlib.pyplot as plt

# x, y の範囲を設定
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)
Z = (1/20) * X**2 + Y**2

# グラフの作成
plt.contour(X, Y, Z, levels=np.linspace(0, 10, 50))
plt.colorbar()
plt.title(r'$f(x, y) = \frac{1}{20}x^2 + y^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
