def factors(n):
    results = []
    for k in range(1, n+1):
        if n % k == 0:
            results.append(k)
    return results

print(factors(60))
print(factors(20))
print(factors(30))
