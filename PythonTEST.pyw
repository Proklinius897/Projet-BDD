import mysql.connector
from tkinter import *
from datetime import *
import re

"""
mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='',
    auth_plugin='mysql_native_password',
    database="psychologue"
)"""

def getvalue(widget,widget2):
    tab =["0","0"] 
    tab[0]=widget.get()
    tab[1]=widget2.get()
    return tab


def pri():
    print("gello")







  




def connection(compte,mdp,thisroot):
  tab1 = getvalue(compte,mdp)
  global mydb
  mydb = mysql.connector.connect(
    host="localhost",
    user=tab1[0],
    passwd=tab1[1],
    auth_plugin='mysql_native_password',
    database="psychologue"
  )
  if mydb!=None:
    deuxieme(thisroot)
    
  
  



"""
sql = "INSERT INTO patient (Id_client,Id_couple,Nom,Prenom,Addresse,Mail,Telephone,Sexe,DateNaissance,Moyen) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
val = ("","123249","John", "Sim", "57 rue de tanger","simon.tancev@yahoo.fr","0657","0","1999-12-16","jzal")
mycursor.execute(sql,val)
mydb.commit()"""





def printable(name):
  mycursor = mydb.cursor()
  mycursor.execute("SELECT * FROM "+name)
  myresult = mycursor.fetchall()
  lenght=len(myresult)
  
  for x in myresult:
    print(x)
    
  return myresult

def deco(root):
  root.destroy()


def premiere (root2):
  if root2!=None:
    deco(root2)
  root = Tk()
  center(root)
  root.title("Connexion page")
  lab1 = Label(root,text="Bienvenue, veuilliez vous connecter")
  lab2 = Label(root,text="Identifiant : ")
  lab3=Label(root,text="Mot de passe")
  entryname= Entry(root)
  entrypass= Entry(root,show='*')

  lab1.grid(column=0, row=0)
  lab2.grid(column=0, row=1)
  entryname.grid(column=1, row=1)
  lab3.grid(column=0, row=2)
  entrypass.grid(column=1, row=2)
  button = Button(root,text='Connexion',command = lambda : connection(entryname,entrypass,root))
  
  button.grid(column=0,row=5)
  
  return root



def deuxieme(root3):
  
  deco(root3)
  root2 = Tk()
  center(root2)
  root2.title("Menu")
  lab1 = Label(root2, text="----------------connexion établie-----------------")
  lab2 =Label(root2, text="Que voulez-vous faire ?")
  button1 =Button(root2, text="Organiser un rdv",command = lambda : inputrdv(root2))
  calendrier = Button(root2,text="Consulter les rendez-vous")
  button2 =Button(root2, text="Informations Clients", command = lambda: infoclients(root2))
  inscrip= Button(root2,text='Inscription de clients ',command = lambda : inscription(root2))
  button3=Button(root2, text="Déconnexion", command = lambda : premiere(root2))
  lab1.grid(column=0, row=0)
  lab2.grid(column=0,row=1)
  button1.grid(column=0,row=2)
  calendrier.grid(column=0,row=3)
  button2.grid(column=0,row=4)
  inscrip.grid(column=0,row=5)
  button3.grid(column=0,row=6)
  return root2

class option():  ###Cette classe nous permet de créer les option pour L'option menu et ainsi de pouvoir input les rdv
  OPTIONannée=[None]*4
  OPTIONmois=[None]*12
  OPTIONjour=[None]*32
  OPTIONheure=[None]*24

  
  
  i=0
  j=0
  k=0
  l=0
  l1=8.0
  today=date.today()
  currentyear = int(today.strftime("%Y"))
  currentmonth=int(today.strftime("%m"))
  currentday=int(today.strftime("%d"))
  while i <3 : 
    OPTIONannée[i]=currentyear
    currentyear=currentyear+1
    i+=1
  while j <12 :
    OPTIONmois[j]=j+1
  
    j+=1
  while k<31:
    OPTIONjour[k]=k+1
    k+=1
  while l1<20:
    
    OPTIONheure[l]=l1
    l+=1
    l1+=0.5
  def toStringheure(self, OPTIONheure): #CELA CONVERTIT POUR L'UTILISATEUR LES HEURE EN FORMAT DOUBLE ----> EN FORMAT LISIBLE
    OPTIONheurestring=[None]*24
    p=0
    print(OPTIONheure)
    print(OPTIONheure[0])
    
    while p<24:
      print (OPTIONheure[p]-float(int(OPTIONheure[p])))
      if OPTIONheure[p]-float(int(OPTIONheure[p]))==0.5:
        OPTIONheurestring[p]=str(int(OPTIONheure[p]))+"h30"
        p+=1
      else :
        OPTIONheurestring[p]=str(int(OPTIONheure[p]))+"h"
        p+=1
    return OPTIONheurestring
  
    
  

  

  
