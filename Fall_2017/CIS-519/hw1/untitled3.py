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


'''
X = [ [ 0 , 0 ] , [ 2 , 2 ] ]
y = [ 0 . 5 , 2 . 5 ]

c l f = t r e e . De c i s i onTr e eRe gr e s sor ( )
c l f = c l f . f i t (X, y )
c l f . p r e d i c t ( [ [ 1 , 1 ] ] )
'''
