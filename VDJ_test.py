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

import numpy as np


import traceback
#import fichier de log

import csv   # extraction des données au format csv



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

dictionnaire4={}
dictionnaire5={}
dictionnaire2={}
dictionnaire3={} # dico qui acceuillira les séquences vquest et mixcr
dictionnaire1={}

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
           vmixcr = line.split('\t')[30]      # recuperation des sorties de gene variable V de mixcr
           vseqid = line.split('\t')[1]      # recuperation des sorties des sequences de notre pipeline
           vseqnumber= line.split('\t')[0]    # numero de la sequence
           vseqvquest= line.split('\t')[3]
           cmixcr = line.split('\t')[27]      # recuperation des sorties de gene constant C de mixcr
           dvquest = line.split('\t')[10]     # recuperation des sorties de gene diversité D de vquest
           dmixcr = line.split('\t')[28]      # recuperation des sorties de gene diversité D de mixcr
           
           
                 # recuperation des sorties de gene variable V de mixcr
           jvquest =  line.split('\t')[7]     # recupération des sorties de gene J de vquest
           jmixcr =  line.split('\t')[32]     # recupération des sorties de gene J de mixcr
           #data.append(vdomain)               # nous sauvegardons tous les vDomain pour une utilisation ulterieure dans l'histogramme

           # dictionnaire4 et dictionnaire 5 qui acceuil les valeurs de j et de d de vquest et mixcr
               
           if vdomain in dictionnaire4:                 # dans un dictionnaire si le VDomain existe on ajoute sa valeur à la liste de valeur VDomain existante
      #        

             # on met dans les deux cas les valeurs de vquest et mixcr dans notre dictionnaire (les j et les d) 
              
              dictionnaire4[vdomain][vseqnumber] = [jmixcr,jvquest] 
              dictionnaire5[vdomain][vseqnumber] = [dmixcr,dvquest]
             
              
           if vdomain not in dictionnaire4 :          # si  le VDomain n'existe pas je le crée avec la valeur correspondan
             
            
              dictionnaire4[vdomain]={vseqnumber:[jmixcr,jvquest]}
              
              dictionnaire5[vdomain]={vseqnumber:[dmixcr,dvquest]}
              
            # dictionnaire1 qui acceuil les valeurs de VQUEST jcdv avec le numero de sequence nous recuperons les sequences avec au moins un v    
      #                
           if vdomain in dictionnaire1:                 # dans un dictionnaire si le VDomain existe on ajoute sa valeur à la liste de valeur VDomain existante
      #
              if vmixcr!='':  # je recupere uniquement les sequences qui produisent des resultats V dans mixcr
                dictionnaire1[vdomain][vmixcr] = [jmixcr,cmixcr,dmixcr,vseqnumber] 
              
           if vdomain not in dictionnaire1:
             if vmixcr!='':
               dictionnaire1[vdomain]={vmixcr:[jmixcr,cmixcr,dmixcr,vseqnumber]}
               
                       
           if vdomain in dictionnaire:                 # dans un dictionnaire si le VDomain existe on ajoute sa valeur à la liste de valeur VDomain existante
      #        
              dictionnaire[vdomain].append(vdomain)
              
              dictionnaire2[vdomain][vseqnumber] = vmixcr
              
              dictionnaire3[vdomain][vseqnumber] = [vmixcr,vseqvquest]

           elif vdomain not in dictionnaire :          # si  le VDomain n'existe pas je le crée avec la valeur correspondante
             
              dictionnaire[vdomain] =[vdomain]
              
              dictionnaire2[vdomain]={vseqnumber:vmixcr}
             
            
              dictionnaire3[vdomain]={vseqnumber:[vmixcr,vseqvquest]}

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
  
  
#affichage()

# Histogramme du VDomain
# Histogramme du VDomain

