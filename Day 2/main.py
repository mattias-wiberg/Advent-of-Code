with open('input') as f:
    lines = f.readlines()

# %% Silver star
depth = 0
horizontal = 0

for line in lines:
    command = line.split(' ')[0]
    position = int(line.split(' ')[1])
    if command == 'forward':
        horizontal += position
    elif command == 'down':
        depth += position
    elif command == 'up':
        depth -= position

print(depth*horizontal)

# %% Gold star
depth = 0
horizontal = 0
aim = 0

for line in lines:
    command = line.split(' ')[0]
    position = int(line.split(' ')[1])
    if command == 'forward':
        horizontal += position
        depth += aim * position
    elif command == 'down':
        aim += position
    elif command == 'up':
        aim -= position

print(depth*horizontal)

# %%
