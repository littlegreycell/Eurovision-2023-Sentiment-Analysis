# Before the Eurovision Finals
# Most Used Words
a = dataBefore['clean_tweet_stopwords'].str.cat(sep=' ')
words = nltk.tokenize.word_tokenize(a)
word_dist = nltk.FreqDist(words)
dff = pd.DataFrame(word_dist.most_common(), 
                    columns=['Word', 'Frequency'])
dff['Word_Count'] = dff.Word.apply(len)
dff[:10]

# Count the common words
dataBefore['clean_tweet_stopwords']= dataBefore['clean_tweet_stopwords'].apply(lambda x:str(x).split())
top = Counter([item for sublist in dataBefore['clean_tweet_stopwords'] for item in sublist])
temp = pd.DataFrame(top.most_common(20))
temp.columns = ['Common_words','count']
temp.style.background_gradient(cmap='Blues')

#Bar Plot
fig = px.bar(temp, x="count", y="Common_words", title='Commmon Words in Selected Text', orientation='h', 
             width=700, height=700,color='Common_words')
fig.show()

# Word Cloud
text = " ".join(str(i) for i in dataBefore.clean_tweet_stopwords )
wordcloud = WordCloud( background_color="white").generate(text)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

# Hashtag analyzing
hashtag_counts = Counter()
for tweet in dataBefore['text']:
    hashtags = [tag.strip("#") for tag in tweet.split() if tag.startswith("#")]
    hashtag_counts.update(hashtags)
​
print("Most popular 20 hashtag:")
for hashtag, count in hashtag_counts.most_common(20):
    print("{}: {}".format(hashtag, count))



# After the Eurovision Finals
# Most Used Words
a = dataAfter['clean_tweet_stopwords'].str.cat(sep=' ')
words = nltk.tokenize.word_tokenize(a)
word_dist = nltk.FreqDist(words)
dff = pd.DataFrame(word_dist.most_common(), 
                    columns=['Word', 'Frequency'])
dff['Word_Count'] = dff.Word.apply(len)
dff[:10]

# Count the common words
dataAfter['clean_tweet_stopwords']= dataAfter['clean_tweet_stopwords'].apply(lambda x:str(x).split())
top = Counter([item for sublist in dataAfter['clean_tweet_stopwords'] for item in sublist])
temp = pd.DataFrame(top.most_common(20))
temp.columns = ['Common_words','count']
temp.style.background_gradient(cmap='Blues')

#Bar Plot
fig = px.bar(temp, x="count", y="Common_words", title='Commmon Words in Selected Text', orientation='h', 
             width=700, height=700,color='Common_words')
fig.show()

# Visualization
text = " ".join(str(i) for i in dataAfter.clean_tweet_stopwords )
wordcloud = WordCloud( background_color="white").generate(text)
plt.figure( figsize=(15,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
