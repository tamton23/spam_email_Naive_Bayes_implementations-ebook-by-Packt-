import numpy as np
def get_likelihood(term_document_matrix, label_index, smoothing=0):
	""" Compute likelihood based on training samples
	Args:
		term_document_matrix (sparse matrix)
		label_index (grouped sample indices by class)
		smoothing (integer, additive Laplace smoothing parameter)
	Returns:
		dictionary, with class as key, corresponding conditional probability P(feature|class) vector as value
	"""

	likelihood = {}
	for label, index in label_index.items():
		likelihood[label] = term_document_matrix[index, :].sum(axis=0) + smoothing
		likelihood[label] = np.asarray(likelihood[label])[0]
		total_count = likelihood[label].sum()
		likelihood[label] = likelihood[label] / float(total_count)
	return likelihood

smoothing = 1
likelihood = get_likelihood(term_docs, label_index, smoothing)
