import timeit

def prime(max):
    global prime_numbers 

    total = []
    prime_numbers = []

    for x in range(2 , max+1):
        total.append(x)
        prime_numbers.append(x)

    for a in range(len(total)):
        for b in range(len(prime_numbers)):
            if total[a] != total[b]:
                if (total[a] % total[b] == 0) and (total[a] in prime_numbers):
                    prime_numbers.remove(total[a])
                    break

    file1 = open("primes.txt", "w")

    for iterate in range(len(prime_numbers)):
        line = str(prime_numbers[iterate])
        file1.write(line)
        file1.write("\n")

    file1.close()


def go():
    prime(100000)

time = timeit.timeit(go , number=1)

print(time)