def histogram():
  fig, ax = plt.subplots(1,1)
  vd, counts= zip(*data)
  width=0.40
  ax.bar(range(len(counts)), counts, width)
  ax.set_xticks(range(len(counts)))
  ax.set_xticklabels(vd,fontsize=4.3)
 
  
  plt.title('Histogram Results VQuest', fontsize=10)
 
  print("sauvegarde de histogramme des VDomain fonctionnalité...dans VDJ_image...")
  
  if not os.path.exists('VDJ_image'):
    os.makedirs('VDJ_image')
  
  plt.savefig('VDJ_image'+'/'+"plot_simple_histogramme.png",dpi=230)
  #plt.show()



# Diagramme circulaire du VDomain
def diagramcirculaire():
  
  val=listvdomain
  sizes = listdicovdomain
  colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

  plt.pie(sizes, labels=val, colors=colors, 
        autopct='%1.1f%%', shadow=True, startangle=90)
  plt.title('Circulaire', fontsize=10)

  plt.axis('equal')
  
#  if not os.path.exists('VDJ_image'):
#    os.makedirs('VDJ_image')
  
  

  
  print("sauvegarde du diagramme circulaire...des VDomain fonctionnalité... dans VDJ_image...")
  if not os.path.exists('VDJ_image'):
    os.makedirs('VDJ_image')
  plt.savefig('VDJ_image'+'/'+"circulaire.png")
  #plt.show()
  
diagramcirculaire()

histogram()

##########################################################################################################################################

######################################################graphisme-à-activer-pour-graphisme####################################################

# bouton pour terminer le programme

#bouton_terminer = Button(fenetre, text = 'Terminer', command = fenetre.destroy)

#bouton_terminer.pack(padx = 10, pady = (0, 10))

#deb=input("entreee l'entréé")
#fin=input("entreee la sortie")

# pour chacune des données de notre pipeline nous allons créer une fenetre d'affichage des données numéro de séquence
#et v de mixcr


#######################################-------#####################################################################################"""""######

######################################################activation interface graphique et format pdf############################################
##for vdomain in dictionnaire2:


  
##  print(str(vdomain)+"A pour nombre de sortie de Séquences:"+str(len(dictionnaire2[vdomain])))
##  print("veuillez entrer par la suite des nombres entre 0 et"+str(len(dictionnaire2[vdomain])))
##  deb=input("Entrez le nombre de début :")
##  fin=input("Entrez le nombre de fin: ")

  
##  liste=list((dictionnaire2[vdomain]).keys())[int(deb):int(fin)]
#  for cle,valeur in (dictionnaire2[vdomain]).items():
##  print(liste)
            # chaque ligne n'a pas de parent, est ajoutée à la fin de la liste, utilise le champ id comme identifiant et on fournit les valeurs pour chacune des colonnes du tableau

  # fenetre principale des résultats Affichage des résultats selon le VDomain Functionnality
 
##  fenetre= Tk()
##  fenetre.title('Resultats du pipeline')

  # libellé des sorties des résultats

##  libelle=Label(fenetre,text='Table des' +'<<'+str(vdomain)+'>>')

##  libelle.pack(padx=10, pady=10)

##  tableau = Treeview(fenetre, columns=('numerosequence', 'vmixcr'))

##  tableau.heading('numerosequence', text='N°SEQUENCE')

##  tableau.heading('vmixcr', text='V MIXCR')
##  tableau.pack(padx = 10, pady = (0, 10))
##  tableau['show'] = 'headings'

##  pdf = fpdf.FPDF(format='letter') # ecriture dans un fichier pdf
##  pdf.add_page()
##  pdf.set_font("Arial", size=7)
##  pdf.cell(60, 10, str(vdomain), 2)
#  pdf.write(5,str(vdomain))
##  pdf.ln()
##  pdf.cell(80,10,"Numero Sequence\t\t",1)
##  pdf.cell(80,10,"V_MIXCR\t\t",1)
##  pdf.ln()
  
# ecriture du fichier au format csv
##  fichier = open(str(vdomain)+"annuaire.csv", "wt")
##  ecrivainCSV = csv.writer(fichier,delimiter=";")
##  ecrivainCSV.writerow([str(vdomain)])
##  ecrivainCSV.writerow(["Numero Sequence","V_MIXCR"])
  

