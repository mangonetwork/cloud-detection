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
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn import svm
from ast import literal_eval
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import confusion_matrix
import heapq
from sklearn.metrics import RocCurveDisplay
from sklearn.preprocessing import LabelBinarizer





#getURLS is the list of URLS corresponding to images that measurements are taken from (in hdf5 format)
urlList = getUrls.getURL()
bigDF = pd.DataFrame()




##SECTION 1: USING GETVALS.PY TO ACQUIRE ALL THE NECESSARY DATA. UNCOMMENT THIS SECTION TO RECOLLECT DATA

#       this for loop is what collects the data, iteraing through GETURLS.py which is a list of the desired images
# for lst in urlList:
    
#     letter = lst[1]
#     #print(lst[0])

        #vals is the function that analyses each image and calculates each relevant feature
#     vals = GetVals.func(lst[0], bigDF)
#     #print(vals)
#     lst[1] = vals[0]
#     lst.append(vals[1])
#     lst.append(vals[2])
#     lst.append(vals[3])
#     lst.append(vals[4])
#     lst.append(letter)
#     #print(lst)
        #this block writes the results to the brightness data csv file where all relevant stats are kept
#     with open('Brightness_Data_Copy.csv', 'w', newline='') as myfile:
#         wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#         wr.writerow(lst)
# newList = []

# df = pd.DataFrame(urlList, columns=['URL', 'Median', '90th Percentile', 'Mean', 'versions', 'version2', 'ClearSky'])
# df.to_csv("./Brightness_Data_Copy.csv", sep = ',', index = False)


##END OF SECTION 1


##SECTION 2: 

data = pd.read_csv("Brightness_Data_Copy.csv") #load the existing csv into a data variable

x = data.drop(['ClearSky'], axis=1) #drop the classification column from the dataset 
urlCol = x['URL'] 
x = x.drop(['URL'], axis = 1) #drop the url column from the dataset
# x['90th Percentile'] = literal_eval(x['90th Percentile']) 
#x = preprocessing.normalize(x, axis=0)
y = data['ClearSky'] #save the classification column as a variable
# for q in range(len(y)):
#     if y[q] == 'N':
#         newList.append(0)
#     else:
#         newList.append(1)

# res =[]
# for d in range(len(bigDF.index)):
#     b = bigDF.iloc[d].to_numpy()
#     #print(b)
#     #print(np.corrcoef(newList, b))
#     if np.corrcoef(newList, b)[0][1] >= 0.55:
#          print(d)
#     res.append(np.corrcoef(newList, b)[0][1])
# print(res.index(min(res)))


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=0) #split the dataset into a test/train duo for fitting (60% of data) and evaluating fit quality (40% of data). Consistent random state is used to ensure testing is consistent 
k_range = list(range(1,26)) #this list is used to generate a plot of the test accuracy depending on the number of nearest neighbors (k). 25 is chosen as the limit rather arbitrarily, but anything beyond 25 is usually victim to overfitting
scores = []
trainingScores = []
# for k in k_range: #this loop iterates through fitting the knn function with the training data at a given k and uses it to try and classify the test dataset. Training data is also tested as a sanity check, and should alwayshave accuracy 100% at k=1
    
#     knn = KNeighborsClassifier(n_neighbors=k)
#     knn.fit(x_train, y_train)
#     y_pred = knn.predict(x_test)
#     scores.append(metrics.accuracy_score(y_test, y_pred))

#     knnTrain = KNeighborsClassifier(n_neighbors=k)
#     knnTrain.fit(x_train, y_train)
#     train_pred = knnTrain.predict(x_train)
#     trainingScores.append(metrics.accuracy_score(y_train, train_pred))

#The below block plots the test accuracy over the given range of k
# plt.figure()
# plt.plot(k_range, scores, 'k.-')  
# plt.xlabel('Range of k [1-25]')
# plt.ylabel('Accuracy given k')
# plt.show()


# #The below block plots the training accuracy over the given range of k
# plt.figure()
# plt.plot(k_range, trainingScores, 'k.-')
# plt.xlabel('Range of k [1-25]')
# plt.ylabel('Training Accuracy given k')
# plt.show()


#As an alternative to the KNN 'lazy' prediction, this block tests logistic regression on the same train/test set as knn
cw = {'Y': 0.9, 'N': 1.5}
logr = LogisticRegression(class_weight=cw)
logr.fit(x_train, y_train)
y_pred = logr.predict(x_test)
print('logr accuracy: ' + str(metrics.accuracy_score(y_test, y_pred)))

#ROC Curve Display Section
RocCurveDisplay.from_estimator(logr, x_test, y_test)
plt.show()
#print(metrics.accuracy_score(y_test, y_pred))
# RocCurveDisplay.from_predictions(y_test, y_pred, pos_label=1)
# plt.show()
#As an alternative to the KNN 'lazy' prediction, this block tests linear SVM on the same train/test set as knn
clf = svm.SVC()
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)
print(metrics.accuracy_score(y_test, y_pred))

#As an alternative to the KNN 'lazy' prediction, this block tests non-linear SVM on the same train/test set as knn
clf = svm.NuSVC(gamma='auto')
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)
print(metrics.accuracy_score(y_test, y_pred))


#knn = KNeighborsClassifier(n_neighbors=5)
#knn.fit(x_train, y_train)

#knn = KNeighborsClassifier(n_neighbors=scores.index(max(scores)))
#knn.fit(x_train, y_train)
    
cm = confusion_matrix(y_test, logr.predict(x_test), normalize='true')
disp = ConfusionMatrixDisplay(cm, display_labels=['cloudy', 'clear'])
disp.plot()
plt.show()


#The remainder of this file displays the images that were incorrectly classified when tested with a given k and prints the link to their hdf5 file for debugging
# u = knn.predict(x_test)
# #print(y_test.keys())
# counter = 0
# misClassList = []
# for i in y_test.keys():
#     if u[counter] == y_test[i]:
#         continue
#         #print("CORRECT: ", x_test.iloc[counter])
#     else:
#         misClassList.append(urlCol[i])
#         # print(y_test[i])
#         # print(u[counter])
#     counter+=1
# print(u)
# print(scores)
# print(k_range)
# viewImage.ViewIncorrect(misClassList)