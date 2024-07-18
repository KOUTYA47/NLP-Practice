import numpy as np
import matplotlib.pyplot as plt

# 関数 f(x, y) の定義
def f(x, y):
    return (1/20) * x**2 + y**2

# 勾配ベクトルの計算
def grad_f(x, y):
    df_dx = x / 10
    df_dy = 2 * y
    return np.array([df_dx, df_dy])

# SGDによる最適化
def sgd(f, grad_f, initial_point, learning_rate, num_steps):
    path = [initial_point]
    point = initial_point

    for _ in range(num_steps):
        gradient = grad_f(point[0], point[1])
        point = point - learning_rate * gradient
        path.append(point)
    
    return np.array(path)

# 初期点、学習率、ステップ数を設定
initial_point = np.array([-7.0, 2.0])
learning_rate = 0.5
num_steps = 30

# 最適化経路の計算
path = sgd(f, grad_f, initial_point, learning_rate, num_steps)

# x, y の範囲を設定
x = np.linspace(-10, 10, 400)
y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# グラフの作成
plt.figure(figsize=(10, 8))
plt.contour(X, Y, Z, levels=np.logspace(-1, 3, 20), cmap='gray')
plt.plot(path[:, 0], path[:, 1], 'ko-', markersize=5)

# ラベルとタイトル
plt.title('SGD Optimization Path on $f(x, y) = \\frac{1}{20}x^2 + y^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

# 軸の設定
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.gca().set_aspect('equal', adjustable='box')

plt.show()
