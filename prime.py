def prime(num):
    x = num ** 0.5
    if num != 1:
        if num != 2: # bug in range
            for i in range(2, num):
                if x * x == num :
                    return False
                elif num % i != 0: # check divisibility to all number before var num.
                    return True  # Divisibility should be != 0 to be a prime number.
                else:
                    return False 
        else:    # 2 is a prime number.
            return True
    else:  # 1 isn't a prime number.
        return False