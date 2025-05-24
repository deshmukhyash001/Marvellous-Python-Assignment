import basic,threading

def evenSum(n):
    sum = 0
    for i in n:
        if i & 1 == 0:
            sum += i
    print(sum)

def oddSum(n):
    sum = 0
    for i in n:
        if i & 1 == 1:
            sum += i
    print(sum)


def main():
    print("Enter array capacity : ")
    k = basic.tupInp(int(input()))      

    t1 = threading.Thread(target=evenSum,args=(k,))
    t1.start()
    
    t2 = threading.Thread(target=oddSum,args=(k,))
    t2.start()
if __name__ == '__main__':
    main()
