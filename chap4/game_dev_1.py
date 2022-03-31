m,n = map(int,input().split())

x, y, direction = map(int,input().split())

maps = []
visit = []
for i in range(n):
    maps.append(list(map(int, input().split())))
    visit.append(0)

ways = [(-1,0),(0,1),(1,0),(0,-1)]