import time
from contextlib import contextmanager
from time import sleep
class cm_timer_1():
    def __enter__(self):
        self.start_time = time.time()
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        end_time = time.time()
        n_time = end_time - self.start_time
        print(f'time: {n_time}')

@contextmanager
def cm_timer_2():
    start_time=time.time()
    try:
        yield
    finally:
        end_time=time.time()
        n_time=end_time-start_time
        print(f'time: {n_time}')
if __name__ =='__main__':
    with cm_timer_1():
        sleep(5.5)
    with cm_timer_2():
        sleep(5.5)
