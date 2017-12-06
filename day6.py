input_file = open('day6input.txt', 'r')
input = input_file.read().strip().split()
numerical_input = list(map(lambda s: int(s), input))

def idx_of_max(list):
    max = None
    max_idx = None
    for i in range(len(list)):
        if (max is None or list[i] > max):
            max = list[i]
            max_idx = i
    return max_idx

def redistribute(list):
    #find the largest element in that list
    max_idx = idx_of_max(list)
    max = list[max_idx]
    #set el at that idx to 0
    list[max_idx] = 0
    #redistribute one each to the rest starting with the next idx
    curr_idx = (max_idx + 1) % len(list)
    while (max > 0):
        list[curr_idx] += 1
        curr_idx = (curr_idx + 1) % len(list)
        max -= 1
    return str(list)


def count_redistributions(list):
    count = 0
    seen = []
    while (True):
        redistribute(list)
        count += 1
        if (str(list) in seen):
            #part 2
            return len(seen) - seen.index(str(list))
            # part 1
            # break
        seen.append(str(list))
     # part 1
     # return count

print(count_redistributions([0,2,7,0]))
print(count_redistributions(numerical_input))
