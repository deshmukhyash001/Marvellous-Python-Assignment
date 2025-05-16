def FactSum(n): 
    sum = 0
    for i in range(n):
        if n%i == 0 :
            sum += i
    return sum

def main():
    
    print("Enter a number : ")
    num = int(input())        
    print(FactSum(num))    
    
if __name__ == "__main__":
    main()