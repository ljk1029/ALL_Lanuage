import torch
 

def print_torch_info():
    print('pytorch version:', torch.__version__)         # pytorch版本
    print('cuda:', torch.version.cuda)        # cuda版本
    print('available:', torch.cuda.is_available()) # 查看cuda是否可用


if __name__ == '__main__':
    print_torch_info()