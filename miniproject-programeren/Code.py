from tkinter import *
import tkinter as Tk
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
    terugwaarde = url, auth=gebruiker
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
    stadinfo.pack_forget()
    infoscherm.pack_forget()
    hoofdscherm.pack(fill='both', expand=True)

def tooninfoscherm():#hier zitten code bij voor het background image
    global informatiescherm
    stadinfo.pack_forget()

    actijden = ReisTijden()
    if actijden == "":
        toonstadinfo()
    else:
        informatiescherm= Frame(master=root)
        infoscherm.pack()
        BGI3 = Tk.Label(master=informatiescherm, image=BGI2)
        BGI3.place(x=0, y=0, width=784, height=590)
        label2 = Label(master=informatiescherm, text='vertrektijden van treinen uit station ' + str(entry.get()), foreground='blue', background='gold', font=('Calibri', 16, 'bold'))
        label2.pack(pady=5)
        terugknop2 = Button(master=informatiescherm, text='terug', background='gold', font=('calibri', 16, 'bold'))
        terugknop2.pack(pady=5)
        label3 = Label(master=informatiescherm, background='gold', foreground='blue', font=('calibri', 9, 'bold'), text=actueletijden)
        label3.pack(pady=(0,15))

        infoscherm.pack(fill='both', expand=True)
        ReisInfo()

def toonstadinfo():
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

hoofdscherm = Frame(master=root)
hoofdscherm.pack(expand=True)

button1 = Button(master=root, text='Ik heb geen OV-chipkaart', background='blue', foreground='white', command=GeenOV)
button1.place(x=300, y=500)

button2 = Button(master=root, text='Ik wil naar het buitenland', background='blue', foreground='white', command=buitenland)
button2.place(x=523, y=500)

button3 = Button(master=root, text='Papieren kaartjes', background='blue', foreground='white', command=papier)
button3.place(x=100, y=500)

button4 = Button(master=root, text='Actuele reisinformatie', background='blue', foreground='white', command=toonstadinfo)
button4.place(x=523, y=50)

stadinfo = Frame(master=root)
stadinfo.pack()
hoofdscherm.pack_forget()

BGI2=Tk.PhotoImage(file='automaat v2.png')
BGL2=Tk.Label(master=stadinfo, image=BGI2)
BGL2.place(x=0, y=0, width=784, height=590)

label = Label(master=stadinfo, text='voer stations naam in', foreground='blue', background='gold', font=('Calibri', 16, 'bold'))
label.pack(pady=5)

entry = Entry(master=stadinfo)
entry.pack(pady=5)

button5 = Button(master=stadinfo, text='check actuele reistijden', background='blue', foreground='white', command=tooninfoscherm)
button5.pack(pady=5)

terugknop = Button(master=stadinfo, text='Terug', background='blue', foreground='white', command=toonhoofdscherm)
terugknop.pack(pady=5)

infoscherm = Frame(master=root)

toonhoofdscherm()
root.mainloop()






