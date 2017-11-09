from tkinter import *
import tkinter as Tk
import requests
import xmltodict
from tkinter.messagebox import showinfo

api = 'KTl93DXFcsc5ePdp8wd_t-d1KMeF6yoiFoUxLBWos9ZbJmFk6VZu3w'
user = 'maarten.postmes@student.hu.nl'

def GeenOV():
    bericht = 'u kunt worden doorgevoerd naar een website om uw eigen ov te bestellen!'
    showinfo(title='sorry!', message=bericht)

def papier():
    bericht = 'U kunt kaartjes kopen bij een van de automaten op uw station' #placeholder verander naar ingevoerdstation
    showinfo(title='sorry!', message=bericht)

def buitenland():
    bericht = 'Wij geven geen buitenlands reisadvies, wij verbinden u door naar de ns international website'
    showinfo(title='sorry!', message=bericht)

def ReisInfo(): #connectie met api
    gebruiker = (user, api)
    url = 'http://webservices.ns.nl/ns-api-avt?station=' + str(entry.get())
    terugwaarde = requests.get(url, auth=gebruiker)
    info = terugwaarde
    return info

def ReisTijden():#voor het geven van de reisinformatie
    terugwaarde = ReisInfo()
    vertrekXML = xmltodict.parse(terugwaarde)
    tijden = ""
    index = 0
    try:
        for vertrek in vertrekXML['actuelevertrektijden', 'Vertrekkendetrein']:
            eindstation = vertrek['EindStation']
            vertrektijd = vertrek['VertrekTijd']
            vertrektijd = vertrektijd[11:16]
            if 'RouteTekst' in vertrek:
                tekst = vertrek['RouteTekst']
                tijd = ('Uw trein vertrekt om ' + vertrektijd + ' richting ' + eindstation + '\n' + 'uw tussenstation(s) zijn ' + tekst)
            else:
                tijd = ('Uw trein vertrekt om ' + vertrektijd + ' richting ' + eindstation)
            tijden = tijden + '\n' + '\n' + tijd
            index = index + 1
            if index < 10:
                print(index)
            else:
                break
    except:
        showinfo(title='error', message='geen geldig stationsnaam ingevoerd!')
        tijden= ""
    return tijden

def toonhoofdscherm():
    infoscherm.pack_forget()
    hoofdscherm.pack(fill='both', expand=True)


def tooninfoscherm():#hier zitten code bij voor het background image
    global informatiescherm

    actijden = ReisTijden()
    if actijden != "":
        informatiescherm= Frame(master=root)
        infoscherm.pack()
        BGI3 = Tk.Label(master=informatiescherm, image=BGI2)
        BGI3.place(x=0, y=0, width=784, height=590)
        label2 = Label(master=informatiescherm, text='vertrektijden van treinen uit station ' + str(entry.get()), foreground='blue', background='gold', font=('Calibri', 16, 'bold'))
        label2.pack(pady=5)
        terugknop2 = Button(master=informatiescherm, text='terug', background='gold', font=('calibri', 16, 'bold'))
        terugknop2.pack(pady=5)
        label3 = Label(master=informatiescherm, background='gold', foreground='blue', font=('calibri', 9, 'bold'), text=actijden)
        label3.pack(pady=(0,15))

        infoscherm.pack(fill='both', expand=True)
        ReisInfo()

root = Tk.Tk()

root.resizable(width=False, height=False)
root.geometry("784x590")
BGI = Tk.PhotoImage(file='automaat v2.png')
BGI2 = Tk.PhotoImage(file='automaat v2.png')
BGL = Tk.Label(master=root, image=BGI)
BGL.place(x=0, y=0, width=784, height=590)

hoofdscherm = Frame(master=root)
hoofdscherm.pack(expand=True)

button1 = Button(master=root, text='Ik heb geen OV-chipkaart',font=('Franklin Gothic Medium', 10, 'bold'), background='blue', foreground='white', command=GeenOV)
button1.place(x=275, y=455, width=217, height=80)

button2 = Button(master=root, text='Ik wil naar het buitenland',font=('Franklin Gothic Medium', 10, 'bold'), background='blue', foreground='white', command=buitenland)
button2.place(x=510, y=455, width=217, height=80)

button3 = Button(master=root, text='Papieren kaartjes',font=('Franklin Gothic Medium', 10, 'bold'), background='blue', foreground='white', command=papier)
button3.place(x=40, y=455, width=217, height=80)

button4 = Button(master=root, text='Actuele reisinformatie',font=('Franklin Gothic Medium', 10, 'bold'), background='blue', foreground='white', command=toonhoofdscherm)
button4.place(x=455, y=8, width=273, height=80)

label = Label(master=root, text='voer stations naam in', foreground='blue', background='gold', font=('Calibri', 16, 'bold'))
label.place(x=500, y=500)

entry = Entry(master=root)
entry.pack(pady=5)

button5 = Button(master=root, text='check actuele reistijden', background='blue', foreground='white', command=tooninfoscherm)
button5.pack(pady=5)

terugknop = Button(master=root, text='Terug', background='blue', foreground='white', command=toonhoofdscherm)
terugknop.pack(pady=5)

infoscherm = Frame(master=root)

toonhoofdscherm()
root.mainloop()






