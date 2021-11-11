# backtracking : n-Queens

count = 0
def n_queens(row, col):
    n = len(col) - 1 
    if (promising(row, col)):
        if (row == n) :
            print(col[1:n+1])
            global count
            count += 1
        else:
            for j in range(1, n+1):
                col[row + 1] = j
                n_queens(row + 1, col)

def promising(row, col):
    k = 1
    flag = True
    while (k < row and flag):
        if (col[row] == col[k] or abs(col[row] - col[k]) == (row-k)):
            flag = False
        k += 1
    return flag

n = 4
col = [0] * (n+1)
n_queens(0, col)
print(count)
