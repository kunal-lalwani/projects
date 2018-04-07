# Donglin Lao
# cs596 Machine Learning 
# adapted from https://www.kaggle.com/ngyptr/lstm-sentiment-analysis-keras

# README
# TO RUN THIS CODE YOU NEED TO INSTALL ALL OF THE PACKAGES I'M IMPORTING
# MOST OF THESE COME WITH ANACONDA PACKAGE BUT YOU WILL NEED TO INSTALL THE FOLLOWING WITH ALL THEIR DEPENDENCIES: 
# 1) KERAS
# 2) TENSORFLOW
# I HAVE 10 MODELS IN HERE HARD CODED IN BUT FOR THE SAKE OF TIME, I CHOSE TO RUN THEM ONE AT A TIME SO IF YOU
# WANT TO RUN THEM ALL YOU WILL NEED TO RUN THEM SEQUENTIALLY AND COMMENT OUT THE DIFFERENT MODELS
import numpy as np 
import pandas as pd 
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM
from sklearn.model_selection import train_test_split
from keras.regularizers import l1_l2, l2, l1
import re

data = pd.read_csv('cs596ML_finalproj_RNN/Tweets.csv')

# extracting tweets and truth values
data = data[['text','airline_sentiment']]

#removing neutral values, only doing Binary classification of Positive or Negative Sentiment
data = data[data.airline_sentiment != "neutral"]
data['text'] = data['text'].apply(lambda x: x.lower())
data['text'] = data['text'].apply((lambda x: re.sub('[^a-zA-z0-9\s]','',x)))

print('total data size: '+str(int(data.size/2)))
print('size of positive data: '+str(int((data[ data['airline_sentiment'] == 'positive'].size)/2)))
print('size of negative data: '+str(int((data[ data['airline_sentiment'] == 'negative'].size)/2)))

#removing retweets
for idx,row in data.iterrows():
    row[0] = row[0].replace('rt',' ')

#vectorize the text and get features max word set at 2000  
max_features = 2000
tokenizer = Tokenizer(num_words=max_features, split=' ')
tokenizer.fit_on_texts(data['text'].values)
X = tokenizer.texts_to_sequences(data['text'].values)
X = pad_sequences(X)

#
Y = pd.get_dummies(data['airline_sentiment']).values
#splitting up train, test and validation set
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.33, random_state = 20)
print(X_train.shape,Y_train.shape)
print(X_test.shape,Y_test.shape)

#validation set
validation_size = 3000
X_validate = X_test[-validation_size:]
Y_validate = Y_test[-validation_size:]
X_test = X_test[:-validation_size]
Y_test = Y_test[:-validation_size]

# #RNN (LSTM layers) setup using Keras
embed_dim = 128
nodes = 100

model = Sequential()
model.add(Embedding(max_features, embed_dim,input_length = X.shape[1]))

# # #model:1 deep
# model.add(LSTM(10, return_sequences=True))
# model.add(LSTM(10, return_sequences=True))
# model.add(LSTM(10, return_sequences=True))
# model.add(LSTM(10, return_sequences=True))
# model.add(LSTM(10, return_sequences=True))

# model.add(LSTM(10, return_sequences=True))
# model.add(LSTM(10, return_sequences=True))
# model.add(LSTM(10, return_sequences=True))
# model.add(LSTM(10, return_sequences=True))
# model.add(LSTM(10, return_sequences=True))

# model.add(LSTM(10, return_sequences=True))
# model.add(LSTM(10, return_sequences=True))
# model.add(LSTM(10, return_sequences=True))
# model.add(LSTM(10, return_sequences=True))
# model.add(LSTM(10, return_sequences=True))

# model.add(LSTM(10, return_sequences=True))
# model.add(LSTM(10, return_sequences=True))
# model.add(LSTM(10, return_sequences=True))
# model.add(LSTM(10, return_sequences=True))
# model.add(LSTM(10, return_sequences=True))

# model.add(LSTM(10, return_sequences=True))
# model.add(LSTM(10, return_sequences=True))
# model.add(LSTM(10, return_sequences=True))
# model.add(LSTM(10, return_sequences=True))
# model.add(LSTM(10,))

#model:2 wide
# model.add(LSTM(100, return_sequences=True))
# model.add(LSTM(100, return_sequences=True))
# model.add(LSTM(100))

#model:3 deep and wide with dropout= .2 nodes = 100
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))

# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))

# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))

# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))

# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.2, dropout_W=0.2))
# model.add(LSTM(nodes, dropout_U=0.2, dropout_W=0.2))

