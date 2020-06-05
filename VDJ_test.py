#!/usr/bin/env python3
#_*_coding:utf-8_*_
import os,re, sys
import time # temps d'execution (bibliothèque)

import matplotlib.pyplot as plt

from tkinter import *
import tkinter.font as tkFont
from tkinter import filedialog
#import fichier de log
import logging

#***************************************************************
logging.basicConfig(filename = 'app.log', level = logging.INFO)
#***************************************************************
#*****************************************************************************************************************************************************#
#----------------------------------------Traitement_d'un_Fichier_Pipeline_VQUEST&MIXCR-------BY_IMGT--------------------------------------------------#

# lecture du fichier issus du VDJ
# declaration des structures de données à utiliser
# dictionnaire des valeur du Vdomain
dictionnaire = {}
data=[]
listvdomain=[]
listdicovdomain=[]

# Recuperation du chemin d'entrée du fichier Pipeline

# nous allons activer le passage en paramètres

pipeline= sys.argv[1]  # le code ci nous permet de faire un passage en paramètre du fichier de pipeline

#pipeline=input("Bonjour Docteur! Entrez le chemin de votre fichier pipeline SVP...\n")

print("Veuillez patientez svp pipeline....",pipeline)

try:
  #
  if os.path.isfile(pipeline):    #si le chemin passer en paramètre est un fichier
    
  

    if re.search("(.+\.results.tsv)",pipeline): # si le fichier est d'extension de sortie de notre pipeline

      filepipeline= open(pipeline, "r")
    
  


 
     
     
  
    
      for line in filepipeline.readlines():
   
        if line[0] != 'S':
                  # v-domain du fichier
           vdomain=line.split('\t')[2]        # recupération de chaque résultat de la colonne VDomain
    
           #data.append(vdomain)               # nous sauvegardons tous les vDomain pour une utilisation ulterieure dans l'histogramme
               
                  
                
      #                
                  
           if vdomain in dictionnaire:                 # dans un dictionnaire si le VDomain existe on ajoute sa valeur à la liste de valeur VDomain existante
      #        
              dictionnaire[vdomain].append(vdomain)
              
           elif vdomain not in dictionnaire :          # si  le VDomain n'existe pas je le crée avec la valeur correspondante
             
              dictionnaire[vdomain] =[vdomain]
    else:
      print("le fichier n'est pas un fichier de sortie du pipeline chargé un autre fichier svp...")
      sys.exit()
  else:
  
    print("erreur le document chargé n'est pas un fichier recommencé...")
    sys.exit()
except Exception as e:
  'Error occured'+str(e)
  
 
# initialize the log settings

 

except IOError as e:
    logging.exception(str(e))
    
start_time=time.time() # temps de début d'execution du programme de comptage

for vdomain in dictionnaire:                  
  
  print(vdomain,len(dictionnaire[vdomain]))         # ecriture du vdomain et de son nombre dans le dictionnaire
  data.append((vdomain,len(dictionnaire[vdomain])))
  listvdomain.append(vdomain)                       # insertion du type du VDomain dans une liste de VDomain
  
  listdicovdomain.append(len(dictionnaire[vdomain]))  # comptage de chaque valeur du VDomain correspondant dans le dictionnaire
#print(dictionnaire)
#readfilevquest()

print("temps d'execution du programme------% seconds-----" %(time.time()-start_time))

# affichage des statistiques des traitements de VQUEST par  VDomain
def affichage():
  
  fenetre = Tk()
  fenetre.geometry("500x100")
  myFont = tkFont.Font(size=18)
  
  for vdomain in dictionnaire:
    
 
  
  
    label = Label(fenetre, text=str(vdomain)+":"+str(len(dictionnaire[vdomain])), font=myFont)
    label.pack()
  print("consultez la fenetre graphique puis...cliquez ensuite sur fermer X pour continuer...")  
  bouton=Button(fenetre, text="Fermer", command=fenetre.quit, fg="red")
  bouton.pack()
  fenetre.mainloop()
  
  
affichage()

# Histogramme du VDomain
def histogram():
  fig, ax = plt.subplots(1,1)
  vd, counts= zip(*data)
  width=0.45
  ax.bar(range(len(counts)), counts, width)
  ax.set_xticks(range(len(counts)))
  ax.set_xticklabels(vd,fontsize=8)
 
  
  plt.title('Histogram Results VQuest', fontsize=10)
 
  print("affichage de histogramme...cliquez ensuite sur fermer X pour continuer...") 
  plt.show()
 
histogram()



# Diagramme circulaire du VDomain
def diagramcirculaire():
  
  val=listvdomain
  sizes = listdicovdomain
  colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

  plt.pie(sizes, labels=val, colors=colors, 
        autopct='%1.1f%%', shadow=True, startangle=90)

  plt.axis('equal')


  plt.show()
  print("affichage de diagramme circulaire...cliquez ensuite sur fermer X pour continuer...")
diagramcirculaire()






