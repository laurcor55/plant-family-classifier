from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import  accuracy_score, plot_confusion_matrix
import numpy as np
import lib


def show_key_words(vectorizer, model):
  words = vectorizer.get_feature_names()
  probabilities = np.exp(model.feature_log_prob_)
  family_names = model.classes_
  for ii, family_name in enumerate(family_names):
    max_inds = np.argsort(probabilities[ii, :])[-100:]
    max_words = [words[max_ind] for max_ind in max_inds]
    print('___________')
    print(family_name)
    print(max_words)
  sns.heatmap(probabilities[:, 500:600], xticklabels=words[500:600], yticklabels=family_names)
  plt.show()

sns.set()

family_names = ['convolvulaceae', 'violaceae', 'solanaceae', 'lamiaceae', 'asteraceae', 'brasicaceae']
(X, Y) = lib.import_data(family_names)

my_stop_words = text.ENGLISH_STOP_WORDS.union(['book'])

vectorizer = TfidfVectorizer(stop_words=my_stop_words)
vectors = vectorizer.fit_transform(X)
vectors_train, vectors_test, Y_train, Y_test = train_test_split(vectors, Y, test_size=0.1)

model = MultinomialNB().fit(vectors_train, Y_train)

show_key_words(vectorizer, model)

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