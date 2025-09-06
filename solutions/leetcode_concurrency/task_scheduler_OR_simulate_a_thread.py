#Implement two methods in a class, schedule() and waitUntilComplete().
#schedule() should enqueue work to be performed and should be non-blocking.
#waitUntilComplete() should block the call untill all scheduled work is completed.


class Task:

    def __init__(self, callable):
        self.callable = callable
        self.dont = False
