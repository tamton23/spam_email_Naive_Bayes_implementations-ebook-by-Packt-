from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(cleaned_emails, labels, test_size=0.3)
term_docs_train = cv.fit_transform(X_train)
label_index = get_label_index(Y_train)
prior = get_prior(label_index)
smoothing = 1
likelihood = get_likelihood(term_docs_train, label_index, smoothing)
term_docs_test = cv.transform(X_test)
posterior = get_posterior(term_docs_test, prior, likelihood)
correct = 0.0
for pred, actual in zip(posterior, Y_test):
	if actual == 1:
		if pred[1] >= 0.5:
			correct += 1
	elif pred[0] > 0.5:
		correct += 1
print('the accuracy on {0} testing samples = {1:.1f}%'.format(len(Y_test), correct/len(Y_test)*100))

