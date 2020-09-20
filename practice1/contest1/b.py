def is_prime(k):
    i = 2

    while i * i <= k:
        if k % i == 0:
            return False
        i += 1

    return True

print("YES" if is_prime(int(input())) else "NO")
