# 1. Before the Eurovision Final 

# Cleaning of datasets
def preprocess_tweet(row):
    text = row['text']
    text = p.clean(text)
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text
dataBefore['clean_tweet'] = dataBefore.apply(preprocess_tweet, axis=1)
dataBefore[:6]

# Remove stop words
nltk.download('stopwords')
stop = stopwords.words('english')
dataBefore['clean_tweet_stopwords'] = dataBefore['clean_tweet'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
dataBefore['clean_tweet_stopwords'][:5]


# 2. After the Eurovision Final 

# Cleaning of datasets
import preprocessor as p
def preprocess_tweet(row):
    text = row['text']
    text = p.clean(text)
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text
dataAfter['clean_tweet'] = dataAfter.apply(preprocess_tweet, axis=1)
dataAfter[:6]

# Remove stop words
stop = stopwords.words('english')
dataAfter['clean_tweet_stopwords'] = dataAfter['clean_tweet'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop)]))
dataAfter['clean_tweet_stopwords'][:5]