def selectname(id,name,name2,group,table):
  mycursor = mydb.cursor()
  mycursor.execute("SELECT "+id+", "+name+", "+name2 + " FROM " + table +" GROUP BY "+ group )
  myresult = mycursor.fetchall()
  lenght=len(myresult)
  
  for x in myresult:
    print(x)
    
    
    
  return myresult

def sortdv (): ###On va ranger dans un tableau l'ordre des consultation
  mycursor = mydb.cursor()
  mycursor.execute("SELECT id_consult FROM consultation ")
  myresult = mycursor.fetchall()
  dernier=myresult[-1][0]
  
  # mysecond=[None]*(len(myresult)-1)
  # p=0

  # while p <len(myresult):
  #   mysecond[p]=int(myresult[p][0])
  #   p+1
    
  return dernier


def inscription(root):
  deco(root)
  root=Tk()
  center(root)
  root.title("Inscription")
  nomlabel=Label(root,text="Nom")
  nom=Entry(root,text="Nom")
  nomlabel.pack(side='top')
  nom.pack(side='top')
  
  prenomlabel=Label(root,text="Prenom")
  prenom=Entry(root,text="Prenom")
  prenomlabel.pack(side='top')
  prenom.pack(side='top')
  agelabel=Label(root,text="Age")
  age=Entry(root,text="Age")
  agelabel.pack(side='top')
  age.pack(side='top')
  
  emaillabel=Label(root,text="Email")
  email=Entry(root,text="Email")
  emaillabel.pack(side='top')
  email.pack(side='top')
  couplelabel=Label(root,text="Êtes vous en couple avec l'un de nos clients?")
  couple=Entry(root,text="Couple")
  couplelabel.pack(side='top')
  couple.pack(side='top')
  passwordlabel=Label(root,text="Veuilliez choisir un mot de passe")
  password=Entry(root,show="*")
  passwordlabel.pack(side='top')
  password.pack(side='top')  
  password2label=Label(root,text="Veuilliez vérifier le mot de passe")
  password2=Entry(root,show="*")
  password2label.pack(side='top')
  password2.pack(side='top')
  connulabel=Label(root,text="Comment avez-vous connu ce cabinet?")
  connu=Entry(root,text="Moyen")  
  connulabel.pack(side='top')
  connu.pack(side='top')
  vals = ['1', '2','3']
  etiqs = ['Homme', 'Femme','Autre']
  varGr = StringVar()
  varGr.set(vals[1])
  for i in range(3):
      b = Radiobutton(root, variable=varGr, text=etiqs[i], value=vals[i])
      b.pack(side='left', expand=1)
  retour=Button(root,text="Retour",command=lambda : deuxieme(root))
  retour.pack(side="bottom")
  
  valider=Button(root,text="Valider",command= lambda : inscrire(nom.get(),prenom.get(),email.get(),password.get(),password2.get(),couple.get(),age.get(),varGr.get(),connu.get()))
  valider.pack(side="bottom")
  ###Pour l'instant vous ne pouvez pas rajouter de couple, il nous faut aller chercher les valeurs des utilisateurs existants, pour permettre au psy de rentrer le couple

  
def getsexe(var):
  
  print(var.get())


