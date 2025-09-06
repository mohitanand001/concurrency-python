import threading

class TaskScheduler:
    def __init__(self):
        self.tasks = []  # List to hold the tasks
        self.lock = threading.Lock()  # Lock to synchronize access to the task queue
        self.condition = threading.Condition(self.lock)  # Condition to notify when all tasks are completed
        self.remaining_tasks = 0  # Count of remaining tasks that need to be completed
    
    def schedule(self, task):
        """ Enqueue a task for execution. Non-blocking method. """
        with self.lock:
            self.tasks.append(task)
            self.remaining_tasks += 1  # Increment the count of tasks
            # No need to notify here because the worker threads will take care of it

    def worker(self):
        """ Worker method to execute tasks. """
        while True:
            with self.lock:
                # If no tasks are left, exit the worker thread
                if not self.tasks:
                    return

                task = self.tasks.pop(0)  # Get the next task
                self.remaining_tasks -= 1  # Decrement the remaining task count

            # Execute the task (assumed to be a callable)
            task()

            with self.lock:
                # If no more tasks are remaining, notify the waiters
                if self.remaining_tasks == 0:
                    self.condition.notify_all()

    def waitUntilComplete(self):
        """ Block until all tasks are completed. """
        with self.condition:
            while self.remaining_tasks > 0:
                self.condition.wait()  # Wait until all tasks are completed

# Example usage:

def sample_task():
    print("Task is being executed.")

# Create TaskScheduler instance
scheduler = TaskScheduler()

# Schedule some tasks
for _ in range(5):
    scheduler.schedule(sample_task)

# Create a few worker threads to execute the tasks
threads = []
for _ in range(3):
    t = threading.Thread(target=scheduler.worker)
    t.start()
    threads.append(t)

# Block until all tasks are completed
scheduler.waitUntilComplete()

# Wait for all worker threads to finish
for t in threads:
    t.join()

print("All tasks have been completed.")

