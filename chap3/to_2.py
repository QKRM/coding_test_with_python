n, m = map(int,input().split())

count = 0

while (n%m != 0):
    count += 1
    n -= 1
while (n != 1):
    count += 1
    n = n//m

print(count)