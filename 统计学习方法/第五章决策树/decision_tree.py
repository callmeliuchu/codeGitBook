from math import log
from collections import Counter

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


def majority(data_set):
	class_list = [vec[-1] for vec in data_set]
	return Counter(class_list).most_common(1)[0][0]





def create_tree(data_set,labels):
	class_list = [vec[-1] for vec in data_set]
	if len(set(class_list))==1:
		return class_list[0]
	if len(data_set[0])==1:
		return majority(data_set)
	best_split = choose_best_split(data_set)
	print(data_set)
	print(labels)
	best_label = labels[best_split]
	my_tree = {best_label:{}}
	del(labels[best_split])
	feat_values = [vec[best_split] for vec in data_set]
	feat_set = set(feat_values)
	for val in feat_set:
		sub_labels = labels[:]
		my_tree[best_label][val] = create_tree(split_data_set(data_set,best_split,val),sub_labels)
	return my_tree



test_arr =[['a'],['b'],['a']]
# print(majority(test_arr))



labels = ['no surfacing','flippers']
data_set = load_data()
print(data_set)
# p = cal_entries(data_set)
# print(p)
# print(split_data_set(data_set,0,1))
# print(choose_best_split(data_set))
tree = create_tree(data_set,labels)
print(tree)