##  for k in liste:
    
#            tableau.insert('', 'end', values=(cle,valeur))
##    tableau.insert('', 'end',iid=k, values=(k,dictionnaire2[vdomain][k]),tags = ('oddrow',))
##    tableau.insert('', 'end', values=('',''),tags = ('evenrow',))
    
##    Style().configure("Treeview", background="#729fcf", foreground="black",fieldbackground ='blue')
##    tableau.tag_configure('oddrow', background='beige')
##    tableau.tag_configure('evenrow', background='white')
  
#    tableau.row(background='#babdb6')
#    tableau.grid()
#    rowItem=tableau.item(k)
#    (rowItem['values'][1]).grid(row=2, column=0,sticky=W+E)
#    pdf.cell(80,10,"V_MIXCR\t\t",1)
#    pdf.write(5,"V_MIXCR\t\t")

    # ecriture du fichier en csv

##    ecrivainCSV.writerow([str(k),str(dictionnaire2[vdomain][k])])
    
    # ecriture du fichier de données dans un format pdf
##    pdf.cell(80,3,str(k),1)
##    pdf.cell(80,3,str(dictionnaire2[vdomain][k]),1)
##    pdf.ln()
##    print('val',k,dictionnaire2[vdomain][k])

    
##  pdf.output(str(vdomain)+"testings.pdf")
    
  
#    Label(fenetre, text=tab, font="helvetica 8 normal").grid(row=2, column=0,sticky=W+E)
#    print('tableau',tableau[k])
#    filename= tempfile.mktemp(".txt")
#    open(filename, "w").write(tableau.item(k))

   # ecriture du fichier dans un format excel:
  
   
  # bouton pour terminer le programme

##  fichier.close()
  
##  bouton_terminer = Button(fenetre, text = 'Terminer', command = fenetre.destroy)
  #bouton_terminer.grid()
##  bouton_terminer.pack(side=RIGHT,padx=10,pady=2)

  # imprimer en pdf
##  def startpdf():
##      os.popen(str(vdomain)+"testings.pdf")
#      os.startfile(str(vdomain)+"testings.pdf",'print')
   
      
     
       
##      filename=tempfile.mktemp(".pdf")
  #  open(filename,"rt")
    
  
##  bouton_pdf = Button(fenetre, text = 'Imprimer pdf', command = startpdf)
  #bouton_pdf.grid()

##  bouton_pdf.pack(side=RIGHT,padx=11, pady=3)
  
  # imprimer en Excel
##  def startexcel():
##    filename=tempfile.mktemp(".csv")
  #  open(filename,"rt")
##    os.startfile(str(vdomain)+"annuaire.csv",'print')
  
##  bouton_excel = Button(fenetre, text = 'Imprimer excel', command =startexcel)
  #bouton_excel.grid()

##  bouton_excel.pack(side=RIGHT,padx=12, pady=4)
  
  #print(tableau.get_children())
  #for child in tableau.get_children():
    #print(tableau.item(child)['values'])
#~#  fenetre.mainloop()

#    print(tableau.item(child)["values"])
#def printer():
#  q= tableau
#  filename= tempfile.mktemp(".txt")
#  open(filename, "w").write(q)
#printer()
###########################################activation du format pdf############################################################

#----------------------------------------------------------------------------------------------------------------------------------------------------------#

##################################""""""--Traitement des sequences des V de MIXCR et VQUEST--"""""""""######################################################

donneconcord = []
donnenonconcord =[]


