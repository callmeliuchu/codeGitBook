from math import log

def load_data():
	data_set = [ [1,1,'yes'],
	             [1,1,'yes'],
	             [1,0,'no'],
	             [0,1,'no'],
	             [0,1,'no']]
	return data_set

def cal_entries(data_set):
	count = {}
	for vec in data_set:
		if vec[-1] not in count:
			count[vec[-1]] = 0
		count[vec[-1]] = count[vec[-1]]+1
	p = 0.0
	for key in count:
		prob = count[key]/float(len(data_set))
		p = p - prob*log(prob,2)
	return p

def split_data_set(data_set,loc,val):
	ret_data = []
	for vec in data_set:
		if vec[loc]==val:
			ret_data.append(vec[:loc]+vec[loc+1:])
	return ret_data



def choose_best_split(data_set):
	n_dimension = len(data_set[0])-1
	p_max = -1.0
	loc = -1
	p_base = cal_entries(data_set)
	for i in range(n_dimension):
		splits = set([vec[i] for vec in data_set])
		p_tmp = 0.0
		for split in splits:
			split_data = split_data_set(data_set,i,split)
			p = len(split_data)/float(len(data_set))
			p_tmp = p_tmp + p*cal_entries(split_data)
		p_gain = p_base - p_tmp
		if p_max<p_gain:
			p_max = p_gain
			loc = i
	return loc










data_set = load_data()
print(data_set)
p = cal_entries(data_set)
print(p)
print(split_data_set(data_set,0,1))
print(choose_best_split(data_set))