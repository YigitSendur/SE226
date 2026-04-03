def factorial(x: int)->int:
    if x<0:
        return "Negatif!!!!!!"
    if x==1 or x==0:
        return 1
    return x*factorial(x-1)

print(factorial(3))

term= lambda x,i : (x**(2*i))/factorial(2*i)
print(term(3,2))

def exp_x(x:int,n:int)->float:
    total=0.0
    for i in range(n):
        total +=(-1)**i * term(x,i)
    return total
print(exp_x(3,2))

sum=0

def geometric_sum(n,r):
    global sum

    sum+=n**r

    if n<0:
        return
    geometric_sum(n-1,r)

geometric_sum(3,2)
print(sum)