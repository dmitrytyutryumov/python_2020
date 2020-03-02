def for_cycle():
	for i in [1, 2, 3]:
		print(i)
		# if i == 3:
		# 	 break
	else:
		print('for finished')


def while_cycle(*args, **kwargs):
	start = 0
	step = 1
	end = None

	if len(args) == 1:
		end = args[0]
	elif len(args) == 2:
		start, end = args
	elif len(args) == 3:
		start, end, step = args
	else:
		raise RuntimeError

	if start >= end:
		raise RuntimeError

	print(start, end, step)

	while start < end:
		 yield start
		 start += step

def line_for():
	return [i for i in while_cycle(5)]


if __name__ == '__main__':
	pass
