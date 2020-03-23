import concurrent.futures
import time
import threading

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print(f'Done Sleeping {seconds}')

t1 = threading.Thread(target=do_something, args=[1])
t2 = threading.Thread(target=do_something, args=[2])
t3 = threading.Thread(target=do_something, args=[4])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

finish = time.perf_counter()
print(f'Finished in {round(finish-start, 2)} second(s)')
