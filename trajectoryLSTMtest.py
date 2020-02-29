from __future__ import print_function
import numpy as np
np.random.seed(1337)  # for reproducibility

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Activation, Embedding, Masking
from keras.layers import LSTM, GRU, SimpleRNN
from keras.datasets import imdb

max_features = 20000
maxlen = 80  # cut texts after this number of words (among top max_features most common words)
batch_size = 32

numSeq = 2000;
halfNumSeq = int(numSeq/2)

print('Loading data...')
#(X_train, y_train), (X_test, y_test) = imdb.load_data(nb_words=max_features)
#print(len(X_train), 'train sequences')
#print(len(X_test), 'test sequences')

#print('Pad sequences (samples x time)')
#X_train = sequence.pad_sequences(X_train, maxlen=maxlen)
#X_test = sequence.pad_sequences(X_test, maxlen=maxlen)
#print('X_train shape:', X_train.shape)
#print('X_test shape:', X_test.shape)

lowClass0 = -10
highClass0 = 10

lowClass1 = -2
highClass1 = 2

#X_train = []   #np.zeros(2,numSamples)
y_train = np.ones(numSeq)
y_train[:halfNumSeq] = 0
# y_train = []

# X_test = []
y_test = np.ones(numSeq)
y_test[:halfNumSeq] = 0
# y_test = []

seqLen = 100
nDim = 2

# for s in range(halfNumSeq):
#
#     #for p in range(seqLen):
#
#     # x1 = np.random.randint(lowClass0, highClass0)
#     #  x2 = np.random.randint(lowClass0, highClass0)
#     # X.append([x1, x2])
#     currX = np.random.randint(lowClass0, highClass0, [nDim,seqLen])
#     currXtest = np.random.randint(lowClass0, highClass0, [nDim, seqLen])
#     X_train.append(currX)
#     X_test.append(currXtest)
#
#     y_train.append(0)
#     y_test.append(0)
#     # y_train[s] = 0
#     # y_test[s] = 0

# for s in range(halfNumSeq):
#
#    # for p in range(seqLen):
#         # x1 = np.random.randint(lowClass1, highClass1)
#         # x2 = np.random.randint(lowClass1, highClass1)
#         # X.append([x1, x2])
#
#     currX = np.random.randint(lowClass1, highClass1, [nDim, seqLen])
#     currXtest = np.random.randint(lowClass1, highClass1, [nDim, seqLen])
#     X_train.append(currX)
#     X_test.append(currXtest)
#
#     y_train.append(0)
#     y_test.append(0)
#
#
#     # y_train[s + halfNumSeq] = 1
#     # y_test[s + halfNumSeq] = 1

X_train0 = np.random.randint(lowClass0, highClass0, [halfNumSeq, seqLen,nDim])
X_train1 = np.random.randint(lowClass1, highClass1, [halfNumSeq, seqLen,nDim])

# X_train0 = lowClass0 + (highClass0 - lowClass0) * np.random.random([halfNumSeq, seqLen,nDim])
# X_train1 = lowClass1 + (highClass1 - lowClass1) * np.random.random([halfNumSeq, seqLen,nDim])

X_train = np.concatenate((X_train0, X_train1))

X_test0 = lowClass0 + (highClass0 - lowClass0) * np.random.random([halfNumSeq, seqLen,nDim])
X_test1 = lowClass1 + (highClass1 - lowClass1) * np.random.random([halfNumSeq, seqLen,nDim])
X_test = np.concatenate((X_test0, X_test1))

print('Build model...')
model = Sequential()
#model.add(Embedding(max_features, 128, dropout=0.2))
model.add(Masking(mask_value=0., input_shape=(seqLen, nDim)))
model.add(GRU(128, dropout_W=0.2, dropout_U=0.2))  # try using a GRU instead, for fun
#model.add(LSTM(128, input_shape=(seqLen, nDim)))
model.add(Dense(1))
model.add(Activation('sigmoid'))

# try using different optimizers and different optimizer configs
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

print('Train...')

model.fit(X_train, y_train, batch_size=batch_size, nb_epoch=3,
          validation_data=(X_test, y_test))
score, acc = model.evaluate(X_test, y_test,
                            batch_size=batch_size)

# model.fit(X, Y, batch_size=batch_size, nb_epoch=5, validation_split=0.5)
# score, acc = model.evaluate(Xtest, Ytest, batch_size=batch_size)
print('Test score:', score)
print('Test accuracy:', acc)
