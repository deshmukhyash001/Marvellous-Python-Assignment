count = 0
def zerosCount(N):
    global count
    Digit = 0
    if N > 0:
        Digit = N % 10
        if Digit == 0:
            count += 1
        
        zerosCount(N // 10)
    
    elif N == 0:
        return 1
    return count
    
def main():
    print(zerosCount(0))

if __name__ == '__main__':
    main()
