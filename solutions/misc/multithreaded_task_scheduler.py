import threading
import time
from collections import deque

class TaskScheduler:
    def __init__(self):
        self.task_queue = deque()  # Holds references to running threads
        self.lock = threading.Lock()  # Ensures thread-safe operations
        self.condition = threading.Condition(self.lock)  # Used to signal completion

    def schedule(self, func, *args, **kwargs):
        """Schedules a task for execution and returns immediately."""
        thread = threading.Thread(target=self._wrap_task, args=(func, *args), kwargs=kwargs,)
        with self.lock:
            self.task_queue.append(thread)
        thread.start()  # Start execution asynchronously

    def _wrap_task(self, func, *args, **kwargs):
        """Executes the function and removes it from the queue when finished."""
        try:
            func(*args, **kwargs)
        finally:
            with self.lock:
                self.task_queue.popleft()  # Remove completed task
                if not self.task_queue:
                    self.condition.notify_all()  # Notify waiting threads

    def waitUntilComplete(self):
        """Waits until all scheduled tasks have completed execution."""
        with self.condition:
                self.condition.wait_for(
                        lambda: len(self.task_queue) == 0)
                self.condition.notify_all()

# Example Usage
if __name__ == "__main__":
    def work(n):
        print(f"Task {n} started")
        time.sleep(2)
        print(f"Task {n} completed")

    scheduler = TaskScheduler()

    # Scheduling multiple tasks
    for i in range(5):
        scheduler.schedule(work, i)

    print("All tasks scheduled. Now waiting for completion.")

    scheduler.waitUntilComplete()
    print("All tasks completed.")

