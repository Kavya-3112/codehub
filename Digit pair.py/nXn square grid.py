def find_smallest_score(N, grid):
    scores = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                scores[i][j] = grid[i][j]
            elif i == 0:
                scores[i][j] = (scores[i][j - 1] // 2) + grid[i][j]
            elif j == 0:
                scores[i][j] = (scores[i - 1][j] // 2) + grid[i][j]
            else:
                scores[i][j] = min((scores[i][j - 1] // 2) + grid[i][j], (scores[i - 1][j] // 2) + grid[i][j])

    return scores[N - 1][N - 1]

# Read input
N = int(input())
grid = []
for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

# Find the smallest score
result = find_smallest_score(N, grid)
print(result)
    
