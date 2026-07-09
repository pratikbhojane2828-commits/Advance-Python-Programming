# Required Function
def additionOfTwoNumber(a,b):
    return "sum of two numbers:",a+b

# keyword Function
def keyFunction(c,d):
    return "diffrence between two numbers:",c-d

#variable length Function
def variableLength(*s):
    return s

#default function
def defaultFunction(a,b,c=20):
    return a+b+c

result=additionOfTwoNumber(10,20)
print(result)

result1=keyFunction(d=10,c=20)
print(result1)

result2=variableLength(10,20,30,"pratik")
print(result2)

result3=defaultFunction(10,20)
print(result3)