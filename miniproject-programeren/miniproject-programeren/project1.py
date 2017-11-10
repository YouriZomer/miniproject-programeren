from tkinter import *
from PIL import Image, ImageTk
from tkinter.messagebox import showinfo
import xmltodict
import requests
from requests.auth import HTTPBasicAuth
#wij hebben voor de hand gekeken wat wij moesten importeren alles word dus gebruikt
root = Tk()

root.geometry("784x590")
root.resizable(width=False, height=False)
bgImg = PhotoImage(file="automaat v2.png")

achtergrond = Label(root, image=bgImg)
achtergrond.pack()

url="https://webservices.ns.nl/ns-api-stations-v2"
auth_details=HTTPBasicAuth ("maarten.postmes@student.hu.nl", "KTl93DXFcsc5ePdp8wd_t-d1KMeF6yoiFoUxLBWos9ZbJmFk6VZu3w")
response = requests.post(url, auth=auth_details)

print(response.content)
print(response)

xmldict=xmltodict.parse(response.content)
print(xmldict)


stationcodes=[]
for station in xmldict['Stations']['Station']:
    print("{:10}{:50}\t{}".format(station['Code'], station['Namen']['Lang'],station['Type']))
    stationcodes.append(station['Code'])


class Window(Frame):

        def __init__(self, master = None): # zorgt ervoor dat het programma in de loop
            Frame.__init__(self, master)

            self.master = master

            self.init_window()

        def init_window(self):
            def GeenOV():
                bericht = 'Wij verkopen hier geen ov u kunt op onze website een ov aanvragen.'
                showinfo(title='sorry!', message=bericht)


            def papier():
                bericht = 'U kunt kaartjes kopen bij een van de automaten op uw station' #placeholder verander naar ingevoerdstation
                showinfo(title='sorry!', message=bericht)

            def buitenland():
                bericht = 'U kunt aan het helpdesk of op onze website buitenlands reisadvies zoeken.'
                showinfo(title='sorry!', message=bericht)

            def ReisInfo(): #connectie met api
                auth_details = ('maarten.postmes@student.hu.nl', "KTl93DXFcsc5ePdp8wd_t-d1KMeF6yoiFoUxLBWos9ZbJmFk6VZu3w")
                api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + str(entry.get())
                response = requests.get(api_url, auth=auth_details)
                info = response
                return info

            def ReisTijden():
                response = ReisInfo()
                vertrekXML = xmltodict.parse(response.text)
                tijden = ''
                index = 0

                try:#Hier word de informatie uit de dict gehaald via xml en in zinnen op scherm gezet
                    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
                        eindbestemming = vertrek['EindBestemming']
                        vertrektijd = vertrek['VertrekTijd']
                        vertrektijd = vertrektijd[11:16]
                        if 'RouteTekst' in vertrek:
                            routetekst = vertrek['RouteTekst']
                            tijd = ('Om ' + vertrektijd + ' vertrekt een trein naar ' + eindbestemming + 'met tussenstation(s) ' + routetekst)
                            label2 = Label(master=root,text='vertrektijden van treinen uit station ' + str(entry.get()), foreground='blue', background='gold', font=('Calibri', 16, 'bold'))
                            label2.place(x=107, y=166)
                            label3 = Label(master=root, font=('calibri', 9, 'bold'), justify=LEFT, text=tijden, height=25, width=114, borderwidth=0)
                            label3.place(x=48, y=206)
                            tijden = tijden + '\n' + '\n' + tijd
                            index = index + 1
                        if index < 15:
                            print(index)
                        else:
                            break
                except:
                    showinfo(title='error', message='geen geldig stationsnaam ingevoerd!')
                    tijden = ""


            def starter():#Hiermee roepen wij de functie voor het reis informatie op.
                ReisInfo()
                ReisTijden()


            self.master.title("Ns Reisplanner")

            self.pack(fill=BOTH, expand=1)
            invoerstring = StringVar
            #De knoppen hieronder zijn voor verschillende processen en roepen dus alle verschillende functies aan

            button1 = Button(master=root, text='Geen OV',font=('Franklin Gothic Medium', 8, 'bold'), background='blue', foreground='white', command=GeenOV)
            button1.place(x=426, y=33, width=150, height=60)

            button2 = Button(master=root, text='Reizen in buitenland',font=('Franklin Gothic Medium', 8, 'bold'), background='blue', foreground='white', command=buitenland)
            button2.place(x=586, y=33, width=150, height=60)

            button3 = Button(master=root, text='Papieren kaartjes',font=('Franklin Gothic Medium', 8, 'bold'), background='blue', foreground='white', command=papier)
            button3.place(x=586, y=99, width=150, height=60)

            def callback(event):
                starter()
            entry = Entry(master=root)# entry stuk voor het invoeren van een station
            entry.bind("<Return>", callback)
            entry.place(x=176, y=126)
            entry.focus_set()

            button4 = Button(master=root, textvariable = invoerstring, text='confirm',font=('Franklin Gothic Medium', 8, 'bold'), background='blue', foreground='white', command=starter)
            button4.place(x=426, y=99, width=150, height=60)


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
