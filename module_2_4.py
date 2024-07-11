numbers = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
k=0
for i in range(len(numbers)):
    a = numbers[i]
    b = numbers[i]
    while a>0:
        if b % a==0:
            k=k+1
        a-=1
    if k==2:
        primes.append(numbers[i])
    if k>2:
        not_primes.append(numbers[i])
    k=0
print(primes)
print(not_primes)
