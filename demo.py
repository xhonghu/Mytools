# author: muzhan
# contact: levio.pku@gmail.com
import os
import sys
import time
import signal
import argparse

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset
from tqdm import tqdm
 

def train_model(duration_mins, num_gpus, verbose, size):
    duration_secs = duration_mins * 60
    data = torch.ones(size, size).to('cuda')

    class MyModel(nn.Module):
        def __init__(self):
            super(MyModel, self).__init__()
            self.fc1 = nn.Linear(size, size)

        def forward(self, x):
            return self.fc1(x)

    model = MyModel().to('cuda')
    model = nn.DataParallel(model, device_ids=list(range(num_gpus)))
    optimizer = optim.SGD(model.parameters(), lr=0.001)
    criterion = nn.MSELoss()
    
    start_time = time.time()
    current_time = start_time
    relax_time = start_time
    # 创建一个进度条
    ratio = verbose / 100  # 计算当前进度
    with tqdm(total=100) as pbar:
        pbar.set_description("Processing")
        while (current_time - start_time) < duration_secs:
            if current_time - relax_time > 300: # 每运行5分钟休息10分钟
                time.sleep(600)
                relax_time = time.time()
            else:
                optimizer.zero_grad()
                outputs = model(data)
                loss = criterion(outputs, data)
                loss.backward()
                optimizer.step()
            current_time = time.time()
            if np.round(((current_time - start_time) / 60) / duration_mins, 1) == np.round(ratio, 1):
                pbar.update(verbose)  # 更新进度条
                ratio += verbose / 100

    total_duration_hours = (current_time - start_time) / 3600
    torch.cuda.empty_cache()
    print(f"GPU RUN TIME: {total_duration_hours:.2f} hours")

 
def gpu_info():
    gpu_status = os.popen('nvidia-smi | grep %').read().split('|')
    gpu_memory = int(gpu_status[2].split('/')[0].split('M')[0].strip())
    gpu_power = int(gpu_status[1].split('   ')[-1].split('/')[0].split('W')[0].strip())
    return gpu_power, gpu_memory
 
 
def narrow_setup(interval=4):
    # 设置信号处理程序
    minu = 10080  #Duration in minutes 7 days
    gpus = 2  #Number of GPUs to use
    size = 15000  #size
    verbose = 1  #进度条: 运行时长的1%更新进度条
    gpu_power, gpu_memory = gpu_info()
    i = 0
    print('===============================================================')
    print('The Process ID is',os.getpid())
    print('Use kill -9',os.getpid(),'To Stop This Process')
    print('===============================================================')
    while gpu_memory > 1000 or gpu_power > 30:  # set waiting condition
        gpu_power, gpu_memory = gpu_info()
        i = i % 5
        symbol = 'monitoring: ' + '>' * i + ' ' * (10 - i - 1) + '|'
        gpu_power_str = 'gpu power:%d W |' % gpu_power
        gpu_memory_str = 'gpu memory:%d MiB |' % gpu_memory
        sys.stdout.write('\r' + gpu_memory_str + ' ' + gpu_power_str + ' ' + symbol)
        sys.stdout.flush()
        time.sleep(interval)
        i += 1
    train_model(minu, gpus, verbose, size)
    

 
if __name__ == '__main__':
    narrow_setup()