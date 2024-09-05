def is_prime_number(num):
    if num<=1:
        print( "{} is not a Prime Number".format(num))


    for i in range (2,num):
        if (num%i)==0:
            print("{} is not a prime number".format(num))
            return
        
    print("{} is a prime number".format(num))

num =int(input("ENTER THE NUMBER YOU WANT TO CHECK: "))
is_prime_number(num)
