def addition():
    n=int(input())
    lst=[]
    for i in range(n):
        a=int(input())
        lst.append(a)
    sum=0
    for i in lst:
        sum+=i
    return sum
result=addition()
print(result)




    


