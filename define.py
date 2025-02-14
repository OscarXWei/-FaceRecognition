K = 3
# 网络放缩系数
NET_SCALE = 8
# 3种滑窗比例，因为RESNET101不算最后一层池化层后，映射为1:32，将最大池化步长改为1后，映射为1:8
ANTHORS_TYPE_NUM = 3
ANTHORS_TYPIES = [] # ANTHORS_TYPIES[NUM][0] -> 宽
for i in range(ANTHORS_TYPE_NUM):
    ANTHORS_TYPIES.append([NET_SCALE*K*2**i,NET_SCALE*K*2**i])
    ANTHORS_TYPIES.append([ANTHORS_TYPIES[i*3][0]*2,ANTHORS_TYPIES[i*3][1]])
    ANTHORS_TYPIES.append([ANTHORS_TYPIES[i*3][0],ANTHORS_TYPIES[i*3][1]*2])
ANTHORS_SIZE = NET_SCALE * K
# 正例IOU
IOU_POSITIVE = 0.5
# 处理图像最小要求高度
MIN_TRAIN_PIC_HEIGHT = 2**ANTHORS_TYPE_NUM * NET_SCALE * K
# 处理图像最小要求宽度
MIN_TRAIN_PIC_WIDTH = 2**ANTHORS_TYPE_NUM * NET_SCALE * K 

DEBUG = True