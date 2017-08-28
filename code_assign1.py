# Create a list with the first ten triangular numbers
# (see https://oeis.org/A000217)

#L = [ for i in range(10)]
L=[]
for i in range(10):
    p=(i*(i+1))/2
    L.append(p)

#print (L)
'''****************************************************************************'''
# Create a function to test if a number is prime
def is_prime(n):
    """
    Test if ``n`` is a prime.
    """
    if (n>1):
        for i in range(2,n):
            if (n%i==0):
                print ("False")
                break
        else:
            print ("True")
    else:
        print ("False")

#print (is_prime(17))
# Tests
# is_prime(2033) == False
# is_prime(2039) == True
'''**************************************************************************'''


# Create a function which returns a list of the first ten prime numbers
# greater than or equal to n

def next_ten_primes(n):
    prime1=[]
    while (len(prime1)!=10):
        for i in range(2,n):
            if (n%i==0):
                break
            else:
                prime1.append(n)
                break
        n=n+1
    return prime1

#print (next_ten_primes(75))

# Tests
# next_ten_primes(2033) == [2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111]
# next_ten_primes(2039) == [2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111]
