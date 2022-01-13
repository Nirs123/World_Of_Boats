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
        self.x = X
        self.y = Y
        self.status = True
        self.passiv_heal = False
        if Boats=="Cruiser":
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
        self.dgts=0
        self.r1 = randint(0,4)
        self.r2 = randint(0,3)
        self.r3 = randint(1,5)
        if self.atq_type == 0:
            self.dgts = self.dgts + (self.atq * self.r1)
            if self.r3 == 1:
                self.dgts = self.dgts + (((self1.get_pv_max()//10)//2)*self.r1)
            self.dgts = self.dgts - ((self1.get_res_obus()*self.dgts)//100)
        elif self.atq_type == 1:
            self.dgts = self.dgts + (self.atq * self.r2)
            self.dgts = self.dgts - ((self1.get_res_torp()*self.dgts)//100)
        elif self.atq_type == 2:
            self.tmp = self.atq // 2
            self.dgts = self.dgts + (self.tmp * self.r1) + (self.tmp * self.r2)
            if self.r3 == 1:
                self.dgts = self.dgts + (((self1.get_pv_max()//10)//2)*self.r1)
            self.dgts = self.dgts - ((((self1.get_res_torp() + self1.get_res_obus()) // 2)*self.dgts)//100)
        self.r4 = randint(0,100)
        if self.r4 <= self1.esquive:
            self.dgts = 0
        else:
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

    def set_ini(self,value):
        self.ini = value
    def get_ini(self):
        return self.ini

    def get_res_obus(self):
        return self.obus_resist
    def get_res_torp(self):
        return self.torp_resist
    def set_res_obus(self,value):
        self.obus_resist = value
    def set_res_torp(self,value):
        self.torp_resist = value

    def get_esquive(self):
        return self.esquive
    def set_esquive(self,value):
        self.esquive = value

    def bonus_vie(self):
        self.set_pv(self.get_pt_vie()+randint(int(self.Pt_Vie//6),int(self.Pt_Vie//4)))
        self.set_bonus(self.get_bonus()-1)
    def set_x(self,X):
        self.x=X
    def set_y(self,Y):
        self.y+=Y

    def get_mvm(self):
        return self.mvm
    def set_mvm(self,value):
        self.mvm = value

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

    def get_range(self):
        return self.range
    def set_range(self,value):
        self.range = value

    def deplacer(self,dx,dy):
        self.x+=dx
        self.y+=dy

    def set_bonus(self,value):
        self.bonus = value
    def get_bonus(self):
        return self.bonus
    def get_pv_max(self):
        return self.pv_max
    def set_pv_max(self,value):
        self.pv_max = value

    def get_atq(self):
        return self.atq
    def set_atq(self,value):
        self.atq = value

    def get_boat(self):
        return self.boats
    def switch_passiv_heal(self):
        if self.passiv_heal:
            self.passiv_heal = False
        elif self.passiv_heal == False:
            self.passiv_heal = True
    def get_passiv_heal(self):
        return self.passiv_heal

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
        elif self.type == "Check":
            self.temp = tk.Checkbutton(self.frame,text = self.text, font =('Courrier',str(self.size)),bg="#000000", fg="grey",variable=self.var,width=50)
        self.temp.grid(row = self.row,column = self.column,padx = self.padx,pady = self.pady,columnspan = self.columnspan, rowspan = self.rowspan)

    def grid_forget(self):
        self.temp.grid_forget()

class index_class:
    def __init__(self):
        self.cui = [100000,18000,"Obus",3,6,3,10,2,7,12]
        self.cru = [80000,16000,"Obus et\nTorpilles",4,5,2,20,5,5,5]
        self.des = [34000,20000,"Obus et\nTorpilles",6,5,0,30,8,4,3]
        self.sub = [25000,24000,"Torpilles",5,5,0,40,10,80,2]
        self.names = ["Cuirassé","Cruiser","Destroyer","Submarine"]
        self.attri = ["PV","ATQ","   Type\nd'attaque","Mouvements","Range","Heals","Initiative","Esquive","Resistance\n   Obus","Resistance\n  Torpilles"]
        self.list = [self.cui,self.cru,self.des,self.sub]

        self.chart = tk.Toplevel(game)
        self.chart.title("Statistiques détaillées")
        self.chart.geometry("1160x540")
        self.chart.minsize(1160,540)
        self.chart.maxsize(1160,540)
        self.chart.config(bg="#000000")

        self.ca2 = tk.Canvas(self.chart, height=455, width=1160, bg="#000000")
        self.show_values()
        self.ca2.pack()
        self.ca2.bind('<Configure>', self.create_grid_2)

        self.tmp = tk.Button(self.chart, text = "QUIT", font=('Courrier',"18","bold"),bg="#000000", fg="#FFFFFF",command = self.quit)
        self.tmp.pack(pady=15)

    def show_values(self):
        self.y = 1
        for name in self.names:
            self.ca2.create_text(52.5,self.y*90+45,text=str(name),font=('Courrier',"13","bold"),fill="white")
            self.y += 1

        self.x = 1
        for attri in self.attri:
            self.ca2.create_text(self.x*105.5+53,45,text=str(attri),font=('Courrier',"13","bold"),fill="white")
            self.x += 1

        self.u = 1
        self.j = 1
        for i in self.list:
            for value in i:
                self.ca2.create_text(self.u*105.5+52.5,self.j*90+45,text=str(value),font=('Courrier',"14","bold"),fill="white")
                self.u += 1
            self.u = 1
            self.j += 1

    def create_grid_2(self,event = None):
        w = self.ca2.winfo_width()
        h = self.ca2.winfo_height()
        self.ca2.delete('grid_line')

        for i in range(0, w, 106):
            self.ca2.create_line([(i, 0), (i, h)], tag='grid_line',fill='white')

        for i in range(0, h-50, 90):
            self.ca2.create_line([(0, i), (w, i)], tag='grid_line',fill='white')

    def quit(self):
        self.chart.destroy()

class Create_Player:
    def __init__(self,e):
        self.equipe = e
        self.temp_choose = tk.Toplevel(game)
        self.temp_choose.title("Création joueur")
        self.temp_choose.geometry("420x420")
        self.temp_choose.minsize(420,450)
        self.temp_choose.maxsize(420,450)
        self.temp_choose.config(bg="#000000")

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

class bonus_choose:
    def __init__(self):
        global nb_p
        self.indexs = []
        self.index = -1
        for key in d_p.keys():
            self.indexs.append(key)
        self.key = str(self.indexs[self.index])
        self.update_player()

    def update_player(self):
        global nb_p
        self.index += 1
        if self.index != len(self.indexs):
            self.key = str(self.indexs[self.index])
        self.bonus_box()

    def bonus_box(self):
        self.classe = d_p[self.key].get_boat()
        self.tmp_bonus = tk.Toplevel(game)
        self.tmp_bonus.config(bg="#000000")
        self.tmp_bonus.geometry("650x400")
        self.tmp_bonus.title("Choix Bonus")
        self.tmp_bonus.minsize(650, 400)
        self.tmp_bonus.maxsize(650, 400)
        t3 = Text_Button_Entry("Label","Choisissez vos 2 bonus: "+str(d_p[self.key].get_pseudo()),self.tmp_bonus,0,1,0,1,18,20,20,None,None)
        self.opt1,self.opt2,self.opt3,self.opt4,self.opt5 = tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar(),tk.IntVar()
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
        o1 = Text_Button_Entry("Check",t1,self.tmp_bonus,1,1,0,1,5,7,14,None,self.opt1)
        o2 = Text_Button_Entry("Check",t2,self.tmp_bonus,2,1,0,1,5,7,14,None,self.opt2)
        o3 = Text_Button_Entry("Check",t3,self.tmp_bonus,3,1,0,1,5,7,14,None,self.opt3)
        o4 = Text_Button_Entry("Check",t4,self.tmp_bonus,4,1,0,1,5,7,14,None,self.opt4)
        o5 = Text_Button_Entry("Check",t5,self.tmp_bonus,5,1,0,1,5,7,14,None,self.opt5)

    def choosen(self):
        global c
        self.tmp_list = []
        self.tmp_list.append(self.opt1.get())
        self.tmp_list.append(self.opt2.get())
        self.tmp_list.append(self.opt3.get())
        self.tmp_list.append(self.opt4.get())
        self.tmp_list.append(self.opt5.get())
        if self.tmp_list.count(1) < 2:
            error_box("ERREUR: Pas assez de bonus choisis")
        if self.tmp_list.count(1) > 2:
            error_box("ERREUR: Trop de bonus choisis")
        if self.tmp_list.count(1) == 2:
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
            if c == nb_p:
                d_p.clear()
                for values in d_tmp:
                    cl_ini2[values] = d_tmp[values].get_ini()
                d_tmp2 = dict(sorted(cl_ini2.items(), key=operator.itemgetter(1),reverse=True))
                for keys in d_tmp2.keys():
                    d_p[keys] = d_tmp[keys]
                main_game()
                frame1.grid_forget()
                frame1.destroy()
            else:
                self.update_player()

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
            if d_p[key].get_pt_vie() <= 0:
                self.rect = self.ca.create_rectangle(tmp_x,tmp_y,tmp_x+44,tmp_y+44,fill='grey')
                self.ca.create_text(tmp_x+22,tmp_y+22,text=" "+str(d_p2[key])+"\n"+str(d_p4[key]),font=('Courrier',"7","bold"))
            else:
                if d_p3[key] == 1:
                    self.rect = self.ca.create_rectangle(tmp_x,tmp_y,tmp_x+44,tmp_y+44,fill='red')
                    self.ca.create_text(tmp_x+22,tmp_y+22,text=" "+str(d_p2[key])+"\n"+str(d_p4[key]),font=('Courrier',"7","bold"))
                elif d_p3[key] == 2:
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

        if d_p[self.key].get_passiv_heal() == True and d_p[self.key].get_pt_vie() != d_p[self.key].get_pv_max():
            d_p[self.key].set_pv(int(d_p[self.key].get_pt_vie()+(d_p[self.key].get_pv_max()/100)))

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
                self.t7 = Text_Button_Entry("Label","Vous avez désormais "+str(d_p[self.key].get_pt_vie())+"PV\nSoins Restants: "+str(d_p[self.key].get_bonus()),self.frame3,0,2,2,1,15,8,24,None,None)
                self.b8 = Text_Button_Entry("Button","OK",self.frame3,0,2,4,1,15,8,18,self.soins_2,None)
            else:
                self.t7 = Text_Button_Entry("Label","Vous n'avez plus de soins",self.frame3,0,2,2,1,15,20,24,None,None)
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
        b3.grid_forget()
        for values in d_tmp:
            cl_ini[values] = d_tmp[values].get_ini()
        d_tmp2 = dict(sorted(cl_ini.items(), key=operator.itemgetter(1),reverse=True))
        for keys in d_tmp2.keys():
            d_p[keys] = d_tmp[keys]
        bonus_choose()

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

frame1 = tk.Frame(game,bg="#000000")

t1 = Text_Button_Entry("Label","Bienvenue sur Monde des Bateaux",frame1,0,1,0,5,0,45,38,None,None)
t2 = Text_Button_Entry("Label","Veuillez créer les joueurs",frame1,1,1,0,5,0,0,28,None,None)
b1 = Text_Button_Entry("Button","Cliquez pour ajouter \nun joueur dans\nl'équipe 1",frame1,2,1,0,2,0,55,20,lambda e=1:Create_Player(e),None)
b2 = Text_Button_Entry("Button","Cliquez pour ajouter \nun joueur dans\nl'équipe 2",frame1,2,1,3,2,0,55,20,lambda e=2:Create_Player(e),None)
b3 = Text_Button_Entry("Button","Play",frame1,6,1,0,5,0,35,26,switch_frame,None)

frame1.pack()

game.mainloop()