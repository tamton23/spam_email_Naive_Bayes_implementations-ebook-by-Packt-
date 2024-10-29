import glob
import os
file_path = 'enron1/ham/'
for filename in glob.glob(os.path.join(file_path, '*.txt')):
        with open(filename, 'r', encoding = "ISO-8859-1") as infile:
                e_mails.append(infile.read())
                labels.append(0)

