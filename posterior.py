def get_posterior(term_document_matrix, prior, likelihood):
	""" Compute posterior of testing samples, based on prior and likelihood
	Args:
		term_document_matrix (sparse matrix)
		prior (dictionary, with class label as key, corresponding prior as the value)
		likelihood (dictionary, with class label as key,
		corresponding conditional probability vector as value)
	Returns:
		dictionary, with class label as key, corresponding posterior as value
	"""
	num_docs = term_document_matrix.shape[0]
	posteriors = []
	for i in range(num_docs):
	# posterior is proportional to prior * likelihood
	# = exp(log(prior * likelihood))
	# = exp(log(prior) + log(likelihood))
		posterior = {key: np.log(prior_label) for key, prior_label in prior.items()}
		for label, likelihood_label in likelihood.items():
			term_document_vector = term_document_matrix.getrow(i)
			counts = term_document_vector.data
			indices = term_document_vector.indices
			for count, index in zip(counts, indices):
				posterior[label] += np.log(likelihood_label[index]) * count
		# exp(-1000):exp(-999) will cause zero division error,
		# however it equates to exp(0):exp(1)
		min_log_posterior = min(posterior.values())
		for label in posterior:
			try:
				posterior[label] = np.exp(posterior[label] - min_log_posterior)
			except:
			# if one's log value is excessively large, assign it infinity
				posterior[label] = float('inf')
		# normalize so that all sums up to 1
		sum_posterior = sum(posterior.values())
		for label in posterior:
			if posterior[label] == float('inf'):
				posterior[label] = 1.0
			else:
				posterior[label] /= sum_posterior
		posteriors.append(posterior.copy())
	return posteriors
