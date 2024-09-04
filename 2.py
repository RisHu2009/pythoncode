#Write a Python program to swap two variables.

a=int(input("ENTER THE FIRST VARIABLE:(a)  "))
b=int(input("ENTER THE SECOND VARIABLE:(b)  "))
print(f"ORIGINAL VALUES: a={a}, b={b}")
temp=a
a=b
b=temp
print(f"SWAPPED VALUES: a={a}, b={b}")


