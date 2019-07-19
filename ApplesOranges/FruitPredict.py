from sklearn import tree

features = [[140, 1], [130, 1], [150, 0], [170, 0]] # 0=bumpy 1=smooth INPUT
labels = [0, 0, 1, 1 ]       # 0 = apple     1 = orange   OUTPUT

clf = tree.DecisionTreeClassifier()  #classifier

clf = clf.fit(features, labels)     #learning algorythim

print (clf.predict([[150,0]]))


