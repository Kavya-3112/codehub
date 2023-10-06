a=int(input())
bride=list(input())
groom=list(input())
for i in bride:
    if i in groom:
        groom.remove(i)

    else:
        break
print(len(groom))
question teacher school tcs
def calculate_children(p, q, r, s):
    total_children = 0
    for length in range(p, q + 1):
        for width in range(r, s + 1):
            while length != width:
                if length > width:
                    length -= width
                else:
                    width -= length
                total_children += 1
            total_children += 1  # One more child for the remaining square
    return total_children

# Read input
p = int(input())
q = int(input())
r = int(input())
s = int(input())

# Calculate and print the total number of children
result = calculate_children(p, q, r, s)
print(result)
