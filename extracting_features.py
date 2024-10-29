from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(stop_words="english", max_features=500)
#stop word 'english' (and, the, him ... duoc cho la khong cung cap tinh hieu)
#max_feature '500' 500 shape co the nang cao len de dat do chinh sac cao hon
term_docs = cv.fit_transform(cleaned_data)
