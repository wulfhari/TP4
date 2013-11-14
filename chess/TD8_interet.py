#! /usr/bin/env python
# -*- coding:Utf-8 -*-

'''
Created on 2013-10-21

@author: C. Besse
'''

from tkinter import *

class Interet:
    '''
    Fenetre pour l'affichage de notre premier TP.
    '''
    def __init__(self):
        '''
        Initialise les différents éléments
        '''
        # Création de la fenêtre
        root = Tk()
        # Création des 3 Labels + entry
        Label(root, text="Montant Initial", width=20,anchor=W).grid(row=0, column=0, sticky=W)
        self.sb = Entry(root, width=25)
        self.sb.insert(0,"1000")
        self.sb.grid(row=0, column=1, sticky=E+W)
        
        Label(root, text="Nombre Années", width=20,anchor=W).grid(row=1, column=0, sticky=W)
        self.na = Entry(root, width=25)
        self.na.insert(0, "12")
        self.na.grid(row=1, column=1, sticky=E+W)
        
        Label(root, text="Taux", width=20,anchor=W).grid(row=2, column=0, sticky=W)
        self.tx = Entry(root, width=25)
        self.tx.insert(0,"5")
        self.tx.grid(row=2, column=1, sticky=E+W)
        # Création du bouton effacant le text
        self.btn = Button(root, text="Clear",command=self.clear)
        self.btn.grid(row=3,column=0,sticky=E+W)           
        # Création du bouton déclanchant le calcul
        self.btn = Button(root, text="Calculer",command=self.calcul)
        self.btn.grid(row=3,column=1,sticky=E+W)           
        # Création de l'affichage
        self.txt = Text(root, height=25, width=100, wrap=WORD)
        self.txt.grid(row=5,columnspan=2,sticky=NSEW)
        # Création de la scrollbar
        sc = Scrollbar(root,orient=VERTICAL) 
        ## association du déplacement de la glissière des scrollbar avec la position visible dans 
        ## le widget Text et inversement.              
        sc.config(command = self.txt.yview)
        self.txt.config(yscrollcommand = sc.set)
        sc.grid(row=5,column=2,sticky=NSEW)
        # Maintient de l'affichage
        root.mainloop()
        
    def clear(self):
        # On efface le text widget
        self.txt.delete(1.0, END)
        
    def calcul(self):
        # On efface le text widget
        self.txt.delete(1.0, END)
        
        startBalance = float(self.sb.get())
        years = int(self.na.get())
        rate = int(self.tx.get())
        # Conversion du taux au format décimal
        rate = rate / 100.0
        
        # Initialisation de l'accumulateur d'intérêt.
        totalInterest = 0.0
        
        # Affichage de l'en-tête de la table
        self.txt.insert(END,"{0:8}{1:>20}{2:>13}{3:>18}\n".format("Année", "Montant initial", "Intérêt", "Montant final"))
        
        # Calcule et affiche le résultat pour chaque année
        for year in range(1, years + 1):
            interest = startBalance * rate
            endBalance = startBalance + interest
            self.txt.insert(END,"{0:8}{1:20.2f}{2:13.2f}{3:18.2f}\n".format(year, startBalance, interest, endBalance))
            startBalance = endBalance
            totalInterest += interest
        
        # Affiche les résultats finaux.
        self.txt.insert(END,"Montant après {0} années : ${1:0.2f}\n".format(years, endBalance))
        self.txt.insert(END,"Intérêt total gagné : ${0:0.2f}\n".format(totalInterest))



if(__name__ == "__main__"):
    Interet()
