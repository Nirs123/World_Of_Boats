from random import randint
import tkinter as tk
import operator

game = tk.Tk()

game.unbind_class("Button", "<Key-space>")
game.title('Monde des Bateaux')
game.geometry('880x980')
game.minsize(880, 980)
game.maxsize(880, 980)
game.iconbitmap("logo.ico")
game.config(bg="#000000")

class perso:
    def __init__(self,pseudo,X,Y,Boats):
        self.x=X
        self.y=Y
        self.status = True
        if Boats=="Cruiser":
            self.name=pseudo
            self.boats="Cruiser"
            self.Pt_Vie=80000
            self.pv_max=80000
            self.attack=17000
            self.torps=0
            self.sub_bombs=10000
            self.bullet="HE"
            self.bonus=2
            self.mvm = 4
            self.range = 5
            self.ini = 20
        if Boats=="Destroyer":
            self.name=pseudo
            self.boats="Destroyer"
            self.Pt_Vie=34000
            self.pv_max=34000
            self.attack=10000
            self.torps=24000
            self.sub_bombs=15000
            self.bullet="HE"
            self.bonus=0
            self.inondation=1
            self.mvm = 5
            self.range = 5
            self.ini = 30
        if Boats=="Cuirasse":
            self.name=pseudo
            self.boats="Cuirasse"
            self.Pt_Vie=100000
            self.pv_max=100000
            self.attack=21000
            self.torps=0
            self.sub_bombs=13000
            self.bullet="AP"
            self.bonus=3
            self.mvm = 3
            self.range = 6
            self.ini = 10
        if Boats=="Submarine":
            self.name=pseudo
            self.boats="Submarine"
            self.Pt_Vie=25000
            self.pv_max=25000
            self.attack=0
            self.torps=29000
            self.sub_bombs=0
            self.bullet="AP"
            self.bonus=0
            self.inondation=2
            self.mvm = 5
            self.range = 5
            self.ini = 40
        self.recharge=0
        self.Pt_vie=self.Pt_Vie

    def Attack(self,self1):
        self.dgts=0
        if self.bullet=="HE":
            a=randint(1,4)
            if a==1:
                self.dgts=self.dgts+120*50
        if self.boats=="Submarine" or self.boats=="Destroyer":
            c=randint(1,4)
            if c==2:
                self.dgts=self.dgts+self.torps//3
                e=randint(self.inondation,6)
                if e==self.inondation:
                    self.dgts=self.dgts+100*90
            elif c==3:
                self.dgts=self.dgts+self.torps//2
                e=randint(self.inondation,5)
                if e==self.inondation:
                    self.dgts=self.dgts+100*90
            else:
                self.dgts=self.dgts+self.torps
                e=randint(self.inondation,4)
                if e==self.inondation:
                    self.dgts=self.dgts+100*90
        if self1.boats=="Submarine" and self.boats!="Submarine":
            self.dgts=0
            self.dgts=randint(4000,self.sub_bombs)
        if self.boats!="Submarine" and self1.boats=="Submarine" or self1.boats=="Destroyer":
            b=randint(1,3)
            if b==2:
                self.dgts=self.dgts+randint(int(self.attack/5),int(self.attack/2))
            else:
                self.dgts=self.dgts+randint(int(self.attack/5),self.attack)
        else:
            self.dgts=self.dgts+randint(int(self.attack/6),self.attack)
        self1.set_pv(self1.get_pt_vie()-self.dgts)

    def get_pseudo(self):
        return self.name

    def get_pt_vie(self):
        return self.Pt_Vie
    def set_pv(self,value):
        self.Pt_Vie = value

    def get_status(self):
        return self.status
    def set_status(self,status):
        self.status = status

    def get_dgts(self):
        return self.dgts

    def get_ini(self):
        return self.ini

    def bonus_vie(self):
        self.set_pv(self.get_pt_vie()+randint(int(self.Pt_Vie//6),int(self.Pt_Vie//4)))
        self.set_bonus(self.get_bonus()-1)
    def set_x(self,X):
        self.x=X
    def set_y(self,Y):
        self.y+=Y

    def get_mvm(self):
        return self.mvm

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

    def get_range(self):
        return self.range

    def deplacer(self,dx,dy):
        self.x+=dx
        self.y+=dy

    def set_bonus(self,value):
        self.bonus = value
    def get_bonus(self):
        return self.bonus
    def get_pv_max(self):
        return self.pv_max

class Text_Button_Entry:
    def __init__(self,type,text,frame,row,rowspan,column,columnspan,padx,pady,size,command,variable):
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
        if self.type == "Label":
            self.temp = tk.Label(self.frame, text = self.text, font=('Courrier',str(self.size)),bg="#000000", fg="#FFFFFF")
        elif self.type == "Button":
            self.temp = tk.Button(self.frame, text = self.text, font=('Courrier',str(self.size)),bg="#000000", fg="#FFFFFF",command = self.command)
        elif self.type == "Entry":
            self.temp = tk.Entry(self.frame,font=('Courrier',str(self.size)),bg="#000000", fg="#FFFFFF",textvariable=self.var)
        self.temp.grid(row = self.row,column = self.column,padx = self.padx,pady = self.pady,columnspan = self.columnspan, rowspan = self.rowspan)

    def grid_forget(self):
        self.temp.grid_forget()

class Create_Player:
    def __init__(self,e):
        self.equipe = e
        self.temp_choose = tk.Toplevel(game)
        self.temp_choose.title("Création joueur")
        self.temp_choose.geometry("400x400")
        self.temp_choose.config(bg="#000000")

        t1_j1 = Text_Button_Entry("Label","Menu de création du joueur",self.temp_choose,0,1,0,2,0,10,20,None,None)

        self.tmp_p = tk.StringVar()
        t2_j1 = Text_Button_Entry("Label","Pseudo:",self.temp_choose,1,1,0,1,25,0,15,None,None)
        e1_j1 = Text_Button_Entry("Entry",None,self.temp_choose,1,1,1,1,15,0,15,None,self.tmp_p)

        self.tmp_c = tk.StringVar()
        t3_j1 = Text_Button_Entry("Label","Classe:",self.temp_choose,2,1,0,1,25,10,15,None,None)
        e2_j1 = Text_Button_Entry("Entry",None,self.temp_choose,2,1,1,1,15,0,15,None,self.tmp_c)

        t4_j1 = Text_Button_Entry("Label","Cuirasse: Bcp de dégats et de vie \nmais rechargement plus long et \nvulnérable aux torpilles",self.temp_choose,3,1,0,2,25,3,12,None,None)
        t5_j1 = Text_Button_Entry("Label","Cruiser: Stats equilibrés et peut \nmettre en feu",self.temp_choose,4,1,0,2,25,3,12,None,None)
        t6_j1 = Text_Button_Entry("Label","Destroyer: Rapide et grosses torpilles, \npeut mettre en feu mais peu de vie",self.temp_choose,5,1,0,2,25,3,12,None,None)
        t7_j1 = Text_Button_Entry("Label","Submarine: Faible vie mais peut esquiver \nles obus et de grosses torpilles",self.temp_choose,6,1,0,2,25,3,12,None,None)

        b1_j1 = Text_Button_Entry("Button","OK ",self.temp_choose,7,1,0,2,25,3,12,self.teams_players,None)

    def teams_players(self):
        global d_p,d_p2,d_p3,nb_p,d_p4
        tmp = str(f"player{nb_p}")
        self.valid = False
        self.temp_choose.destroy()
        if str(self.tmp_p.get()) != "":
            if str(self.tmp_c.get()) == "Cruiser" or str(self.tmp_c.get()) == "Destroyer" or str(self.tmp_c.get()) == "Cuirasse" or str(self.tmp_c.get()) == "Submarine":
                nb_p += 1
                if self.equipe == 1:
                    if len(e_1) < 3:
                        q = perso(self.tmp_p.get(),randint(0,2),randint(0,19),self.tmp_c.get())
                        t8 = Text_Button_Entry("Label","Pseudo: "+str(self.tmp_p.get())+"\nClasse: "+str(self.tmp_c.get()),frame1,3+len(e_1),1,0,2,0,25,20,None,None)
                        e_1[tmp] = q.get_pseudo()
                        self.valid = True
                elif self.equipe == 2:
                    if len(e_2) < 3:
                        q = perso(self.tmp_p.get(),randint(17,19),randint(0,19),self.tmp_c.get())
                        t9 = Text_Button_Entry("Label","Pseudo: "+str(self.tmp_p.get())+"\nClasse: "+str(self.tmp_c.get()),frame1,3+len(e_2),1,3,2,0,25,20,None,None)
                        e_2[tmp] = q.get_pseudo()
                        self.valid = True
            else:
                error_box("ERREUR: Classe")
        else:
            error_box("ERREUR: Pseudo")
        if self.valid:
            d_tmp[tmp] = q
            d_p2[tmp] = q.get_pseudo()
            d_p3[tmp] = self.equipe
            d_p4[tmp] = self.tmp_c.get()

class error_box:
    def __init__(self,msg):
        self.msg = msg
        self.tmp_box = tk.Toplevel(game)
        self.tmp_box.title("ERREUR")
        self.tmp_box.config(bg="#000000")
        t = Text_Button_Entry("Label",msg,self.tmp_box,0,1,0,1,10,10,20,None,None)
        b = Text_Button_Entry("Button","OK",self.tmp_box,1,1,0,1,0,0,14,self.tmp_box.destroy,None)

class main_game:
    def __init__(self):
        global e_1,e_2,d_p,d_p2,d_p3,nb_p,a
        self.tour = 1
        self.frame2 = tk.Frame(game,bg="#000000")
        self.frame3 = tk.Frame(game,bg="#000000")

        self.indexs = []
        for key in d_p.keys():
            self.indexs.append(key)
        self.index = -1
        self.tmp_player = str(self.indexs[self.index])

        self.ca = tk.Canvas(self.frame2,height=880,width=880,bg="#03005e",highlightthickness=0)
        self.ca.pack(fill=tk.BOTH, expand=True)
        self.ca.bind('<Configure>', self.create_grid)

        self.draw_players()

        self.update_tour()

        self.frame2.pack()
        self.frame3.pack()

        self.a = False

        game.bind('<Left>',self.mvm_left)
        game.bind('<Right>',self.mvm_right)
        game.bind('<Up>',self.mvm_up)
        game.bind('<Down>',self.mvm_down)

    def create_grid(self,event=None):
        w = self.ca.winfo_width()
        h = self.ca.winfo_height()
        self.ca.delete('grid_line')

        for i in range(0, w, 44):
            self.ca.create_line([(i, 0), (i, h)], tag='grid_line')

        for i in range(0, h, 44):
            self.ca.create_line([(0, i), (w, i)], tag='grid_line')

    def draw_players(self):
        self.tmp_coord = []
        for key in d_p:
            tmp_x = d_p[key].get_x()*44
            tmp_y = d_p[key].get_y()*44
            self.tmp_coord.append(tuple((d_p[key].get_x(),d_p[key].get_y())))
            if d_p3[key] == 1:
                if d_p[key].get_pt_vie() <= 0:
                    self.rect = self.ca.create_rectangle(tmp_x,tmp_y,tmp_x+44,tmp_y+44,fill='grey')
                    self.ca.create_text(tmp_x+22,tmp_y+22,text=" "+str(d_p2[key])+"\n"+str(d_p4[key]),font=('Courrier',"7","bold"))
                else:
                    self.rect = self.ca.create_rectangle(tmp_x,tmp_y,tmp_x+44,tmp_y+44,fill='red')
                    self.ca.create_text(tmp_x+22,tmp_y+22,text=" "+str(d_p2[key])+"\n"+str(d_p4[key]),font=('Courrier',"7","bold"))
            elif d_p3[key] == 2:
                if d_p[key].get_pt_vie() <= 0:
                    self.rect = self.ca.create_rectangle(tmp_x,tmp_y,tmp_x+44,tmp_y+44,fill='grey')
                    self.ca.create_text(tmp_x+22,tmp_y+22,text=" "+str(d_p2[key])+"\n"+str(d_p4[key]),font=('Courrier',"7","bold"))
                else:
                    self.rect = self.ca.create_rectangle(tmp_x,tmp_y,tmp_x+44,tmp_y+44,fill='green')
                    self.ca.create_text(tmp_x+22,tmp_y+22,text=" "+str(d_p2[key])+"\n"+str(d_p4[key]),font=('Courrier',"7","bold"))

    def update_tour(self):
        self.a = False
        self.delete_frame()
        if self.index + 1 < len(self.indexs):
            self.index += 1
            self.tmp_player = str(self.indexs[self.index])
        else:
            self.index = 0
            self.tmp_player = str(self.indexs[self.index])
            self.tour += 1
        if len(e_1) == len(e_1d):
            self.end_game(1)
        elif len(e_2) == len(e_2d):
            self.end_game(2)
        else:
            if d_p[self.tmp_player].get_pt_vie() <=0:
                self.update_tour()
            else:
                self.update_frame3(self.tmp_player)

    def update_frame3(self,key):
        self.key = key
        self.tmp_mvm = d_p[self.key].get_mvm()
        self.t1 = Text_Button_Entry("Label","Tour n°"+str(self.tour),self.frame3,0,2,0,1,0,14,22,None,None)

        self.circle(d_p[self.key].get_x(),d_p[self.key].get_y(),d_p[self.key].get_range())

        self.t2 = Text_Button_Entry("Label","Joueur: "+str(d_p2[self.key]),self.frame3,0,1,1,1,20,8,20,None,None)
        self.t3 = Text_Button_Entry("Label","PV: "+str(d_p[self.key].get_pt_vie()),self.frame3,1,1,1,1,0,0,20,None,None)
        self.b1 = Text_Button_Entry("Button","Skip",self.frame3,0,2,2,1,15,8,18,self.passer,None)
        self.b2 = Text_Button_Entry("Button","Attaque",self.frame3,0,2,3,1,15,8,18,self.attack,None)
        self.b3 = Text_Button_Entry("Button","Soins",self.frame3,0,2,4,1,15,8,18,self.soins,None)
        self.b4 = Text_Button_Entry("Button","Déplacement",self.frame3,0,2,5,1,15,8,18,self.deplacement,None)

    def circle(self,x,y,r):
        self.r = (r * 44) + 22
        self.x = (x * 44) + 22
        self.y = (y * 44) + 22
        self.x0 = self.x - self.r
        self.y0 = self.y - self.r
        self.x1 = self.x + self.r
        self.y1 = self.y + self.r
        self.temp_ca = self.ca.create_oval(self.x0,self.y0,self.x1,self.y1,width=2,outline='yellow')

    def passer(self):
        self.delete_buttons()
        self.t4 = Text_Button_Entry("Label","Tour Skippé\ncliquez sur OK",self.frame3,0,2,2,1,15,8,24,None,None)
        self.b5 = Text_Button_Entry("Button","OK",self.frame3,0,2,3,1,15,8,18,self.passer_2,None)

    def passer_2(self):
        self.t4.grid_forget()
        self.b5.grid_forget()
        self.update_tour()

    def attack(self):
        self.tmp_target = tk.StringVar()
        self.delete_buttons()
        self.t5 = Text_Button_Entry("Label","Qui voulez\nvous attaquer ?",self.frame3,0,2,2,1,15,8,24,None,None)
        self.e1 = Text_Button_Entry("Entry",None,self.frame3,0,2,3,1,15,8,16,None,self.tmp_target)
        self.b6 = Text_Button_Entry("Button","OK",self.frame3,0,2,4,1,15,8,18,self.attack_2,None)

    def attack_2(self):
        self.t5.grid_forget()
        self.e1.grid_forget()
        self.b6.grid_forget()
        self.target_key = [k for k, v in d_p2.items() if v == self.tmp_target.get()]
        if len(self.target_key) == 0:
            self.t6 = Text_Button_Entry("Label","Erreur lors de la séléction",self.frame3,0,2,2,1,15,18,24,None,None)
            self.b7 = Text_Button_Entry("Button","OK",self.frame3,0,2,4,1,15,18,18,self.attack_3,None)
        else:
            if d_p3[self.target_key[0]] == d_p3[self.key]:
                self.t6 = Text_Button_Entry("Label","Vous ne pouvez pas\nattaquer un allié",self.frame3,0,2,2,1,15,8,24,None,None)
                self.b7 = Text_Button_Entry("Button","OK",self.frame3,0,2,4,1,15,8,18,self.attack_3,None)
            else:
                if ((d_p[self.target_key[0]].get_x()-d_p[self.key].get_x())**2) + ((d_p[self.target_key[0]].get_y()-d_p[self.key].get_y())**2) <= ((d_p[self.key].get_range())**2):
                    if d_p[self.target_key[0]].get_pt_vie() >0:
                        d_p[self.tmp_player].Attack(d_p[self.target_key[0]])
                        if d_p[self.target_key[0]].get_pt_vie() <=0:
                            self.t6 = Text_Button_Entry("Label",str(self.tmp_target.get())+" est mort",self.frame3,0,2,2,1,15,18,24,None,None)
                            self.b7 = Text_Button_Entry("Button","OK",self.frame3,0,2,4,1,15,8,18,self.attack_3,None)
                            if d_p[self.target_key[0]].get_status() == True:
                                if d_p3[self.target_key[0]] == 1:
                                    e_1d.append(self.target_key[0])
                                if d_p3[self.target_key[0]] == 2:
                                    e_2d.append(self.target_key[0])
                                self.delete_frame_2()
                                self.draw_players()
                                d_p[self.target_key[0]].set_status(False)
                        else:
                            self.t6 = Text_Button_Entry("Label",str(self.tmp_target.get())+" a désormais "+str(d_p[self.target_key[0]].get_pt_vie())+"PV\nDégats infligés: "+str(d_p[self.key].get_dgts())+"PV",self.frame3,0,2,2,1,15,8,24,None,None)
                            self.b7 = Text_Button_Entry("Button","OK",self.frame3,0,2,4,1,15,8,18,self.attack_3,None)
                    else:
                        self.t6 = Text_Button_Entry("Label","Vous ne pouvez pas attaquer un mort",self.frame3,0,2,2,1,15,18,24,None,None)
                        self.b7 = Text_Button_Entry("Button","OK",self.frame3,0,2,4,1,15,8,18,self.attack_3,None)
                else:
                    self.t6 = Text_Button_Entry("Label","Vous êtes trop loin",self.frame3,0,2,2,1,15,18,24,None,None)
                    self.b7 = Text_Button_Entry("Button","OK",self.frame3,0,2,4,1,15,18,18,self.attack_3,None)

    def attack_3(self):
        self.t6.grid_forget()
        self.b7.grid_forget()
        self.update_tour()

    def soins(self):
        self.delete_buttons()
        if d_p[self.key].get_pt_vie() != d_p[self.key].get_pv_max():
            if d_p[self.key].get_bonus() > 0 :
                d_p[self.key].bonus_vie()
                if d_p[self.key].get_pt_vie() > d_p[self.key].get_pv_max():
                    d_p[self.key].set_pv(d_p[self.key].get_pv_max())
                self.t7 = Text_Button_Entry("Label","Vous avez désormais "+str(d_p[self.key].get_pt_vie())+"PV\nBonus Restants: "+str(d_p[self.key].get_bonus()),self.frame3,0,2,2,1,15,8,24,None,None)
                self.b8 = Text_Button_Entry("Button","OK",self.frame3,0,2,4,1,15,8,18,self.soins_2,None)
            else:
                self.t7 = Text_Button_Entry("Label","Vous n'avez plus de bonus",self.frame3,0,2,2,1,15,20,24,None,None)
                self.b8 = Text_Button_Entry("Button","OK",self.frame3,0,2,4,1,15,8,18,self.soins_2,None)
        else:
            self.t7 = Text_Button_Entry("Label","Vous êtes déjà a vos PV Max",self.frame3,0,2,2,1,15,20,24,None,None)
            self.b8 = Text_Button_Entry("Button","OK",self.frame3,0,2,4,1,15,8,18,self.soins_2,None)

    def soins_2(self):
        self.t7.grid_forget()
        self.b8.grid_forget()
        self.update_tour()

    def deplacement(self):
        self.a = True
        self.delete_buttons()
        self.valid = True
        if self.tmp_mvm > 0:
            self.t8 = Text_Button_Entry("Label","Déplacements réstants: "+str(self.tmp_mvm)+" ",self.frame3,0,1,0,1,0,20,22,None,None)
            self.b9 = Text_Button_Entry("Button"," ↑ ",self.frame3,0,1,1,1,15,20,24,self.dep_haut,None)
            self.b10 = Text_Button_Entry("Button","←",self.frame3,0,1,2,1,15,20,24,self.dep_gauche,None)
            self.b11 = Text_Button_Entry("Button","→",self.frame3,0,1,3,1,15,20,24,self.dep_droite,None)
            self.b12 = Text_Button_Entry("Button"," ↓ ",self.frame3,0,1,4,1,15,20,24,self.dep_bas,None)
            self.b13 = Text_Button_Entry("Button","SKIP",self.frame3,0,1,5,1,15,20,18,self.skip,None)
        else:
            self.t8 = Text_Button_Entry("Label","Déplacements finis",self.frame3,0,2,2,1,15,20,24,None,None)
            self.b9 = Text_Button_Entry("Button","OK",self.frame3,0,2,4,1,15,8,18,self.skip_2,None)
            self.a = False
        
    def skip(self):
        self.delete_buttons_2()
        self.passer()

    def skip_2(self):
        self.delete_buttons_2()
        self.update_tour()

    def dep_haut(self):
        if d_p[self.key].get_y() - 1 >= 0:
            for elements in self.tmp_coord:
                if tuple((d_p[self.key].get_x(),d_p[self.key].get_y()-1)) == elements:
                    self.valid = False
            if self.valid:
                d_p[self.key].deplacer(0,-1)
        self.dep()

    def dep_bas(self):
        if d_p[self.key].get_y() + 1 <=19:
            for elements in self.tmp_coord:
                if tuple((d_p[self.key].get_x(),d_p[self.key].get_y()+1)) == elements:
                    self.valid = False
            if self.valid:
                d_p[self.key].deplacer(0,1)
        self.dep()

    def dep_gauche(self):
        if d_p[self.key].get_x() - 1 >= 0:
            for elements in self.tmp_coord:
                if tuple((d_p[self.key].get_x()-1,d_p[self.key].get_y())) == elements:
                    self.valid = False
            if self.valid:
                d_p[self.key].deplacer(-1,0)
        self.dep()

    def dep_droite(self):
        if d_p[self.key].get_x() + 1 <= 19:
            for elements in self.tmp_coord:
                if tuple((d_p[self.key].get_x()+1,d_p[self.key].get_y())) == elements:
                    self.valid = False
            if self.valid:
                d_p[self.key].deplacer(1,0)
        self.dep()

    def dep(self):
        self.delete_buttons_2()
        self.tmp_mvm -= 1
        self.delete_frame_2()
        self.draw_players()
        self.deplacement()

    def mvm_left(self,arg):
        if self.a:
            self.dep_gauche()

    def mvm_right(self,arg):
        if self.a:
            self.dep_droite()

    def mvm_up(self,arg):
        if self.a:
            self.dep_haut()

    def mvm_down(self,arg):
        if self.a:
            self.dep_bas()

    def delete_frame(self):
        self.frame3.grid_forget()

    def delete_frame_2(self):
        self.ca.delete('all')
        self.create_grid()

    def delete_buttons(self):
        self.t1.grid_forget()
        self.t2.grid_forget()
        self.t3.grid_forget()
        self.b1.grid_forget()
        self.b2.grid_forget()
        self.b3.grid_forget()
        self.b4.grid_forget()
        self.ca.delete(self.temp_ca)

    def delete_buttons_2(self):
        self.t8.grid_forget()
        self.b9.grid_forget()
        self.b10.grid_forget()
        self.b11.grid_forget()
        self.b12.grid_forget()
        self.b13.grid_forget()

    def end_game(self,lose):
        self.lose = lose
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
    if nb_p == 0:
        error_box("ERREUR: Aucun Joueur")
    else:
        frame1.grid_forget()
        frame1.destroy()
        for values in d_tmp:
            cl_ini[values] = d_tmp[values].get_ini()
        d_tmp2 = dict(sorted(cl_ini.items(), key=operator.itemgetter(1),reverse=True))
        for keys in d_tmp2.keys():
            d_p[keys] = d_tmp[keys]
        print(d_p)
        main_game()

e_1 = {}
e_2 = {}
e_1d = []
e_2d = []
nb_p = 0
d_tmp = {}
d_tmp2 = {}
cl_ini = {}
d_p = {}
d_p2 = {}
d_p3 = {}
d_p4 = {}

frame1 = tk.Frame(game,bg="#000000")

t1 = Text_Button_Entry("Label","Bienvenue sur Monde des Bateaux",frame1,0,1,0,5,0,45,38,None,None)
t2 = Text_Button_Entry("Label","Veuillez créer les joueurs",frame1,1,1,0,5,0,0,28,None,None)
b1 = Text_Button_Entry("Button","Cliquez pour ajouter \nun joueur dans\nl'équipe 1",frame1,2,1,0,2,0,55,20,lambda e=1:Create_Player(e),None)
b2 = Text_Button_Entry("Button","Cliquez pour ajouter \nun joueur dans\nl'équipe 2",frame1,2,1,3,2,0,55,20,lambda e=2:Create_Player(e),None)
b3 = Text_Button_Entry("Button","Play",frame1,6,1,0,5,0,35,26,switch_frame,None)

frame1.pack()

game.mainloop()