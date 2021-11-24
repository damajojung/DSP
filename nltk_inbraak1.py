
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


from nltk.probability import FreqDist
from nltk import word_tokenize

import string
from nltk.stem.porter import PorterStemmer
from nltk import pos_tag


def preprocess(filename):
    f = open(filename,'r')
    text = f.read()
    text = text.lower()
    
    text_p = "".join([char for char in text if char not in string.punctuation])
    
    words = word_tokenize(text_p)
    
    stop_words = stopwords.words('english')
    filtered_words = [word for word in words if word not in stop_words]
    
    porter = PorterStemmer()
    stemmed = [porter.stem(word) for word in filtered_words]
    
    pos = pos_tag(filtered_words)
    
    return words, filtered_words, stemmed, pos

words, filtered_words, stemmed, pos = preprocess('/Users/dj/Documents/GitHub/inbraak_1.txt')

#print('Words:', words[:50])

#print('Filtered words:', filtered_words[:50])

#print('Stemmed words:', stemmed[:50])

# print('Part of Speech:', pos[:50]) Test

freq = FreqDist(filtered_words)

freq.plot(100)




# freq.items()
test = freq.max
print(type(test))

for word, frequency in freq.most_common(20):
    print(u'{};{}'.format(word, frequency))

### Specific Words


"""
# Let's take the specific words only if their frequency is greater than 3.
specific_words = dict([(m, n) for m, n in freq.items() if len(m) > 10])
 
for key in sorted(specific_words):
    print("%s: %s" % (key, specific_words[key]))
 
data_analysis = FreqDist(specific_words)
 
data_analysis.plot(25, cumulative=False)
"""





