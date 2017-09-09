


def load_data(file_path):
	ret_data = []
	with open(file_path) as f:
		for line in f.readlines():
			data = line.split()
			ret_data.append([float(num) for num in data])
		f.close()
	return  ret_data


file_path = 'data/ex00.txt'
print(load_data(file_path))


