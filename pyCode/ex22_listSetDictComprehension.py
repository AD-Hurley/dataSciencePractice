integers = [i for i in range(10)]
binaries = [int(format(i,'b')) for i in integers]

binary_dictionary = {integer:binary for integer, binary in zip(integers, binaries)}

print(integers)
print(binaries)
print(binary_dictionary)

additive_inverse = [-1*i for i in integers]
print(additive_inverse)

integer_list = [1, -1, 2, -2, 3, -3]
sq_set = {i**2 for i in integer_list}
print(sq_set)
