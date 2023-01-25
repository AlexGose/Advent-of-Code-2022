

# Advent of Code 2022, Day 6
import timeit
import array
import numpy as np

def message_start_index(line):
    for index, character in enumerate(line):
        if index >= 13:
            repeat_found = False
            for i in range(13):
                if line[index-i] in line[index-13:index-i-1] or \
                        line[index-i] in line[index-i+1:index+1]:
                            repeat_found = True
                            break
            if not repeat_found:
                return index + 1


def message_start_index_set(line):
    for index in range(14, len(line)):
        if len(set(c for c in line[index-14:index])) == 14:
            return index


def message_start_index_list(line):
    """
    Same as message_start_index_array but uses a list instead of an array
    """
    i = 14
    mem = [0]*26
    excess = 0

    for ch in line[0:14]:
        pos = ord(ch) - ord('a')
        if (mem[pos] > 0): excess += 1
        mem[pos] += 1

    if (excess == 0):
        return 14

    for ch in line[14:]:
        i += 1
        pos = ord(ch) - ord('a')
        if (mem[pos] > 0): excess += 1
        mem[pos] += 1
        pos = ord(line[i-15]) - ord('a')
        if (mem[pos] > 1): excess -= 1
        mem[pos] -= 1
        if (excess == 0): break

    return i


def message_start_index_array(line):
    """
    Source for this solution:
    https://www.reddit.com/r/adventofcode/comments/zdw0u6/comment/ize9jp0/?utm_source=share&utm_medium=web2x&context=3
    """
    i = 14
    mem = array.array('I',[0]*26)
    excess = 0

    for ch in line[0:14]:
        pos = ord(ch) - ord('a')
        if (mem[pos] > 0): excess += 1
        mem[pos] += 1

    if (excess == 0):
        return 14

    for ch in line[14:]:
        i += 1
        pos = ord(ch) - ord('a')
        if (mem[pos] > 0): excess += 1
        mem[pos] += 1
        pos = ord(line[i-15]) - ord('a')
        if (mem[pos] > 1): excess -= 1
        mem[pos] -= 1
        if (excess == 0): break

    return i


def message_start_index_faster(line):
    index = 1
    prev_repeat = -1
    while index < len(line):
        repeat_index = line.find(line[index], prev_repeat+1, index)
        if repeat_index == -1 and index - prev_repeat >= 14:
            return index + 1
        
        if repeat_index > -1:
            prev_repeat = repeat_index
        index += 1


def message_start_index_bits(line):
    for index in range(len(line)-14):
        filt = 0
        for c in line[index:index+14]:
            encoded = 2 ** (ord(c) - ord('a'))
            filt = (filt ^ encoded) if (encoded & filt) == 0 else filt
        if sum(int(c) for c in np.binary_repr(filt)) == 14:
            return index + 14


def message_start_index_bits_np(line):
    one = np.uint32(0)
    for index in range(len(line)-14):
        filt = np.uint32(0)
        for c in line[index:index+14]:
            encoded = np.left_shift(one, ord(c)-ord('a'))
            if np.bitwise_and(filt, encoded) == 0:
                filt = np.bitwise_xor(filt, encoded)
        if sum(int(c) for c in np.binary_repr(filt)) == 14:
            return index + 14


if __name__ == '__main__':
    for line in open(0):
        for index, character in enumerate(line):
            if index >= 3:
                c1 = line[index-3]
                c2 = line[index-2]
                c3 = line[index-1]
                c4 = line[index]
                if not ( (c1==c2) or (c1==c3) or (c1==c4) or (c2==c3) or (c2==c4)
                        or (c3==c4)):
                    print("start of packet at:", index+1)
                    break

        print('  runtime for message_start_index:')
        print(timeit.repeat('message_start_index(line)', number=100,
            globals=globals()))
        p2 = message_start_index(line)
        print('  runtime for message_start_index_set:')
        print(timeit.repeat('message_start_index_set(line)', number=100,
            globals=globals()))
        p2set = message_start_index_set(line)
        print('  runtime for message_start_index_list:')
        print(timeit.repeat('message_start_index_list(line)', number=100,
            globals=globals()))
        p2list = message_start_index_list(line)
        print('  runtime for message_start_index_array:')
        print(timeit.repeat('message_start_index_array(line)', number=100,
            globals=globals()))
        p2array = message_start_index_array(line)
        print('  runtime for message_start_index_faster:')
        print(timeit.repeat('message_start_index_faster(line)', number=100,
            globals=globals()))
        p22 = message_start_index_faster(line)
        print('  runtime for message_start_index_bits:')
        print(timeit.repeat('message_start_index_bits(line)', number=100,
            globals=globals()))
        pbits = message_start_index_bits(line)
        print('  runtime for message_start_index_bits_np:')
        print(timeit.repeat('message_start_index_bits_np(line)', number=100,
            globals=globals()))
        pbitsnp = message_start_index_bits(line)
print("start of message at:", p2, p2set, p2list, p2array, p22, pbits, pbitsnp)
