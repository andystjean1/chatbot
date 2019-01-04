
import get_transcript as get_tran
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.corpus import stopwords
import string
import random
import re

import warnings
warnings.filterwarnings("ignore")

GREETING_TRIGGERS = ["hi", "hey", "hello"]


#table to get rid of punctuation
no_punct = str.maketrans('', '', string.punctuation)
bye_words = ['bye', 'bye!']

#get scripts
script = get_tran.get_scripts()
sentences = nltk.sent_tokenize(script)
words = nltk.word_tokenize(script)

#get greetings and farewells from script data
greetings = [s for s in sentences if re.match(r'hey', s)]
farewells = [s for s in sentences if re.match(r'bye', s)]


print("# of sentences: ", len(sentences))
print("# of words: ", len(words))

def lem_tokens(tokens):
    lemmer = nltk.stem.WordNetLemmatizer()
    return [lemmer.lemmatize(t) for t in tokens]

def lem_normalize(text):
    return lem_tokens(nltk.word_tokenize(text.lower().translate(no_punct)))

def response(user_response):
    chat_response = ' '
    sentences.append(user_response)
    tfid_vec = TfidfVectorizer(tokenizer=lem_normalize, stop_words='english')
    tfidf = tfid_vec.fit_transform(sentences)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if(req_tfidf==0):
        chat_response = chat_response+" I DIDNT GET THAT OK"
        return chat_response
    else:
        chat_response = chat_response+sentences[idx]
        return chat_response

if __name__ == '__main__':
    #setup
    flag = True
    print("Whats up say something: ", end= "")

    while(flag==True):
        user_response = input().lower()

        if(user_response not in bye_words):
            if(user_response in GREETING_TRIGGERS):
                print("\nChatty: ", random.choice(greetings))
            else:
                print("\nChatty: ", response(user_response))
                sentences.remove(user_response)

        else:
            flag = False
            print(random.choice(farewells))