for vdomain in dictionnaire3:
  
  if dictionnaire3[vdomain].values()!= '':
   
   
  
   
         #i=0
    print("Affichage du nombre de sequences ceci en tenant compte des séquences avec des V non vide dans mixcr")
    print(str(vdomain)+"   A pour nombre de sortie de Séquences:    "+str(len(dictionnaire3[vdomain])))
  
    
  # ecriture du fichier au format csv
    if not os.path.exists('VDJ_CSV'):
      os.makedirs('VDJ_CSV')
    vq_vmix = open('VDJ_CSV'+'/'+str(vdomain)+"vq_vmix.csv", "wt")
    vq_vmixCSV = csv.writer(vq_vmix,delimiter=";")
    vq_vmixCSV.writerow([str(vdomain)+"   nombre_sequence:          "+str(len(dictionnaire3[vdomain]))])
    vq_vmixCSV.writerow(["V_VQUEST","V_MIXCR","SEQ_NUMBER"])

    # ecrivons l'entete des sequences qui différent
    
                
    vq_vmixdiff = open('VDJ_CSV'+'/'+str(vdomain)+"Vq_Vmix_diff.csv", "wt") # nous ouvrons le fichier qui contiendra les sequences non concordantes vquest mixcr

    vq_vmixmem = open('VDJ_CSV'+'/'+str(vdomain)+"Vq_Vmix_mem.csv", "wt")
    
    vq_vmixdiffCSV = csv.writer(vq_vmixdiff,delimiter=";")
    vq_vmixmemCSV = csv.writer(vq_vmixmem,delimiter=";")
    vq_vmixdiffCSV.writerow(["V_VQUEST","V_MIXCR","SEQ_NUMBER"])
    vq_vmixmemCSV.writerow(["V_VQUEST","V_MIXCR","SEQ_NUMBER"])
    ##############################################
    for cle,valeur in (dictionnaire3[vdomain]).items():
      vq_vmixCSV.writerow([str(valeur[1]),str(valeur[0]),str(cle)])
      
      # ecriture du fichier de données dans un format pdf
           #pdf.cell(80,3,str(k),1)
           #pdf.cell(80,3,str(dictionnaire3[vdomain][k]),1)
           #pdf.ln()
      ##############################################
      
      

    vq_vmix.close() # ici nous fermons un fichier en fait ce fichier contient des sequences Vvquest et Vmixcr avec v mixcr au moins une donnée
    
    #os.popen(str(vdomain)+"Vq_Vmix.csv") # fonction pour l'ouverture directe du fichier csv
    print("ecriture du fichier csv des v de vquest et v mixc sans tenir compte de la difference consulter fichier Vq_Vmix.csv de VDJ_image")
    # nous essayerons de comparer les resultat des cle concordante et non concordante ici nous nous basons sur les recherches des V
    listetotalv=[]  # listetotalv contiendra toutes les nombres  des v concordants de mixcr-vquest
    listetotaldico=[]

    
    for cle,valeur in (dictionnaire3[vdomain]).items(): # je recupere les valeurs vvquest et vmixcr ce sont chacun des listes
      
      listdifferentcle=[]
      listdifferentvaleur=[]
      listememclev=[]
      listememvaleurv=[]
      dicocle={}
      #cle=cle.lstrip("Homsap ")  # traitement sur l'homme uniquement clé vquest
      #clelist=cle.split(" or Homsap ") # decoupage sur l'homme uniquement
      clelist= re.split("[ ,*]",valeur[1])
      

      for elt in clelist:
        #a=elt.split('*') # 2eme decoupage par element sur* de l'homme 
        if elt.startswith('I') or elt.startswith('T') or elt=='':
          dicocle[elt]=elt
          
      
      
      dicovaleur={}

      valeurlist=valeur[0].split(",")

      # traitement sur les valeur valeur de la cle du dictionnaire c'est à dire ceux de mixcr
      v=0
      for elt in valeurlist:
        b=elt.split('*')
  
        dicovaleur[b[0]]=b[0]
     
      for valer in dicocle:
        if valer in dicovaleur: # ici c'est pour traiter les valeurs pour construire l'histogramme2
          
          
          v=v+1
          listememclev.append(valer)
        if valer not in dicovaleur:
          # offsider, juste pour recuperer les valeur pour construire les listes différentes de sequences non concordantes
          listdifferentcle.append(valer)
      for vale in dicovaleur:
        if vale in dicocle:
          listememvaleurv.append(vale)
        if vale not in dicocle:
          listdifferentvaleur.append(vale)
          
          
      listetotalv.append(v)  # listetotalv contiendra toutes les nombres  des v concordants de mixcr-vquest
      listetotaldico.append(len(dicovaleur))
      if listdifferentcle!=[] and listdifferentvaleur!=[]:
        vq_vmixdiffCSV.writerow([" ".join(listdifferentcle)," ".join(listdifferentvaleur),cle]) # ecrivons dans le fichier excel les valeurs qui sont differente de vmixcr et vquest
      if listememclev!=[] and listememvaleurv!=[]:
        vq_vmixmemCSV.writerow([" ".join(listememclev)," ".join(listememvaleurv),cle])
    vq_vmixdiff.close()
    vq_vmixmem.close()
    #os.popen(str(vdomain)+"Vq_Vmix_diff.csv") # activation de l'affichage direct
    print("ecriture du fichier Vq_Vmix_diff.csv qui tient compte uniquement de la difference des sequences V de mixcr et V de vquest")
    print("le fichier qui a été crée est le fichier des sequences de V de mixcr et de V vquest retrouvez celle-ci dans le dossier VDJ")
      # ecrivons dans un fichier les sequences qui seront aux résultats différents
      
    totalconcordmixcr=sum(listetotalv)
    totaldemixcr=sum(listetotaldico)
    totalnonconcordmixcr=totaldemixcr-totalconcordmixcr
    donneconcord.append((vdomain,totalconcordmixcr))
    donnenonconcord.append((vdomain,totalnonconcordmixcr))
      # ecriture des sequences qui ne sont pas les memes dans vquest et mixcr
      

