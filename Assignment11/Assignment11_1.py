count = 1
def printN(N):
    
    global count
    if count<=N:
        print(count)
        count +=1
        printN(N)

def main():
    printN(4)


if __name__ == '__main__':
    main()
