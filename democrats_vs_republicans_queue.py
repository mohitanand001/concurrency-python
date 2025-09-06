import threading
import time
import random
from queue import Queue

# Function to simulate time taken by a person based on their name
def f(name):
    # Return the length of the name for simplicity, can be customized
    return len(name)

# Class representing the bathroom and managing the queue system
class Bathroom:
    def __init__(self, capacity=3):
        self.capacity = capacity
        self.democrats_in_bathroom = 0
        self.republicans_in_bathroom = 0
        self.democrat_queue = Queue()
        self.republican_queue = Queue()
        self.lock = threading.Lock()  # Ensure thread safety

    def enter_bathroom(self, person):
        with self.lock:
            # If the bathroom is empty, accept the person
            if self.democrats_in_bathroom == 0 and self.republicans_in_bathroom == 0:
                if person[0] == 'D':
                    self.democrats_in_bathroom += 1
                    print(f"{person[1]} (Democrat) enters the bathroom")
                    time.sleep(f(person[1]))
                    self.democrats_in_bathroom -= 1
                    print(f"{person[1]} (Democrat) leaves the bathroom")
                else:
                    self.republicans_in_bathroom += 1
                    print(f"{person[1]} (Republican) enters the bathroom")
                    time.sleep(f(person[1]))
                    self.republicans_in_bathroom -= 1
                    print(f"{person[1]} (Republican) leaves the bathroom")
            # Check for Democrats queue
            elif person[0] == 'D' and self.democrats_in_bathroom < self.capacity:
                self.democrats_in_bathroom += 1
                print(f"{person[1]} (Democrat) enters the bathroom")
                time.sleep(f(person[1]))
                self.democrats_in_bathroom -= 1
                print(f"{person[1]} (Democrat) leaves the bathroom")
            # Check for Republicans queue
            elif person[0] == 'R' and self.republicans_in_bathroom < self.capacity:
                self.republicans_in_bathroom += 1
                print(f"{person[1]} (Republican) enters the bathroom")
                time.sleep(f(person[1]))
                self.republicans_in_bathroom -= 1
                print(f"{person[1]} (Republican) leaves the bathroom")
            else:
                # Queue the person to wait if conditions are not met
                if person[0] == 'D':
                    self.democrat_queue.put(person)
                else:
                    self.republican_queue.put(person)

    def process_queue(self):
        # Process the waiting queues (for both Democrats and Republicans)
        while True:
            if self.democrats_in_bathroom < self.capacity and not self.democrat_queue.empty():
                person = self.democrat_queue.get()
                self.enter_bathroom(person)
            
            if self.republicans_in_bathroom < self.capacity and not self.republican_queue.empty():
                person = self.republican_queue.get()
                self.enter_bathroom(person)
            
            time.sleep(1)  # Small delay before re-checking the queue

# Thread function to simulate each person's attempt to use the bathroom
def bathroom_usage(bathroom, person):
    bathroom.enter_bathroom(person)

# Example usage:
if __name__ == "__main__":
    # Initialize the bathroom system
    bathroom = Bathroom()

    # Create a list of people with their name and political affiliation (D for Democrat, R for Republican)
    people = [
        ('D', 'Alice'),
        ('R', 'Bob'),
        ('D', 'Charlie'),
        ('R', 'David'),
        ('D', 'Eve'),
        ('R', 'Frank'),
        ('D', 'Grace'),
        ('R', 'Hank')
    ]

    # Create threads for each person
    threads = []
    for person in people:
        t = threading.Thread(target=bathroom_usage, args=(bathroom, person))
        threads.append(t)
        t.start()

    # Create a thread to process the queues
    queue_processor_thread = threading.Thread(target=bathroom.process_queue)
    queue_processor_thread.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    # Stop the queue processing thread
    queue_processor_thread.join()

