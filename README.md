- 本代码关于用蚁群算法解决TSP问题, 该算法一定程度上避免了局部最优的出现

- input_data :该目录存放TSPLIB数据集
- ouput_data :该目录存放numpy对象（城市网络）
- solution.py:基线模型
- solution1.py:改进模型1.0 (改进了信息素的初始化）
- solution2.py:改进模型2.0 （改进了信息素更新）
- solution3.py:改进模型3.0（加入了融断机制 最终模型）
- read.py:将input_data中的数据转换为numpy对象并存储于output_data中
- evaluation.py:对模型进行评估，计算它们的平均相对误差