def histogram2():               # histogramme des cas concordants et des cas non concordants de V
  
  fig, ax = plt.subplots(1,1)
  vdc, countss= zip(*donneconcord)
  vds, countsss=zip(*donnenonconcord)
  width=0.40
  ind= np.arange(len(countsss))
  ax.bar(range(len(countss)), countss, width)
  ax.bar(ind + width , countsss, width)
  ax.set_xticks(range(len(countss)))
  ax.set_xticks(ind + width / 2)
  
  ax.set_xticklabels(vdc,fontsize=4.3)
  
  ax.legend(((ax.bar(range(len(countss)), countss, width))[0],(ax.bar(ind + width , countsss, width))[0]), ('concordant', 'NoConcordant'))
  
  plt.title('Histogram V Results Concordant & non concordants', fontsize=10)
  print("Sauvegarde de histogramme des V de VQUEST ET MIXCR...cet histogramme est consultable dans le dossier VDJ_image..")
  
  if not os.path.exists('VDJ_image'):
    os.makedirs('VDJ_image')
  
  plt.savefig('VDJ_image'+'/'+"plot_simple_histogramme_V.png",dpi=230)
  #plt.show()
histogram2()  

#----------------------------------------------------------------------------------------------------------------------------------------------#

######################---traitement des sequences des J de VQUEST et de MIXCR---###############################################################""

