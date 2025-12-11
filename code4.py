def sas(n):
    if n == 0:
        return 1
    
    return n * sas(n-1)
    
n = int(input("give me number"))
result = sas(n)
print(result)
