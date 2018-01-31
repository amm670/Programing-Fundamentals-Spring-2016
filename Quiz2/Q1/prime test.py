#Alexandra Montgomery
#Prime Factors

def main():
    ## Determine largest and smallest prime factors of a number.
    n = int(input("Enter a positive integer: "))
    print("Largest prime factor:", extremeFactors(n) [0])
    print("Smallest primt factor:", extremeFactors(n) [1])
    print("The prime factorization is:", primeFactors(n) [:])

def extremeFactors(n):
    listOfPrimeFactors = [ ]
    f = 2
    while n > 1:
        if n // f == n / f: #True if f divides n
            listOfPrimeFactors.append(f)
            n = n // f
        else:
            f +=1
    largestPrimeFactor = max(listOfPrimeFactors)
    smallestPrimeFactor = min(listOfPrimeFactors)
    return (largestPrimeFactor, smallestPrimeFactor)

def primeFactors(n):
    factors = [ ]
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break
    return factors

main()
    
            