##model:4 wide with dropout=.2
# model.add(LSTM(100, return_sequences=True, dropout_U=0.4, dropout_W=0.4))
# model.add(LSTM(100, return_sequences=True,dropout_U=0.4, dropout_W=0.4))
# model.add(LSTM(100, dropout_U=0.4, dropout_W=0.4))

##model:5 deep and wide dropout = .4
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.4, dropout_W=0.4))
# model.add(LSTM(nodes, return_sequences=True,dropout_U=0.4, dropout_W=0.4))
# model.add(LSTM(nodes, return_sequences=True,dropout_U=0.4, dropout_W=0.4))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.4, dropout_W=0.4))
# model.add(LSTM(nodes, return_sequences=True,dropout_U=0.4, dropout_W=0.4))

# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.4, dropout_W=0.4))
# model.add(LSTM(nodes, return_sequences=True,dropout_U=0.4, dropout_W=0.4))
# model.add(LSTM(nodes, return_sequences=True,dropout_U=0.4, dropout_W=0.4))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.4, dropout_W=0.4))
# model.add(LSTM(nodes, return_sequences=True,dropout_U=0.4, dropout_W=0.4))

# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.4, dropout_W=0.4))
# model.add(LSTM(nodes, return_sequences=True,dropout_U=0.4, dropout_W=0.4))
# model.add(LSTM(nodes, return_sequences=True,dropout_U=0.4, dropout_W=0.4))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.4, dropout_W=0.4))
# model.add(LSTM(nodes, return_sequences=True,dropout_U=0.4, dropout_W=0.4))

# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.4, dropout_W=0.4))
# model.add(LSTM(nodes, return_sequences=True,dropout_U=0.4, dropout_W=0.4))
# model.add(LSTM(nodes, return_sequences=True,dropout_U=0.4, dropout_W=0.4))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.4, dropout_W=0.4))
# model.add(LSTM(nodes, return_sequences=True,dropout_U=0.4, dropout_W=0.4))

# model.add(LSTM(nodes, return_sequences=True,dropout_U=0.4, dropout_W=0.4))
# model.add(LSTM(nodes, return_sequences=True, dropout_U=0.4, dropout_W=0.4))
# model.add(LSTM(nodes, return_sequences=True,dropout_U=0.4, dropout_W=0.4))
# model.add(LSTM(nodes, return_sequences=True,dropout_U=0.4, dropout_W=0.4))
# model.add(LSTM(nodes, dropout_U=0.4, dropout_W=0.4))

##model:6 wide network with L1/L2 and dropout
# model.add(LSTM(100, recurrent_dropout=0.4, dropout=0.4, return_sequences=True, kernel_regularizer=l2(0.01)))
# model.add(LSTM(100, recurrent_dropout=0.4, dropout=0.4, return_sequences=True, kernel_regularizer=l2(0.01)))
# model.add(LSTM(100, recurrent_dropout=0.4, dropout=0.4, kernel_regularizer=l2(0.01)))

##model:7 wide network with l1 = .01
model.add(LSTM(100, recurrent_dropout=0.4, dropout=0.4, return_sequences=True, kernel_regularizer=l1(0.01)))
model.add(LSTM(100, recurrent_dropout=0.4, dropout=0.4, return_sequences=True, kernel_regularizer=l1(0.01)))
model.add(LSTM(100, recurrent_dropout=0.4, dropout=0.4, kernel_regularizer=l1(0.01)))

##model:8 wide network with dropout using relu function
# model.add(LSTM(100, activation = 'relu', dropout=0.5, return_sequences=True))
# model.add(LSTM(100, activation = 'relu', dropout=0.5, return_sequences=True))
# model.add(LSTM(100, activation = 'relu', dropout=0.5))

##model:9 wide network with l1 and l2 = .01
# model.add(LSTM(100, return_sequences=True, kernel_regularizer=l1_l2(0.01)))
# model.add(LSTM(100, return_sequences=True, kernel_regularizer=l1_l2(0.01)))
# model.add(LSTM(100, kernel_regularizer=l1_l2(0.01)))

#model:10 small network with dropout
# model.add(LSTM(10, dropout=0.5, return_sequences=True))
# model.add(LSTM(10, dropout=0.5, return_sequences=True))
# model.add(LSTM(10, dropout=0.5))

model.add(Dense(2,activation='softmax'))

model.compile(loss = 'categorical_crossentropy', optimizer='adam',metrics = ['accuracy'])
print(model.summary())


batch_size = 100
model.fit(X_train, Y_train, epochs = 20, batch_size=batch_size, verbose = 2)


#evaluate model with test data
score,acc = model.evaluate(X_test, Y_test, verbose = 2, batch_size = batch_size)
print("score: %.4f" % (score))
print("acc: %.4f" % (acc))