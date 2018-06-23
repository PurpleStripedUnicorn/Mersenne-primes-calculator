

#####

# set these variables
startat = 2282 # 2^n is the number to start at
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



good = True
y = startat
while good:
    if ch(y):
        if showshort:
            nre = "2 ^ " + str(y) + " - 1"
        else:
            nre = str(2 ** y - 1)
        print("\n\n\n\nPrime found -- "+nre)
        good = False
    else:
        if showshort:
            nre = "2 ^ " + str(y) + " - 1"
        else:
            nre = str(2 ** y - 1)
        print(nre+" checked, not prime")

    y += 1
