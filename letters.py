def foo(a):
    if a:
        if a[0] in x:
            return  foo(a[1:])
        else:
            return a[0] + foo(a[1:])
    else:
        return ""

def  foot(a,t=""):
    if a:
        if a[0] in x:
            return  foot(a[1:], t = a[1:])
        else:
            return a[0] + foot(a[1:], t = a[1:])
    else:
        return ""

# TODO: Implement
    pass

if  __name__  == "__main__":
    x = ['a','e','i','o','u']

s = "the  lazy  dog  jumped  over  the  sleeping  fox quietly"
print(foo(s))
print(foot(s))