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
**************************************************************************
    ques=race
N = int(input())  # Number of participants
T = int(input())  # Total time in seconds

participants = []

# Read participant data
for _ in range(N):
    data = list(map(int, input().split()))
    participants.append(data)

# Initialize a list to keep track of the number of times each participant leads
leading_count = [0] * N

# Calculate the leader at each time slice
for t in range(T):
    leader_distance = -1
    leading_indices = []

    for i in range(N):
        distance = sum(participants[i][:t+1])  # Calculate the distance covered by the participant at time t
        if distance >= leader_distance:
            if distance > leader_distance:
                leader_distance = distance
                leading_indices = [i]
            else:
                leading_indices.append(i)

    for i in leading_indices:
        leading_count[i] += 1

# Find the winner based on the leading count
winner_index = leading_count.index(max(leading_count)) + 1

# Print the winner's index
print(winner_index)
