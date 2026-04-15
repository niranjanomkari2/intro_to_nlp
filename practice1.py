
import pandas as pd
data = pd.read_csv("tripadvisor_hotel_reviews.csv")
data['review_lower_case']=data['Review'].str.lower()

from nltk.corpus import stopwords
eng_stopwords = stopwords.words('english')
eng_stopwords.remove("not")
import re
data['review_no_stopwords'] = data['review_lower_case'].apply(lambda x: ' '.join([word for word in x.split() if word not in eng_stopwords ]))
data['review_no_stopwords_no_punc']=data['review_no_stopwords'].apply(lambda x:re.sub(r'[*]',' star',x))
data['review_no_stopwords_no_punc'] = data['review_no_stopwords_no_punc'].apply(lambda x: re.sub(r'[^\w\s]','',x))

from nltk.tokenize import word_tokenize,sent_tokenize
data['word_tokens'] = data['review_no_stopwords_no_punc'].apply(lambda x: word_tokenize(x))
#STEMMING
from nltk.stem import PorterStemmer
ps = PorterStemmer()
#data['word_tokens'] = data['word_tokens'].apply(lambda x: [ps.stem(i) for i in x])

#LEMMATIZER
from nltk.stem import WordNetLemmatizer
lemmatize = WordNetLemmatizer()
data['word_tokens_Lemm'] = data['word_tokens'].apply(lambda x: [lemmatize.lemmatize(i) for i in x])
#print(data['word_tokens_Lemm'][0])

#NGRAMS
tokens_clean = sum(data['word_tokens_Lemm'],[])

import nltk
unigrams = pd.Series(nltk.ngrams(tokens_clean,2)).value_counts()
print(unigrams)
import matplotlib.pyplot as plt
unigrams[0:10].sort_values().plot.barh(color='yellow')
plt.show()
