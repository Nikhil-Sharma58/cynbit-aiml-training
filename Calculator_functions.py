def add(a,b):
    return a+b
def sub(c,d):
    return c-d
def mul(e,f):
    return e*f
def div(g,h):
    if h==0:
        return "Error! Division by zero is not possible"
    return g/h

print("Addition:",add(6,8))
print("Subtraction:",sub(5,2))
print("Multiplication:",mul(22,5))
print("Division:",div(10,2))