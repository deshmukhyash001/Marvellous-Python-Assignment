import threading 

def first_TE():
    for i in range(1,10+1):
        if i&1 == 0:
            print(i)
            
def first_TO():
    for i in range(1,10+1):
        if i&1 == 1:
            print(i)
    
def main():
    t1 = threading.Thread(target=first_TE)
    t2 = threading.Thread(target=first_TO)
    
    t1.start()
    # t2.start()

if __name__ == '__main__':
    main()
