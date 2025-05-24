import threading
def num():
    for i in range(1,51):
        print(i)

def rev():
    for i in range(50,0,-1):
        print(i)
        
def main():
    t1 = threading.Thread(target=num)
    t2 = threading.Thread(target=rev)
    
    t1.start()
    t1.join()
    
    t2.start()
    t2.join()

if __name__ == '__main__':
    main()
