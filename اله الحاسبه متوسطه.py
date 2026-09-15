num1 =  float(input ("الرقم الاول : ") )
c1 =    str(input ("ماهي عمليتك : ") )
num2 =  float(input ("الرقم الثاني : ") )
if c1 == "*":
    print(num1 * num2);
elif c1 == "/":
    print(num1 / num2);
elif c1 == "-":
    print(num1 - num2);
elif c1 == "+":
    print(num1 + num2);
elif c1 == "%":
    print(num1 % num2);
else:
    print("يوجد شيء كتبته انت خاطئ = ",c1);
