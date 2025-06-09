k = 1
def numbers(n):
    global k
    if k <=n:
        print(k)
        k+=1
        numbers(n)
    
def main():
    print("Enter a number : ")
    k = int(input())
    
    numbers(k)
    
if __name__ == '__main__':
    main()
