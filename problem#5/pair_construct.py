def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(f):
    return f(lambda a,b : a)

def cdr(f):
    return f(lambda a,b : b)

c = cons(3,4)
print(car(c))
print(cdr(c))