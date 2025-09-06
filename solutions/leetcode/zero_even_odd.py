#https://www.lintcode.com/problem/2090/

import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.turn = 0
        self.one_or_two = 2
        self.curr = 0
        self.turn_lock = threading.Condition()


	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            with self.turn_lock:
                self.turn_lock.wait_for(
                    lambda: self.turn == 0
                )
                #print(0, self.turn)
                if self.one_or_two == 2:
                    self.one_or_two = 1
                else:
                    self.one_or_two = 2
                self.turn = self.one_or_two
                printNumber(0)
                self.curr +=1
                self.turn_lock.notify_all()
                #from zero_even_odd import ZeroEvenOdd



    def even(self, printNumber: 'Callable[[int], None]') -> None:

        for i in range(self.n//2):
            with self.turn_lock:
                #print(2, self.turn)
                self.turn_lock.wait_for(
                    lambda: self.turn == 2
                )
                self.turn = 0
                printNumber(self.curr)
                self.turn_lock.notify_all()




    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range((self.n + 1)//2):
            with self.turn_lock:
                self.turn_lock.wait_for(
                    lambda: self.turn == 1
                )
                #print(1, self.turn)
                self.turn = 0
                printNumber(self.curr)
                self.turn_lock.notify_all()


