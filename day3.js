def manhattan_distance_in_spiral(num):
  #the current num (as we count up)
  curr = 1

  #number of steps to the left from center
  left = 0

  #number of steps up from center
  up = 0


  curr_dist_in_curr_direction = 0
  total_dist_in_curr_direction = 1

  #an index
  curr_direction = 0

  #to look up the plain english version of the direction (so i can follow my own crazy logic)
  directions = ['right', 'up', 'left', 'down']
  while (curr < num):
    #increment curr
    curr += 1

    #go one step in curr direction
    curr_dist_in_curr_direction += 1

    #increment left or up
    if (directions[curr_direction] == 'right'):
      left -= 1
    elif (directions[curr_direction] == 'up'):
      up += 1
    elif (directions[curr_direction] == 'left'):
      left += 1
    elif (directions[curr_direction] == 'down'):
      up -= 1

    #if curr_dist_in_curr_direction == total_dist_in_curr_direction change directions
    if(curr_dist_in_curr_direction == total_dist_in_curr_direction):
      curr_direction = (curr_direction + 1) % 4
      curr_dist_in_curr_direction = 0

    #if curr_direction is right or left, add one to total_dist_in_curr_direction
    if(directions[curr_direction] == 'right' or directions[curr_direction] == 'left'):
      total_dist_in_curr_direction += 1

    return abs(up) + abs(left)

print(manhattan_distance_in_spiral(12))
