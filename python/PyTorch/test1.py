# https://fancyerii.github.io/books/pytorch/
#

import torch
import pytorch_version
import numpy as np
import sys
sys.path.append('..')
from function_base.base_log.log import CustomLogger as mylog

# 全局logger变量
#log_obj = None


def empty():
    x = torch.empty(5, 3)
    print(x, x.size())
    x = torch.rand(5, 3)
    print(x, x.size())
    x = torch.zeros(5, 3, dtype=torch.long)
    print(x, x.size())
    x = torch.tensor([5.5, 3])
    print(x, x.size())
    x = x.new_ones(5, 3, dtype=torch.double)      # new_* methods take in sizes
    print(x, x.size())
    x = torch.randn_like(x, dtype=torch.float)    # override dtype!
    print(x, x.size())
    
    # 相加
    y = torch.rand(5, 3)
    print(x, '\n', y)
    print(x + y)
    # x和y不变
    print(torch.add(x, y))
    print(x, '\n', y)
    # x + y的结果放到result里。
    result = torch.empty(5, 3)
    torch.add(x, y, out=result) 
    print(result) 
    # 把x加到y
    y.add_(x)
    print(y)

    x = torch.randn(1)
    print(x)
    print(x.item())

def view():
    x = torch.empty(5, 3)
    #打印x的第一列
    print(x[:, 1])
    x = torch.randn(4, 4)
    y = x.view(16)
    z = x.view(-1, 8)  # -1的意思是让PyTorch自己推断出第一维的大小。
    print(x.size(), y.size(), z.size())
    print(x)
    print(y)
    print(z)

def num():
    a = torch.ones(5)
    print(a)
    b = a.numpy()
    print(b)
    a.add_(1)
    print(a)
    print(b)

    a = np.ones(5)
    b = torch.from_numpy(a)
    print(a)
    print(b)
    np.add(a, 1, out=a)
    print(a)
    print(b)

def cuda():
    if torch.cuda.is_available():
        device = torch.device("cuda")          # 一个CUDA device对象。
        y = torch.ones_like(x, device=device)  # 直接在GPU上创建tensor
        x = x.to(device)                       # 也可以使用``.to("cuda")``把一个tensor从CPU移到GPU上
        z = x + y
        print(z)
        print(z.to("cpu", torch.double)) 
    else :
        print('no have cuda')


def tran_test():
    #创建tensor时设置属性requires_grad=True，PyTorch就会记录用于反向梯度计算的信息
    x = torch.ones(2, 2, requires_grad=True)
    print(x)
    y = x + 2
    print(y)

    z = y * y * 3
    out = z.mean()
    mylog.static_log(z, out)

    a = torch.randn(2, 2)
    a = ((a * 3) / (a - 1))
    mylog.static_log(a.requires_grad)
    a.requires_grad_(True)
    mylog.static_log(a.requires_grad)
    b = (a * a).sum()
    mylog.static_log(b.grad_fn)
    logger.log(b.grad_fn)

    out.backward()
    logger.log(x.grad)

if __name__ == '__main__':
    pytorch_version.print_torch_info()
    global logger
    logger = mylog()
    # empty()
    # view()
    # num()
    # cuda()
    tran_test()