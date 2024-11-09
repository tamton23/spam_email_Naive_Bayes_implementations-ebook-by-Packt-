# spam_email_Naive_Bayes_implementations-ebook-by-Packt
# Data
    1. [install data email] (http://www.aueb.gr/users/ion/data/enron-spam/preprocessed/enron1.tar.gz.)
# In Linux
    ls -l enron1/ham/*.txt |wc -l to check folder constrain file NoSpam
    ls -l enron1/spam/*.txt |wc -l to check folder constrain file Spam
# Implement Module
    1. use exec(open("file.py").read()) to run module or create init call module
    2. exec Module loadSpamEmail and loadHamEmail with label 0 and 1
    3. use Module clean date to clean files email.
