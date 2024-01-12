import random

def neighbor(f, p, h):
    p1 = [p_i + random.uniform(-h, h) for p_i in p] #對每個維度進行微小的行動
    f1 = f(*p1) #計算新的目標函數
    return p1, f1

def hillClimbing(f, p, h=0.01):
    failCount = 0                    # 失敗次數歸零
    while (failCount < 10000):       # 如果失敗次數小於一萬次就繼續執行
        fnow = f(*p)                  # fxy 為目前高度
        p1, f1 = neighbor(f, p, h)
        if f1 >= fnow:               # 如果移動後高度比現在高
            fnow = f1                #   就移過去
            p = p1
            print('p=', p, 'f(p)=', fnow)
            failCount = 0            # 失敗次數歸零
        else:                        # 若沒有更高
            failCount = failCount + 1#   那就又失敗一次
    return p,fnow              # 結束傳回 （已經失敗超過一萬次了）

def f(x, y, z):
    return -1*(x**2+y**2+z**2)

hillClimbing(f, [2,1,3])