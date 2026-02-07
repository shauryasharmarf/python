num=int(input("Enter a number: "))
def fact_rec(num):
    if num==1:
        return 1
    else:
        factorial=num*fact_rec(num-1)
        return factorial
result=fact_rec(num)
print("The factorial of",num,"is",result)