donneconcordj = []
donnenonconcordj =[]
for vdomain in dictionnaire4:

  if dictionnaire3[vdomain].values()!= '':
   
    
  
   
         
    print(str(vdomain)+"   A pour nombre de sortie de Séquences:    "+str(len(dictionnaire3[vdomain])))
  


    # ecrivons l'entete des sequences qui différent
  if not os.path.exists('VDJ_CSV'):
    os.makedirs('VDJ_CSV')
  jvq_jmixdiff = open('VDJ_CSV'+'/'+str(vdomain)+"Jvq_Jmix_diff.csv", "wt")
  jvq_jmixmem = open('VDJ_CSV'+'/'+str(vdomain)+"Jvq_Jmix_mem.csv", "wt")
  jvq_jmixmemCSV = csv.writer(jvq_jmixmem,delimiter=";")
  jvq_jmixdiffCSV = csv.writer(jvq_jmixdiff,delimiter=";")
    
  jvq_jmixdiffCSV.writerow(["J_VQUEST","J_MIXCR","SEQ_NUMBER"])
  jvq_jmixmemCSV.writerow(["J_VQUEST","J_MIXCR","SEQ_NUMBER"])
    ##############################################

    # nous essayerons de comparer les resultat des cle concordante et non concordante ici nous nous basons sur les recherches des J
  listetotalvj=[]  # listetotalv contiendra toutes les nombres  des vj concordants de mixcr-vquest
  listetotaldicoj=[]
  
  for cle,valeur in (dictionnaire4[vdomain]).items(): # je recupere les valeurs jvquest et jmixcr ce sont chacun des listes
      
    listdifferentclej=[]
    listdifferentvaleurj=[]
    listememclej=[]
    listememvaleurj=[]
    dicoclej={}
     
    clelistj= re.split("[ ,*]",valeur[1])    # decoupage des cles des j vquest
      

    for elt in clelistj:
       
      if elt.startswith('I') or elt.startswith('T')or elt=='':
        dicoclej[elt]=elt
          
     # ce dictionnaire contient toutes nos valeurs J de vquest
      
    dicovaleurj={}

    valeurlistj=valeur[0].split(",")

      # traitement sur les valeur valeur de la cle du dictionnaire c'est à dire ceux de mixcr
    v=0
    for elt in valeurlistj:
      c=elt.split('*')
  
      dicovaleurj[c[0]]=c[0]
    
    for valer in dicoclej:
      print("les valeurs sont les suivantes:",valer)
#      # ici c'est pour traiter les valeurs pour construire l'histogramme2
      for valerr in dicovaleurj:
        if valer==valerr:
          print("les valeurs concordantes sont les suivantes:",valer)
          v=v+1
          listememclej.append(valer)
#       
#        
      if valer not in dicovaleurj:
          # offsider, juste pour recuperer les valeur pour construire les listes différentes de sequences non concordantes
        listdifferentclej.append(valer)
    for vale in dicovaleurj:
#     
      for vales in dicoclej:
        if vale==vales:
          listememvaleurj.append(vale)
#        
      if vale not in dicoclej:
        listdifferentvaleurj.append(vale)
          
          
    listetotalvj.append(v)  # listetotalv contiendra tous les nombres  des j concordants de mixcr-vquest
    listetotaldicoj.append(len(dicovaleurj))
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              print(valeur[1])
    if listdifferentclej!=[] and listdifferentvaleurj!=[]:
#      
       jvq_jmixdiffCSV.writerow([" ".join(listdifferentclej)," ".join(listdifferentvaleurj),cle]) # ecrivons dans le fichier excel les valeurs qui sont differente de vmixcr et vquest
    if listememclej!=[] and listememvaleurj!=[]:
#    
       jvq_jmixmemCSV.writerow([" ".join(listememclej)," ".join(listememvaleurj),cle]) # ecrivons dans le fichier excel les valeurs qui sont les memes de jmixcr et jvquest
  jvq_jmixdiff.close()
  jvq_jmixmem.close()
  #os.popen(str(vdomain)+"Jvq_Jmix_diff.csv")
  print("ecriture du fichier Jq_Jmix_diff.csv qui tient compte uniquement de la difference des sequences J de mixcr et J de vquest")
  print("le fichier qui a été crée est le fichier des sequences des J de mixcr avec détails retrouvez celle-ci dans le dossier VDJ")
      # ecrivons dans un fichier les sequences qui seront aux résultats différents
      
  totalconcordmixcrj=sum(listetotalvj)
  totaldemixcrj=sum(listetotaldicoj)
  totalnonconcordmixcrj=totaldemixcrj-totalconcordmixcrj
  donneconcordj.append((vdomain,totalconcordmixcrj))
  donnenonconcordj.append((vdomain,totalnonconcordmixcrj))
      # ecriture des sequences qui ne sont pas les memes dans vquest et mixcr


      
      
    
