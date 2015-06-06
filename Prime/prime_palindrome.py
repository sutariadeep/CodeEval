"""
Write a program which determines the largest prime palindrome less than 1000.

INPUT SAMPLE:

There is no input for this program.

OUTPUT SAMPLE:

Print to stdout the largest prime palindrome less than 1000.

929
"""
num = 1000

primes = [True for n in xrange(0, num)]

primes[0] = False
primes[1] = False

for i in xrange(1, int(num ** 0.5 + 1)):
    if primes[i]:
        for j in xrange(i ** 2, num, i):
            primes[j] = False

for i in xrange(999,0, -1):
    if primes[i]:
        if str(i) == str(i)[::-1]:
            print i
            break

