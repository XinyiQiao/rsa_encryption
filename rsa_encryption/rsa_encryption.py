# -*- coding: utf-8 -*-

"""Main module."""

import random

first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]

# generate a random prime candidate with n bits
def nBitRandom(n):
    return random.randrange(2**(n-1)+1,2**n-1)

# low level primality test
def getLowLevelPrime(n):
    '''Generate a prime candidate divisible
      by first primes'''

    while True:
        # Obtain a random number
        prime_candidate = nBitRandom(n)

        for divisor in first_primes_list:
            if prime_candidate % divisor == 0 and divisor**2 <= prime_candidate:
                break
            # If no divisor found, return value
            else:
                return prime_candidate

def isMillerRabinPassed(miller_rabin_candidate):
    '''Run 20 iterations of Rabin Miller Primality test'''

    maxDivisionsByTwo = 0
    evenComponent = miller_rabin_candidate-1

    while evenComponent % 2 == 0:
        evenComponent >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * evenComponent == miller_rabin_candidate-1)

    def trialComposite(round_tester):
        if pow(round_tester, evenComponent,
               miller_rabin_candidate) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * evenComponent,miller_rabin_candidate)== miller_rabin_candidate-1:
                return False
        return True

    # Set number of trials here
    numberOfRabinTrials = 20
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2,
                       miller_rabin_candidate)
        if trialComposite(round_tester):
            return False
    return True

# generate a n-bit prime
def generate_prime(n):
    while True:
        prime_candidate = getLowLevelPrime(n)
        if not isMillerRabinPassed(prime_candidate):
            continue
        else:
            print("prime candidate:\n", prime_candidate, "\ngenerated")
            return prime_candidate

def encrypt(n, e, m):
    p = generate_prime(n)
    click.echo('p:', p)
    click.echo('q:', q)
    q = generate_prime(n)
    modulus = p*q
    return (m**e) % modulus

def decrypt(p, q, m):
    phi = (p-1)*(q-1)