def histogramj():               # histogramme des cas concordants et des cas non concordants de J
  
  fig, ax = plt.subplots(1,1)
  vdcc, countssss= zip(*donneconcordj)
  vdss, countsssss=zip(*donnenonconcordj)
  width=0.40
  ind= np.arange(len(countsssss))
  ax.bar(range(len(countssss)), countssss, width)
  ax.bar(ind + width , countsssss, width)
  ax.set_xticks(range(len(countssss)))
  ax.set_xticks(ind + width / 2)
  
  ax.set_xticklabels(vdcc,fontsize=4.3)
  
  ax.legend(((ax.bar(range(len(countssss)), countssss, width))[0],(ax.bar(ind + width , countsssss, width))[0]), ('concordant', 'NoConcordant'))
  
  plt.title('Histogram J Resultats Concordant & non concordants', fontsize=10)
  print("affichage de histogramme...cliquez ensuite sur fermer X pour continuer...retrouver l'image dans le dossier vdj_image")
  
  if not os.path.exists('VDJ_image'):
    os.makedirs('VDJ_image')
  
  plt.savefig('VDJ_image'+'/'+"plot_simple_histogramme_J.png",dpi=230)
  #plt.show()
histogramj()



#-------------------------------------------------------------------------------------------------------------------------------------------#


#######################---traitement des sequences des D de VQUEST et de MIXCR---############################################################


donneconcordd = []
donnenonconcordd =[]
for vdomain in dictionnaire5:

  if dictionnaire3[vdomain].values()!= '':
   
    
  
   
         #i=0
    print(str(vdomain)+"   A pour nombre de sortie de Séquences:    "+str(len(dictionnaire3[vdomain])))
  if not os.path.exists('VDJ_CSV'):
    os.makedirs('VDJ_CSV')
    # ecrivons l'entete des sequences qui différent  
  dvq_dmixdiff = open('VDJ_CSV'+'/'+str(vdomain)+"Dvq_Dmix_diff.csv", "wt")
  dvq_dmixmem = open('VDJ_CSV'+'/'+str(vdomain)+"Dvq_Dmix_mem.csv", "wt")
  
  dvq_dmixdiffCSV = csv.writer(dvq_dmixdiff,delimiter=";")
  dvq_dmixmemCSV = csv.writer(dvq_dmixmem,delimiter=";")
    
  dvq_dmixdiffCSV.writerow(["D_VQUEST","D_MIXCR","SEQ_NUMBER"])
  dvq_dmixmemCSV.writerow(["D_VQUEST","D_MIXCR","SEQ_NUMBER"])
    ##############################################

#    os.popen(str(vdomain)+"vq_vmix.csv")
    # nous essayerons de comparer les resultat des cle concordante et non concordante ici nous nous basons sur les recherches des D
  listetotalvd=[]  # listetotalv contiendra toutes les nombres  des vd concordants de mixcr-vquest
  listetotaldicod=[]
  
  for cle,valeur in (dictionnaire5[vdomain]).items(): # je recupere les valeurs d vquest et d mixcr ce sont chacun des listes
      
    listdifferentcled=[]
    listdifferentvaleurd=[]
    listememcled=[]
    listememvaleurd=[]
    dicocled={}
      
    clelistd= re.split("[ ,*]",valeur[1])    # decoupage des cles des d vquest
      

    for elt in clelistd:
        #a=elt.split('*') # 2eme decoupage par element sur* de l'homme 
      if elt.startswith('I') or elt.startswith('T')or elt=='':
        dicocled[elt]=elt
          

      
    dicovaleurd={}

    valeurlistd=valeur[0].split(",")

      # traitement sur les valeur valeur de la cle du dictionnaire c'est à dire ceux de mixcr
    v=0
    for elt in valeurlistd:
      d=elt.split('*')
  
      dicovaleurd[d[0]]=d[0]
   
    for valer in dicocled:
      if valer in dicovaleurd: # ici c'est pour traiter les valeurs pour construire l'histogramme d
          
      
        v=v+1
        listememcled.append(valer)
      if valer not in dicovaleurd:
          # offsider, juste pour recuperer les valeur pour construire les listes différentes de sequences non concordantes
        listdifferentcled.append(valer)
    for vale in dicovaleurd:
      if vale in dicocled:
        listememvaleurd.append(vale)
      if vale not in dicocled:
        listdifferentvaleurd.append(vale)
          
          
    listetotalvd.append(v)  # listetotalv contiendra toutes les nombres  des D concordants de mixcr-vquest
    listetotaldicod.append(len(dicovaleurd))
    if listdifferentcled!=[] and listdifferentvaleurd!=[]:
      dvq_dmixdiffCSV.writerow([" ".join(listdifferentcled)," ".join(listdifferentvaleurd),cle]) # ecrivons dans le fichier excel les valeurs qui sont differente de d mixcr et d vquest
    if listememcled!=[] and listememvaleurd!=[]:
      dvq_dmixmemCSV.writerow([" ".join(listememcled)," ".join(listememvaleurd),cle]) # ecrivons dans le fichier excel les valeurs qui sont les memes de vmixcr et vquest
  dvq_dmixdiff.close()
  dvq_dmixmem.close()
  #os.popen(str(vdomain)+"Dvq_Dmix_diff.csv")
  print("le fichier qui a été crée est le fichier des sequences D de vquest et mixcr uniquement")
     
      
  totalconcordmixcrd=sum(listetotalvd)
  totaldemixcrd=sum(listetotaldicod)
  totalnonconcordmixcrd=totaldemixcrd-totalconcordmixcrd
  donneconcordd.append((vdomain,totalconcordmixcrd))
  donnenonconcordd.append((vdomain,totalnonconcordmixcrd))
      


      
      
    
