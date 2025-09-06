import threading
import random
import time

class TaskScheduler:

    def __init__(self):
        self.count_lock  = threading.Condition()
        self.count = 0

    def submit(self, func, *args, **kwargs):
        try:
            t = threading.Thread(target=self._do_work, args=(func, args, kwargs))
            t.start()
        except Exception as e:
            print(e)
            return e
        finally:
            with self.count_lock:
                self.count +=1

    def _do_work(self, func, *args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(e)
            return e
        finally:
            with self.count_lock:
                self.count-=1
                if self.count == 0:
                    self.count_lock.notify_all()

    def waitTillFinish(self):
        with self.count_lock:
            self.count_lock.wait_for(
                    lambda: self.count == 0)
            print("finished all")
            self.count_lock.notify_all()


def f1(*args, **kwargs):
    time.sleep(1)
    print('starting job ', args[0])
    time.sleep(1)
    print('finishing job', args[0])




ts  = TaskScheduler()
N = 20
for i in range(N):
    
    ts.submit(f1, i)
    print("submitted", i)


ts.waitTillFinish()
print("done all")

