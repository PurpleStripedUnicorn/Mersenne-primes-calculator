

#####

# set these variables
check = 1203 # 2^n is the number to check
showshort = True # show 2^x instead of entire number

#####



import math

def ch(n):
    # get primes
    po = n
    num = 2 ** po - 1

    lucseq = po - 1
    i = 2
    curluc = 4
    curpers = 0
    while i <= lucseq:
        curluc = curluc ** 2 - 2
        curluc = curluc % num
        i += 1

        # percentage done indicator
        floorpers = math.floor(i / (lucseq + 1) * 100)
        if (floorpers != curpers):
            print(str(floorpers)+"% done, "+str(i)+" operations done")
            curpers = floorpers


    if curluc == 0:
        return True
    else:
        return False



good = True
y = check
while good:
    if ch(y):
        if showshort:
            nre = "2 ^ " + str(y) + " - 1"
        else:
            nre = str(2 ** y - 1)
        print("\n\n\nPrime found -- "+nre)
    else:
        if showshort:
            nre = "2 ^ " + str(y) + " - 1"
        else:
            nre = str(2 ** y - 1)
        print("\n\n\n"+nre+" checked, not prime")

    good = False
    y += 1
