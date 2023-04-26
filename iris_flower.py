import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
data = pd.read_csv('Iris.csv')
#get the feature data in x, the label data as y
x = data.drop(['Species'], axis=1)
x = x.drop(['Id'], axis = 1)
y = data['Species']
#plotting = sns.pairplot(data, hue='Species')
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.9, random_state=5)

#KNN Form
k_range = list(range(1,26))
scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    scores.append(metrics.accuracy_score(y_test, y_pred))

knn = KNeighborsClassifier(n_neighbors=15)
knn.fit(x, y)
u = knn.predict([[10, 9, 5, 4]])
print(u)


#logistic regression form
#logreg = LogisticRegression()
#logreg.fit(x_train, y_train)
#y_pred = logreg.predict(x_test)
#print(metrics.accuracy_score(y_test, y_pred))
#histogram
#plt.plot(k_range, scores)
#plt.xlabel('Value of k for KNN')
#plt.ylabel('Accuracy Score')
#plt.title('Accuracy Scores for Values of k of k-Nearest-Neighbors')
#plt.show()