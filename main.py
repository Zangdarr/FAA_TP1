#! /usr/bin/env python2
#coding=utf-8

#############################
# Calcul du modèle linéaire #
#############################


#librairie de gestion de matrices
import numpy as np
#récupération des matrices
x = np.loadtxt("t.txt")
y = np.loadtxt("p.txt")

#création d'une matrice de, longueur de x, 1
xbis = np.ones((len(x)))
#print xbis

#concaténation des matrice x et xbis
xfinal = np.vstack((x,xbis))
#print xfinal

#multiplication de xfinal et de sa transposé
mul_x_xT = np.dot(xfinal,xfinal.T)
#print mul_x_xT

#inversion de la matrice mul_x_xT
inv_mul_x_xT = np.linalg.inv(mul_x_xT)
#print inv_mul_x_xT

#multiplication des matrices x et y
mul_x_y = np.dot(xfinal,y)
#print mul_x_y

#multiplication de l'inversion et mul_x_y
mul_inv_xy = np.dot(inv_mul_x_xT, mul_x_y)
print mul_inv_xy




##########################
# Affichage de la droite #
##########################


import pylab as pl
pl.plot(mul_inv_xy)
#pl.plot(x,y)




##########################################
# Calcul de l'erreur moyenne quadratique #
##########################################

