"""
  @Author       : liujianhan
  @Date         : 21/1/26 22:49
  @Project      : DailyTinyImprovement
  @FileName     : 02_thread_daemon_join.py
  @Description  : Placeholder
"""
import time
from threading import Thread


def get_html(url):
    print('get detail html started')
    time.sleep(2)
    print('get detail html ended.')


def get_url(url):
    print('get detail url started')
    time.sleep(4)
    print('get detail url ended.')


if __name__ == '__main__':
    option = 3
    # 此处有三个线程程：主线程，t1，t2
    # # 版本1：三个线程同时运行，耗时测试不准确
    if option == 1:
        t1 = Thread(target=get_url, args=('',))
        t2 = Thread(target=get_html, args=('',))
        s1 = time.time()
        t1.start()
        t2.start()
        print(f"\nlast time: {time.time() - s1:.2f}s")

    # 版本2：主线程退出后，子线程也退出：setDaemon
    if option == 2:
        t1 = Thread(target=get_url, args=('',))
        t2 = Thread(target=get_html, args=('',))
        t1.setDaemon(True)
        t2.setDaemon(True)
        s1 = time.time()
        t1.start()
        t2.start()
        print(f"\nlast time: {time.time() - s1:.2f}s")

    # 版本3：将t1,t2阻塞执行完成后，交回控制给主线程
    if option == 3:
        t1 = Thread(target=get_url, args=('',))
        t2 = Thread(target=get_html, args=('',))
        s1 = time.time()
        t1.start()
        t2.start()
        # 阻塞主线程
        t1.join()
        t2.join()
        # 运行完之后返回主线程
        print(f"last time: {time.time() - s1:.2f}s")