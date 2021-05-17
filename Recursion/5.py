def uniquePath(row,col):
    #base case
    if row == 1 or col == 1: return 1
    return uniquePath(row-1,col) + uniquePath(row,col-1)

print(uniquePath(3,3))