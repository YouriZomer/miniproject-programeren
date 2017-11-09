from tkinter import *
from PIL import Image, ImageTk
from tkinter.messagebox import showinfo
import xmltodict
import requests
from requests.auth import HTTPBasicAuth

root = Tk()

root.geometry("784x590")
root.resizable(width=False, height=False)
bgImg = PhotoImage(file="automaat v2.png")

achtergrond = Label(root, image=bgImg)
achtergrond.pack()

url="https://webservices.ns.nl/ns-api-stations-v2"
auth_details=HTTPBasicAuth ("maarten.postmes@student.hu.nl", "KTl93DXFcsc5ePdp8wd_t-d1KMeF6yoiFoUxLBWos9ZbJmFk6VZu3w")
response = requests.post(url, auth=auth_details)

print(response)
print(response.content)

xmldict=xmltodict.parse(response.content)
print(xmldict)


stationcodes=[]
for station in xmldict['Stations']['Station']:
    print("{:10}{:50}\t{}".format(station['Code'], station['Namen']['Lang'],station['Type']))
    stationcodes.append(station['Code'])


class Window(Frame):

        def __init__(self, master = None):
            Frame.__init__(self, master)

            self.master = master

            self.init_window()

        def init_window(self):
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
                auth_details = ('maarten.postmes@student.hu.nl', "KTl93DXFcsc5ePdp8wd_t-d1KMeF6yoiFoUxLBWos9ZbJmFk6VZu3w")
                api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + str(entry.get())
                response = requests.get(api_url, auth=auth_details)
                info = response
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
                informatiescherm.pack_forget()
                toonhoofdscherm.pack(fill='both', expand=True)

            def tooninfoscherm():#hier zitten code bij voor het background image
                global informatiescherm

                actijden = ReisTijden()
                if actijden == "":
                    toonhoofdscherm()
                else:
                    informatiescherm= Frame(master=root)
                    informatiescherm.pack()
                    # BGI3 = Tk.Label(master=informatiescherm, image=BGI2)
                    # BGI3.place(x=0, y=0, width=784, height=590)
                    label2 = Label(master=informatiescherm, text='vertrektijden van treinen uit station ' + str(entry.get()), foreground='blue', background='gold', font=('Calibri', 16, 'bold'))
                    label2.pack(pady=5)
                    terugknop2 = Button(master=informatiescherm, text='terug', background='gold', font=('calibri', 16, 'bold'))
                    terugknop2.pack(pady=5)
                    label3 = Label(master=informatiescherm, background='gold', foreground='blue', font=('calibri', 9, 'bold'), text=actijden)
                    label3.pack(pady=(0,15))

                    informatiescherm.pack(fill='both', expand=True)
                    ReisInfo()


            self.master.title("Ns Reisplanner")

            self.pack(fill=BOTH, expand=1)

            entry = Entry(master=root)
            entry.pack(pady=5)

            button1 = Button(master=root, text='Ik heb geen OV-chipkaart',font=('Franklin Gothic Medium', 10, 'bold'), background='blue', foreground='white', command=GeenOV)
            button1.place(x=275, y=455, width=217, height=80)

            button2 = Button(master=root, text='Ik wil naar het buitenland',font=('Franklin Gothic Medium', 10, 'bold'), background='blue', foreground='white', command=buitenland)
            button2.place(x=510, y=455, width=217, height=80)

            button3 = Button(master=root, text='Papieren kaartjes',font=('Franklin Gothic Medium', 10, 'bold'), background='blue', foreground='white', command=papier)
            button3.place(x=40, y=455, width=217, height=80)

            button4 = Button(master=root, text='Ander station',font=('Franklin Gothic Medium', 20, 'bold'), background='blue', foreground='white', command=toonhoofdscherm)
            button4.place(x=455, y=8, width=273, height=80)



            mEntry = Entry()
            mEntry.pack()



            # self.usertext = StringVar()
            # self.myentry = Entry(self.master, textvariable = self.usertext)
            # # self.myentry.grid(row=1,column=0)
            #
            # self.usertext.get()

        def client_exit(self):
            exit()

        def showImg(self):
            load = Image.open("automaat v2.png")
            render = ImageTk.PhotoImage(load)

            img = Label(self, image = render)
            img.image = render
            img.place(x=0, y=0)


app = Window(root)

root.mainloop()
