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
for lst in urlList:
    
    letter = lst[1]
    #print(lst[0])

        #vals is the function that analyses each image and calculates each relevant feature
    
    vals = GetVals.func(bigDF, lst[0])
    #print(vals)
    lst[1] = vals[0]
    lst.append(vals[1])
    lst.append(vals[2])
    lst.append(vals[3])
    lst.append(vals[4])
    lst.append(letter)
    #print(lst)
       # this block writes the results to the brightness data csv file where all relevant stats are kept
    with open('Brightness_Data_Copy.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(lst)
newList = []

df = pd.DataFrame(urlList, columns=['URL', 'Median', '90th Percentile', 'Mean', 'versions', 'version2', 'ClearSky'])
df.to_csv("./Brightness_Data_Copy.csv", sep = ',', index = False)


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



# newList = []


# for q in range(len(y)):
#     if y[q] == 'N':
#         newList.append(0)
#     else:
#         newList.append(1)

# res =[]
# indicies = []
# for d in range(len(bigDF.index)):
#     b = bigDF.iloc[d].to_numpy()
#     #print(b)
#     #print(np.corrcoef(newList, b))
#     if np.corrcoef(newList, b)[0][1] <= -0.55:
#         print(d)
#         indicies.append(d)
#         print(np.corrcoef(newList, b)[0][1])
#         res.append(np.corrcoef(newList, b)[0][1])
# #print(res.index(min(res)))
# print(res) #All the following dated sept 23: after data pruning, best features are 1/449 at -0.69089 and 449/157050 at -0.6450 for negatives. There are a ton of positives > 0.55, but use those only if necessary. For positives >0.6, we have 453/157494 at 0.6310, 7199/150751 at 0.60578, and 8549/150751 at 0.6044
# print(indicies) #1, 449, 450, 157050 for <= -0.55, 450 = [1][0] of the fourier transform, 157050 = [349][0]. For >= 0.5, we have 453, 7199 at .5449505 and .5302 (.53019) 8549 at 0.5300 (.5296682). Two indicators from < -0.55, is 1 at -0.58547 and 450/157050 at -0.59064
max_score = 0.0
avg = []
for j in range(3,7):
    summ = 0
    for i in range(1, 10000):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=j/10, random_state=i) #split the dataset into a test/train duo for fitting (60% of data) and evaluating fit quality (40% of data). Consistent random state is used to ensure testing is consistent 
        #k_range = list(range(1,26)) #this list is used to generate a plot of the test accuracy depending on the number of nearest neighbors (k). 25 is chosen as the limit rather arbitrarily, but anything beyond 25 is usually victim to overfitting
        scores = []
        trainingScores = []


        #As an alternative to the KNN 'lazy' prediction, this block tests logistic regression on the same train/test set as knn
        cw = {'Y': 1.0, 'N': 1.4}
        ##try 1.75 on the larger set of 100000
        logr = LogisticRegression(class_weight=cw)
        try:
            logr.fit(x_train, y_train)
        except ValueError as e:
            continue
        y_pred = logr.predict(x_test)
        y_test_pred = logr.predict(xTest)
        curr_score = metrics.accuracy_score(y_test, y_pred)
        summ += curr_score
        if curr_score > max_score:
            max_score = curr_score
            curr_best2 = i
            curr_best = j
    totalAvg = summ/9999
    avg.append([totalAvg, j])
print(max_score)
print(curr_best)
print(curr_best2)
print(avg)
print(y.shape)
print(y_pred.shape)
print('logr accuracy: ' + str(metrics.accuracy_score(y_test, y_pred)))
print(y_pred)
print(y_test)
# for i in range(len(y_test)):
#     if y_pred[i] != y_test.iloc[i]:
#       #  print(x_test)
#     # print(y_test)
#      #   print(y_pred)
#         print('true val: ' + str(y_test.iloc[i]))
#         print('predicted val: ' + str(y_pred[i]))
#         print(x_test.iloc[i])
#         print(i)
# ROC Curve Display Section

plt.rcParams.update({'font.size': 15})
RocCurveDisplay.from_estimator(logr, x, y)
plt.show()

#Confusion Matrix Display
cm = confusion_matrix(y, logr.predict(x), normalize='true')
disp = ConfusionMatrixDisplay(cm, display_labels=['cloudy', 'clear'])
disp.plot()
plt.show()