def inscrire(nom,prenom,email,password,passwordmatch,couple,age,hf,connu):
  ###A finir, pour l'instant on ne peut rajouter de couple
  if couple=="":
    couple="NULL"
  if password == passwordmatch:
    mycursor=mydb.cursor()
    sql = "INSERT INTO psychologue.user (id_user, nom, prenom, email, password, couple, age, sexe,connu) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    val = ("NULL",nom , prenom , email ,password,None,age,hf,connu)
    mycursor.execute(sql,val)
    mydb.commit()
  if password != passwordmatch:
    root=Tk()
    center(root)
    root.title("Le mot de passe ne correspond pas")
    label=Label(root,text="Attention le mot de passe ne correspond pas")
    Recommencer = Button(root,text="Ok",command=lambda : root.destroy())
    label.pack()
    Recommencer.pack()

  


  


  



def inputrdv(root):
  
  OPTION = option()
  x=int(OPTION.currentyear)-1
  y=int(OPTION.currentmonth)-1
  z=int(OPTION.currentday)-1


  HstringOption=OPTION.toStringheure(OPTION.OPTIONheure)
  CLIENTS = selectname("id_user","nom","prenom","id_user","user")
  CLIENTS.append(None)
  deco(root)
  root4=Tk()
  center(root4)
  root4.geometry("350x300")
  labelNA=Label(root4,text="VEUILLIEZ ENTREZ LES INFORMATION DU CLIENT")
  
  ###LABELS
  labelClient=Label(root4,text="Clients")
  labelDaterdv=Label(root4,text="Date")
  varclients=StringVar(root4)
  varclients.set(CLIENTS[len(CLIENTS)-1])
  varclients2=StringVar(root4)
  varclients2.set(CLIENTS[len(CLIENTS)-1])
  varclients3=StringVar(root4)
  varclients3.set(CLIENTS[len(CLIENTS)-1])
  variableyear=IntVar(root4)
  variableyear.set(OPTION.OPTIONannée[0])

  variablemonth =IntVar(root4)
  variablemonth.set(OPTION.OPTIONmois[y])

  variableday = IntVar(root4)
  variableday.set(OPTION.OPTIONjour[z])

  variablehour=StringVar(root4)
  variablehournotstring=DoubleVar(root4)
  variablehournotstring.set(OPTION.OPTIONheure[0])
  variablehour.set(HstringOption[0])
  

  Optionpersonne = OptionMenu(root4,varclients,*CLIENTS)
  Optionpersonne2 = OptionMenu(root4,varclients2,*CLIENTS)
  Optionpersonne3 = OptionMenu(root4,varclients3,*CLIENTS)
  
  Optionyear = OptionMenu(root4,variableyear,*OPTION.OPTIONannée)
  Optionmois = OptionMenu(root4,variablemonth,*OPTION.OPTIONmois)
  Optionjour = OptionMenu(root4,variableday,*OPTION.OPTIONjour)
  OptionHeure = OptionMenu(root4,variablehour,*HstringOption)

  labelNA.pack(side=TOP)
  labelClient.pack(side=TOP)
  Optionpersonne.pack(padx=5,pady=5)
  Optionpersonne.config(width=20)
  Optionpersonne2.pack(padx=5,pady=7)
  Optionpersonne2.config(width=20)
  Optionpersonne3.pack(padx=5,pady=6)
  Optionpersonne3.config(width=20)

  labelDaterdv.pack(padx=5,pady=6)
  Optionyear.pack(padx=0,pady=7 ,side=LEFT)
  Optionmois.pack(padx=0, pady=7 ,side=LEFT)
  Optionjour.pack(padx=0,pady=7,side=LEFT)
  OptionHeure.pack(padx=0,pady=7,side=LEFT)

  retour=Button(root4,text="Retour",command=lambda : deuxieme(root4))
  retour.pack(side="bottom")

  Valider= Button(root4,text="Valider/Vérifier", command= lambda : checkvalid(varclients.get(),varclients2.get(),varclients3.get(),variableyear.get(),variableday.get(),variablemonth.get(),variablehour.get()))
  Valider.pack(padx=5,pady=9,side=BOTTOM)

  return root4


 

  
