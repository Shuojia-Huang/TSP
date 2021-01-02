'''
测试基线模型和改进模型的正确率和误差
选用数据：rand50.tsp rand75.tsp rand100.tsp
最优解：
rand50 : 5553
rand75 : 7054
rand100 : 7891
'''
import solution
import solution1
import solution2
import solution3
import numpy as np

if __name__ == "__main__":
    times = 10 #实验次数  
    filename = 'output_data/eil51.npy'
    best = 426
    net = np.load(filename)
    sum0 = 0
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for i in range(times):
        sum0 += solution.TSP(net)
        sum1 += solution1.TSP(net)
        sum2 += solution2.TSP(net)
        sum3 += solution3.TSP(net)
    e1 = ((sum0 / times) - best) / best
    e2 = ((sum1 / times) - best) / best
    e3 = ((sum2 / times) - best) / best
    e4 = ((sum3 / times) - best) / best
    print('基线模型平均相对误差:{}'.format(e1))
    print('改进模型1.0平均相对误差:{}'.format(e2))
    print('改进模型2.0平均相对误差:{}'.format(e3))
    print('改进模型3.0平均相对误差:{}'.format(e4))