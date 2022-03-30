row_col = input()

row = int(row_col[1])
col = int(ord(row_col[0])-ord('a') + 1)

ways = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

count = 0

for way in ways:
    after_move_row = row + way[0]
    after_move_col = col + way[1]
    if after_move_col > 0 and after_move_col <= 8 and after_move_row > 0 and after_move_row <= 8:
        count += 1

print(count)