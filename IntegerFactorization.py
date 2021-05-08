import prime

def integerFactorization(num):
    primeNums = (2, 3, 5, 7)
    result = []  # save our numbers
    if prime.prime(num) == False:    
        while num != 1:
            for i in primeNums:
                if num % i == 0:
                    num /= i
                    result.append(i)  # add it to result
                    break
    else:
        return "It's a prime number."
    return result  # our result