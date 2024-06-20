# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 17:39:53 2024

@author: sekha
"""
# the programe about tip calculation 
x=str(input("how much was the meal?:\t"))
x1=x.split('.')[0]
#print(x1)
y=''.join(letter for letter in x1 if letter.isalnum())
z=float(y)
#print(z)
per=str(input("what percentage would you like to tip\t"))
p=''.join(letter for letter in per if letter.isalnum())
q=float(p)
#print(q)
pers=(q*z)/100
print("Leave", "$%.2f"%(pers))