def checkvalid(clientid,clientid2,clientid3,année,jour,mois,heure):

  client=clientid[1]
  if clientid2!="None":
    
    client2=re.sub("[^0-9]","",clientid2)
    
  if clientid3!="None":
    client3=re.sub("[^0-9]","",clientid3)
  heure = heure.split("h")
  heureadd = heure
  if heure[1] != '':
    heureadd=int(heure[0])*100+100
    heure=int(heure[0])*100+int(heure[1])
    
  else :
    heureadd=int(heure[0])*100+30
    heure=int(heure[0])*100
    
  

  today=date.today()
  currentyear = int(today.strftime("%Y"))
  currentmonth=int(today.strftime("%m"))
  currentday=int(today.strftime("%d"))
  currenthour=int(today.strftime("%H"))
  
  currentminutes=int(today.strftime("%M"))/60
  

  x=1
  if année==currentyear:
    if mois<currentmonth:
      print("Mois pas bon")
      x=0
    if jour<currentday and mois<=currentmonth:
      print("le jour n'est pas valide")
      x=0
 
  if  x==1: 
  
    mycursor = mydb.cursor()
    sql = "INSERT INTO consultation (id_consult, date, heuredebut, heurefin, prix, mode, anxiete, commentaires) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"

    val = ("NULL", str(année)+"-"+str(mois)+"-"+str(jour) , heure , heureadd ,100,""," "," ")
    mycursor.execute(sql,val)
    mydb.commit()
    id_consult=sortdv()

    sql2="INSERT INTO consult_patient (id_user, id_consult) VALUES (%s,%s)"
    val2 = (str(client),str(id_consult))
    mycursor.execute(sql2,val2)
    mydb.commit()
    if clientid2 !="None":
      sql3="INSERT INTO consult_patient (id_user, id_consult) VALUES (%s,%s)"
      val3 = (str(client2),str(id_consult))
      mycursor.execute(sql3,val3)
      mydb.commit()
    if clientid3 !="None":
      sql4="INSERT INTO consult_patient (id_user, id_consult) VALUES (%s,%s)"
      val4 = (str(client3),str(id_consult))
      mycursor.execute(sql4,val4)
      mydb.commit()

      

    ##mycursor.execute("INSERT INTO `psychologue`.`consultation` (`id_consult`, `date`, `heuredebut`, `heurefin`, `prix`, `mode`, `anxiete`, `commentaires`) VALUES (NULL," +str(année)+"-"+str(mois)+"-"+str(jour)+" , " + str(heure)+ " , " +str(heureadd)+ " , " +"''"+","+"''" +","+ "' '" +","+"' ' );")
    print("Insert is successful")          
    

  

def infoclients(root2):

  deco(root2)
  root3 = Tk()
  center(root3)
  Id=Label(root3,text="Id")
  Nom=Label(root3, text="Nom")
  PreNom=Label(root3, text="Prenom")
  Mail=Label(root3, text="Mail")




  textId=Text(root3,width=20,height=15)
  textPrenom=Text(root3,width=20,height=15)
  textNom=Text(root3,width=20,height=15)
  textMail=Text(root3,width=20,height=15)
  liste=printable("user")

  Retour=Button(root3,text="Retour",command= lambda: deuxieme(root3))

  
  for x in liste:
    
    textId.insert(END,str(x[0])+'\n')
    textPrenom.insert(END,str(x[1])+'\n')
    textNom.insert(END,str(x[2])+'\n')
    textMail.insert(END,str(x[3])+'\n')
  
  lab1 = Label(root3, text="----------------Vos clients-----------------")
  ##lab2 = Label(root3, text=table)
  
  lab1.grid(column=0, row=0)
  
  
  Id.grid(column=0,row=1)
  textId.grid(column=0, row=2)
  PreNom.grid(column=1,row=1)
  textPrenom.grid(column=1, row=2)
  Nom.grid(column=2, row=1)
  textNom.grid(column=2, row=2)
  Mail.grid(column=3,row=1)
  textMail.grid(column=3, row=2)
  Retour.grid(column=5, row=5)
  ##lab2.grid(column=0, row=1)

  return root3



  
def center(root):
    # Gets the requested values of the height and widht.
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    print("Width",windowWidth,"Height",windowHeight)

    # Gets both half the screen width/height and window width/height
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)

    # Positions the window in the center of the page.
    root.geometry("+{}+{}".format(positionRight, positionDown))

  
  


  
def menu():
  root = premiere()
  
  root.mainloop()

if __name__ == "__main__":
  root = premiere(None)
  
  root.mainloop()
   
  ## menu()



"""selectdb= "use psychologue"""



    





