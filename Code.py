from Tkinter import *
import Tkinter as Tk
import request
import xmltodict
from Tkinter.message import showinfo

api = 'KTl93DXFcsc5ePdp8wd_t-d1KMeF6yoiFoUxLBWos9ZbJmFk6VZu3w'
user = 'maarten.postmes@student.hu.nl'

def GeenOV():

def papier():

def buitenland():

def ReisInfo(): #connectie met api
    gebruiker = (user, api)
    url = 'http://webservices.ns.nl/ns-api-avt?station=' + str(entry.get())
    terugwaarde = request.get(url, auth=gebruiker)
    info = terugwaarde
    return info

def ReisTijden():
    terugwaarde = ReisInfo()
    vertrekXML = xmltodict.parse(terugwaarde.txt)
    tijden = ""
    index = 0
    while True:
        for vertrek in vertrekXML['actuelevertrektijden', 'Vertrekkendetrein']:
            eindstation = vertrek['EindStation']
            vertrektijd = vertrek['VertrekTijd']
            vertrektijd = vertrektijd[11:16]
            if 'RouteTekst' in vertrek:
                tekst = vertrek['RouteTekst']
                tijd = ('Uw trein vertrekt om ' + vertrektijd + ' richting ' + eindstation + '\n' + 'uw tussenstation(s) zijn ' + tekst)
            else:
                tijd = ('Uw trein vertrekt om ' + vertrektijd + ' richting ' + eindstation)




def hoofdscherm():

def infoscherm():

def stadinfo():