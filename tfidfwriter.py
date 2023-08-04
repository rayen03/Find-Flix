import json
import math
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))
#loading movies.json (modify this if you want to work with a different dataset)
f = open('movies.json', encoding="utf8")
data = json.load(f)

# Document Set
documents = []
for movie in data['movies']:
    documents.append(movie['title'])

def tokenize(text):
    tokens = nltk.word_tokenize(text)
    tokens = [token.lower() for token in tokens if token.isalpha() and token.lower() not in stop_words]
    return tokens

def calculate_tfidf(documents):
    f = open("tfidf.txt", "w")
    f.write('{"documents":[')
    tokens_list = [tokenize(document) for document in documents]
    for i, tokens in enumerate(tokens_list):
        tf = {}
        for token in tokens:
            tf[token] = tf.get(token, 0) + 1
        for token, count in tf.items():
            denominator = sum([1 for document in documents if token in document])
            if denominator == 0:
                idf = 0
            else:
                idf = math.log(len(documents) / denominator)
            tfidf= tf[token] * idf
            f.write('{')
            f.write('"number": {0}, "word": "{1}", "score": {2} '.format(i, token, tfidf))
            f.write('},')
            
    f.write("]}")
    f.close()
    

tfidf_scores = calculate_tfidf(documents)