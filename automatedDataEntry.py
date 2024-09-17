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
import testURLS
import scipy




#getURLS is the list of URLS corresponding to images that measurements are taken from (in hdf5 format)
urlList = getUrls.getURL()
bigDF = pd.DataFrame()




##SECTION 1: USING GETVALS.PY TO ACQUIRE ALL THE NECESSARY DATA. UNCOMMENT THIS SECTION TO RECOLLECT DATA

#       this for loop is what collects the data, iteraing through GETURLS.py which is a list of the desired images
# 
##END OF SECTION 1

#THIS PART DISPLAYS A SELECT FOURIER FEATURE AS A PATTERN
# lst = np.zeros((350, 450))
# lst[349, 3] = 1
# inverted = scipy.fft.ifft2(lst)
# #inverted = abs(inverted)
# inverted =  inverted.real
# plt.imshow(inverted)
# plt.show()





##SECTION 2: 

data = pd.read_csv("Brightness_Data_Copy.csv") #load the existing csv into a data variable

x = data.drop(['ClearSky'], axis=1) #drop the classification column from the dataset 
urlCol = x['URL'] 
x = x.drop(['URL'], axis = 1) #drop the url column from the dataset
y = data['ClearSky'] #save the classification column as a variable

dataTest = pd.read_csv("Brightness_Data_Test.csv") #load the existing csv into a data variable

xTest = dataTest.drop(['ClearSky'], axis=1) #drop the classification column from the dataset 
urlColTest = xTest['URL'] 
xTest = xTest.drop(['URL'], axis = 1) #drop the url column from the dataset
yTest = dataTest['ClearSky'] #save the classification column as a variable



# # newList = []


# # for q in range(len(y)):
# #     if y[q] == 'N':
# #         newList.append(0)
# #     else:
# #         newList.append(1)

# # res =[]
# # for d in range(len(bigDF.index)):
# #     b = bigDF.iloc[d].to_numpy()
# #     #print(b)
# #     #print(np.corrcoef(newList, b))
# #     if np.corrcoef(newList, b)[0][1] <= -0.55:
# #          print(d)
# #          print(np.corrcoef(newList, b)[0][1])
# #     res.append(np.corrcoef(newList, b)[0][1])
# # # #print(res.index(min(res)))

max_score = 0.0
avg = []
# for j in range(1,10):
#     summ = 0
#     for i in range(1, 10000):
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0) #split the dataset into a test/train duo for fitting (60% of data) and evaluating fit quality (40% of data). Consistent random state is used to ensure testing is consistent 
#k_range = list(range(1,26)) #this list is used to generate a plot of the test accuracy depending on the number of nearest neighbors (k). 25 is chosen as the limit rather arbitrarily, but anything beyond 25 is usually victim to overfitting
scores = []
trainingScores = []


#As an alternative to the KNN 'lazy' prediction, this block tests logistic regression on the same train/test set as knn
cw = {'Y': 1.0, 'N': 1.65}
logr = LogisticRegression(class_weight=cw)
#try:
logr.fit(x_train, y_train)
# except ValueError as e:
    # continue
y_pred = logr.predict(x_test)
y_test_pred = logr.predict(xTest)
        # curr_score = metrics.accuracy_score(y_test, y_pred)
        # summ += curr_score
        # if curr_score > max_score:
        #     max_score = curr_score
        #     curr_best2 = i
        #     curr_best = j
    # totalAvg = summ/9999
    # avg.append([totalAvg, j])
# print(max_score)
# print(curr_best)
# print(curr_best2)
# print(avg)
print(y.shape)
print(y_pred.shape)
print('logr accuracy: ' + str(metrics.accuracy_score(y_test, y_pred)))

#ROC Curve Display Section
plt.rcParams.update({'font.size': 15})
RocCurveDisplay.from_estimator(logr, x, y)
plt.show()

#Confusion Matrix Display
cm = confusion_matrix(y, logr.predict(x), normalize='true')
disp = ConfusionMatrixDisplay(cm, display_labels=['cloudy', 'clear'])
disp.plot()
plt.show()