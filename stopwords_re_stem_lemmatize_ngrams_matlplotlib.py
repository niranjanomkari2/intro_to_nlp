from nltk.corpus import stopwords
english_sw = stopwords.words('english')
#print(english_sw)
sentence = "it was too far to go to the shop and he did not want her to walk"

english_sw.remove("did")
english_sw.remove("not")
english_sw.append("go")
sentence_no_sw = ' '.join([word for word in sentence.split() if word not in english_sw])
#print(sentence_no_sw)

import re
# print text without using raw string indicator
my_folder = r"C:\desktop\notes"
result_search = re.search("pattern","do you know where pattern is..and here is another pattern")
string = r"sara was able to help me find the items i needed quickly"
result_search = re.sub("sara","Saraaaaaah",string)
customer_reviews = ['sam was a great help to me in the store', 
                    'the cashier was very rude to me, I think her name was eleanor', 
                    'amazing work from sadeen!', 
                    'sarah was able to help me find the items i needed quickly', 
                    'lucy is such a great addition to the team', 
                    'great service from sara she found me what i wanted'
                   ]
pattern_to_find = r'[^\w\s]' 
sara_reviews = []
for review in customer_reviews:
    no_punc_string = re.sub(pattern_to_find,"",review)
    sara_reviews.append(no_punc_string)
#print(sara_reviews)
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize,sent_tokenize
sentences = "Her cat's name is Luna. Her dog's name is max"
#print(sent_tokenize(sentences))
#------------------------------------------------
from nltk.stem import PorterStemmer
ps = PorterStemmer()
connect_tokens = ['connecting', 'connected', 'connectivity', 'connect', 'connects']
for token in connect_tokens:
    pass
    #print(token, ":" , ps.stem(token))
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()
likes_tokens = ['likes', 'better', 'worse']
for token in likes_tokens:
    pass
    #print(token, ":" , wnl.lemmatize(token))
#--------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
tokens = ['the', 'rise', 'of', 'artificial', 'intelligence', 'has', 'led', 'to', 'significant', 'advancements', 'in', 'natural', 'language', 'processing', 'computer', 'vision', 'and', 'other', 'fields', 'machine', 'learning', 'algorithms', 'are', 'becoming', 'more', 'sophisticated', 'enabling', 'computers', 'to', 'perform', 'complex', 'tasks', 'that', 'were', 'once', 'thought', 'to', 'be', 'the', 'exclusive', 'domain', 'of', 'humans', 'with', 'the', 'advent', 'of', 'deep', 'learning', 'neural', 'networks', 'have', 'become', 'even', 'more', 'powerful', 'capable', 'of', 'processing', 'vast', 'amounts', 'of', 'data', 'and', 'learning', 'from', 'it', 'in', 'ways', 'that', 'were', 'not', 'possible', 'before', 'as', 'a', 'result', 'ai', 'is', 'increasingly', 'being', 'used', 'in', 'a', 'wide', 'range', 'of', 'industries', 'from', 'healthcare', 'to', 'finance', 'to', 'transportation', 'and', 'its', 'impact', 'is', 'only', 'set', 'to', 'grow', 'in', 'the', 'years', 'to', 'come']

unigrams = pd.Series(nltk.ngrams(tokens,1)).value_counts()
unigrams[0:10].sort_values().plot.bar(color='green',width=0.9,figsize=(12,8))
plt.title('Most Frequently Occuring N-grams')
plt.xlabel('# of occurences')
plt.ylabel('N-grams')
plt.show()
