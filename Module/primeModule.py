def isprime(n):
    if (n == 0):
        print(n," is Not Prime")
    elif (n == 1):
        print(n," is Not Prime")

    for i in range(2,n):
        if(n % i == 0):
            print(n," is Not Prime")
            break

    else:
        print(n," is Prime")
