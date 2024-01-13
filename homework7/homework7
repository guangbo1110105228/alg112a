import numpy as np

# 函數 f 的範例：平方和
def f(p):
    return np.sum(np.square(p))

# 函數 f 對變數 p[k] 的偏微分
def df(f, p, k, step=1e-5):
    p1 = p.copy()
    p1[k] = p[k] + step
    return (f(p1) - f(p)) / step

# 梯度：函數 f 在點 p 上的梯度
def grad(f, p):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k)
    return gp

# 梯度下降法
def gradient_descent(f, initial_point, learning_rate=0.01, max_iterations=1000, tolerance=1e-6):
    current_point = initial_point.copy()
    
    for iteration in range(max_iterations):
        gradient = grad(f, current_point)
        current_point -= learning_rate * gradient
        
        # 判斷是否收斂
        if np.linalg.norm(gradient) < tolerance:
            print("Converged after", iteration, "iterations.")
            break
    
    return current_point

# 測試
initial_point = np.array([1.0, 2.0, 3.0])
result = gradient_descent(f, initial_point)

print("Optimal point:", result)
print("Minimum value:", f(result))
