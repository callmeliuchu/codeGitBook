



def load_data_set():
	train_data = [[1,'S'],[1,'M'],[1,'M'],[1,'S'],[1,'S'],[1,'S'],[2,'M'],[2,'M'],
	               [2,'L'],[2,'L'],[2,'L'],[3,'M'],[3,'M'],[3,'L'],[3,'L']]
	label = [-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1]
	return train_data,label


def get_label_data(data_set,labels,label):
	return_data = []
	for i in range(len(labels)):
		if label == labels[i]:
			return_data.append(data_set[i])
	return return_data


def count_data(data_set,i,x):
	count = 0
	for vec in data_set:
		if vec[i]==x:
			count=count+1
	return count



def calculate_proab(train_data,labels,vec):
	label_set = set(labels)
	p_res = -1
	for label in label_set:
		label_data = get_label_data(train_data,labels,label)
		p_temp = len(label_data)/float(len(train_data))
		for i in range(len(vec)):
			count = count_data(label_data,i,vec[i])
			p_temp = p_temp*count/float(len(label_data))
		if p_res<p_temp:
			p_res = p_temp
			label_res = label
	return label_res












train_data,labels = load_data_set()
for i in range(len(train_data)):
	print(train_data[i],labels[i])

print(calculate_proab(train_data,labels,[2,'S']))



