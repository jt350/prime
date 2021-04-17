"""
start = 11
end = 25

for val in range(start, end + 1):
    if val > 1:
        for n in range(2, val//2 + 2):
            if (val % n) == 0:
                break
            else:
                if n == val//2 + 1:
                    print(val)
"""

primeList = [x for x in range(11, 97+1) if all(x % y != 0 for y in range(2, x))]
print(primeList)