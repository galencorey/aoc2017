input_file = open('day4input.txt', 'r')
input = input_file.read()

def is_valid_passphrase(str):
    words = str.split()
    seen = {}
    for word in words:
        if word in seen:
            return False
        seen[word] = True
    return True

def is_anagram(word1, word2):
    if (len(word1) != len(word2)):
        return False
    return ''.join(sorted(list(word1))) == ''.join(sorted(list(word2)))

def is_valid_part2_passphrase(str):
    words = str.split()
    seen = []
    for word in words:
        for seen_word in seen:
            if (is_anagram(word, seen_word)):
                return False
        seen.append(word)
    return True

num_valid_passphrases = reduce(lambda acc, str: acc + is_valid_passphrase(str), input.split('\n'), 0)
num_valid_part2_passphrases = reduce(lambda acc, str: acc + is_valid_part2_passphrase(str), input.split('\n'), 0)

print(num_valid_part2_passphrases)

# def count_valid_passphrases(str):
#     phrases = str.split('\n')
#     total = 0
#     for phrase in phrases:
#         if (is_valid_passphrase(phrase)):
#             print('valid: ', phrase)
#             total += 1
#         else:
#             print('invalid: ', phrase)
#     return total
#
#
# print(count_valid_passphrases(input))

# print(is_valid_passphrase('aa bb cc dd ee'))
# print(is_valid_passphrase('aa bb cc dd aa'))
# print(is_valid_passphrase('aa bb cc dd aaa'))
