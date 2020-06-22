
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
																																				 
		message3:  "sauvegarde de l'histogramme...des VDomain fonctionnalité dans VDJ_image"

3-     Sauvegarde de l'histogramme
	 a- à la suite de la fermeture de la fenêtre des statistiques il est immédiatement sauvegardé l'image de l'histogramme dans VDJ_image 
	 

                                                                                                                                   
         message4:  "sauvegarde du diagramme circulaire... des VDomain fonctionnalité... dans VDJ_image..."
                                                                                                            
4-   Saouvegarde du diagramme circulaire 
     a- Il est sauvegardé directement un diagramme circulaire 
                                                                                                       
 5-   Affichage du nombre de séquences ceci en tenant compte des séquences avec des V non vide dans mixcr

     a- nous affichons ici pour chaque fonctionnalité du VDomain le nombre de (rearrangement found, unproductive, no results...) 
     Message:5    <<no rearrangement found  a pour nombre de sorties de séquences: 5273>>
     b- nous écrivons dans le fichier adéquat, c'est-à-dire le fichier << V de VQUEST et V de mixcr (vq_vmix.csv)>>
     Message:6    <<écriture du fichier cSv de v de vquest et mixcr sans tenir compte de la différence>>
     c- nous écrivons également un fichier Vq_Vmix_diff.csv qui tient compte de la différence des V de mixcr et V de vquest

                    << ecriture du fichier Vq_Vmix_diff.csv qui tient compte uniquement de la difference des sequences V de mixcr et V de vquest>>

     d- nous écrivons également un fichier Jq_Jmix_diff.csv qui tient compte de la différence des J de mixcr et J de vquest

                    <<ecriture du fichier Jq_Jmix_diff.csv qui tient compte uniquement de la difference des sequences J de mixcr et J de vquest>>

    
     e- nous écrivons également un fichier Dq_Jmix_diff.csv qui tient compte de la différence des D de mixcr et D de vquest

                    <<ecriture du fichier Dq_Dmix_diff.csv qui tient compte uniquement de la difference des sequences D de mixcr et D de vquest>> 

     Message:7    <<le fichier qui a été créé est le fichier des séquences de V de mixcr et de vquest, retrouver celui dans le dossier VDJ_CSV>>
 
6-   Affichage de l'histogramme des nombres des séquences tenant compte de la fonctionnalité du VDomain
     
     a- il s'agit ici de sauvegarder dans un histogramme par rapport au domaine V les quantités dans le pipeline des sequences concordantes et les sequences non concordantes
     Message:8   <<sauvegarde  de l'histogramme des V de VQUEST ET MIXCR... cet histogramme est consultable dans le dossier VDJ_image>>
     b- il s'agit ici de sauvegarder dans un histogramme par rapport au domaine D les quantités dans le pipeline des sequences concordantes et les sequences non concordantes
     Message:9   << sauvegarde de l'histogramme des D de VQUEST et MIXCR... cet histogramme est consultable dans le dossier VDJ_image>>
     c- il s'agit ici de sauvegarder dans un histogramme par rapport au domaine J les quantités dans le pipeline des séquences concordantes et les séquences non concordantes
     Message:10   <<sauvegarde de l'histogramme des J de MIXCR et VQUEST... cet histogramme est consultable dans le dossier VDJ_image>>

7-   Affichage du nombre de sorties des séquences V de mixcr en tenant compte uniquement des V non vide sorti (VDJC de mixcr et numéro de la séquence) 
     Message: 11  <<NO Results a pour sortie de séquence 3223>>

8-   Creation d'un fichier CSV des séquences VDJC ET Numero séquence de mixcr des séquences vdjc qui n'ont pas de résultat dans vquest
     Message: 12 << le fichier qui a été créé est le fichier des séquences des V de mixcr avec détails retrouver celui-ci dans le dossier VDJ_CSV  
                                          

                        


                             C - QUELQUES ERREURS COURANTES
							 

        Erreur1:   "erreur le document chargé n'est pas un fichier recommencé..."

        Erreur1 :vous avez passé en paramètre un nom de fichier qui n'existe pas ou un dossier ou un nom quelconque vous ont pour retour:
                 ou bien vous n'avez chargé votre fichier pipeline dans le répertoire du programme :               
                                                
        Erreur2:   "le fichier n'est pas un fichier de sortie du pipeline, chargé un autre fichier svp..."

        Erreur 2: vous pouvez également avoir ce type d'erreur quand le fichier de sortie n'est pas du type d'extension du pipeline vous avez généralement
                  ce type d'erreur quand vous avez exécuté un fichier autre que ce lui du pipeline  
