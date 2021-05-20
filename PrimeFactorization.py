def factor(num):
    result = []
    x = 2
    while x * x <= num :
        if num % x == 0 :
            rTimes = 0
            while num % x == 0:
                num /= x
                rTimes += 1
            result.append((x, rTimes))
        x += 1
    if num > 1:
        result.append((num, 1))
    return result