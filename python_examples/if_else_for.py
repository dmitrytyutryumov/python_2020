

def campare(a: int):
	if a == 1:
		print(1)
	elif a == 2:
		print(2)
	else:
		print(a)
	# print(a)
	return a


def comapare_immut_types():
	if not []:
		print('empty')
	if not {}:
		print({})
	if not False:
		print(False)
	if not 0:
		print(0)

	if True:
		print(True)

	if set({1, 1}):
		print(True)


def compare_long():
	a, b, c, v = 1, 2, 3, 4

	if a == 1 and b == 2 and c == 3 or v == [1, 2, 3] and isinstance(v,(set, list)):
		print(True)

	if a == 1 and b == 2 and c == 3 or \
		v == [1, 2, 3] and isinstance(v,(set, list)):
		print(True)

	if all([
		a == 1,
		b == 2,
		c == 3,
		any([
			v == [1, 2, 3],
			isinstance(v,(set, list))
		])
	]):
		print(True)


	compare_query = a == 1 and b == 2 and c == 3 or v == [1, 2, 3] and isinstance(v,(set, list))
	if compare_query:
		print(True)



def line_compare(a, b, c):
	return a if b == 2 else c


if __name__ == '__main__':
	main()
