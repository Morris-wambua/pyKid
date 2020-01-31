"""
Write and save a program to generate and print squares of numbers
between 1 and 100. The output should be in eight right justified
columns
"""

for i in range(1, 26):
    print('{0:5d} {1:5d} {2:6d} {3:6d} {4:6d} {5:6d} {6:6d} {7:6d}'.format(i, i * i, (i + 25), ((i + 25) * (i + 25)), (i + 50), ((i + 50) * (i + 50)),
          (i + 75), ((i + 75) * (i + 75))))
