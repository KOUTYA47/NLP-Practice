import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# クラスのパラメータ
mu1, sigma1 = 2, 1  # C1の平均と標準偏差
mu2, sigma2 = 5, 1  # C2の平均と標準偏差

# x軸の範囲
x = np.linspace(-1, 8, 1000)

# 確率密度関数
p_x_C1 = norm.pdf(x, mu1, sigma1)
p_x_C2 = norm.pdf(x, mu2, sigma2)

# 事前確率
P_C1 = 0.5
P_C2 = 0.5

# 事後確率の計算（この例では単純化しています）
P_C1_x = p_x_C1 * P_C1
P_C2_x = p_x_C2 * P_C2

# 正規化（この例では既にP_C1とP_C2が等しいため省略）

# 描画
plt.figure(figsize=(10, 6))
plt.plot(x, p_x_C1, label='$p(x|C_1)$', color='blue')
plt.plot(x, p_x_C2, label='$p(x|C_2)$', color='red')

# 決定境界
decision_boundary = (mu1 + mu2) / 2
plt.axvline(decision_boundary, color='green', linestyle='--', label='Decision Boundary')

# 誤分類領域のハッチング
plt.fill_between(x, 0, p_x_C1, where=(x > decision_boundary), color='blue', alpha=0.3)
plt.fill_between(x, 0, p_x_C2, where=(x < decision_boundary), color='red', alpha=0.3)

# ラベルと凡例
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Probability Density Functions with Decision Boundary')
plt.legend()
plt.grid(True)
plt.show()
