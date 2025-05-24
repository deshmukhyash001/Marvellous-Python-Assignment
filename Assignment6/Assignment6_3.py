def main():
    print("Enter a number for printing multiplication table")
    i = int(input())
    
    k = 1
    while k <= 10:
        print(f"{i} * {k} = {i*k}")
        k+=1
if __name__ == '__main__':
    main()
