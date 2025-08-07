count = 1
def Patern(N):
    global count
    if N > 0:
        print("* "*count)
        count +=1
        
        Patern(N-1)
        
def main():
    Patern(7)

if __name__ == '__main__':
    main()
