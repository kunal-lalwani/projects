from __future__ import division
import sklearn
import matplotlib.pyplot as varPlot
import pandas
from sklearn.cross_validation import train_test_split
import numpy
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.metrics import accuracy_score


Tweet= pandas.read_csv('Tweets.csv')
Tweet.head()


(len(Tweet)-Tweet.count())/len(Tweet)
del Tweet['tweet_coord']
del Tweet['airline_sentiment_gold']
del Tweet['negativereason_gold']

def newTweetLength(unchangedTweet):
    onlyAlphabets = re.sub("[^a-zA-Z]", " ",unchangedTweet) 
    words = onlyAlphabets.lower().split()                             
    stops = set(stopwords.words("english"))                  
    refinedWords = [w for w in words if not w in stops] 
    return(len(refinedWords))

#2 gram of models is used to extract the features example: ["not good","is not"]
def convertToWords(unchangedTweet):
    onlyAlphabets = re.sub("[^a-zA-Z]", " ",unchangedTweet) 
    words = onlyAlphabets.lower().split()                             
    stops = set(stopwords.words("english"))                  
    refinedWords = [w for w in words if not w in stops]
    bigramFeatureVector = []
    for item in nltk.bigrams(refinedWords):
        bigramFeatureVector.append(' '.join(item))
    return str(bigramFeatureVector) 

Tweet['sentiment']=Tweet['airline_sentiment'].apply(lambda x: 0 if x=='negative' else(1 if x=='positive' else 2))

Tweet['refinedTweets']=Tweet['text'].apply(lambda x: convertToWords(x))
Tweet['Tweet_length']=Tweet['text'].apply(lambda x: newTweetLength(x))
train,test = train_test_split(Tweet,test_size=0.2,random_state=42)

train_refinedTweets=[]
for tweet in train['refinedTweets']:
    train_refinedTweets.append(tweet)
test_refinedTweets=[]
for tweet in test['refinedTweets']:
    test_refinedTweets.append(tweet)


v = CountVectorizer(analyzer = "word")
trainFeatures= v.fit_transform(train_refinedTweets)
testFeatures=v.transform(test_refinedTweets)

ListOfClassifiers = [
LogisticRegression(C=0.000000001,solver='liblinear',max_iter=200),
RandomForestClassifier(n_estimators=200),
DecisionTreeClassifier(),
 SVC(kernel="rbf", C=0.025, probability=True)
 GradientBoostingClassifier(n_estimators=100, learning_rate=1.0,max_depth=4, random_state=0),
 AdaBoostClassifier(base_estimator=DecisionTreeClassifier(max_depth=18, min_samples_leaf=25, min_samples_split=10), n_estimators=10)
    ]

advanceFeatures=trainFeatures.toarray()
advanceFeaturesTest= testFeatures.toarray()
Accuracy=[]
ClassifierModel=[]
for classifier in ListOfClassifiers:
    try:
        fit = classifier.fit(trainFeatures,train['sentiment'])
        pred = fit.predict(testFeatures)
    except Exception:
        fit = classifier.fit(advanceFeatures,train['sentiment'])
        pred = fit.predict(advanceFeaturesTest)
    accuracy = accuracy_score(pred,test['sentiment'])
    Accuracy.append(accuracy)
    ClassifierModel.append(classifier.__class__.__name__)
    print ('Accuracy of '+classifier.__class__.__name__+' is '+str(accuracy))

positions = [1,2,3,4,5,6,7]
varPlot.bar(positions,Accuracy)
varPlot.xticks(positions, ClassifierModel,rotation=45)
varPlot.ylabel('Accuracy')
varPlot.xlabel('ClassifierModel')
varPlot.title('Accuracies of ClassifierModels')