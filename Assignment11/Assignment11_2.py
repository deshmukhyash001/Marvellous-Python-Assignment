Fact = 1
def Factorial(num):
    
    global Fact
    if num>0:
        Fact *=num
        Factorial(num-1)
        
    return Fact
        
def main():
    print(Factorial(5))

if __name__ == '__main__':
    main()
