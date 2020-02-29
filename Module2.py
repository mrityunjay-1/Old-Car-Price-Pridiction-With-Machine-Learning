import pandas as pd
data = pd.read_csv('trained_data2.csv', header = 0)
features = []

for i in range(len(data)):
    x = list(data.iloc[i])             # data is come in the form of row
    x.pop()                            # pop last value because it is the Label(Result)
    features.append(x)


label = list(data.Price)
print(features)                        # this contains the features of the object
print(label)                           # this contains the label means the result

# now very simply i perform the machine Learning funtion to predict the Price Using sklearn

from sklearn import tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, label)

print(clf.predict([[3.5, 6.0, 225.0, 18.0, 24.0, 3880.0, 115.0, 197.0, 16605.0]]))
