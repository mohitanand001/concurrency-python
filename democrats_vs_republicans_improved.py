import threading
import random
import time

class Seat:

    def __init__(self):
        self.dem_or_rep = threading.Condition()
        self.count = 0
        self.turn = -1  # -1 indicates no one is currently using the seat

    def seatdem(self):
        print("trying dem")
        with self.dem_or_rep:
            print("entered dem")
            # If no one has started yet, give the seat to democrats
            if self.turn == -1:
                self.turn = 0

            # Wait until it's the democrat's turn
            while self.turn != 0:
                time.sleep(0.25)
                print("waiting dem")
                self.dem_or_rep.wait()

            # Democrat occupies the seat
            self.count += 1
            print("DEM")
            if self.count == 3:
                self.count = 0
                self.turn = -1
                print("==========")

            # Notify all waiting threads that they can check the condition
            self.dem_or_rep.notify_all()

    def seatrep(self):
        print("trying rep")
        with self.dem_or_rep:
            print("entering rep")
            # If no one has started yet, give the seat to republicans
            if self.turn == -1:
                self.turn = 1

            # Wait until it's the republican's turn
            while self.turn != 1:
                time.sleep(0.25)
                print("waiting rep")
                self.dem_or_rep.wait()

            # Republican occupies the seat
            self.count += 1
            print("REP")
            if self.count == 3:
                self.count = 0
                self.turn = -1
                print("==========")

            # Notify all waiting threads that they can check the condition
            self.dem_or_rep.notify_all()


seat = Seat()

# Create a list of threads with random choices
threads = []
for i in range(3):
    val = int((random.random() * 1000) % 2)  # Randomly choose dem or rep
    if val == 1:
        func = seat.seatdem
    else:
        func = seat.seatrep
    threads.append(threading.Thread(target=func))

# Start the threads
for t in threads:
    t.start()

# Wait for all threads to complete
for t in threads:
    t.join()

