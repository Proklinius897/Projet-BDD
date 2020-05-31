import mysql.connector
from tkinter import *
from datetime import *

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




def premiere ():
  root = Tk()
  center(root)
  root.title("Connexion page")
  lab1 = Label(root,text="Bienvenue, veuilliez vous connecter")
  lab2 = Label(root,text="Identifiant : ")
  lab3=Label(root,text="Mot de passe")
  entryname= Entry(root)
  entrypass= Entry(root)

  lab1.grid(column=0, row=0)
  lab2.grid(column=0, row=1)
  entryname.grid(column=1, row=1)
  lab3.grid(column=0, row=2)
  entrypass.grid(column=1, row=2)
  button = Button(root,text='Submit',command = lambda : connection(entryname,entrypass,root))
  button.grid(column=0,row=5)
  return root

def deco (root):
  root.destroy()

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
  button3=Button(root2, text="Déconnexion", command = lambda : deco(root2))
  lab1.grid(column=0, row=0)
  lab2.grid(column=0,row=1)
  button1.grid(column=0,row=2)
  calendrier.grid(column=0,row=3)
  button2.grid(column=0,row=4)
  button3.grid(column=0,row=5)
  return root2

class option(): 
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
  def toStringheure(self, OPTIONheure):
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
  
    
  

  

  
def selectname(name,name2,group,table):
  mycursor = mydb.cursor()
  mycursor.execute("SELECT "+name+", "+name2 + " FROM " + table +" GROUP BY "+ group )
  myresult = mycursor.fetchall()
  lenght=len(myresult)
  
  for x in myresult:
    print(x)
    
    
  return myresult

      



def inputrdv(root):
  
  OPTION = option()
  
  
  x=int(OPTION.currentyear)-1
  y=int(OPTION.currentmonth)-1
  z=int(OPTION.currentday)-1
  

  HstringOption=OPTION.toStringheure(OPTION.OPTIONheure)
  CLIENTS = selectname("nom","prenom","id_user","user")
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

  Valider= Button(root4,text="Valider/Vérifier", command= lambda : checkvalid(varclients.get(),variableyear.get(),variableday.get(),variablemonth.get(),variablehour.get()))
  Valider.pack(padx=5,pady=9,side=BOTTOM)
  return root4


 

  
def checkvalid(client,année,jour,mois,heure):
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
  
  print(heure)
  print(today.strftime("%H"))
  x=1
  if année==currentyear:
    if mois<currentmonth:
      print("Mois pas bon")
      x=0
    if jour<currentday and mois<currentmonth:
      print("le jour n'est pas valide")
      x=0
 
  if  x==1: 
  
    mycursor = mydb.cursor()
    sql = "INSERT INTO consultation (id_consult, date, heuredebut, heurefin, prix, mode, anxiete, commentaires) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"

    val = ("NULL", str(année)+"-"+str(mois)+"-"+str(jour) , heure , heureadd ,100,""," "," ")
    mycursor.execute(sql,val)
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




  textId=Text(root3,width=20)
  textPrenom=Text(root3,width=20)
  textNom=Text(root3,width=20)
  textMail=Text(root3,width=20)
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

  """
  print("Connectez-vous")
  identifiant = input("\n Indentifiant : ")
  mdp = input("\n Mot de passe : ")
  connection(identifiant,mdp)
  
  if mydb != None:
    print("connection établie")

  print("------------------------------Bienvenu sur Psynote------------------------------ \t")
  print("Que voulez-vous faire ?")
  print("1.Prendre un rdv")
  print("2.Voir les rendez-vous")
  print("3.Informations Clients") 
  print("4.Déconnexion")
  
  
  while 1:
    choix = input("\n Choix : ")
    if choix =='1':
      fenetre("Hello man")  
      
    if choix == '3':
      while 1:
        
        print("1.Montrer client")
        print("2.Montrer adresse")
        print("3.Quittez")
        choix2 =input("\n Choix 2 : ")
        if choix2 =='1':
          printable("patient")
        if choix2 == '2':

          printable("adresse")
        if choix2 == '3':
          break

        



    if choix == '4':
      print("Au revoir")
      break
    """

if __name__ == "__main__":
   
   menu()



"""selectdb= "use psychologue"""



    





