import threading
import time

def func(i):
    time.sleep(2)
    print(f"func called by thread {i}")
    return

threads = []
for i in range(10):
    t = threading.Thread(target=func, args=(i,))
    threads.append(t)
    t.start()

# join() will only block the main thread
for t in threads:
    t.join()

print("done")