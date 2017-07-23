###########input##############
lines = open("input.txt").read().split("\n")
lines.pop(len(lines) - 1)
adj_m = []
for i in lines:
    a = []
    for j in i:
        if j == '-':
            a.append(0)
        else:
            a.append(int(j))
    adj_m.append(a)
#initial adjacency matrix
print "Before \n"
print '\n'.join(''.join(str(row)) for row in adj_m)
print
for k in range(len(adj_m)):
    for i in range(len(adj_m)):
        for j in range(len(adj_m)):
            if adj_m[i][j] > adj_m[i][k] + adj_m[k][j]:
                adj_m[i][j] = adj_m[i][k] + adj_m[k][j]
print "After \n"
print '\n'.join(''.join(str(row)) for row in adj_m)
#final adjacency matrix
