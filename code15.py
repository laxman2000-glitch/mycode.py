def div(a,b):
    print(a/b)
def smart_dev(funt):
    def inner (a,b):
        if a <b:
            a,b= b,a
            return funt(a,b)
    return inner
div = smart_dev(div)
div (3,5)
