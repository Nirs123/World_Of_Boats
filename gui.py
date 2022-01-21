#Importation de modules
from random import randint
import tkinter as tk
import operator

#Initialisation de la fenêtre de jeu
game = tk.Tk()
#Paramètres de la fenêtre de jeu
game.unbind_class("Button", "<Key-space>")
game.title('Monde des Bateaux')
game.geometry('880x980')
game.minsize(880, 980)
game.maxsize(880, 980)
game.iconbitmap("logo.ico")
game.config(bg="#000000")

#Classe personnage
class perso:
    def __init__(self,pseudo,X,Y,Boats):
        '''
        Initialisation du personnage, en prenant en compte son pseudo de jeu,
        ses coordonnées de départ (de 0 a 20 en x et y) et son type de bateau qui
        définira ses différentes statistiques (PV / ATQ / Range / Mouvements etc...)
        '''
        self.x = X
        self.y = Y
        self.status = True
        self.passiv_heal = False
        if Boats=="Cruiser":
            #Statistiques du Cruiser
            self.name = pseudo
            self.boats = "Cruiser"
            self.Pt_Vie = 80000
            self.pv_max = 80000
            self.atq = 16000
            self.atq_type = 2
            self.bonus = 2
            self.mvm = 4
            self.range = 5
            self.ini = 20
            self.esquive = 5
            self.obus_resist = 5
            self.torp_resist = 5
        if Boats=="Destroyer":
            #Statistiques du Destroyer
            self.name = pseudo
            self.boats = "Destroyer"
            self.Pt_Vie = 34000
            self.pv_max = 34000
            self.atq = 20000
            self.atq_type = 2
            self.bonus=0
            self.mvm = 6
            self.range = 5
            self.ini = 30
            self.esquive = 8
            self.obus_resist = 4
            self.torp_resist = 3
        if Boats=="Cuirasse":
            #Statistiques du Cuirasse
            self.name = pseudo
            self.boats = "Cuirasse"
            self.Pt_Vie = 100000
            self.pv_max = 100000
            self.atq = 4500
            self.atq_type = 0
            self.bonus = 3
            self.mvm = 3
            self.range = 6
            self.ini = 10
            self.esquive = 2
            self.obus_resist = 7
            self.torp_resist = 12
        if Boats=="Submarine":
            #Statistiques du Submarine
            self.name = pseudo
            self.boats = "Submarine"
            self.Pt_Vie = 25000
            self.pv_max = 25000
            self.atq = 8000
            self.atq_type = 1
            self.bonus = 0
            self.mvm = 5
            self.range = 5
            self.ini = 40
            self.esquive = 10
            self.obus_resist = 80
            self.torp_resist = 2

    def Attack(self,self1):
        '''
        Fonction qui permet au bateau self d'attaquer un autre bateau self1
        '''
        #Initialisation des dégats
        self.dgts=0
        #Résultats aléatoires qui serviront a déterminer le nombre de dégats
        self.r1 = randint(0,4)
        self.r2 = randint(0,3)
        self.r3 = randint(1,5)
        #Calcul des dégats si le bateau a que des Obus (atq.type == 0)
        if self.atq_type == 0:
            self.dgts = self.dgts + (self.atq * self.r1)
            if self.r3 == 1:
                self.dgts = self.dgts + (((self1.get_pv_max()//10)//2)*self.r1)
            #Application des résistances aux obus du bateau
            self.dgts = self.dgts - ((self1.get_res_obus()*self.dgts)//100)
        #Calcul des dégats si le bateau a que des Torpilles (atq.type == 1)
        elif self.atq_type == 1:
            self.dgts = self.dgts + (self.atq * self.r2)
            #Application des résistances aux torpilles du bateau
            self.dgts = self.dgts - ((self1.get_res_torp()*self.dgts)//100)
        #Calcul des dégats si le bateau a des Obus et des Torpilles
        elif self.atq_type == 2:
            self.tmp = self.atq // 2
            self.dgts = self.dgts + (self.tmp * self.r1) + (self.tmp * self.r2)
            if self.r3 == 1:
                self.dgts = self.dgts + (((self1.get_pv_max()//10)//2)*self.r1)
            #Application des résistances aux obus / torpilles du bateau
            self.dgts = self.dgts - ((((self1.get_res_torp() + self1.get_res_obus()) // 2)*self.dgts)//100)
        #Test de l'esquive
        self.r4 = randint(0,100)
        if self.r4 <= self1.esquive:
            self.dgts = 0
        #Si l'esquive a échoué, inflige les dégats
        else:
            self1.set_pv(self1.get_pt_vie()-self.dgts)

    #Méthodes d'acquisition / modification du nom / type de bateau / status
    def get_pseudo(self):
        return self.name
    def get_boat(self):
        return self.boats
    def get_status(self):
        return self.status
    def set_status(self,status):
        self.status = status

    #Méthodes d'acquisition / modification de la stat d'initiative
    def set_ini(self,value):
        self.ini = value
    def get_ini(self):
        return self.ini

    #Méthodes d'acquisition / modification des stats de résistance
    def get_res_obus(self):
        return self.obus_resist
    def get_res_torp(self):
        return self.torp_resist
    def set_res_obus(self,value):
        self.obus_resist = value
    def set_res_torp(self,value):
        self.torp_resist = value

    #Méthodes d'acquisition / modification de la stat d'esquive
    def get_esquive(self):
        return self.esquive
    def set_esquive(self,value):
        self.esquive = value

    #Méthodes d'acquisition / modification des déplacements / positions
    def set_x(self,X):
        self.x=X
    def set_y(self,Y):
        self.y+=Y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_mvm(self):
        return self.mvm
    def set_mvm(self,value):
        self.mvm = value
    def deplacer(self,dx,dy):
        self.x+=dx
        self.y+=dy

    #Méthodes d'acquisition / modification de la stat de range
    def get_range(self):
        return self.range
    def set_range(self,value):
        self.range = value

    #Méthodes d'acquisition / modification des stats de PV / Bonus de PV / PV_Max
    def bonus_vie(self):
        self.set_pv(self.get_pt_vie()+randint(int(self.Pt_Vie//6),int(self.Pt_Vie//4)))
        self.set_bonus(self.get_bonus()-1)
    def set_bonus(self,value):
        self.bonus = value
    def get_bonus(self):
        return self.bonus
    def get_pt_vie(self):
        return self.Pt_Vie
    def set_pv(self,value):
        self.Pt_Vie = value
    def get_pv_max(self):
        return self.pv_max
    def set_pv_max(self,value):
        self.pv_max = value
    def switch_passiv_heal(self):
        if self.passiv_heal:
            self.passiv_heal = False
        elif self.passiv_heal == False:
            self.passiv_heal = True
    def get_passiv_heal(self):
        return self.passiv_heal

    #Méthodes d'acquisition / modification des stats de dégats
    def get_dgts(self):
        return self.dgts
    def get_atq(self):
        return self.atq
    def set_atq(self,value):
        self.atq = value

#Classe permettant la création de texte / bouton / entrée / checkcase en tkinter plus facilement
class Text_Button_Entry:
    def __init__(self,type,text,frame,row,rowspan,column,columnspan,padx,pady,size,command,variable):
        '''
        Créée l'élement en prenant en compte son contenu, sa frame, sa colonne, sa ligne,
        son padx, son pady, sa taille etc...
        '''
        self.text = text
        self.frame = frame
        self.row = row
        self.rowspan = rowspan
        self.column = column
        self.columnspan = columnspan
        self.pady = pady
        self.padx = padx
        self.size = size
        self.type = type
        self.command = command
        self.var = variable
        #Création de l'élement en fonction de son type
        if self.type == "Label":
            self.temp = tk.Label(self.frame, text = self.text, font=('Courrier',str(self.size)),bg="#000000", fg="#FFFFFF")
        elif self.type == "Button":
            self.temp = tk.Button(self.frame, text = self.text, font=('Courrier',str(self.size)),bg="#000000", fg="#FFFFFF",command = self.command)
        elif self.type == "Entry":
            self.temp = tk.Entry(self.frame,font=('Courrier',str(self.size)),bg="#000000", fg="#FFFFFF",textvariable=self.var)
        elif self.type == "Check":
            self.temp = tk.Checkbutton(self.frame,text = self.text, font =('Courrier',str(self.size)),bg="#000000", fg="grey",variable=self.var,width=50)
        #Affichage de l'élement
        self.temp.grid(row = self.row,column = self.column,padx = self.padx,pady = self.pady,columnspan = self.columnspan, rowspan = self.rowspan)

    def grid_forget(self):
        '''
        Permet de supprimer l'élement qui a été crée
        '''
        self.temp.grid_forget()

#Class permettant d'afficher la fenêtre des stats détaillés des classes
class index_class:
    def __init__(self):
        #Stats des bateaux
        self.cui = [100000,18000,"Obus",3,6,3,10,2,7,12]
        self.cru = [80000,16000,"Obus et\nTorpilles",4,5,2,20,5,5,5]
        self.des = [34000,20000,"Obus et\nTorpilles",6,5,0,30,8,4,3]
        self.sub = [25000,24000,"Torpilles",5,5,0,40,10,80,2]
        #Noms des bateaux et leurs stats
        self.names = ["Cuirassé","Cruiser","Destroyer","Submarine"]
        self.attri = ["PV","ATQ","   Type\nd'attaque","Mouvements","Range","Heals","Initiative","Esquive","Resistance\n   Obus","Resistance\n  Torpilles"]
        self.list = [self.cui,self.cru,self.des,self.sub]

        #Création de la nouvelle fenêtre et de ses paramètres
        self.chart = tk.Toplevel(game)
        self.chart.title("Statistiques détaillées")
        self.chart.geometry("1160x540")
        self.chart.minsize(1160,540)
        self.chart.maxsize(1160,540)
        self.chart.config(bg="#000000")

        #Initialisation du canvas permettant l'affiche du tableau
        self.ca2 = tk.Canvas(self.chart, height=455, width=1160, bg="#000000")
        self.show_values()
        self.ca2.pack()
        self.ca2.bind('<Configure>', self.create_grid_2)

        #Création du bouton pour quitter la fenêtre
        self.tmp = tk.Button(self.chart, text = "QUIT", font=('Courrier',"18","bold"),bg="#000000", fg="#FFFFFF",command = self.quit)
        self.tmp.pack(pady=15)

    def show_values(self):
        '''
        Permet l'affiche de toutes les valeurs / nom de bateaux / nom d'attributs
        '''
        #Compteur de ligne
        self.y = 1
        #Affichage des noms de bateaux
        for name in self.names:
            self.ca2.create_text(52.5,self.y*90+45,text=str(name),font=('Courrier',"13","bold"),fill="white")
            self.y += 1

        #Compteur de colone
        self.x = 1
        #Affichage du noms des attributs
        for attri in self.attri:
            self.ca2.create_text(self.x*105.5+53,45,text=str(attri),font=('Courrier',"13","bold"),fill="white")
            self.x += 1

        #Compteur de colonne / lignes pour les valeurs
        self.u = 1
        self.j = 1
        #Affichage de toutes les valeurs
        for i in self.list:
            for value in i:
                self.ca2.create_text(self.u*105.5+52.5,self.j*90+45,text=str(value),font=('Courrier',"14","bold"),fill="white")
                self.u += 1
            self.u = 1
            self.j += 1

    def create_grid_2(self,event = None):
        '''
        Permet l'affichage du tableau
        '''
        w = self.ca2.winfo_width()
        h = self.ca2.winfo_height()
        self.ca2.delete('grid_line')

        #Affichage des colonnes
        for i in range(0, w, 106):
            self.ca2.create_line([(i, 0), (i, h)], tag='grid_line',fill='white')

        #Affichage des lignes
        for i in range(0, h-50, 90):
            self.ca2.create_line([(0, i), (w, i)], tag='grid_line',fill='white')

    def quit(self):
        #Ferme la fenêtre
        self.chart.destroy()

#Classe pour l'affiche du menu de création d'un joueur
class Create_Player:
    def __init__(self,e):
        self.equipe = e
        #Initialisation et paramétrage de la fenêtre de création de joueur
        self.temp_choose = tk.Toplevel(game)
        self.temp_choose.title("Création joueur")
        self.temp_choose.geometry("420x420")
        self.temp_choose.minsize(420,450)
        self.temp_choose.maxsize(420,450)
        self.temp_choose.config(bg="#000000")

        #Affichage des texts (Titre, Cases d'entrées pseudo/classe, noms des classes et leurs description)
        t1_j1 = Text_Button_Entry("Label","Menu de création du joueur",self.temp_choose,0,1,0,2,0,10,20,None,None)
        self.tmp_p = tk.StringVar()
        t2_j1 = Text_Button_Entry("Label","Pseudo:",self.temp_choose,1,1,0,1,25,0,14,None,None)
        e1_j1 = Text_Button_Entry("Entry",None,self.temp_choose,1,1,1,1,0,0,14,None,self.tmp_p)
        self.tmp_c = tk.StringVar()
        t3_j1 = Text_Button_Entry("Label","Classe:",self.temp_choose,2,1,0,1,25,10,15,None,None)
        e2_j1 = Text_Button_Entry("Entry",None,self.temp_choose,2,1,1,1,0,0,15,None,self.tmp_c)
        t4_j1 = Text_Button_Entry("Label","Cuirasse: Tank a beaucoup de PV et Résistances\nPeu de Mouvement, beaucoup de Range\nDégats de type Obus",self.temp_choose,3,1,0,2,25,5,12,None,None)
        t5_j1 = Text_Button_Entry("Label","Cruiser: PV / ATQ / Range / Mouvement Equilibrés\nDégats de type Obus et Torpilles",self.temp_choose,4,1,0,2,25,5,12,None,None)
        t6_j1 = Text_Button_Entry("Label","Destroyer: Beaucoup d'ATQ et de Mouvement\n Assez peu de PV donc assez vulnérable\nDégats de type Obus et Torpilles",self.temp_choose,5,1,0,2,25,5,12,None,None)
        t7_j1 = Text_Button_Entry("Label","Submarine: Beaucoup d'ATQ / Mouvement / Range\n Très résistant aux Obus mais très peu de PV\nDégats de types torpilles",self.temp_choose,6,1,0,2,25,5,12,None,None)
        b1_j1 = Text_Button_Entry("Button","OK ",self.temp_choose,7,1,1,1,25,5,12,self.teams_players,None)
        b2_j1 = Text_Button_Entry("Button","Stats détaillées",self.temp_choose,7,1,0,1,15,3,14,index_class,None)

    def teams_players(self):
        global d_p,d_p2,d_p3,nb_p,d_p4
        tmp = str(f"player{nb_p}")
        self.valid = False
        self.temp_choose.destroy()
        #Vérification que le pseudo n'est pas vide, sinon renvoie une box d'erreur
        if str(self.tmp_p.get()) != "":
            #Vérification que le nom de la classe est valide
            if str(self.tmp_c.get()) == "Cruiser" or str(self.tmp_c.get()) == "Destroyer" or str(self.tmp_c.get()) == "Cuirasse" or str(self.tmp_c.get()) == "Submarine":
                nb_p += 1
                #Vérification dans quelle équipe se trouvera le joueur (pour définir l'intervalle des x et y au spawn)
                if self.equipe == 1:
                    #Vérification pour ne pas dépasser le nombre de joueurs max par équipe (3)
                    if len(e_1) < 3:
                        #Création du personnage
                        q = perso(self.tmp_p.get(),randint(0,2),randint(0,19),self.tmp_c.get())
                        t8 = Text_Button_Entry("Label","Pseudo: "+str(self.tmp_p.get())+"\nClasse: "+str(self.tmp_c.get()),frame1,3+len(e_1),1,0,2,0,25,20,None,None)
                        e_1[tmp] = q.get_pseudo()
                        self.valid = True
                elif self.equipe == 2:
                    #Vérification pour ne pas dépasser le nombre de joueurs max par équipe (3)
                    if len(e_2) < 3:
                        #Création du personnage
                        q = perso(self.tmp_p.get(),randint(17,19),randint(0,19),self.tmp_c.get())
                        t9 = Text_Button_Entry("Label","Pseudo: "+str(self.tmp_p.get())+"\nClasse: "+str(self.tmp_c.get()),frame1,3+len(e_2),1,3,2,0,25,20,None,None)
                        e_2[tmp] = q.get_pseudo()
                        self.valid = True
            else:
                error_box("ERREUR: Classe")
        else:
            error_box("ERREUR: Pseudo")
        if self.valid:
            #Si tout est valide, on stockage 
            d_tmp[tmp] = q
            d_p2[tmp] = q.get_pseudo()
            d_p3[tmp] = self.equipe
            d_p4[tmp] = self.tmp_c.get()

#Classe pour l'affichage d'une erreur sur une nouvelle fenêtre
class error_box:
    def __init__(self,msg):
        self.msg = msg
        self.tmp_box = tk.Toplevel(game)
        self.tmp_box.title("ERREUR")
        self.tmp_box.config(bg="#000000")
        t = Text_Button_Entry("Label",msg,self.tmp_box,0,1,0,1,10,10,20,None,None)
        b = Text_Button_Entry("Button","OK",self.tmp_box,1,1,0,1,0,0,14,self.tmp_box.destroy,None)

#Classe pour l'affichage des choix de bonus
class bonus_choose:
    def __init__(self):
        global nb_p
        #Initialisation des indexs et du premier joueur a choisir
        self.indexs = []
        self.index = -1
        for key in d_p.keys():
            self.indexs.append(key)
        self.key = str(self.indexs[self.index])
        self.update_player()

    def update_player(self):
        global nb_p
        #Gestion des index
        self.index += 1
        if self.index != len(self.indexs):
            self.key = str(self.indexs[self.index])
        self.bonus_box()

    def bonus_box(self):
        #Initialisation et paramétrage de le fenêtre de choix
        self.classe = d_p[self.key].get_boat()
        self.tmp_bonus = tk.Toplevel(game)
        self.tmp_bonus.config(bg="#000000")
        self.tmp_bonus.geometry("650x400")
        self.tmp_bonus.title("Choix Bonus")
        self.tmp_bonus.minsize(650, 400)
        self.tmp_bonus.maxsize(650, 400)
        #Affichage du texte et initialisation des valeurs pour stocker l'information choisis des bonus (0 ou 1)
        t3 = Text_Button_Entry("Label","Choisissez vos 2 bonus: "+str(d_p[self.key].get_pseudo()),self.tmp_bonus,0,1,0,1,18,20,20,None,None)
        self.opt1,self.opt2,self.opt3,self.opt4,self.opt5 = tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()
        #Affichage des bonus en fonction de la classe
        if self.classe == "Cuirasse":
            self.checkbuttons("+5% PV","+5% Résistance Obus","+5% Résistance Torpilles","1% de récupération PV chaque tour","+15 Initiative")
        if self.classe == "Cruiser":
            self.checkbuttons("+3% ATQ","+3% PV","+1 PM","+1 Range","+15 Initiative")
        if self.classe == "Submarine":
            self.checkbuttons("+1 PM","+1 Range","+5% ATQ","+10% d'esquive","+1 Soins")
        if self.classe == "Destroyer":
            self.checkbuttons("+5% de ATQ","+1 Range","+7% d'ésquive","+1 Soins","+15 Initiative")
        b4 = Text_Button_Entry("Button","OK",self.tmp_bonus,6,1,0,1,0,15,14,self.choosen,None)

    def checkbuttons(self,t1,t2,t3,t4,t5):
        #Création des 5 boutons pour chaque bonus possible
        o1 = Text_Button_Entry("Check",t1,self.tmp_bonus,1,1,0,1,5,7,14,None,self.opt1)
        o2 = Text_Button_Entry("Check",t2,self.tmp_bonus,2,1,0,1,5,7,14,None,self.opt2)
        o3 = Text_Button_Entry("Check",t3,self.tmp_bonus,3,1,0,1,5,7,14,None,self.opt3)
        o4 = Text_Button_Entry("Check",t4,self.tmp_bonus,4,1,0,1,5,7,14,None,self.opt4)
        o5 = Text_Button_Entry("Check",t5,self.tmp_bonus,5,1,0,1,5,7,14,None,self.opt5)

    def choosen(self):
        global c
        #Prise des réponses et stockage dans la liste
        self.tmp_list = []
        self.tmp_list.append(self.opt1.get())
        self.tmp_list.append(self.opt2.get())
        self.tmp_list.append(self.opt3.get())
        self.tmp_list.append(self.opt4.get())
        self.tmp_list.append(self.opt5.get())
        #Vérification du bon nombre de réponses choisis
        if self.tmp_list.count(1) < 2:
            error_box("ERREUR: Pas assez de bonus choisis")
        if self.tmp_list.count(1) > 2:
            error_box("ERREUR: Trop de bonus choisis")
        if self.tmp_list.count(1) == 2:
            #En fonctions des classes et des bonus choisis, affecte le bonus choisis au joueur
            if self.classe == "Cuirasse":
                if self.opt1.get() == 1:
                    d_p[self.key].set_pv(int(d_p[self.key].get_pt_vie()+((d_p[self.key].get_pt_vie()*5)/100)))
                    d_p[self.key].set_pv_max(d_p[self.key].get_pt_vie())
                if self.opt2.get() == 1:
                    d_p[self.key].set_res_obus(d_p[self.key].get_res_obus()+5)
                if self.opt3.get() == 1:
                    d_p[self.key].set_res_torp(d_p[self.key].get_res_torp()+5)
                if self.opt4.get() == 1:
                    d_p[self.key].switch_passiv_heal()
                if self.opt5.get() == 1:
                    d_p[self.key].set_ini(d_p[self.key].get_ini()+15)
            elif self.classe == "Destroyer":
                if self.opt1.get() == 1:
                    d_p[self.key].set_atq(int(d_p[self.key].get_atq()+((d_p[self.key].get_atq()*3)/100)))
                if self.opt2.get() == 1:
                    d_p[self.key].set_range(d_p[self.key].get_range()+1)
                if self.opt3.get() == 1:
                    d_p[self.key].set_esquive(d_p[self.key].get_esquive()+7)
                if self.opt4.get() == 1:
                    d_p[self.key].set_bonus(d_p[self.key].get_bonus()+1)
                if self.opt5.get() == 1:
                    d_p[self.key].set_ini(d_p[self.key].get_ini()+15)
            elif self.classe == "Submarine":
                if self.opt1.get() == 1:
                    d_p[self.key].set_mvm(d_p[self.key].get_mvm()+1)
                if self.opt2.get() == 1:
                    d_p[self.key].set_range(d_p[self.key].get_range()+1)
                if self.opt3.get() == 1:
                    d_p[self.key].set_atq(int(d_p[self.key].get_atq()+((d_p[self.key].get_atq()*5)/100)))
                if self.opt4.get() == 1:
                    d_p[self.key].set_esquive(d_p[self.key].get_esquive()+10)
                if self.opt5.get() == 1:
                    d_p[self.key].set_bonus(d_p[self.key].get_bonus()+1)
            elif self.classe == "Cruiser":
                if self.opt1.get() == 1:
                    d_p[self.key].set_atq(int(d_p[self.key].get_atq()+((d_p[self.key].get_atq()*3)/100)))
                if self.opt2.get() == 1:
                    d_p[self.key].set_pv(int(d_p[self.key].get_pt_vie()+((d_p[self.key].get_pt_vie()*3)/100)))
                    d_p[self.key].set_pv_max(d_p[self.key].get_pt_vie())
                if self.opt3.get() == 1:
                    d_p[self.key].set_mvm(d_p[self.key].get_mvm()+1)
                if self.opt4.get() == 1:
                    d_p[self.key].set_range(d_p[self.key].get_range()+1)
                if self.opt5.get() == 1:
                    d_p[self.key].set_ini(d_p[self.key].get_ini()+15)
            self.tmp_bonus.destroy()
            c = c + 1
            #Si tout les joueurs ont choisis leurs bonus
            if c == nb_p:
                #Recréation du dictionnaire d_p au cas ou si le nombre d'initiative a été modifié (ce qui change l'ordre de passage)
                d_p.clear()
                for values in d_tmp:
                    cl_ini2[values] = d_tmp[values].get_ini()
                d_tmp2 = dict(sorted(cl_ini2.items(), key=operator.itemgetter(1),reverse=True))
                for keys in d_tmp2.keys():
                    d_p[keys] = d_tmp[keys]
                #Fermeture de la fenêtre et lancement du jeu
                main_game()
                frame1.grid_forget()
                frame1.destroy()
            else:
                #Sinon passe au prochain joueur
                self.update_player()

#Classe activant le jeu et initialisation de la partie
class main_game:
    def __init__(self):
        global e_1,e_2,d_p,d_p2,d_p3,nb_p,a
        #Compteur du nombres de tours
        self.tour = 1
        #Création de 2 frames (l'une pour l'affichage du jeu, l'autre pour les choix d'action)
        self.frame2 = tk.Frame(game,bg="#000000")
        self.frame3 = tk.Frame(game,bg="#000000")

        #Création d'index et initialisation des keys pour chaque joueur
        self.indexs = []
        for key in d_p.keys():
            self.indexs.append(key)
        self.index = -1
        self.tmp_player = str(self.indexs[self.index])

        #Création du canvas pour la grille et l'affichage des joueurs
        self.ca = tk.Canvas(self.frame2,height=880,width=880,bg="#03005e",highlightthickness=0)
        self.ca.pack(fill=tk.BOTH, expand=True)
        #Appel de la fonction grid pour créer la grille de 20x20
        self.ca.bind('<Configure>', self.create_grid)
        #Appel de la méthode d'affiche des joueurs (voir description méthode)
        self.draw_players()

        #Appel de la fonction update_tour qui permet le début du déroulement du jeu
        self.update_tour()

        #Pack des 2 frames du jeu
        self.frame2.pack()
        self.frame3.pack()

        #Bind des 4 flèches pour la méthode de déplacement
        game.bind('<Left>',self.mvm_left)
        game.bind('<Right>',self.mvm_right)
        game.bind('<Up>',self.mvm_up)
        game.bind('<Down>',self.mvm_down)
        
        #Création d'une variable booléenne pour savoir si les flèches peuvent agir ou non (sera activer en true dès que la méthode/action mouvement est activé) 
        self.a = False

    def create_grid(self,event=None):
        w = self.ca.winfo_width()
        h = self.ca.winfo_height()
        self.ca.delete('grid_line')

        #Lignes vérticales
        for i in range(0, w, 44):
            self.ca.create_line([(i, 0), (i, h)], tag='grid_line')

        #Lignes horizontales
        for i in range(0, h, 44):
            self.ca.create_line([(0, i), (w, i)], tag='grid_line')

    def draw_players(self):
        #Cette fonction draw_players sera réactivée a chaque début d'un tour d'un joueur
        self.tmp_coord = []
        #Pour chaque joueur dans le jeu
        for key in d_p:
            #On obtient ses coordonnées que l'on multiplie par 44 (correspond a la taille d'un carré géneré par la grille)
            tmp_x = d_p[key].get_x()*44
            tmp_y = d_p[key].get_y()*44
            self.tmp_coord.append(tuple((d_p[key].get_x(),d_p[key].get_y())))
            #Si le joueur est mort, affichage mais en gris
            if d_p[key].get_pt_vie() <= 0:
                self.rect = self.ca.create_rectangle(tmp_x,tmp_y,tmp_x+44,tmp_y+44,fill='grey')
                self.ca.create_text(tmp_x+22,tmp_y+22,text=" "+str(d_p2[key])+"\n"+str(d_p4[key]),font=('Courrier',"7","bold"))
            else:
                #Sinon l'affiche soit en vert ou en rouge en fonction de son équipe
                if d_p3[key] == 1:
                    #Remplissage du carré par la couleure
                    self.rect = self.ca.create_rectangle(tmp_x,tmp_y,tmp_x+44,tmp_y+44,fill='red')
                    #Affichage du pseudo et classe de bateau du joueur
                    self.ca.create_text(tmp_x+22,tmp_y+22,text=" "+str(d_p2[key])+"\n"+str(d_p4[key]),font=('Courrier',"7","bold"))
                elif d_p3[key] == 2:
                    self.rect = self.ca.create_rectangle(tmp_x,tmp_y,tmp_x+44,tmp_y+44,fill='green')
                    self.ca.create_text(tmp_x+22,tmp_y+22,text=" "+str(d_p2[key])+"\n"+str(d_p4[key]),font=('Courrier',"7","bold"))

    def update_tour(self):
        self.a = False
        self.delete_frame()
        #Vérifications pour ne pas dépasser le nombre de joueurs
        if self.index + 1 < len(self.indexs):
            #Si il y a encore des joueurs qui doivent jouer dans le tour, alors augmentation de l'index
            self.index += 1
            self.tmp_player = str(self.indexs[self.index])
        else:
            #Sinon, on remet l'index a 0 et on incrémente le compteur de tours
            self.index = 0
            self.tmp_player = str(self.indexs[self.index])
            self.tour += 1
        #Si le nombres de joueurs morts dans une équipe correspond a ce nombre de joueurs dans la même équipe, alors lance la méthode de fin du jeu
        if len(e_1) == len(e_1d):
            self.end_game(1)
        elif len(e_2) == len(e_2d):
            self.end_game(2)
        else:
            #Sinon
            if d_p[self.tmp_player].get_pt_vie() <=0:
                #Si le joueur est mort, on passe son tour
                self.update_tour()
            else:
                #Sinon, active la méthode update_frame3 pour l'affichage des possibles actions
                self.update_frame3(self.tmp_player)

    def update_frame3(self,key):
        self.key = key
        self.tmp_mvm = d_p[self.key].get_mvm()
        #Affichage du nombre de tours
        self.t1 = Text_Button_Entry("Label","Tour n°"+str(self.tour),self.frame3,0,2,0,1,0,14,22,None,None)

        #Appel de la méhtode d'affichage de la range du bateau
        self.circle(d_p[self.key].get_x(),d_p[self.key].get_y(),d_p[self.key].get_range())

        #Si le joueur dispose du bonus de heal par tour et qu'il n'est pas full pv, alors lui rajoute son bonus
        if d_p[self.key].get_passiv_heal() == True and d_p[self.key].get_pt_vie() != d_p[self.key].get_pv_max():
            d_p[self.key].set_pv(int(d_p[self.key].get_pt_vie()+(d_p[self.key].get_pv_max()/100)))

        #Affichage du pseudo du joueur et de ses PV, ainsi que les 4 options disponible (skip, attaque, soins, déplacement)
        self.t2 = Text_Button_Entry("Label","Joueur: "+str(d_p2[self.key]),self.frame3,0,1,1,1,20,8,20,None,None)
        self.t3 = Text_Button_Entry("Label","PV: "+str(d_p[self.key].get_pt_vie()),self.frame3,1,1,1,1,0,0,20,None,None)
        self.b1 = Text_Button_Entry("Button","Skip",self.frame3,0,2,2,1,15,8,18,self.passer,None)
        self.b2 = Text_Button_Entry("Button","Attaque",self.frame3,0,2,3,1,15,8,18,self.attack,None)
        self.b3 = Text_Button_Entry("Button","Soins",self.frame3,0,2,4,1,15,8,18,self.soins,None)
        self.b4 = Text_Button_Entry("Button","Déplacement",self.frame3,0,2,5,1,15,8,18,self.deplacement,None)

    def circle(self,x,y,r):
        #Création des valeurs requises pour l'affiche du cercle
        self.r = (r * 44) + 22
        self.x = (x * 44) + 22
        self.y = (y * 44) + 22
        self.x0 = self.x - self.r
        self.y0 = self.y - self.r
        self.x1 = self.x + self.r
        self.y1 = self.y + self.r
        #Création du cercle de range
        self.temp_ca = self.ca.create_oval(self.x0,self.y0,self.x1,self.y1,width=2,outline='yellow')

    def passer(self):
        #Si le joueur a skip, supprime les boutons
        self.delete_buttons()
        #Et affiche un message de confirmation
        self.t4 = Text_Button_Entry("Label","Tour Skippé\ncliquez sur OK",self.frame3,0,2,2,1,15,8,24,None,None)
        self.b5 = Text_Button_Entry("Button","OK",self.frame3,0,2,3,1,15,8,18,self.passer_2,None)

    def passer_2(self):
        #Lorsque le message de confirmation de la méthode passer a été cliqué
        #Supprime le message de confirmation et appelle update_tour pour passer au prochain joueur ou au prochain tour
        self.t4.grid_forget()
        self.b5.grid_forget()
        self.update_tour()

    def attack(self):
        #Si le joueur a cliquer sur attaquer, supprime les boutons
        self.tmp_target = tk.StringVar()
        self.delete_buttons()
        #Et affiche un message pour demander quel est la cible du joueur
        self.t5 = Text_Button_Entry("Label","Qui voulez\nvous attaquer ?",self.frame3,0,2,2,1,15,8,24,None,None)
        self.e1 = Text_Button_Entry("Entry",None,self.frame3,0,2,3,1,15,8,16,None,self.tmp_target)
        self.b6 = Text_Button_Entry("Button","OK",self.frame3,0,2,4,1,15,8,18,self.attack_2,None)

    def attack_2(self):
        #Lorsque le joueur a cliquer sur OK lors de la séléction de la cible, supprime alors le message
        self.t5.grid_forget()
        self.e1.grid_forget()
        self.b6.grid_forget()
        #Accès a la clé de la cible choisis
        self.target_key = [k for k, v in d_p2.items() if v == self.tmp_target.get()]
        #Or si il n'y a aucune clé
        if len(self.target_key) == 0:
            #Alors la séléction de la cible a échoué
            self.t6 = Text_Button_Entry("Label","Erreur lors de la séléction",self.frame3,0,2,2,1,15,18,24,None,None)
            self.b7 = Text_Button_Entry("Button","OK",self.frame3,0,2,4,1,15,18,18,self.attack_3,None)
        else:
            #Sinon, on vérifie que ce n'est pas un allié
            if d_p3[self.target_key[0]] == d_p3[self.key]:
                #Sinon affiche un message d'erreur
                self.t6 = Text_Button_Entry("Label","Vous ne pouvez pas\nattaquer un allié",self.frame3,0,2,2,1,15,8,24,None,None)
                self.b7 = Text_Button_Entry("Button","OK",self.frame3,0,2,4,1,15,8,18,self.attack_3,None)
            else:
                #Vérification si la cible est dans la range du joueur qui attaque
                if ((d_p[self.target_key[0]].get_x()-d_p[self.key].get_x())**2) + ((d_p[self.target_key[0]].get_y()-d_p[self.key].get_y())**2) <= ((d_p[self.key].get_range())**2):
                    #Vérification si la cible n'est pas déjà morte
                    if d_p[self.target_key[0]].get_pt_vie() >0:
                        #Sinon, toutes les vérifications sont passés, active la méthode d'attaque du joueur
                        d_p[self.tmp_player].Attack(d_p[self.target_key[0]])
                        #Si le joueurs a moins ou égal a 0PV
                        if d_p[self.target_key[0]].get_pt_vie() <=0:
                            #Alors affiche le message de mort
                            self.t6 = Text_Button_Entry("Label",str(self.tmp_target.get())+" est mort",self.frame3,0,2,2,1,15,18,24,None,None)
                            self.b7 = Text_Button_Entry("Button","OK",self.frame3,0,2,4,1,15,8,18,self.attack_3,None)
                            if d_p[self.target_key[0]].get_status() == True:
                                #Puis le rajouté dans la liste des joueurs morts en fonction de son équipe
                                if d_p3[self.target_key[0]] == 1:
                                    e_1d.append(self.target_key[0])
                                if d_p3[self.target_key[0]] == 2:
                                    e_2d.append(self.target_key[0])
                                #Puis update la frame du jeu pour afficher le joueur mort en gris
                                self.delete_frame_2()
                                self.draw_players()
                                d_p[self.target_key[0]].set_status(False)
                        else:
                            #Sinon affiche le nombre de dégats infligés
                            self.t6 = Text_Button_Entry("Label",str(self.tmp_target.get())+" a désormais "+str(d_p[self.target_key[0]].get_pt_vie())+"PV\nDégats infligés: "+str(d_p[self.key].get_dgts())+"PV",self.frame3,0,2,2,1,15,8,24,None,None)
                            self.b7 = Text_Button_Entry("Button","OK",self.frame3,0,2,4,1,15,8,18,self.attack_3,None)
                    else:
                        #Sinon affiche un message d'erreur
                        self.t6 = Text_Button_Entry("Label","Vous ne pouvez pas attaquer un mort",self.frame3,0,2,2,1,15,18,24,None,None)
                        self.b7 = Text_Button_Entry("Button","OK",self.frame3,0,2,4,1,15,8,18,self.attack_3,None)
                else:
                    #Sinon affiche un message d'erreur
                    self.t6 = Text_Button_Entry("Label","Vous êtes trop loin",self.frame3,0,2,2,1,15,18,24,None,None)
                    self.b7 = Text_Button_Entry("Button","OK",self.frame3,0,2,4,1,15,18,18,self.attack_3,None)

    def attack_3(self):
        #Lorsque le bouton de confirmation a été cliqué
        #Supprime les messages et appelle update_tour pour passer au prochain joueur ou au prochain tour
        self.t6.grid_forget()
        self.b7.grid_forget()
        self.update_tour()

    def soins(self):
        #Si le joueurs a décidé de se soignés, supprime les boutons
        self.delete_buttons()
        #Vérifique qu'il n'est pas déjà a ses PV Max
        if d_p[self.key].get_pt_vie() != d_p[self.key].get_pv_max():
            #Vérifie qu'il lui reste encore des bonus de soins
            if d_p[self.key].get_bonus() > 0 :
                #Après les vérifications, applique le bonus de soins
                d_p[self.key].bonus_vie()
                #Vérifie que le joueur ne dépasse pas ses PV Max
                if d_p[self.key].get_pt_vie() > d_p[self.key].get_pv_max():
                    #Sinon, mets tout simplement ses PV a ses PV Max
                    d_p[self.key].set_pv(d_p[self.key].get_pv_max())
                #Affiche les PV après s'être soigné
                self.t7 = Text_Button_Entry("Label","Vous avez désormais "+str(d_p[self.key].get_pt_vie())+"PV\nSoins Restants: "+str(d_p[self.key].get_bonus()),self.frame3,0,2,2,1,15,8,24,None,None)
                self.b8 = Text_Button_Entry("Button","OK",self.frame3,0,2,4,1,15,8,18,self.soins_2,None)
            else:
                #Sinon affiche le message d'erreur
                self.t7 = Text_Button_Entry("Label","Vous n'avez plus de soins",self.frame3,0,2,2,1,15,20,24,None,None)
                self.b8 = Text_Button_Entry("Button","OK",self.frame3,0,2,4,1,15,8,18,self.soins_2,None)
        else:
            #Sinon affiche le message d'errur
            self.t7 = Text_Button_Entry("Label","Vous êtes déjà a vos PV Max",self.frame3,0,2,2,1,15,20,24,None,None)
            self.b8 = Text_Button_Entry("Button","OK",self.frame3,0,2,4,1,15,8,18,self.soins_2,None)

    def soins_2(self):
        #Après avoir cliqué sur OK dans la méthode de soins
        self.t7.grid_forget()
        self.b8.grid_forget()
        self.update_tour()

    def deplacement(self):
        #Si le joueur a choisis le déplacement
        #Alors active la possibilité de se déplacer avec les flèches
        self.a = True
        #Supprime les boutons
        self.delete_buttons()
        self.valid = True
        #Si il lui restes des points de mouvement
        if self.tmp_mvm > 0:
            #Affiche le nombre de mouvements restants et les boutons pour se déplacer
            self.t8 = Text_Button_Entry("Label","Déplacements réstants: "+str(self.tmp_mvm)+" ",self.frame3,0,1,0,1,0,20,22,None,None)
            self.b9 = Text_Button_Entry("Button"," ↑ ",self.frame3,0,1,1,1,15,20,24,self.dep_haut,None)
            self.b10 = Text_Button_Entry("Button","←",self.frame3,0,1,2,1,15,20,24,self.dep_gauche,None)
            self.b11 = Text_Button_Entry("Button","→",self.frame3,0,1,3,1,15,20,24,self.dep_droite,None)
            self.b12 = Text_Button_Entry("Button"," ↓ ",self.frame3,0,1,4,1,15,20,24,self.dep_bas,None)
            self.b13 = Text_Button_Entry("Button","SKIP",self.frame3,0,1,5,1,15,20,18,self.skip,None)
        else:
            #Sinon, affiche le message qu'il n'y a plus de déplacements
            self.t8 = Text_Button_Entry("Label","Déplacements finis",self.frame3,0,2,2,1,15,20,24,None,None)
            self.b9 = Text_Button_Entry("Button","OK",self.frame3,0,2,4,1,15,8,18,self.skip_2,None)
            self.a = False

    def skip(self):
        #Si le joueur a skip alors qu'il lui restait des mouvements
        #Supprime les boutons et appelle la fonction passer pour faire le reste des commandes
        self.delete_buttons_2()
        self.passer()

    def skip_2(self):
        #Lorsque le joueur a finis ses déplacements
        #Supprime les boutons et appelle update_tour pour passer au prochain joueur ou au prochain tour
        self.delete_buttons_2()
        self.update_tour()

    def dep_haut(self):
        #Lorsque la méthode de déplacement vers le haut activé
        #Vérifique le joueur ne sortirait pas de la map en faisant cela
        if d_p[self.key].get_y() - 1 >= 0:
            for elements in self.tmp_coord:
                if tuple((d_p[self.key].get_x(),d_p[self.key].get_y()-1)) == elements:
                    self.valid = False
            if self.valid:
                #Après les vérifications, déplace le joueur
                d_p[self.key].deplacer(0,-1)
        self.dep()

    def dep_bas(self):
        #Lorsque la méthode de déplacement vers le bas activé
        #Vérifique le joueur ne sortirait pas de la map en faisant cela
        if d_p[self.key].get_y() + 1 <=19:
            for elements in self.tmp_coord:
                if tuple((d_p[self.key].get_x(),d_p[self.key].get_y()+1)) == elements:
                    self.valid = False
            if self.valid:
                #Après les vérifications, déplace le joueur
                d_p[self.key].deplacer(0,1)
        self.dep()

    def dep_gauche(self):
        if d_p[self.key].get_x() - 1 >= 0:
            for elements in self.tmp_coord:
                if tuple((d_p[self.key].get_x()-1,d_p[self.key].get_y())) == elements:
                    self.valid = False
            if self.valid:
                #Après les vérifications, déplace le joueur
                d_p[self.key].deplacer(-1,0)
        self.dep()

    def dep_droite(self):
        if d_p[self.key].get_x() + 1 <= 19:
            for elements in self.tmp_coord:
                if tuple((d_p[self.key].get_x()+1,d_p[self.key].get_y())) == elements:
                    self.valid = False
            if self.valid:
                #Après les vérifications, déplace le joueur
                d_p[self.key].deplacer(1,0)
        self.dep()

    def dep(self):
        #Après avoir déplacé ou non le joueur
        #Supprime les boutons, décrémente le nombre de points de mouvement, actualise la frame et rappelle la fonction mouvement
        self.delete_buttons_2()
        self.tmp_mvm -= 1
        self.delete_frame_2()
        self.draw_players()
        self.deplacement()

    def mvm_left(self,arg):
        #Si la flèche gauche a été appuyé
        #Vérifie que c'est valide ou non
        if self.a:
            #Appelle la fonction de déplacement vers la gauche
            self.dep_gauche()

    def mvm_right(self,arg):
        #Si la flèche droite a été appuyé
        #Vérifie que c'est valide ou non
        if self.a:
            #Appelle la fonction de déplacement vers la droite
            self.dep_droite()

    def mvm_up(self,arg):
        #Si la flèche haut a été appuyé
        #Vérifie que c'est valide ou non
        if self.a:
            #Appelle la fonction de déplacement vers le haut
            self.dep_haut()

    def mvm_down(self,arg):
        #Si la flèche bas a été appuyé
        #Vérifie que c'est valide ou non
        if self.a:
            #Appelle la fonction de déplacement vers le bas
            self.dep_bas()

    def delete_frame(self):
        #Supprime la frame 3
        self.frame3.grid_forget()

    def delete_frame_2(self):
        #Supprime le canvas de la frame 2
        self.ca.delete('all')
        self.create_grid()

    def delete_buttons(self):
        #Supprime tout les boutons 
        self.t1.grid_forget()
        self.t2.grid_forget()
        self.t3.grid_forget()
        self.b1.grid_forget()
        self.b2.grid_forget()
        self.b3.grid_forget()
        self.b4.grid_forget()
        self.ca.delete(self.temp_ca)

    def delete_buttons_2(self):
        #Supprimes d'autres boutons
        self.t8.grid_forget()
        self.b9.grid_forget()
        self.b10.grid_forget()
        self.b11.grid_forget()
        self.b12.grid_forget()
        self.b13.grid_forget()

    def end_game(self,lose):
        #Si la game est finie
        self.lose = lose
        #En fonction de l'équipe qui a perdu, affiche les joueurs de l'équipe gagnante
        if self.lose == 1:
            self.tmp_str = ""
            for element in e_2:
                self.tmp_str = self.tmp_str + d_p[element].get_pseudo() + " "
            t = Text_Button_Entry("Label","Partie terminé\nGagnants: "+str(self.tmp_str),self.frame3,0,1,0,1,15,8,24,None,None)
            b = Text_Button_Entry("Button","QUIT",self.frame3,0,1,1,2,15,20,24,game.destroy,None)
        elif self.lose == 2:
            self.tmp_str = ""
            for element in e_1:
                self.tmp_str = self.tmp_str + d_p[element].get_pseudo() + " "
            t = Text_Button_Entry("Label","Partie terminé\nGagnants: "+str(self.tmp_str),self.frame3,0,1,0,1,15,8,24,None,None)
            b = Text_Button_Entry("Button","QUIT",self.frame3,0,1,1,2,15,20,24,game.destroy,None)

def switch_frame():
    #Lorsque le bouton play est appuyé
    #Vérifie qu'il y a au moins 1 joueurs
    if nb_p == 0:
        error_box("ERREUR: Aucun Joueur")
    else:
        #Sinon
        b3.grid_forget()
        #Dictionnaire pour trier les joueurs en fonction de leur initiative
        for values in d_tmp:
            cl_ini[values] = d_tmp[values].get_ini()
        d_tmp2 = dict(sorted(cl_ini.items(), key=operator.itemgetter(1),reverse=True))
        #Dans l'ordre de l'initiative, calsse les joueurs
        for keys in d_tmp2.keys():
            d_p[keys] = d_tmp[keys]
        #Appelle la classe bonus_choose pour la séléction des bonus pour chaque joueur 
        bonus_choose()

#Initialisation de plusieurs variables
e_1 = {}
e_2 = {}
e_1d = []
e_2d = []
nb_p = 0
d_tmp = {}
d_tmp2 = {}
cl_ini = {}
cl_ini2 = {}
d_p = {}
d_p2 = {}
d_p3 = {}
d_p4 = {}
c = 0

#Création de la frame du menyu
frame1 = tk.Frame(game,bg="#000000")

#Affichage des texts
t1 = Text_Button_Entry("Label","Bienvenue sur Monde des Bateaux",frame1,0,1,0,5,0,45,38,None,None)
t2 = Text_Button_Entry("Label","Veuillez créer les joueurs",frame1,1,1,0,5,0,0,28,None,None)
b1 = Text_Button_Entry("Button","Cliquez pour ajouter \nun joueur dans\nl'équipe 1",frame1,2,1,0,2,0,55,20,lambda e=1:Create_Player(e),None)
b2 = Text_Button_Entry("Button","Cliquez pour ajouter \nun joueur dans\nl'équipe 2",frame1,2,1,3,2,0,55,20,lambda e=2:Create_Player(e),None)
b3 = Text_Button_Entry("Button","Play",frame1,6,1,0,5,0,35,26,switch_frame,None)

#Pack de la frame
frame1.pack()

game.mainloop()