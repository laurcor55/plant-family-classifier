import wikipedia
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, plot_confusion_matrix
import numpy as np

sns.set()

def import_descriptions(family_name):
  file_name = 'family_descriptions/' + family_name + '.txt'
  f = open(file_name, "r")
  content = f.read()
  descriptions = content.split('\n')
  descriptions = [description for description in descriptions if len(description)>3]
  return descriptions


family_names = ['convolvulaceae', 'violaceae', 'solanaceae']
X = []
Y = []
for family_name in family_names:
  descriptions = import_descriptions(family_name)
  X.extend(descriptions)
  Y.extend([family_name]*len(descriptions))

print(len(X))
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(X)
vectors_train, vectors_test, Y_train, Y_test = train_test_split(vectors, Y, test_size=0.1)

#vectors_train = vectorizer.fit_transform(X_train)
model = MultinomialNB().fit(vectors_train, Y_train)
#words = np.asarray(vectorizer.get_feature_names())
#transform = vectorizer.fit_transform(Y)

words = vectorizer.get_feature_names()
probabilities = np.exp(model.feature_log_prob_)
plot_ind = 30

for ii, family_name in enumerate(family_names):
  probs = probabilities[ii, :]
  print(probs.shape)
  max_inds = np.argsort(probs)[-100:]
  max_words = [words[max_ind] for max_ind in max_inds]
 # max_probabilities = probabilities[: , max_ind]
 # max_words = words[max_ind]

#
#vector_test = vectorizer.fit_transform(X_test)
predict_categories = model.predict(vectors_test)
correct_count = sum([predict_category == y_test for predict_category, y_test in zip(predict_categories, Y_test)])
total_count = len(Y_test)
print(correct_count/total_count)



sns.heatmap(probabilities[:, 500:600], xticklabels=words[500:600], yticklabels=family_names)
plt.show()

mat = plot_confusion_matrix(model, vectors_test, Y_test)
#sns.heatmap(mat.T, square = True, annot=True, fmt = "d", xticklabels=Y_test,yticklabels=Y_test)
plt.xlabel("true labels")
plt.ylabel("predicted label")
plt.show()