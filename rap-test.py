import json
import numpy as np
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

with open('rap-test.json', 'r') as f:
    datastore = json.load(f)

sentences = []
labels = []

num_epochs = 30
training_size = 50
vocab_size = 10000
embedding_dim = 16
max_length = 100
trunc_type = 'post'
padding_type = 'post'

for item in datastore["root"]:
    sentences.append(item['lyric'])
    labels.append(item['is_rap'])

training_sentences = sentences[0:training_size]
testing_sentences = sentences[training_size:]
training_labels = labels[0:training_size]
testing_labels = labels[training_size:]

new_tokenizer = Tokenizer(num_words=vocab_size, oov_token='<OOV>')
new_tokenizer.fit_on_texts(training_sentences)

new_word_index = new_tokenizer.word_index

training_sequences = new_tokenizer.texts_to_sequences(training_sentences)
training_padded = pad_sequences(training_sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

testing_sequences = new_tokenizer.texts_to_sequences(testing_sentences)
testing_padded = pad_sequences(testing_sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

model = keras.Sequential([
    keras.layers.Embedding(vocab_size, 16, input_length=100),
    keras.layers.GlobalAveragePooling1D(),
    keras.layers.Dense(24, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

training_padded = np.array(training_padded)
training_labels = np.array(training_labels)
testing_padded = np.array(testing_padded)
testing_labels = np.array(testing_labels)

history = model.fit(training_padded, training_labels, epochs=num_epochs,
                    validation_data=(testing_padded, testing_labels), verbose=2)

new_sentences = ["bob wants to go take a crap", "the weather is sunny today",
                 "Ridin' in that motherfuckin' Bentley"]

new_sequences = new_tokenizer.texts_to_sequences(new_sentences)
new_sentences_padded = pad_sequences(new_sequences, maxlen=max_length, padding=padding_type, truncating=trunc_type)

print(model.predict(new_sentences_padded))
