from nltk.corpus import names
from nltk.stem import WordNetLemmatizer
def letters_only(astr):
	return astr.isalpha()

all_names = set(names.words())
lemmatizer = WordNetLemmatizer()
def clean_text(docs):
	cleaned_docs = []
	for doc in docs:
		cleaned_docs.append(' '.join([lemmatizer.lemmatize(word.lower())
		for word in doc.split()
			if letters_only(word)
				and word not in all_names]))
	return cleaned_docs

