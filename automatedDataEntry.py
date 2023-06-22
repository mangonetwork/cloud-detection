import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
import getUrls
import GetVals
import csv
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn import neighbors, datasets
from matplotlib.colors import ListedColormap
import math
import viewImage


urlList = getUrls.getURL()

for lst in urlList:
    
    letter = lst[1]
    #print(lst[0])
    vals = GetVals.func(lst[0])
    lst[1] = vals[0]
    lst.append(vals[1])
    lst.append(vals[2])
    lst.append(letter)
    # with open('Brightness_Data_Copy.csv', 'w', newline='') as myfile:
    #     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    #     wr.writerow(lst)


df = pd.DataFrame(urlList, columns=['URL', 'Median', '90th Percentile', '10th Percentile', 'ClearSky'])
df.to_csv("./Brightness_Data_Copy.csv", sep = ',', index = False)


data = pd.read_csv("Brightness_Data_Copy.csv")
x = data.drop(['ClearSky'], axis=1)
urlCol = x['URL']
x = x.drop(['URL'], axis = 1)
y = data['ClearSky']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=3)
k_range = list(range(1,26))
scores = []
trainingScores = []
for k in k_range:
    
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    scores.append(metrics.accuracy_score(y_test, y_pred))

    knnTrain = KNeighborsClassifier(n_neighbors=k)
    knnTrain.fit(x_train, y_train)
    train_pred = knnTrain.predict(x_train)
    trainingScores.append(metrics.accuracy_score(y_train, train_pred))

plt.figure()
plt.plot(k_range, scores, 'k.-')
plt.xlabel('Range of k [1-25]')
plt.ylabel('Accuracy given k')
#plt.show()

plt.figure()
plt.plot(k_range, trainingScores, 'k.-')
plt.xlabel('Range of k [1-25]')
plt.ylabel('Training Accuracy given k')
#plt.show()

knn = KNeighborsClassifier(n_neighbors=8)
knn.fit(x_train, y_train)


u = knn.predict(x_test)
print(y_test.keys())
counter = 0
misClassList = []
for i in y_test.keys():
    if u[counter] == y_test[i]:
        continue
        #print("CORRECT: ", x_test.iloc[counter])
    else:
        misClassList.append(urlCol[counter])
        print(y_test[i])
        print(u[counter])
    counter+=1
print(u)
print(scores)
print(k_range)
viewImage.ViewIncorrect(misClassList)