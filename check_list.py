

#####

# set these variables
checks = range(3, 500) # check all numbers in a given range (numbers are 2^n)
showshort = True # show 2^x instead of entire number

#####



def ch(n):
    # get primes
    po = n
    num = 2 ** po - 1

    lucseq = po - 1
    i = 2
    curluc = 4
    while i <= lucseq:
        curluc = curluc ** 2 - 2
        curluc = curluc % num
        i += 1

    if curluc == 0:
        return True
    else:
        return False





pl = []

for y in checks:
    if ch(y):
        if showshort:
            nre = str(y)
        else:
            nre = str(2 ** y - 1)
        print(nre+": prime")
        pl.append(y)
    else:
        if showshort:
            nre = str(y)
        else:
            nre = str(2 ** y - 1)
        print(nre+": not prime")

print("\n\n\n\nFound " + str(len(pl)) + " primes")
if len(pl) > 0:
    print("\nPrimes found:")
    for i in pl:
        if showshort:
            print("--- 2 ^ " + str(i) + " - 1")
        else:
            nn = str(2 ** i - 1)
            print("--- " + nn)
