from sklearn import tree

features = [[140, 1], [130, 1], [150, 0], [170, 0]] # 0=bumpy 1=smooth INPUT
labels = ["apple", "apple", "oranges", "oranges" ]       #    OUTPUT

clf = tree.DecisionTreeClassifier()  #classifier

clf = clf.fit(features, labels)     #learning algorythim

print()
print (clf.predict([[150,0]]))
print()


