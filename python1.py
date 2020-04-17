def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a**b
def divide(a,b):
    return a//b
operation = input('Operate:')
a = float(input('1st number:'))
b = float(input('2nd number:'))
if operation == '+':
    print(a,'+',b,'=',add(a,b))
elif operation =='-':
    print(a,'-',b,'=',subtract(a,b))
elif operation =='//':
    print(a,'/',b,'=',divide(a,b))
elif operation =='**':
    print(a,'*',b,'=',multiply(a,b))
else:
    print('Input is invalid')
