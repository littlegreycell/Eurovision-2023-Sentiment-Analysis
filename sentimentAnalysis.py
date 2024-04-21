# Before the Eurovision Final
# Polarity
#Sentiment Analysis
SIA = SentimentIntensityAnalyzer()
dataBefore["clean_tweet"]= dataBefore["clean_tweet"].astype(str)
# Applying Model, Variable Creation
dataBefore['Polarity Score']=dataBefore["clean_tweet"].apply(lambda x:SIA.polarity_scores(x)['compound'])
dataBefore['Neutral Score']=dataBefore["clean_tweet"].apply(lambda x:SIA.polarity_scores(x)['neu'])
dataBefore['Negative Score']=dataBefore["clean_tweet"].apply(lambda x:SIA.polarity_scores(x)['neg'])
dataBefore['Positive Score']=dataBefore["clean_tweet"].apply(lambda x:SIA.polarity_scores(x)['pos'])
# Converting 0 to 1 Decimal Score to a Categorical Variable
dataBefore['Sentiment']=''
dataBefore.loc[dataBefore['Polarity Score']>0,'Sentiment']='Positive'
dataBefore.loc[dataBefore['Polarity Score']==0,'Sentiment']='Neutral'
dataBefore.loc[dataBefore['Polarity Score']<0,'Sentiment']='Negative'
dataBefore[:20]

# Visualizations
temp = dataBefore.groupby('Sentiment').count()['text'].reset_index().sort_values(by='text',ascending=False)
temp.style.background_gradient(cmap='Purples')

plt.figure(figsize=(12,6))
sns.countplot(x='Sentiment',data=dataBefore)

fig = go.Figure(go.Funnelarea(
    text =temp.Sentiment,
    values = temp.text,
    title = {"position": "top center", "text": "Funnel-Chart of Sentiment Distribution"}
    ))
fig.show()

# Most common words Sentiments Wise
Positive_sent = dataBefore[dataBefore['Sentiment']=='Positive']
Negative_sent = dataBefore[dataBefore['Sentiment']=='Negative']
Neutral_sent = dataBefore[dataBefore['Sentiment']=='Neutral']

#Positive
#MosT common positive words
top = Counter([item for sublist in Positive_sent['clean_tweet_stopwords'] for item in sublist])
temp_positive = pd.DataFrame(top.most_common(20))
temp_positive.columns = ['Common_words','count']
temp_positive.style.background_gradient(cmap='Greens')
fig = px.bar(temp_positive, x="count", y="Common_words", title='Most Commmon Positive Words', orientation='h', 
             width=700, height=700,color='Common_words')
fig.show()

#Negative
#MosT common negative words
top = Counter([item for sublist in Negative_sent['clean_tweet_stopwords'] for item in sublist])
temp_negative = pd.DataFrame(top.most_common(20))
temp_negative = temp_negative.iloc[1:,:]
temp_negative.columns = ['Common_words','count']
temp_negative.style.background_gradient(cmap='Reds')
fig = px.bar(temp_negative, x="count", y="Common_words", title='Most Commmon Negative Words', orientation='h', 
             width=700, height=700,color='Common_words')
fig.show()

#Neutral
#MosT common Neutral words
top = Counter([item for sublist in Neutral_sent['clean_tweet_stopwords'] for item in sublist])
temp_neutral = pd.DataFrame(top.most_common(20))
temp_neutral = temp_neutral.loc[1:,:]
temp_neutral.columns = ['Common_words','count']
temp_neutral.style.background_gradient(cmap='Blues')
fig = px.bar(temp_neutral, x="count", y="Common_words", title='Most Commmon Neutral Words', orientation='h', 
             width=700, height=700,color='Common_words')
fig.show()


# After the Eurovision Final
# Polarity
#Sentiment Analysis
SIA = SentimentIntensityAnalyzer()
dataAfter["clean_tweet"]= dataAfter["clean_tweet"].astype(str)
# Applying Model, Variable Creation
dataAfter['Polarity Score']=dataAfter["clean_tweet"].apply(lambda x:SIA.polarity_scores(x)['compound'])
dataAfter['Neutral Score']=dataAfter["clean_tweet"].apply(lambda x:SIA.polarity_scores(x)['neu'])
dataAfter['Negative Score']=dataAfter["clean_tweet"].apply(lambda x:SIA.polarity_scores(x)['neg'])
dataAfter['Positive Score']=dataAfter["clean_tweet"].apply(lambda x:SIA.polarity_scores(x)['pos'])
# Converting 0 to 1 Decimal Score to a Categorical Variable
dataAfter['Sentiment']=''
dataAfter.loc[dataAfter['Polarity Score']>0,'Sentiment']='Positive'
dataAfter.loc[dataAfter['Polarity Score']==0,'Sentiment']='Neutral'
dataAfter.loc[dataAfter['Polarity Score']<0,'Sentiment']='Negative'
dataAfter[:20]

# Visualizations
temp = dataAfter.groupby('Sentiment').count()['text'].reset_index().sort_values(by='text',ascending=False)
temp.style.background_gradient(cmap='Purples')

plt.figure(figsize=(12,6))
sns.countplot(x='Sentiment',data=dataAfter)

fig = go.Figure(go.Funnelarea(
    text =temp.Sentiment,
    values = temp.text,
    title = {"position": "top center", "text": "Funnel-Chart of Sentiment Distribution"}
    ))
fig.show()

# Most common words Sentiments Wise
Positive_sent = dataAfter[dataAfter['Sentiment']=='Positive']
Negative_sent = dataAfter[dataAfter['Sentiment']=='Negative']
Neutral_sent = dataAfter[dataAfter['Sentiment']=='Neutral']

#Positive
#MosT common positive words
top = Counter([item for sublist in Positive_sent['clean_tweet_stopwords'] for item in sublist])
temp_positive = pd.DataFrame(top.most_common(20))
temp_positive.columns = ['Common_words','count']
temp_positive.style.background_gradient(cmap='Greens')
fig = px.bar(temp_positive, x="count", y="Common_words", title='Most Commmon Positive Words', orientation='h', 
             width=700, height=700,color='Common_words')
fig.show()

#Negative
#MosT common negative words
top = Counter([item for sublist in Negative_sent['clean_tweet_stopwords'] for item in sublist])
temp_negative = pd.DataFrame(top.most_common(20))
temp_negative = temp_negative.iloc[1:,:]
temp_negative.columns = ['Common_words','count']
temp_negative.style.background_gradient(cmap='Reds')
fig = px.bar(temp_negative, x="count", y="Common_words", title='Most Commmon Negative Words', orientation='h', 
             width=700, height=700,color='Common_words')
fig.show()

#Neutral
#MosT common Neutral words
top = Counter([item for sublist in Neutral_sent['clean_tweet_stopwords'] for item in sublist])
temp_neutral = pd.DataFrame(top.most_common(20))
temp_neutral = temp_neutral.loc[1:,:]
temp_neutral.columns = ['Common_words','count']
temp_neutral.style.background_gradient(cmap='Blues')
fig = px.bar(temp_neutral, x="count", y="Common_words", title='Most Commmon Neutral Words', orientation='h', 
             width=700, height=700,color='Common_words')
fig.show()
