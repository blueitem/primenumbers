#primenumbers.py
#author = Jon Gozoph
#date = 10/30/2014
# Program that, given a number, finds all primes up to that number

# for input statement
import sys
#for math.sqrt
import math


# checks if number is prime, returns true if prime, false if not
# A number is prime if it is only divisible without remainder by itself and 1
def checkPrime(number):
    for j in range(2,int(math.sqrt(number) +1)):
        if (number % j) == 0:
            return False
    return True

# takes input in the form of primenumbers.py integer , and prints out list of prime numbers below that integer.
# it doesn't actually implement the sieve of Eratosthenes, but it does use the optimization, specifically:
# 1. It only checks odd numbers
# 2. the checkPrime method only checks up to the square root of the number
def findPrimes():
    #casts to int because range needs ints to work
    upperbound = int(input("Upper boundary? "))

    # to prevent an input of 1 or a negative number having 2 show up as a prime
    if (upperbound < 2):
        print "No primes exist before",

    # 0 and 1 are not prime by definition, so starts at 3
    # 2 is only even prime, printed outside loop so loop only has to check odd numbers.
    print 2,
    for i in range(3, upperbound, 2):
        if checkPrime(i):
            print ",",
            print i,
# I don't entirely understand this, but it looks like it can set a "main"' method to be used in the same way
# that main is used in Java.
if __name__ == "__main__":
    findPrimes()



