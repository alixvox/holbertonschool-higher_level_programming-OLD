#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in range(0, len(matrix)):
        count = 0
		for y in x:
			if count < len(x) - 1:
				print("{:d}".format(y), end=" ")
			else:
				print("{:d}".format(y), end="")
			count = count + 1
		print()
