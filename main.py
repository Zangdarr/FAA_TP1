#! /usr/bin/env python2
#coding=utf-8

print '\n\nSTART\n'
#############################
#           THETA           #
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


#on a trouvé theta
theta = mul_inv_xy

print '\nValeur de Theta : '
print theta 


#############################
#    ERREUR QUADRATIQUE     #
#############################

#On calcul l'erreur quadratique moyenne pondérée à l'aidde de la formule suivante :
# (1/N)(y - theta.T * x )² CEPENDANT RAPPEL : A² = A.T*A
# => (1/N)(y - x.T * theta).T * (y - theta.T*x) 
a = y - np.dot(xfinal.T, theta)

a = np.dot(a.T, a)
errQ = (1.0/len(x)) * a

print '\nValeur de l\'erreur quadratique moyenne pondérée : '
print errQ


########################
#       F_THETA        #
########################

f_theta = np.dot(theta.T, xfinal)


#######################################
# Affichage des points et de f_theta  #
#######################################


import matplotlib.pyplot as pl
pl.xlabel('Temps')
pl.ylabel('Positions')
pl.title('TP1 - Fonction = f_theta(Temps)')
pl.plot(x,y, '*')
pl.plot(x,f_theta)
pl.grid(True)
pl.show()
print('\nLe graphe représentant la fonction F_Theta dans le temps a été tracé.')


