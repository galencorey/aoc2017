input_file = open('day2input.txt', 'r')
input = list(map(lambda l: l.split(), input_file.read().split('\n')))

def diff_between_largest_and_smallest(list):
  if len(list):
    largest = None
    smallest = None
    for num in list:
      num = int(num)
      if smallest is None or num < smallest:
        smallest = num
      if largest is None or num > largest:
        largest = num
    return largest - smallest
  return 0

def get_checksum(list):
  sum = 0
  for sublist in list:
    sum += diff_between_largest_and_smallest(sublist)
  return sum

print(get_checksum(input))

# print(diff_between_largest_and_smallest([5, 1, 9, 5]))
# print(diff_between_largest_and_smallest([7, 5, 3]))
# print(diff_between_largest_and_smallest([2, 4, 6, 8]))

# print(get_checksum([[5, 1, 9, 5],[7, 5, 3],[2, 4, 6, 8]]))
