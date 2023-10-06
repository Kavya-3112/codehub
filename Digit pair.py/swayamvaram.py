a=int(input())
bride=list(input())
groom=list(input())
for i in bride:
    if i in groom:
        groom.remove(i)

    else:
        break
print(len(groom))
question teacher school tcs********************************************************************************************
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
atm=tcs****************************************************************************************
N = int(input())
withdrawal_amount = int(input())
notes_100 = int(input())
notes_200 = int(input())
notes_500 = int(input())
notes_1000 = int(input())

# Calculate the maximum number of currency notes possible
max_notes = 0

while withdrawal_amount >= 100 and N > 0:
    if withdrawal_amount >= 1000 and notes_1000 > 0:
        withdrawal_amount -= 1000
        notes_1000 -= 1
        max_notes += 1
    elif withdrawal_amount >= 500 and notes_500 > 0:
        withdrawal_amount -= 500
        notes_500 -= 1
        max_notes += 1
    elif withdrawal_amount >= 200 and notes_200 > 0:
        withdrawal_amount -= 200
        notes_200 -= 1
        max_notes += 1
    elif withdrawal_amount >= 100 and notes_100 > 0:
        withdrawal_amount -= 100
        notes_100 -= 1
        max_notes += 1
    else:
        break

# Print the maximum number of currency notes possible
print(max_notes)