def histogramd():               # histogramme des cas concordants et des cas non concordants de d
  
  fig, ax = plt.subplots(1,1)
  vdcc, countssss= zip(*donneconcordd)
  vdss, countsssss=zip(*donnenonconcordd)
  width=0.40
  ind= np.arange(len(countsssss))
  ax.bar(range(len(countssss)), countssss, width)
  ax.bar(ind + width , countsssss, width)
  ax.set_xticks(range(len(countssss)))
  ax.set_xticks(ind + width / 2)
  
  ax.set_xticklabels(vdcc,fontsize=4.3)
  
  ax.legend(((ax.bar(range(len(countssss)), countssss, width))[0],(ax.bar(ind + width , countsssss, width))[0]), ('concordant', 'NoConcordant'))
  
  plt.title('Histogram D Resultats Concordant & non concordants', fontsize=10)
  print("affichage de histogramme...cliquez ensuite sur fermer X pour continuer...")

  if not os.path.exists('VDJ_image'):
    os.makedirs('VDJ_image')
  
  plt.savefig('VDJ_image'+'/'+"plot_simple_histogramme_D.png",dpi=230)
  #plt.show()
histogramd()

#-------------------------------------------------------------------------------------------------------------------------------------------#
###############################################------- FICHIER CSV des sorties de VDJC de MIXCR et le numero de la sequence ------------------------------######################################
for vdomain in dictionnaire1:


   
    
  
   
         
    print(str(vdomain)+"A pour nombre de sortie de Séquences:    "+str(len(dictionnaire1[vdomain])))
    if not os.path.exists('VDJ_CSV'):
      os.makedirs('VDJ_CSV')
    
  # ecriture du fichier au format csv
    productive = open('VDJ_CSV'+'/'+str(vdomain)+".csv", "wt")
    productivCSV = csv.writer(productive,delimiter=";")
    productivCSV.writerow([str(vdomain)+"nombre_sequence:          "+str(len(dictionnaire1[vdomain]))])
    productivCSV.writerow(["V_MIXCR","J_MIXCR","C_MIXCR","D_MIXCR","N_SEQ"])
    
 
    for k in (dictionnaire1[vdomain]).keys():
      productivCSV.writerow([str(k),str(dictionnaire1[vdomain][k][0]),str(dictionnaire1[vdomain][k][1]),str(dictionnaire1[vdomain][k][2]),str(dictionnaire1[vdomain][k][3])])
   
      
      

    productive.close()
    print("le fichier qui a été crée est le fichier des sequences des v de mixcr avec détails retrouvez celle-ci dans le dossier VDJ")
    #os.popen(str(vdomain)+".csv") # ici lancement de mon fichier csv dans le cas contraire dossier des VDJ
      


