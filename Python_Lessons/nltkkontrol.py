import nltk
nltk.download('punkt')

from nltk.tokenize import word_tokenize

text = "Merhaba Mustafa. Bu bir testtir."
print(word_tokenize(text))
