n = int(input())
count = 0

for i in range(1, n // 2 + 2):
    count += n % i == 0

print(n if n < 3 else count + 1)