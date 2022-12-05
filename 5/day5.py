

def parse_crate_labels(text: str):
    lines = text.strip('\n').split('\n')
    num_rows = len(lines)
    num_cols = (len(lines[0]) - 3) // 4 + 1
    crate_labels = [['' for i in range(num_cols)] for j in range(num_rows)]
    for row, line in enumerate(lines):
        for col in range(num_cols):
            crate_labels[row][col] = line[1 + 4 * col]
            col += 1
    return crate_labels


def get_stacks(crate_labels):
    num_rows = len(crate_labels)
    num_cols = len(crate_labels[0])
    stacks = [[] for i in range(num_cols)]
    for row in range(num_rows - 1, -1, -1):
        for col in range(num_cols):
            if crate_labels[row][col] != ' ':
                stacks[col].append(crate_labels[row][col])
    return stacks


if __name__ == "__main__":
    p1 = ""
    p2 = ""
    raw_crate_data = ""
    stacks_done = False
    stacks = []
    stacks2 = []

    temp_stack=[]
    for line in open(0):
        if not stacks_done and line.startswith('move'):
            labels = parse_crate_labels(raw_crate_data)
            stacks = get_stacks(labels)
            stacks2 = [[] for i in range(len(stacks))]
            for i in range(len(stacks)):
                stacks2[i] = stacks[i].copy()

            stacks_done = True

        if line.startswith("move"):
            i, f, t = list(map(int, line
                .replace('move','')
                .replace('from',' ')
                .replace('to',' ')
                .split()))
            for j in range(i):
                crate = stacks[f-1].pop()
                stacks[t-1].append(crate)

                crate2 = stacks2[f-1].pop()
                temp_stack.append(crate2)
            for j in range(i):
                crate2 = temp_stack.pop()
                stacks2[t-1].append(crate2)
        elif line.startswith('  ') or line.startswith('['):
            raw_crate_data += line

    print('Part 1')
    for k in range(len(stacks)):
        p1 += stacks[k].pop()
    print(p1)
    print('Part 2')
    for k in range(len(stacks2)):
        p2 += stacks2[k].pop()
    print(p2)
