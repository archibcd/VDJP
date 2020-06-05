
le Programme python VDJ_1.0 de IMGT s'exécute sur la version python 3.8.0 il est développé par des chercheurs de l'IMGT

il est conçu pour fonctionné sur des serveurs Debian de version de noyau 5.4.13.1 il existe également une version windows.10

la procédure de déploiement commence par l'installation des paquets qui nous seront utiles sur debian

                A-PREPARATION DE L'ENVIRONNEMENT

0- vous pouvez commencer par une mise à jour des options avec la commande

        apt-get update

 
1- Telechargement des paquets Python version 3.8.0

    a- vous devez télécharger des paquets pour l'installation de python3.8.0 il s'agit de l'archive Python-3.8.0.tgz
               - le lien de téléchargement est le suivant: https://www.python.org/ftp/python/3.8.0/Python-3.8.0.tgz

2- rendez-vous pour exécuter la procédure d'installation sous Debian 5

     a-placez vous dans le répertoire de votre choix
        - le mien c'est:  debian:/home/user1/Desktop
     b-vous pouvez exécutez la commande suivante dans le répertoire que vous avez au préalable sélectionné: 

         tar xfz Python-3.8.0.tgz

        - exemple: debian:/home/user1/Desktop# tar xfz Python-3.8.0.tgz

3- après que l'interpréteur est rendu la main, pensez à exécuter la commande ls pour voir les fichiers de votre répertoire

         ls

        a- vous aurez donc un dossier présent dans votre répertoire qui portera le nom:

        Python-3.8.0
        b- je vous invite ici à aller dans le répertoire de ce dossier avec la commande

        cd ./Python-3.8.0
        
        - exemple: debian:/home/user1/Desktop# cd ./Python-3.8.0
                   debian:/home/user1/Desktop/Python-3.8.0#

4- lancer l'installation, vous pouvez lancer l'installation de votre version de python comme suit:
       a lancer l'outil de configuration

           ./configure --enable-optimizations 

        Exemple:   debian:/home/user1/Desktop/Python-3.8.0#  ./configure --enable-optimizations
       
       b  lancement du processus d'installation avec les commandes (assurez-vous d'avoir les privilèges d'administration):
            make -j 4
            sudo make altinstall
            exemple:   debian:/home/user1/Desktop/Python-3.8.0#  make -j 4
                       debian:/home/user1/Desktop/Python-3.8.0#  sudo make altinstall  
         
        c une fois terminer l'interpréteur remet la mainvous pouvez vérifier que l'installation c'est bien passé en vérifiant votre version
            python3.8 --version
            exemple:   debian:/home/user1/Desktop/Python-3.8.0#  python3.8 --version

5- installation de packages: 

       a- vous pouvez installer le package matplotlib par la suite avec la commande suivante:

            apt-get install python-matplotlib

            exemple:   debian:/home/user1/Desktop/Python-3.8.0#  apt-get install python3-matplotlib

Une fois l'environnement installé vous pouvez lancer votre programme VDJ pour l'analyse de votre pipeline

6- il vous suffit de télécharger le programme open source sur github, le mettre dans le répertoire de votre choix, ensuite l'exécuter
                                a- lien github:    github.com/archibcd/VDJP

7- après avoir téléchargé le fichier d'analyse du pipeline, l'étape qui suit est celle du lancement du programme:
                                a- aller dans le répertoire  où vous avez téléchargé le fichier vous pouvez le déplacer avec la commande :
                                                     mV chemin1/fichier chemin2  
                                     exemple: osboxes@osboxes~$: mv /home/downloads    /home/Desktop/Documents

                                b-placer vous dans le répertoire où le fichier a été déplacé utiliser la commande:

                                             exemple:          cd  /home/Desktop/Documents et exécuter :
                                                              
                                                       * changer tout d'abord les droits du fichier (vous devez être connecté en administrateur)

                                                                     - utiliser la commande: changer les droits avec la commande sudo chmod 751 VDJ_test.py


                                                                      NB(les administrateurs peuvent éditer le fichier avec la commande sudo nano 751 VDJ_test.py )

                                 c- parfait vous pouvez lancer le programme avec la commande suivante:

                                            osboxes@osboxes~$:   ./VDJ_test.py CR3156R.pipeline.results.tsv


                                             NB: le fichier passé en argument est un fichier d'extension de sortie de votre pipeline, dans le cas contraire 
                                                 une erreur est générée sur votre terminal noté que le fichier doit être obligatoirement d'extension  << .results.tsv>>.

                                       ayant chargé le bon fichier,  nous pouvons suivre le déroulement  de notre programme 


                         B- DEROULEMENT DU PROGRAMME
						   
						   
						   
	 Message0: "Patientez pendant l'exécution..."

Pendant le bon déroulement du programme suite à votre insertion du fichier  vous recevez un message au terminal 
qui demande de patienter pendant l'exécution
une fois l'exécution terminée, quelques résultats vous sont produits notamment:
																
	Message1:  "temps d'exécution du programme..."
																										
1- affiche au terminal la durée d'exécution en seconde  pour produire des résultats. exemple 0.044seconds
2- une fenêtre graphique qui vous donne les premiers résultats du pipeline notamment les résultats des nombres de séquences
par type de fonction du vdomain vu par mixcr   (No results, productive , unproductive..):

	message2:    "  consulter la fenêtre graphique puis...  cliquer sur fermer X pour continuer"

    a- un message au terminal vous est affiché qui demande de quitter après consultation
	NB: vous devez fermer la fenêtre graphique pour continuer l'exécution du programme verifier qu'il n'y a
		plus de fenêtre active. Dans le cas contraire, le programme ne continuera pas l'exécution. 
																																				 
		message3:  "affichage de l'histogramme... cliquez ensuite sur fermer X pour continuer"

3-     Affichage de l'histogramme
	 a- à la suite de la fermeture de la fenêtre des statistiques il est immédiatement affiché la fenêtre de
	Consultation de l'histogramme. Vous pouvez choisir de l'enregistrer avec l'icône tout  en bas de l'image.
	vous avez tout à côté un boutton à 4 flèches vertes (configure subplot ) qui vous permettra de modifier les
	paramètres d'affichage de l'histogramme 
	N. B. Enregistrez l'image en PNG et n'oubliez pas de fermer la fenêtre pour continuer
                                                                                                                                   
        message4:  "affichage du diagramme circulaire."
                                                                                                            
4-   Affichage du diagramme circulaire 
     a- à la fermeture de la fenêtre de l'histogramme tout comme cette dernière, il est affiché directement un 
     diagramme circulaire avec les mêmes options de visualisation le (configure subplot ) et le boutton d'enregistrement
                                                                                                       
                                           

                        


                             C - QUELQUES ERREURS COURANTES
							 

        Erreur1:   "erreur le document chargé n'est pas un fichier recommencé..."

        Erreur1 :vous avez passé en paramètre un nom de fichier qui n'existe pas ou un dossier ou un nom quelconque vous ont pour retour:
                 ou bien vous n'avez chargé votre fichier pipeline dans le répertoire du programme :               
                                                
        Erreur2:   "le fichier n'est pas un fichier de sortie du pipeline, chargé un autre fichier svp..."

        Erreur 2: vous pouvez également avoir ce type d'erreur quand le fichier de sortie n'est pas du type d'extension du pipeline vous avez généralement
                  ce type d'erreur quand vous avez exécuté un fichier autre que ce lui du pipeline  
