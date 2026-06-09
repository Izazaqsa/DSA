num = int (input ('enter number : '))
def prime (num):
    if num <= 1 :
        print ("is not prime number")
    else :
        is_prime = True
        for i in range (2, num ):
            if (num % i == 0 ):
                is_prime = False
        if is_prime :
            print ("the number is prime")
        else :
            print ("the number is not a prime")

prime (num)
