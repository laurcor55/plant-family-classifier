from sklearn.feature_extraction import text
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def import_descriptions(family_name):
  file_name = 'family_descriptions/' + family_name + '.txt'
  f = open(file_name, "r")
  content = f.read()
  descriptions = content.split('\n')
  descriptions = [description for description in descriptions if len(description)>3]
  return descriptions

def import_data(family_names):
  
  X = []
  Y = []
  for family_name in family_names:
    descriptions = import_descriptions(family_name)
    print(family_name + ': ' + str(len(descriptions)))
    X.extend(descriptions)
    Y.extend([family_name]*len(descriptions))
  return X, Y

