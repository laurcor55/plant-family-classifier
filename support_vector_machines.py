
from sklearn import svm
import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction import text
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, plot_confusion_matrix

import lib
import seaborn as sns


family_names = ['convolvulaceae', 'violaceae', 'solanaceae', 'lamiaceae', 'asteraceae', 'brasicaceae']
(X, Y) = lib.import_data(family_names)
my_stop_words = text.ENGLISH_STOP_WORDS.union(['book'])
vectorizer = TfidfVectorizer(stop_words=my_stop_words)
vectors = vectorizer.fit_transform(X)
vectors_train, vectors_test, Y_train, Y_test = train_test_split(vectors, Y, test_size=0.1)

model = svm.SVC(kernel='linear')
model.fit(vectors_train, Y_train)

words = vectorizer.get_feature_names()

Y_test_predicted = model.predict(vectors_test)
accuracy = accuracy_score(Y_test, Y_test_predicted)
print(accuracy)

mat = plot_confusion_matrix(model, vectors_test, Y_test, normalize='pred')
plt.xlabel("true labels")
plt.ylabel("predicted label")
plt.show()

mat = plot_confusion_matrix(model, vectors_train, Y_train, normalize='pred')
plt.xlabel("true labels")
plt.ylabel("predicted label")
plt.show()