import threading
import time


class MyThread(threading.Thread):
    def __init__(self, name, counter, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
        self.delay = delay

    def run(self):
        print(f"Поток {self.name} запущен")
        self.timer(self.name, self.counter, delay=1)
        print(f"Поток {self.name} завершен")

    def timer(self, name, counter, delay):
        while counter:
            time.sleep(delay)
            print(f"{self.name} {time.ctime(time.time())}\n")
            counter -= 1


thread1 = MyThread('thread1', 10, 1)
thread2 = MyThread("thread2", 5, 2)
thread1.start()
thread2.start()
