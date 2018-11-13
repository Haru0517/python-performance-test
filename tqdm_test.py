from tqdm import tqdm
from datetime import datetime
from time import time


def log_msg(message):
    """現在時刻と一緒にログを表示"""
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), message)


def without_tqdm(loop_num):
    """tqdmを使わずにループ"""
    result = 0
    for i in range(loop_num):
        result += i


def with_tqdm(loop_num):
    """tqdmを使ってループ"""
    result = 0
    for i in tqdm(range(loop_num), desc='tqdm test'):
        result += i


if __name__ == '__main__':
    loop_num = 10000000
    start_time = time()
    log_msg('Starting...')

    without_tqdm(loop_num)

    elapsed_time = time() - start_time
    log_msg(f'Finish: elapsed time is {elapsed_time}[sec]')
