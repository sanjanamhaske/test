from matplotlib.axis import YAxis
from sklearn import tree
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, y)
tree.plot_tree(clf)
X_pred = clf.predict(X)
new_var = X_pred == YAxis