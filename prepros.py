import re
import nltk
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.corpus import stopwords

def remove_html(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def preprocess_text(text):

    #Remove HTML tags
    text = remove_html(text)

    # Lowercase
    text = text.lower()

    #Tokenize
    tokens = nltk.word_tokenize(text)
    
    #Remove punctuation
    #tokens = [word for word in tokens if word.isalnum()]
    
    #Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    #Stemmer
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(word) for word in tokens]

    #Lemmatize
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    #Join tokens back to string
    processed_text = ' '.join(lemmatized_tokens)
    
    return processed_text
