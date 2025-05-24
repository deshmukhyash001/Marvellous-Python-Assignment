def main():

    print("How many elements you want to store in array : ")
    list1 = []

    for i in range(int(input())):
        n = int(input())
        list1.append(n)

    sum = 0
    for i in list1:
        sum += i

    print(sum)

if __name__ == "__main__":
    main()