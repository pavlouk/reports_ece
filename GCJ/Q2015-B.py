# Google Code Jam 2015 Qualification Round, problem 2

txtfile = open("B-large-practice.in", "r")
output_file = open("large_output.txt", "w")
T = txtfile.readline()

for i in range(int(T)):
    D = txtfile.readline()
    Diners = txtfile.readline()
    diners = Diners.split()
    diners = map(int, diners)
    max_pan = max(diners)

    for j in range(1, max(diners) + 1):
        total_moves = 0
        for k in diners:
            total_moves += (k - 1)/j
        max_pan = min(max_pan, total_moves + j)
        
    output_file.write("Case #" + str(i + 1) + ": " + str(max_pan) + '\n')

output_file.close()
txtfile.close()
