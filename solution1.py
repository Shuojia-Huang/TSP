'''
改进模型1.0
更改了初始化信息素浓度的方式
'''
import numpy as np
import random as ra

def TSP(net):
    '''初始化'''
    n = net.shape[0]
    h = 0.1 #挥发率
    m = 3 #蚂蚁数量
    t0 = m / TanXin(n, net) #初始信息素浓度
    a = 1
    b = 2
    #存储结构
    R = np.ones([m, n+1], dtype=int) #蚂蚁路径矩阵
    T = np.ones([n, n])  #信息浓度矩阵 
    #初始化信息浓度矩阵
    sum_edge = 0
    num_edge = 0
    for i in range(n):
        for j in range(n):
            if i == j or net[i, j] == float('inf'):
                continue
            sum_edge += 1.0 / net[i, j]
            num_edge += 1;
    for i in range(n):
        for j in range(n):
            if i == j or net[i, j] == float('inf'):
                continue
            T[i, j] = num_edge * t0 * 1 / net[i, j] / sum_edge
    C = np.ones(m)        #路径长度序列
    global_best = float('inf') #全局最优值
    global_bestR = None #全局最优路径

    '''循环'''
    for turn in range(50):
        for k in range(m):  # 蚂蚁k
            for p in range(n + 1):
                if p == 0:
                    R[k][0] = ra.randint(0, n-1)
                elif p == n:
                    R[k][n] = R[k][0]
                else:
                    i = R[k][p - 1]  # 前一个结点
                    js = neighbor(n, net, i)
                    js = list(set(js) - set(R[k][:p]))  # 下一个可能节点
                    tjs = [T[i, j]**a * (1 / net[i, j])**b for j in js]
                    sum_tjs = sum(tjs)
                    pjs = [tj / sum_tjs for tj in tjs]  # 下一个可能节点的概率
                    # 轮盘算法求下一个节点j
                    r = ra.random()
                    for z in range(len(pjs)):
                        if r <= pjs[z]:
                            j = js[z]
                        else:
                            r -= pjs[z]
                    R[k][p] = j  # 把j加入k蚂蚁的路径
            C[k] = sum([net[R[k][i], R[k][i+1]] for i in range(n)])
        # 更新t
        for i in range(n):
            for j in range(n):
                T[i, j] = (1-h)* T[i, j]
                for k in range(m):
                    if j == R[k][list(R[k]).index(i)+1]:
                        T[i, j] += 1 / C[k]
        #更新全局最优值
        local_best = min(C) #局部最优值
        bestk = list(C).index(local_best) #局部最优值对应的蚂蚁编号
        if local_best < global_best:
            global_best = local_best
            global_bestR = R[bestk].copy()
            

    # '''输出'''
    # print('最短路径为：', global_best)
    # print('最短路径长度：', global_bestR)
    return global_best


def TanXin(n, net):
    R = np.ones(n+1, dtype=int)
    while True:
        for p in range(n+1):
            if p == 0:
                R[0] = ra.randint(0, n-1)
            elif p == n:
                R[n] = R[0]
            else:
                i = R[p-1]
                js = neighbor(n, net, i)
                js = list(set(js)-set(R[:p]))
                ljs = [net[i, j] for j in js]
                j = js[ljs.index(min(ljs))]
                R[p] = j
        C = sum([net[R[i], R[i+1]] for i in range(n)])
        if C != float('inf'):
            break
    return C

def neighbor(n, net, i):
    return [j for j in range(n) if j != i if net[i][j] != float('inf')]

if __name__ == '__main__':
    net = np.array([[float('inf'), 3, 1, 2],
                    [3, float('inf'), 5, 4],
                    [1, 5, float('inf'), 2],
                    [2, 4, 2, float('inf')]])
    print(TSP(net))