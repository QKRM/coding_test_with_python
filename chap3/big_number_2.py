n,m,k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

result = 0

body = ((first * k) + second) * (m//k)
tail = m%(k+1)*first

result = body + tail

print(result)