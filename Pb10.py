def fib(n):
    a=1
    b=1

    print("1 ->",a)
    print("2 ->",b)

    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(i+1,"->",c)

a = input("Scrie numarul: ")
fib(int(a))