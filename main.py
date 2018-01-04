"""this is a test"""

def _add(_a, _b):
    return _a + _b

print "Hello World"
A = 1
print A
B = 2
print A + B
print _add(A, B)

X = 1
if X == 1:
    print "true"
else:
    print "false"

for I in range(0, 100):
    print I

EXIT = ' '
while EXIT != 'q':
    LHS = int(raw_input("Insert a value for the lhs: "))
    RHS = int(raw_input("Insert a value for the rhs: "))
    SIGN = raw_input("Math operation you want to perform add, sub, mult, div: ")
    if SIGN == "add":
        print LHS + RHS
    elif SIGN == "sub":
        print LHS - RHS
    elif SIGN == "mult":
        print LHS * RHS
    elif SIGN == "div":
        print LHS / RHS
    EXIT = raw_input("Press any key to use again or q to exit")