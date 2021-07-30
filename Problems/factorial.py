# factorial iterative
def fact(num):
    factorial = 1

    if num <= 1:
        return 1
    else:
        for i in range(1, num+1):
            factorial = factorial * i
        return factorial


print(fact(10))

# factorial iterative


def facto(num):
 
    if num == 1:
        return 1
    else:
       return num*facto(num - 1)



print(facto(10))
