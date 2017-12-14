input_file = open('day10input.txt', 'r')
input = input_file.read().strip().split(',')

def tie_one_knot(nums, length, start_pos):
    end_pos = start_pos + length;
    if (end_pos < len(nums)):
        part_to_flip = nums[start_pos:end_pos]
        flipped = part_to_flip[::-1]
        return nums[:start_pos]+flipped+nums[end_pos:]
    else:
        end_pos -=len(nums)
        part_to_flip = nums[start_pos:] + nums[:end_pos]
        flipped = part_to_flip[::-1]
        return flipped[len(flipped) - end_pos:]+nums[end_pos:start_pos] + flipped[:len(flipped) - end_pos]

# print(tie_one_knot([0,1,2,3,4], 3, 0))
# print(tie_one_knot([0,1,2,3,4,5], 3, 4 ))
#


def do_knots(lengths):
    current_position = 0
    skip_size = 0
    nums = list(range(256))
    for length in lengths:
        l = int(length)
        nums = tie_one_knot(nums, l, current_position)
        current_position = (current_position + skip_size + l) % len(nums)
        skip_size += 1
    return nums[0] * nums[1]

print(do_knots(input))
