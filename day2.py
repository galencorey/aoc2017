input_file = open('day2input.txt', 'r')
def split_and_convert_to_ints(str):
  return list(map(lambda s: int(s), str.split()))
input = list(map(split_and_convert_to_ints, input_file.read().split('\n')))

def diff_between_largest_and_smallest(list):
  if len(list):
    largest = None
    smallest = None
    for num in list:
      if smallest is None or num < smallest:
        smallest = num
      if largest is None or num > largest:
        largest = num
    return largest - smallest
  return 0

def quotient_of_divisible(list):
  if len(list):
    sorted_list = sorted(list)
    for i in range(len(sorted_list)):
      for j in range(i + 1, len(sorted_list)):
        if (sorted_list[j]%sorted_list[i] == 0):
          return sorted_list[j] / sorted_list[i];
  return 0


def get_checksum(list, fn):
  sum = 0
  for sublist in list:
    sum += fn(sublist)
  return sum



print(get_checksum(input, diff_between_largest_and_smallest))
print(get_checksum(input, quotient_of_divisible))


# print(diff_between_largest_and_smallest([5, 1, 9, 5]))
# print(diff_between_largest_and_smallest([7, 5, 3]))
# print(diff_between_largest_and_smallest([2, 4, 6, 8]))

# print(get_checksum([[5, 1, 9, 5],[7, 5, 3],[2, 4, 6, 8]]))
