# try:
#     a = 5/0
#     print(a)
# except ZeroDivisionError as e:
#     print("Exception occor",e)
#     raise
# finally:
#     print("executed always")

# try:
#     a = int(input("Enter a:"))
#     b = int(input("Enter b:"))
#     c = a/b;
#     print("a/b = %d"%c)
# except Exception:
#     print("can't divide by zero")
# else:
#     print("Hi I am else block")

# multiple Exception
try:
    a=10/0
except(ArithmeticError,IOError):
    print("Arithmetic Exception")
    raise        # reraising exception
else:
    print("Successfully Done")
