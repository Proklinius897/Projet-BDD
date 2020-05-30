import mysql.connector
from tkinter import *


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
  button1 =Button(root2, text="Organiser un rdv")
  button2 =Button(root2, text="Informations Clients", command = lambda: infoclients(root2))
  button3=Button(root2, text="Déconnexion", command = lambda : deco(root2))
  lab1.grid(column=0, row=0)
  lab2.grid(column=0,row=1)
  button1.grid(column=0,row=2)
  button2.grid(column=0,row=3)
  button3.grid(column=0,row=4)
  return root2

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
  liste=printable("patient")

  Retour=Button(root3,text="Retour",command= lambda: deuxieme(root3))

  
  for x in liste:
    
    textId.insert(END,str(x[0])+'\n')
    textPrenom.insert(END,str(x[2])+'\n')
    textNom.insert(END,str(x[3])+'\n')
    textMail.insert(END,str(x[4])+'\n')
  
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



    





