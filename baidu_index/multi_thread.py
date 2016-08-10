# !/usr/bin/env python
# -*- coding:utf-8 -*-
import Queue
import sys
import requests
import threading
import time


class Worker(threading.Thread):  # 处理工作请求
    def __init__(self, work_queue, result_queue, **kwargs):
        threading.Thread.__init__(self, **kwargs)
        self.setDaemon(True)
        self.work_queue = work_queue
        self.result_queue = result_queue

    def run(self):
        while 1:
            try:
                task_key, func, args, kwargs = self.work_queue.get(False)  # get task
                res = func(*args, **kwargs)
                self.result_queue.put((task_key, res))  # put result
            except Queue.Empty:
                break


class WorkManager:  # 线程池管理,创建
    def __init__(self, num_of_workers=10):
        self.work_queue = Queue.Queue()  # 请求队列
        self.result_queue = Queue.Queue()  # 输出结果的队列
        self.workers = []
        self.init_threads(num_of_workers)

    def init_threads(self, num_of_workers):
        for i in range(num_of_workers):
            worker = Worker(self.work_queue, self.result_queue)  # 创建工作线程
            self.workers.append(worker)  # 加入到线程队列

    def start(self):
        for w in self.workers:
            w.start()

    def wait_for_complete(self):
        while len(self.workers):
            worker = self.workers.pop()  # 从池中取出一个线程处理请求
            worker.join()
            if worker.isAlive() and not self.work_queue.empty():
                self.workers.append(worker)  # 重新加入线程池中

    def add_job(self, task_key, func, *args, **kwargs):
        self.work_queue.put((task_key, func, args, kwargs))  # 向工作队列中加入请求

    def get_all_result_dict_from_queue(self):
        all_result_dict = {}
        while not self.result_queue.empty():
            task_key, result = self.result_queue.get(False)
            all_result_dict[task_key] = result
        return all_result_dict


def main():
    def download_file(url):
        return requests.get(url).text

    try:
        num_of_threads = int(sys.argv[1])
    except:
        num_of_threads = 10
    _st = time.time()
    wm = WorkManager(num_of_threads)
    print num_of_threads
    urls = ['http://www.baidu.com'] * 100
    for index, i in enumerate(urls):
        wm.add_job(index, download_file, i)
    wm.start()
    wm.wait_for_complete()
    print time.time() - _st
    all_result_dict = wm.get_all_result_dict_from_queue()
    for k, v in all_result_dict.items():
        print k, v


if __name__ == '__main__':
    main()