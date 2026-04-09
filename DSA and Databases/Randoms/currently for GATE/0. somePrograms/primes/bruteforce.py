# else clause of for loop
print('PRIMES:', end=' ')
for n in range(2, 30):
    for x in range(2, n):
        if n % x == 0:
            # print(n, 'equals', x, '*', n//x, end=', ')
            break
    else:
        # loop fell through without finding a factor
        print(n, end=',' if n+1 < 30 else '\n')
