# _*_ coding:utf-8 _*_
__author__ = 'wang'
__date__ = '2018/6/24 16:40'

TESTER_CYCLE = 20
GETTER_CYCLE = 20
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# API配置
API_HOST = '0.0.0.0'
API_PORT = 5555

from multiprocessing import Process
import time

from api import app
from getter import Getter
from tester import Tester


class Scheduler():
    def scheduler_tester(self,cycle=TESTER_CYCLE):
        """
        定时测试代理
        """
        tester = Tester()
        while True:
            print('测试器开始运行')
            tester.run()
            time.sleep(cycle)

    def scheduler_getter(self,cycle=GETTER_CYCLE):
        """
        定时获取代理
        """
        getter = Getter()
        while True:
            print('测试器开始运行')
            getter.run()
            time.sleep(cycle)

    def scheduler_api(self):
        """
        开启api
        """
        app.run(API_HOST,API_PORT)

    def run(self):
        print('代理池开始运行')
        if TESTER_ENABLED:
            tester_process = Process(target=self.scheduler_tester)
            tester_process.start()

        if GETTER_ENABLED:
            getter_process = Process(target=self.scheduler_getter)
            getter_process.start()

        if API_ENABLED:
            api_process = Process(target=self.scheduler_api)
            api_process.start()

if __name__ == '__main__':
    scheduler = Scheduler()
    scheduler.run()