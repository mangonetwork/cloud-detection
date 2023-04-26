import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
data = pd.read_csv("Brightness_Data.csv")
x = data.drop(['ClearSky'], axis=1)
x = x.drop(['URL'], axis = 1)
y = data['ClearSky']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=3)
k_range = list(range(1,26))
scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    scores.append(metrics.accuracy_score(y_test, y_pred))
plt.figure()
plt.plot(k_range, scores, 'k.-')
plt.show()
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x, y)
u = knn.predict([[2733, 3564.1, 1917]])
print(u)