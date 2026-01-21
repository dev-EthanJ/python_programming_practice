# threading 
import threading
import time

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working: %s\n" % i)

print("Start")

threads = []
for i in range(5):
    # long_task()
    t = threading.Thread(target=long_task) # thread 생성
    threads.append(t)

for t in threads:
    t.start() # thread 실행

for t in threads:
    t.join() # join으로 thread가 종료될때까지 대기

print("End")