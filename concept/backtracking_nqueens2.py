def check(current_candidate, candidate_col):
    current_row = len(current_candidate)
    for row in range(current_row):
        if current_candidate[row] == candidate_col or abs(current_candidate[row] - candidate_col) == current_row - row:
            return False
    return True


def dfs(N, current_row, current_candidate, result):
    if current_row == N:
        result.append(current_candidate[:])
        return

    for candidate_col in range(N):
        if check(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            dfs(N, current_row + 1, current_candidate, result)
            current_candidate.pop()


def solve_n_queens(N):
    result = []
    dfs(N, 0, [], result)
    return len(result)

N = int(input())
print(solve_n_queens(N))