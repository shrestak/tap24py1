# Basic data types

h = "hello"
w = "world"

print(h,w)
print(h+w)

n1 = 5
# print(h+n1)

# How to concatenate str with number?
# typecasting

multilinestring = """
    str() - cast to string
    int() - cast to integer
    float() - cast to float
"""

print(h+str(n1))

# Formatted Strings

n1 = 5
n2 = 3
out = f"{n1}+{n2}={n1+n2}"
print(out)

# Logical operators
# Code block

n1=5
n2=5
if n1<n2:
    print("Lesser")
    print("<"*6)
elif n1==n2:
    print("Equal")
    print('====')
else:
    print("Greater")
    print(">"*len("Greater"))


# blocks in python use indentation
# used in if statements/functions def

f = 17.4
print(type(f))
