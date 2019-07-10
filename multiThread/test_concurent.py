#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import threading
from concurrent import futures

import logging
import time

FORMAT = '%(asctime)-15s\t  %(process)s %(threadName)s %(process)s %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)

# 这是一个IO 密集型的函数，建议使用多线程
def worker(n):
    logging.info('begin to work{}'.format(n))
    time.sleep(5)
    logging.info('finisdhed{}'.format(n))
    return n

# 创建线程池，容量为3个
executor = futures.ThreadPoolExecutor(max_workers=3)

fs = []
for i in range(1):
    # 提交任务
    future = executor.submit(worker, i)
    fs.append(future)


while True:
    time.sleep(1)
    logging.info(threading.enumerate())

    flag = True
    for f in fs:
        logging.info(f.done())
        flag = flag and f.done()

    if flag:
        for f in fs:
            logging.info('the ans is {}'.format(f.result()))
        # logging.info(threading.enumerate())
        # logging.info('====================')
        executor.shutdown()
        logging.info(threading.enumerate())
        break

logging.info('--------------------')

