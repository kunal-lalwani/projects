#Adapted from http://ipullrank.com/step-step-twitter-sentiment-analysis-visualizing-united-airlines-pr-crisis/
import pandas,re, nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from random import randint

tweet_data = pandas.read_csv("Tweets.csv")

#Preprocess tweets
def processTweet(tweet):
    #Convert to lower case
    tweet = tweet.lower()
    #Convert www.* or https?://* to URL
    tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
    #Convert @username to AT_USER
    tweet = re.sub('@[^\s]+','AT_USER',tweet)
    #Remove additional white spaces
    tweet = re.sub('[\s]+', ' ', tweet)
    #Replace #word with word
    tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
    #trim
    tweet = tweet.strip('\'"')
    return tweet    

#Words ignored in tweets
#download from nltk.download()
stops = stopwords.words("english")
stops.append(unicode('URL'))
stops.append(unicode('AT_USER'))
stops=set(stops)

def replaceTwoOrMore(s):
    #look for 2 or more repetitions of character and replace with the character itself
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)
 
def getFeatureVector(tweet):
    featureVector = []
    #split tweet into words
    words = tweet.split()
    for w in words:
        #replace two or more with two occurrences
        w = replaceTwoOrMore(w)
        #strip punctuation
        w = w.strip('\'"?,.!')
        #check if the word begins with a letter or number
        val = re.search(r"^[a-zA-Z][a-zA-Z0-9]*$", w)
        #ignore if it is a stop word
        if(w in stops or val is None):
            continue
        else:
            featureVector.append(w.lower())
    return featureVector

index=range(len(tweet_data['text']))
#Splits into training and testing data, along with their indices
train,test,train_index,test_index = train_test_split(tweet_data,index,test_size=0.20,random_state=randint(0,2147483647))

train_tweets=[]
actual_sentiments=[]        
word_features=[]  

#Processes each training tweet and obtains its features
for i in range(len(train)):
    sentiment = train['airline_sentiment'][train_index[i]]
    tweet = train['text'][train_index[i]]
    processedTweet = processTweet(tweet)
    featureVector = getFeatureVector(processedTweet)
    word_features.extend(featureVector)
    train_tweets.append((featureVector, sentiment))

#Used for evaluation purposes after completing test        
for i in range(len(test)):
    sentiment = test['airline_sentiment'][test_index[i]]
    actual_sentiments.append((sentiment))

#Extracts each feature from the tweet and stores it in a dictionary            
def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    #This takes a while
    for word in word_features:
        features['contains(%s)' % word] = (word in tweet_words)
    return features

#Remove featureList duplicates
word_features = list(set(word_features))

#Trains using Naive Bayes and then tests
training_set = nltk.classify.util.apply_features(extract_features, train_tweets)
NBClassifier = nltk.NaiveBayesClassifier.train(training_set)
test_set=test['text'].apply(lambda tweet:extract_features(getFeatureVector(processTweet(tweet))))
test_sentiment=test_set.apply(lambda test: NBClassifier.classify(test))

#Accuracy, precision and recall
acc=0
true_pos=0
true_neu=0
true_neg=0
pos_pre=0
neg_pre=0
neu_pre=0
pos_re=0
neg_re=0
neu_re=0

#Obtains the number for accuracy, precision, and recall
for i in range(len(test)):
    if (test_sentiment[test_index[i]]==actual_sentiments[i]):
        acc=acc+1
        if(test_sentiment[test_index[i]]=='positive'):
            true_pos=true_pos+1
        elif(test_sentiment[test_index[i]]=='neutral'):
            true_neu=true_neu+1
        else:
            true_neg=true_neg+1
            
    if (test_sentiment[test_index[i]]=='positive'):
        pos_re=pos_re+1
    elif (test_sentiment[test_index[i]]=='neutral'):
        neu_re=neu_re+1
    else:
        neg_re=neg_re+1
    
    if (actual_sentiments[i]=='positive'):
        pos_pre=pos_pre+1
    elif (actual_sentiments[i]=='neutral'):
        neu_pre=neu_pre+1
    else:
        neg_pre=neg_pre+1         

acc=acc/float(len(test))
pos_re=true_pos/float(pos_re)
neu_re=true_neu/float(neu_re)
neg_re=true_neg/float(neg_re)
pos_pre=true_pos/float(pos_pre)
neu_pre=true_neu/float(neu_pre)
neg_pre=true_neg/float(neg_pre)

print "Accuracy is " + str(acc)
print "Positive recall is " + str(pos_re)
print "Neutral recall is " + str(neu_re)
print "Negative recall is " + str(neg_re)
print "Positive precision is " + str(pos_pre)
print "Neutral precision is " + str(neu_pre)
print "Negative precision is " + str(neg_pre)