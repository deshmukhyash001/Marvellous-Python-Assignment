import threading,basic


def main():
    print("Enter a string :  ")        
    k = input()
    
    t1 = threading.Thread(target=basic.small,args=(k,))
    t1.start()

    t2 = threading.Thread(target=basic.capital,args=(k,))
    t2.start()
    
    t3 = threading.Thread(target=basic.digit,args=(k,))
    t3.start()
if __name__ == '__main__':
    main()
