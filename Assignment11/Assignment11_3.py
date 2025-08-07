sum = 0
def sumDigits(Digit):
    global sum
    
    if Digit > 0:
        sum += (Digit%10)
        Digit = (Digit//10)
        sumDigits(Digit)        
    
    return sum

def main():
    print(sumDigits(1234))

if __name__ == '__main__':
    main()
