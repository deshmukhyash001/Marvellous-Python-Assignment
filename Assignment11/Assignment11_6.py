Sum = 0
def NSum(num):
    
    global Sum
    if num>0:
        Sum +=num
        NSum(num-1)
        
    return Sum
        
def main():
    print(NSum(5))

if __name__ == '__main__':
    main()
