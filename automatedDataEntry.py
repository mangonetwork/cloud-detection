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


##SECTION 2: 

data = pd.read_csv("Brightness_Data_Copy.csv") #load the existing csv into a data variable

x = data.drop(['ClearSky'], axis=1) #drop the classification column from the dataset 
urlCol = x['URL'] 
x = x.drop(['URL'], axis = 1) #drop the url column from the dataset
y = data['ClearSky'] #save the classification column as a variable

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=0) #split the dataset into a test/train duo for fitting (60% of data) and evaluating fit quality (40% of data). Consistent random state is used to ensure testing is consistent 
k_range = list(range(1,26)) #this list is used to generate a plot of the test accuracy depending on the number of nearest neighbors (k). 25 is chosen as the limit rather arbitrarily, but anything beyond 25 is usually victim to overfitting
scores = []
trainingScores = []


#As an alternative to the KNN 'lazy' prediction, this block tests logistic regression on the same train/test set as knn
cw = {'Y': 0.9, 'N': 1.5}
logr = LogisticRegression(class_weight=cw)
logr.fit(x_train, y_train)
y_pred = logr.predict(x_test)
print('logr accuracy: ' + str(metrics.accuracy_score(y_test, y_pred)))

#ROC Curve Display Section
RocCurveDisplay.from_estimator(logr, x_test, y_test)
plt.show()

#Confusion Matrix Display
cm = confusion_matrix(y_test, logr.predict(x_test), normalize='true')
disp = ConfusionMatrixDisplay(cm, display_labels=['cloudy', 'clear'])
disp.plot()
plt.show()