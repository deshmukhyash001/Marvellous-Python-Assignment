from multiprocessing import Process 
import basic

def square(n):
    k = []
    for i in range(len(n)):
        k.append(n[i]**2)
        
    print(k)
    
def main():
    k = basic.arrInp(int(input("Enter size of array : ")))
    P1 = Process(target=square,args=(k,))

    P1.start()
if __name__ == '__main__':
    main()
