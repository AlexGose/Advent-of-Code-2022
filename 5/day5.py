p1 = ""
p2 = ""

stacks = [["N","B","D","T","V","G","Z","J"],["S","R","M","D","W","P","F"],["V","C","R","S","Z"],["R","T","J","Z","P","H","G"],["T","C","J","N","D","Z","Q","F"],["N","V","P","W","G","S","F","M"],["G","C","V","B","P","Q"],["Z","P","B","N"],["W","P","J"]]

stacks2 = [["N","B","D","T","V","G","Z","J"],["S","R","M","D","W","P","F"],["V","C","R","S","Z"],["R","T","J","Z","P","H","G"],["T","C","J","N","D","Z","Q","F"],["N","V","P","W","G","S","F","M"],["G","C","V","B","P","Q"],["Z","P","B","N"],["W","P","J"]]

temp_stack=[]

for line in open(0):
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


print('Part 1')
for k in range(len(stacks)):
    p1 += stacks[k].pop()
print(p1)
print('Part 2')
for k in range(len(stacks2)):
    p2 += stacks2[k].pop()
print(p2)

