import threading,time

def p5():
    for i in range(1,6):
        print(i)

def main():

    t1 = threading.Thread(target=p5) 
    t1.start()       

    time.sleep(1)
    
    t2 = threading.Thread(target=p5) 
    t2.start()       

    time.sleep(1)
    
    t2 = threading.Thread(target=p5) 
    t2.start()       


if __name__ == '__main__':
    main()

