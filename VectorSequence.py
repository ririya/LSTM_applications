from __future__ import print_function
import numpy as np
import math as math
import functions as func


from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import LSTM
from keras.optimizers import RMSprop
from keras.utils.data_utils import get_file
import numpy as np
import random
import sys

seqLen = 5
N = 10000
offset = 0

Xlong = np.zeros(N)
Xlong[0] = 1
Xlong[1] = 2
# Xlong = repmat(Xlong, 1, N)

#b = func.doSomething(1)

for i in range(2,N):
    Xlong[i] = Xlong[i-1] + Xlong[i-2]
    if abs(Xlong[i]) > 4:
        Xlong[i] = -Xlong[i]


Xlong = np.matlib.repmat(Xlong, 3, 1)

#start_index = random.randint(0, len(Xlong) - seqLen - 1)
#Xlong = np.roll(Xlong,-start_index)

vmap = np.unique(Xlong)
vocabSize = vmap.shape[0]

dict_value_ind = dict((v, i) for i, v in enumerate(vmap))
dict_ind_value = dict((i, v) for i, v in enumerate(vmap))

#Xmap = func.getXmap(Xlong, vmap, vocabSize, seqLen, offset)
#offset = seqLen;
#Ymap = func.getXmap(Xlong, vmap, vocabSize, 1, offset)

step = 1

sentences = []
next_chars = []

dim = Xlong.shape[0]

for i in range(0, Xlong.shape[1] - seqLen, step):
    sentences.append(Xlong[:,i: i + seqLen])
    next_chars.append(Xlong[:,i + seqLen])
print('nb sequences:', len(sentences))

# X = np.zeros((len(sentences), seqLen, vocabSize), dtype=np.bool)
# y = np.zeros((len(sentences), vocabSize), dtype=np.bool)
X = np.zeros((len(sentences), seqLen, dim))
y = np.zeros((len(sentences), dim))

for i, sentence in enumerate(sentences):
    # for t, char in enumerate(sentence):
    for t in range(0, seqLen):
        # X[i, t, dict_value_ind[char]] = 1
        # y[i, dict_value_ind[next_chars[i]]] = 1
        char = sentence[:,t]
        X[i, t, :] = char
        y[i, :] = next_chars[i]

# build the model: a single LSTM
print('Build model...')
model = Sequential()
# model.add(LSTM(128, input_shape=(seqLen, vocabSize)))
model.add(LSTM(128, input_shape=(seqLen, dim)))
model.add(Dense(3))
# model.add(Dense(vocabSize))
# model.add(Activation('softmax'))
model.add(Activation('sigmoid'))


optimizer = RMSprop(lr=0.01)
model.compile(loss='categorical_crossentropy', optimizer=optimizer)

#numIt = 60;
#numIt = 2;
#for iteration in range(1, numIt):

#print()
#print('-' * 50)
#print('Iteration', iteration)
model.fit(X, y, batch_size=128, nb_epoch=3)

#start_index = random.randint(0, len(Xlong) - seqLen - 1)

start_index = 0

# generated = ''
# sentence = Xlong[start_index: start_index + seqLen]
generated = []
sentence = []
for currX in Xlong[start_index:start_index+seqLen]:
    sentence.append(currX)
    generated.append(currX)
# generated += sentence

# print('----- Generating with seed: "' + sentence + '"')
# sys.stdout.write(generated)

for i in range(N-seqLen):
    x = np.zeros((1, seqLen, vocabSize))
    for t, char in enumerate(sentence):
        x[0, t, dict_value_ind[char]] = 1.

    preds = model.predict(x, verbose=0)[0]
    # next_index = sample(preds, diversity)
    next_index = np.argmax(preds)
    next_char = dict_ind_value[next_index]

    # generated += next_char
    # sentence = sentence[1:] + next_char

    # generated = np.append(generated,  next_char)
    generated.append(next_char)
    sentence = generated[-seqLen:]

    pass

       # sys.stdout.write(next_char)
       #sys.stdout.flush()
    #print()

generatedArray = np.asarray(generated)

errors = Xlong - generatedArray
sumErrors = sum(abs(errors))

pass