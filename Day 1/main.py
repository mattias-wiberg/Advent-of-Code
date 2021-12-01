with open('input') as f:
    lines = f.readlines()


def get_increases(scans) -> int:
    increases = 0
    # Part 1
    for i in range(1, len(scans)):
        if scans[i-1] < scans[i]:
            increases += 1
    return increases


scans = list(map(int, lines))

# Part 1
print(get_increases(scans))

# Part 2
sums = []
for i in range(0, len(scans)-2):
    sums.append(sum(scans[i:i+3]))

print(get_increases(sums))
