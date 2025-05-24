import threading,multiprocessing,time

def milli():
    k = 0
    for i in range(1,10000000):
        k += i
    print(k)
def main():
    fs = time.time()
    milli()
    
    fe = time.time()
    t1 = threading.Thread(target=milli)
    t1.start()
    te = time.time()
    p1 = multiprocessing.Process(target = milli)
    p1.start()
    pe = time.time()
    
    print("time  require for function is : ",fe - fs,"\ntime require for thread : ",te - fe,"\ntime require for process is : ",pe-te )
if __name__ == '__main__':
    main()
