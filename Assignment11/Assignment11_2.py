fact = 1

def facto(n):
    global fact
    if n >= 1:
        fact *= n
        n = n-1
        facto(n)
    return  fact


def main():
    print(facto(5))

if __name__ == '__main__':
    main()
