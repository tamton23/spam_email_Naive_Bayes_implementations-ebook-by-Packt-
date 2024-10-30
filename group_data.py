def get_label_index(labels):
	from collections import defaultdict
	label_index = defaultdict(list)
	for index, label in enumerate(labels):
		label_index[label].append(index)
	return label_index

