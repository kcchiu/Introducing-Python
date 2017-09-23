# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 20:51:30 2017

@author: kcchi
"""

from sklearn import tree

X=[[0,0],[2,2]]
y=[0.5,2.5]


clf=tree.DecisionTreeRegressor()
clf=clf.fit(X,y)
print clf.predict([[1,1]])
