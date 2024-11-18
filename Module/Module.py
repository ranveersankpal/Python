def add(a,b):
    sum=a+b
    print("Addition Is : ",sum)

def sub(a,b):
    sum=a-b
    print("Substraction Is : ",sum)

def mul(a,b):
    sum=a*b
    print("Multiplication Is : ",sum)

def div(a,b):
    sum=a/b
    print("Division Is : ",sum)

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print("Factorial of",n ,"is : ", fact)


# def fibbo(n):
#     for i in range (1,n+1):
#         if(i==0 || i==1):
#             print(i)

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



