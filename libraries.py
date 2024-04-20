!pip install tweet-preprocessor
!pip install palettable
!pip install textblob
import preprocessor as p
import plotly.express as px
import tweepy
import csv
import pandas as pd
import numpy as np
from plotly import graph_objs as go
import datetime
import seaborn as sns
import nltk
import re
import string
from textblob import TextBlob
import matplotlib.pyplot as plt
from keras.models import Sequential
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from collections import Counter
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.sentiment.util import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer

# Download Required NLTK Files.
nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
