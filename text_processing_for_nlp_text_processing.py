#TexT_Processing_For_NLP

# Import Necessary Libraries
"""

import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

"""# Sample Text"""

sample_text = """
Natural language processing (NLP) is a field of artificial intelligence that focuses on the interaction
between computers and humans through natural language. The ultimate goal of NLP is to read, decipher,
understand, and make sense of human language in a way that is both valuable and meaningful.Additionally, researchers are exploring Quantum Natural Language Processing (QNLP), aiming to leverage quantum computing for more efficient language tasks.
Moreover, AI is being utilized to decode animal communications, potentially transforming our understanding of interspecies interactions
"""

"""# Tokenization"""

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')

sentences = sent_tokenize(sample_text)
words = [word_tokenize(sentence) for sentence in sentences]

"""# Lowercasing and Removing Special Characters"""

cleaned_words = [[re.sub(r'[^a-zA-Z0-9]', '', word.lower()) for word in sentence] for sentence in words]

"""# Removing Stopwords"""

stop_words = set(stopwords.words('english'))
filtered_words = [[word for word in sentence if word not in stop_words] for sentence in cleaned_words]

"""# Stemming and Lemmatization"""

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

stemmed_words = [[stemmer.stem(word) for word in sentence] for sentence in filtered_words]
lemmatized_words = [[lemmatizer.lemmatize(word) for word in sentence] for sentence in filtered_words]

"""# Printing Processed Sentences"""

print("Original Sentences:")
for sentence in sentences:
    print(sentence)

print("\nProcessed Sentences (Lemmatized):")
for sentence in lemmatized_words:
    print(' '.join(sentence))

