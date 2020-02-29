from sklearn import tree
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print("Lets Pridict the type of fruit : \n")
print("Please Enter the weight of that fruit (in gms): ")
x = eval(input())
print("\nPlease Enter the nature of that fruit (1 for bumpy, 0 for smooth): ")
y = eval(input())


arr = clf.predict([[x, y]])


if arr[0] == 1:
    print("It's Apple")
else:
    print("it's Orange")


print(type(labels))
print(type(features))



