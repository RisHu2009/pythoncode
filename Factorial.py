#Write a Python Program to Find the Factorial of a Number.
num=int(input("ENTER THE NUMBER : "))
Factorial=1
if num<0:
    print("THE FACTORIAL OF NEGATIVE NUMBERS DOES NOT EXIST: ")
elif num==0:
    print("THE FACTORIAL OF 0 IS 1")


for i in range(1,num+1):
    Factorial=Factorial*i
print("THE FACTORIAL OF {} IS ".format(num),Factorial)
