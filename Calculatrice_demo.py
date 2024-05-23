#importer mes bibliotheques 1
import tkinter
from tkinter import *


#ma fenetre 2
root = Tk()
root.title("Calculatrice demo")
root.geometry("360x550+300+100")
root.resizable(False,False)
root.configure(bg = "#17161b")


#Mes fonctios
 
#Actualiser
actualiser  = ""


#afficher 8
def afficher(value):
    global actualiser
    actualiser+=value
    lblresultat.config(text = actualiser)
#Effacer 7
def effacer():
    global actualiser
    actualiser = ""
    lblresultat.config(text=actualiser)


# calculer 9
def calculer():
    global actualiser
    resultat = ""
    if actualiser !="":
        try:
            resultat = eval(actualiser)
        except:
            resultat="Erreur"
            actualiser=""
    lblresultat.config(text=resultat)


#Resultat de mes calcules 4
lblresultat = Label(root, width = 25, height = 2, text = "", font=("arial", 30),fg="#fff", bg="#17161b")
lblresultat.pack()


#Mes boutons 5
Button(root, text="AC", width = 3, height = 1, font = ("arial", 26, "bold"), bd=0, fg="#fff",
       bg="#9F9F9F", command=lambda: effacer()).place(x=10, y=100)
Button(root, text="+/-", width = 3, height = 1, font = ("arial", 26, "bold"), bd=0, fg="#fff",
       bg="#9F9F9F", command=lambda :afficher("-")).place(x=100, y=100)
Button(root, text="%", width = 3, height = 1, font = ("arial", 26, "bold"), bd=0, fg="#fff",
       bg="#9F9F9F", command=lambda :afficher("%")).place(x=190, y=100)
Button(root, text="÷", width = 3, height = 1, font = ("arial", 26, "bold"), bd=0, fg="#fff",
       bg="#FF9400", command=lambda :afficher("/")).place(x=280, y=100)

Button(root, text="7", width = 3, height = 1, font = ("arial", 26, "bold"), bd=0, fg="#fff",
       bg="#9F9F9F", command=lambda :afficher("7")).place(x=10, y=190)
Button(root, text="8", width = 3, height = 1, font = ("arial", 26, "bold"), bd=0, fg="#fff",
       bg="#9F9F9F", command=lambda :afficher("8")).place(x=100, y=190)
Button(root, text="9", width = 3, height = 1, font = ("arial", 26, "bold"), bd=0, fg="#fff",
       bg="#9F9F9F", command=lambda :afficher("9")).place(x=190, y=190)
Button(root, text="X", width = 3, height = 1, font = ("arial", 26, "bold"), bd=0, fg="#fff",
       bg="#FF9400", command=lambda :afficher("*")).place(x=280, y=190)

Button(root, text="4", width = 3, height = 1, font = ("arial", 26, "bold"), bd=0, fg="#fff",
       bg="#9F9F9F", command=lambda :afficher("4")).place(x=10, y=280)
Button(root, text="5", width = 3, height = 1, font = ("arial", 26, "bold"), bd=0, fg="#fff",
       bg="#9F9F9F", command=lambda :afficher("5")).place(x=100, y=280)
Button(root, text="6", width = 3, height = 1, font = ("arial", 26, "bold"), bd=0, fg="#fff",
       bg="#9F9F9F", command=lambda :afficher("6")).place(x=190, y=280)
Button(root, text="-", width = 3, height = 1, font = ("arial", 26, "bold"), bd=0, fg="#fff",
       bg="#FF9400", command=lambda :afficher("-")).place(x=280, y=280)

Button(root, text="1", width = 3, height = 1, font = ("arial", 26, "bold"), bd=0, fg="#fff",
       bg="#9F9F9F", command=lambda :afficher("1")).place(x=10, y=370)
Button(root, text="2", width = 3, height = 1, font = ("arial", 26, "bold"), bd=0, fg="#fff",
       bg="#9F9F9F", command=lambda :afficher("2")).place(x=100, y=370)
Button(root, text="3", width = 3, height = 1, font = ("arial", 26, "bold"), bd=0, fg="#fff",
       bg="#9F9F9F", command=lambda :afficher("3")).place(x=190, y=370)
Button(root, text="+", width = 3, height = 1, font = ("arial", 26, "bold"), bd=0, fg="#fff",
       bg="#FF9400", command=lambda :afficher("+")).place(x=280, y=370)

Button(root, text="0", width = 7, height = 1, font = ("arial", 26, "bold"), bd=0, fg="#fff",
       bg="#9F9F9F", command=lambda :afficher("0")).place(x=10, y=460)
Button(root, text=",", width = 3, height = 1, font = ("arial", 26, "bold"), bd=0, fg="#fff",
       bg="#9F9F9F", command=lambda :afficher(".")).place(x=190, y=460)
Button(root, text="=", width = 3, height = 1, font = ("arial", 26, "bold"), bd=0, fg="#fff",
       bg="#FF9400", command=lambda :calculer()).place(x=280, y=460)

#Run 3
root.mainloop()