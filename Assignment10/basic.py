def arrInp(no_of_element):
    arr = []
    for i in range(no_of_element):
        arr.append(int(input()))
        
    return arr

def tupInp(no_of_element):
    arr = []
    for i in range(no_of_element):
        arr.append(int(input()))
        
    return tuple(arr)

def maxx(arr):
    max = 0 
    for i in arr:
        if i > max:
            max = i
            
    return max

def small(s):
    k = 0
    sm = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x''y','z')
    
    for i in s:
        if i in sm:
            k+=1 
    print(k)
    
def capital(s):
    k = 0
    up = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
    for i in s:
        if i in up:
            k+=1 
    print(k)
    
def digit(s):
    k = 0
    num = ("0","1","2","3","4","5","6","7","8","9")
    for i in s:
        if i in num:
            k+=1 
    print(k)