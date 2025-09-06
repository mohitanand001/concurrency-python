import threading
import random
import time

class ABPrinter:
    def __init__(self):
        # Condition variable to control alternating between A and B
        self.condition = threading.Condition()
        # The flag will be dynamically set based on the first thread that runs
        self.turn = None  # None means no turn is set yet
        self.barr = threading.Barrier(3)
    
    def print_A(self):
        print("trying A")
        with self.condition:
            print("entered A condtion")
            # Wait until it's A's turn, if the turn is not set yet, set it to A
            if self.turn is None:
                self.turn = "A"
            while self.turn != "A":
                time.sleep(0.1)
                self.condition.wait()
            
            # Set the turn to B after printing A
            print("A", end="")
            self.barr.wait()
            self.turn = "B"
            self.condition.notify_all()  # Notify the other thread to run
    
    def print_B(self):
        print("trying B")
        with self.condition:
            # Wait until it's B's turn, if the turn is not set yet, set it to B
            if self.turn is None:
                self.turn = "B"
            while self.turn != "B":
                self.condition.wait()
            
            # Set the turn to A after printing B
            print("B", end="")
            self.barr.wait()
            self.turn = "A"
            self.condition.notify_all()  # Notify the other thread to run

# Instantiate the ABPrinter class
printer = ABPrinter()

# Create threads for 50 A's and 50 B's
threads = []

for _ in range(50):
    threads.append(threading.Thread(target=printer.print_A))
    threads.append(threading.Thread(target=printer.print_B))

random.shuffle(threads)

# Start all threads
for t in threads:
    t.start()

# Join all threads to ensure they complete
for t in threads:
    t.join()
