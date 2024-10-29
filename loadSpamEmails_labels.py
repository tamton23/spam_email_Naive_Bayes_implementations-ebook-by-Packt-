import glob
import os
e_mails, labels = [], []
file_path = 'enron1/spam/'
for filename in glob.glob(os.path.join(file_path, '*.txt')):
	with open(filename, 'r', encoding = "ISO-8859-1") as f:
		e_mails.append(f.read())
		labels.append(1)
