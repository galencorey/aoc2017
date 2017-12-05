input_file = open('day5input.txt', 'r')
input = input_file.read().strip().split('\n')
numerical_input = list(map(lambda s: int(s), input))

def traverse_maze(maze):
    curr_idx = 0
    total_steps = 0
    while(curr_idx >= 0 and curr_idx<len(maze) ):
        total_steps +=1
        step_dist = maze[curr_idx]
        maze[curr_idx] += 1
        curr_idx += step_dist
    return total_steps

def traverse_maze_part_2(maze):
    curr_idx = 0
    total_steps = 0
    step_dist = maze[curr_idx]
    while(curr_idx >= 0 and curr_idx<len(maze) ):
        total_steps +=1
        step_dist = maze[curr_idx]
        if (maze[curr_idx] < 3):
            maze[curr_idx] += 1
        else:
            maze[curr_idx] -= 1
        curr_idx += step_dist
    return total_steps

# print(traverse_maze_part_2([0, 3,  0,  1,  -3,]))
# print(traverse_maze(numerical_input))
print(traverse_maze_part_2(numerical_input))
