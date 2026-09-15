print(" |=== Welcome in the great calclator ===| ")

def p():
    print("+ = ",num1 + num2)

def s():
    print("- = ",num1 - num2)

def k():
    print("/ = ",num1 / num2)

def d():
    print("* = ",num1 * num2)

num1 = float( input("write number 1 : ") )
c = str( input("write ( - , + , * , / ) : ") )
num2 = float( input("write number 2 : ") )

if c == "+":
    p()
elif c == "-":
    s()
elif c == "/":
    k()
elif c == "*":
    d()
else:
    print(" Nothing!! ")
