# -*- coding: utf-8 -*-
"""Mini Projet Algorithmes Python

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ruY7T1OOqy_gD_ROZ0e74jKF8XC9PESG
"""

# Exercice 1:

print("Hello, world!")

#Exercice2:

nombre = int(input("Entrez un nombre : "))
print("Le double de votre nombre est :",nombre * 2)

#Exercice3:

nombre1 = int(input("Entrez le premier nombre :"))
nombre2 = int(input("Entrez le second nombre :"))
print("La somme des deux nombres est:", nombre1 + nombre2)

#Exercice 4:

nombre = int(input("Entrez un nombre entier : "))
if nombre % 2 == 0:
    print("Le nombre est pair.")
else:
    print("Le nombre est impair.")

#Exercice5:
nombre = int(input("Entrez un nombre entier : "))
for i in range(1, nombre + 1):
    print(i)

#Exercice6:

chaine = input("Entrez une chaîne de caractères : ")
for char in chaine:
    print(char)

#Exercice7:
chaine = input("Entrez une chaîne de caractères : ")
print("La chaîne en majuscules est :", chaine.upper())

#Exercice 8:
mot = input("Entrez un mot : ")
if mot == mot[::-1]:
    print("Le mot est un palindrome.")
else:
    print("Le mot n'est pas un palindrome.")

#Exercice9:
nombre = int(input("Entrez un nombre entier : "))
for i in range(1, 11):
    print(f"{nombre} x {i} = {nombre * i}")

#Exercice10:

liste = input("Entrez une liste de nombres séparés par des espaces : ")
nombres = list(map(int, liste.split()))
print("La somme des nombres est :", sum(nombres))