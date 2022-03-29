target = int(input())

hour, minute, second = 0,0,0

count = 0

for i in range(hour + 1):
    for j in range(minute):
        for k in range(second):
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)