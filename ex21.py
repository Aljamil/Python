def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

def floatOperate1(w,x,y,z):
    return subtract(add(w, divide(x, y)), z)

def floatOperate2(w,x,y,z):
    return w + x / y - z

print "Let's do some math with just functions!"
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand?"

a = float(raw_input('Enter num1: '))
b = float(raw_input('Enter num2: '))
c = float(raw_input('Enter num3: '))
d = float(raw_input('Enter num4: '))

print "USING OPERATION1: " 
print floatOperate1(a,b,c,d)
print "USING OPERATION2: "
print floatOperate2(a,b,c,d)
