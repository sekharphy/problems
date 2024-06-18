# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 17:56:01 2024

@author: sekha
"""

#play back programme on 
x="This is CS50"
y="This is our week on functions"
z="Let's implement a function called hello"
def playback(x,y,z):
    for item in x,y,z:
        x1=x.replace(' ','...')
        y1=y.replace(' ','...')
        z1=z.replace(' ','...')
    print( x1,'\n',y1,'\n',z1)

playback(x,y,z)