import json
import nltk
from nltk.corpus import stopwords

nltk.download('punkt')

moviesfile = open('movies.json', encoding="utf8")
data = json.load(moviesfile)

# Document Set ()
documents = []
for movie in data['movies']:
    documents.append(movie['title'])

# Tokenization function
def tokenize(text):
    tokens = nltk.word_tokenize(text)
    tokens = [token.lower() for token in tokens if token.isalpha()]
    return tokens
#loading tfidf.json
TfidfFile = open('tfidf.json', encoding="utf8")
tfidf_scores = json.load(TfidfFile)


# main function
def search(query):
    score=0
    tokens = tokenize(query)
    search_results = []
    for i, document in enumerate(documents):
        if all(token in document.lower() for token in tokens):
            index=0
            find = False
            while not(find == True or index>len(documents)):
                if tfidf_scores['documents'][index]['number']==i:
                    find = True
                else:
                    index = index+1
            ff=index
            while tfidf_scores['documents'][ff]['number'] == i:
                score =score +sum([tfidf_scores['documents'][ff]['score'] for token in tokens if tfidf_scores['documents'][ff]['word']==token])
                ff=ff+1
            search_results.append((i, document, score))
            score = 0
    search_results.sort(key=lambda x: x[2], reverse=True) #ranking based on score
    return search_results
