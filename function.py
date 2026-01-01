x=122
sqrt = (x**2)
print(sqrt)



def sqrt(x):
    sqrt= x**(0.5)
    print(sqrt)
    return sqrt

sqrt(2)
sqrt(4)
sqrt(25)


def r(x):
    a=x+10
    s=a*3
    print(s**2)
    print(r(5))







    def add_and_divide():
        total = 0
for i in range(10):
    num=int(input("enter number: "))
    total += num

    result = total / 2
    print("result", result)

    add_and_divide()