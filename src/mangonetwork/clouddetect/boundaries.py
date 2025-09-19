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

urlList = getUrls.getURL()

# for lst in urlList:
    
#     letter = lst[1]
#     #print(lst[0])
#     vals = GetVals.func(lst[0])
#     lst[1] = vals[0]
#     lst.append(vals[1])
#     lst.append(vals[2])
#     lst.append(letter)
#     with open('Brightness_Data_Copy.csv', 'w', newline='') as myfile:
#         wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#         wr.writerow(lst)


# df = pd.DataFrame(urlList, columns=['URL', 'Median', '90th Percentile', 'Mean', 'ClearSky'])
# df.to_csv("./Brightness_Data_Copy.csv", sep = ',', index = False)


data = pd.read_csv("Brightness_Data_Copy.csv")
x = data.drop(['ClearSky'], axis=1)
x = x.drop(['URL'], axis = 1)
y = data['ClearSky']



x = np.asarray(x)

y = np.asarray(y)
cmap_light = ListedColormap(["cyan", "orange"])
cmap_bold = ["darkorange", "c"]

n_neighbors = 8
X = x[:, [0, 1]]
for weights in ["uniform", "distance"]:
    clf = LogisticRegression()
    # print(X.shape)
    # print(y.shape)
    clf.fit(X, y)
    _, ax = plt.subplots()
    DecisionBoundaryDisplay.from_estimator(clf, X, cmap=cmap_light, ax=ax, response_method="predict", plot_method="pcolormesh", shading="auto", xlabel="Mean Pixel Brightness", ylabel="Fourier Feature 453")
    sns.scatterplot(x=X[:, 0], y=X[:, 1], palette=cmap_bold, alpha=1.0, edgecolor="black", hue=data['ClearSky'])

plt.show()
#improved speed
#got svm up
#tried new params
#started getting ready for practical application
#dataset expansion
