'''
读取数据为numpy格式，并保存起来
'''
import numpy as np
import math
import os 

def read_save(filename):
    '''
    功能：将TSPLIB数据文件转化为numpy对象(存储着城市网络)
    输入：文件路径
    输出：numpy对象保存地址
    '''
    #提取城市数
    filename_list = filename.split('.')
    index = None
    for i in range(len(filename_list[0])):
        ch = filename_list[0][i]
        if ch.isdigit():
            index = i
            break;
    if index == None:
        print('文件有问题')
    else:
        n = int(filename_list[0][index:])
        # print('城市数为:'.format(n))
    #建立城市网络矩阵net并赋值
    net = np.ones([n, n])*float('inf')
    point_list = []
    with open(filename, 'rt') as f:
        while True:
            lineStr = f.readline().strip()
            if lineStr == 'EOF':
                break
            lineStr_list = lineStr.split()
            if not lineStr_list[0].isdigit():
                continue
            point_list.append((float(lineStr_list[1]), float(lineStr_list[2])))
    # for i in range(len(point_list)):
    #     print(point_list[i])
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            net[i][j] = distance(point_list[i], point_list[j])
    #保存numpy对象
    filename = 'output_data/' + filename_list[0].strip().split('/')[-1] + '.npy'
    f = open(filename, 'wt')
    f.close()
    np.save(filename, net)
    return filename


def distance(point1, point2, type='EUC_2D'):
    return math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)


if __name__ == "__main__":
    # for filename in os.listdir('input_data'):
    #     filename = filename.strip()
    #     filename_list = filename.split('.')
    #     if filename_list[1] == 'tsp':
    #         filename = 'input_data/' + filename
    #         read_save(filename)
    net = np.load('output_data/rat99.npy')
    print(net)