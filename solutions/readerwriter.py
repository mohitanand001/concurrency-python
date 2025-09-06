import threading
import time
import random

class ReaderWriter:
    def __init__(self):
        self.resource = 0  # Shared resource
        self.reader_lock = threading.Lock()  # Lock to protect the reader count
        self.writer_lock = threading.Lock()  # Lock to protect the shared resource for writing
        self.reader_count = 0  # Number of active readers

    def read(self):
        # Reader section
        with self.reader_lock:
            self.reader_count += 1
            if self.reader_count == 1:
                # First reader locks the writer lock to prevent writing while reading
                self.writer_lock.acquire()

        print(f"Reader {threading.current_thread().name} is reading the resource: {self.resource}")
        time.sleep(random.uniform(0.5, 1.5))  # Simulate reading operation

        with self.reader_lock:
            self.reader_count -= 1
            if self.reader_count == 0:
                # Last reader releases the writer lock
                self.writer_lock.release()

    def write(self):
        # Writer section
        print(f"Writer {threading.current_thread().name} is writing to the resource.")
        self.writer_lock.acquire()  # Exclusively acquire writer lock
        self.resource += 1  # Modify the shared resource
        print(f"Writer {threading.current_thread().name} updated the resource to {self.resource}")
        time.sleep(random.uniform(0.5, 1.5))  # Simulate writing operation
        self.writer_lock.release()  # Release the writer lock after writing

def reader_task(rw):
    rw.read()

def writer_task(rw):
    rw.write()

if __name__ == "__main__":
    rw = ReaderWriter()

    # Create multiple reader and writer threads
    threads = []
    for i in range(5):
        threads.append(threading.Thread(target=reader_task, args=(rw,), name=f"Reader-{i+1}"))
    for i in range(3):
        threads.append(threading.Thread(target=writer_task, args=(rw,), name=f"Writer-{i+1}"))

    # Shuffle the order of threads so they start randomly
    random.shuffle(threads)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print("All tasks completed.")

