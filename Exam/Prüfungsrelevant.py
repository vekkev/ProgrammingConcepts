# Python Generators: iterator, generator, yield:
# Generator No. 1:


# def matrno_generator1(i=100):
# 	while i < 111:
# 		i += 3
# 		yield i
#
#
# for elem in matrno_generator1():
# 	print(elem)

# Erklärung -->


# Generator No. 2

# def matrno_generator2(i=100):
# 		yield i + 3
# 		yield i + 2
# 		yield i + 1
#
#
# for elem in matrno_generator2():
# 	print(elem)

# Erklärung -->


#Generator No.3:

# def matrno_generator3(i=100):
# 	return [str(i+3)]
# 	return [str(i+2)]
# 	return [str(i+1)]
#
#
# for elem in matrno_generator3():
# 	print(elem)

# Erklärung -->


#Generator No.4:

def matrno_generator4(i=100):
	while i < 111:
		yield i + 3


for elem in matrno_generator4():
	print(elem)


# Erklärung -->