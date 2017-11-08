from tkinter import *
import tkinter as Tk
import xmltodict

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
    terugwaarde = request.get(url, auth=gebruiker)
    info = terugwaarde
    return info

def ReisTijden():#voor het geven van de reisinformatie
    terugwaarde = ReisInfo()
    vertrekXML = xmltodict.parse(terugwaarde.txt)
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

def hoofdscherm():
    stadinfo.pack_forget()
    infoscherm.pack_forget()
    hoofdscherm.pack(fill='both', expand=True)

def infoscherm():#hier zitten code bij voor het background image
    global informatiescherm
    stadinfo.pack_forget()

    actijden = ReisTijden()
    if actijden == "":
        stadinfo()
    else:
        informatiescherm= Frame(master=root)
        infoscherm.pack()
        BGI3 = Tk.Label(master=informatiescherm, image=BGI2)
        BGI3.place(x=0, y=0, width=784, height=590)
def stadinfo():
    hoofdscherm.pack_forget()
    infoscherm.pack_forget()
    stadinfo.pack(fill='both', expand=True)


root = Tk.Tk()

root.resizable(width=False, height=False)
root.geometry("784x590+300+50")
BGI = Tk.PhotoImage(file='automaat v2.png')
BGI2 = Tk.PhotoImage(file='geel.png')
BGL = Tk.Label(master=root, image=BGI)
BGL.place(x=0, y=0, width=784, height=590)

hoofdscherm =Frame(master=root)
hoofdscherm.pack(expand=True)
