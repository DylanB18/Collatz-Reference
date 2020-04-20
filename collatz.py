def collatz(n):
    while n>1:
        print(n)
        if n % 2 == 1:
            n = n*3+1
        else:
            n = n/2
    else:
        print n

collatz(5)