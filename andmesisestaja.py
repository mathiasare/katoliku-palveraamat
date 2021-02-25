
import datetime as dt
import json
from tkinter import *
import tkinter
from tkinter import ttk
from tkinter import messagebox
import random
import os



folder="FS" #PATH TO JSON FOLDER
lastDate=None

class DailyData:
    def __init__(self, id,name, year, month, day, saint,liturgicalTime,imgID,psalmID,tags,kohustuslik):
        self.id = id
        self.date = [year,month,day]
        self.tags=tags
        self.liturgicalTime=liturgicalTime
        self.content=[name,imgID,psalmID]
        self.kohustuslik=kohustuslik
    
    def toJSON(self):
        d = {
            'id':self.id,
            'date':self.date,
            'tags':self.tags,
            'liturgicalTime':self.liturgicalTime,
            'content':self.content,
            'kohustuslik':self.kohustuslik
        }
        return json.dumps(d)






def run():
    d=getInputs()
    year=d["date"][2]
    month=d["date"][1]
    path=folder+"\\"+year+"\\"+month+".json"
    if(os.path.exists(path)):
        with open(path,"r") as f:
            sisu=f.read()
        res = addToJson(sisu,d)
        with open(path,"w") as f:
            json.dump(res,f)
    else:
        if(not(os.path.exists(folder+"\\"+year))):
            os.mkdir(folder+"\\"+year)
        
        with open(path,"w") as f:
            initial={'days':[d]}
            json.dump(initial,f)
    global lastDate
    lastDate=d["date"]
    votaTagasi["state"]=ACTIVE

    

def undo():
    if(not(lastDate==None)):
        path=folder+"\\"+lastDate[2]+"\\"+lastDate[1]+".json"
        with open(path) as f:
            d=json.loads(f.read())
        d["days"].pop()
        
        with open(path,"w") as f:
            json.dump(d,f)
        votaTagasi["state"]=DISABLED
        


def resetGUI():
    nimi.delete(0,"end")
    pyhak.delete(0,"end")
    imgID.delete(0,"end")
    psalmID.delete(0,"end")
    paev.delete(0,"end")
    kuu.delete(0,"end")
    sisu.delete("1.0",END)
    v1.set(options1[0])
    v2.set(options2[0])
    v3.set(options3[0])


def getInputs():

    name=nimi.get()
    saint=pyhak.get()
    image=imgID.get()
    psalm=psalmID.get()
    liturgicalTime=v1.get()
    day=paev.get()
    month=kuu.get()
    year=v2.get()
    text=sisu.get("1.0",END)
    mandatory= True if v3.get()=='jah' else False

    resetGUI()

    if(not(None in(name,saint,psalm,liturgicalTime,day,month,year,text))):

        ID=day+month+year
        d = {
                'id':ID,
                'date':(day,month,year),
                'tags':[],
                'liturgicalTime':liturgicalTime,
                'content':{'name':name,'saint':saint,'imageID':image,'psalmID':psalm,'text':text},
                'mandatory':mandatory
            }
    
        return d
    else:
        return None
    

def addToJson(content,newInstance):
    c=json.loads(content)
    c["days"].append(newInstance)
    return c

# GUI
print("KÄIVITAN GUI")
raam = Tk()
raam.title("Katoliku äppi andmesisestaja")
raam.resizable(True, True)
raam.geometry("800x400")

var = IntVar()
var.set(1)

vasak=Frame(raam)
parem=Frame(raam)


group2=Frame(vasak)
silt21 = ttk.Label(group2, text="Nimi")
silt21.grid(row=1,column=1,padx=10)
silt22 = ttk.Label(group2, text="Pildi ID")
silt22.grid(row=1,column=2,padx=10)
silt23 = ttk.Label(group2, text="Psalmi ID")
silt23.grid(row=1,column=3,padx=10)


nimi = ttk.Entry(group2)
nimi.grid(row=2,column=1,padx=10)
imgID = ttk.Entry(group2)
imgID.grid(row=2,column=2,padx=10)
psalmID = ttk.Entry(group2)
psalmID.grid(row=2,column=3,padx=10)
group2.grid(row=2,column=2,pady=35)

group3=Frame(vasak)
silt31 = ttk.Label(group3, text="Liturgiline Aeg")
silt31.grid(row=1,column=1,padx=10)
silt32 = ttk.Label(group3, text="Pühaku nimi")
silt32.grid(row=1,column=2,padx=10)
silt33 = ttk.Label(group3, text="Kas on kohustuslik?")
silt33.grid(row=1,column=3,padx=10)

options1=('VALI AEG','advendiaeg', 'jõuluaeg', 'tavaline aeg', 'paastuaeg', 'ülestõusmisaeg')
v1 = StringVar()
v1.set(options1[0])
la = ttk.OptionMenu(group3,v1,*options1)
la.grid(row=2,column=1,padx=10)


pyhak = ttk.Entry(group3)
pyhak.grid(row=2,column=2,padx=10)


options3=('TEE VALIK','jah','ei')
v3 = StringVar()
v3.set(options1[0])
kohustuslik = ttk.OptionMenu(group3,v3,*options3)
kohustuslik.grid(row=2,column=3,padx=10)

group3.grid(row=3,column=2,pady=35)

group4=Frame(vasak)
silt4 = ttk.Label(group4, text="Päev")
silt4.grid(row=1,column=1,padx=10)
silt5 = ttk.Label(group4, text="Kuu")
silt5.grid(row=1,column=2,padx=10)
silt6 = ttk.Label(group4, text="Aasta")
silt6.grid(row=1,column=3,padx=10)
paev = ttk.Spinbox(group4,from_=1,to=31)
paev.grid(row=2,column=1,padx=10)
kuu = ttk.Spinbox(group4,from_=1,to=12)
kuu.grid(row=2,column=2,padx=10)

options2=('VALI AASTA',"2021","2022","2023")
v2 = StringVar()
v2.set(options2[0])
aasta = ttk.OptionMenu(group4,v2,*options2)
aasta.grid(row=2,column=3,padx=10)
group4.grid(row=4,column=2,padx=10)


group5=Frame(parem)
silt5 = ttk.Label(group5, text="Päeva lugemine")
silt5.pack()
sisu = Text(group5,width=50)
sisu.pack(side=LEFT)
group5.grid(row=1,column=3)

vasak.pack(side=LEFT)
parem.pack(side=RIGHT)



votaTagasi = Button(vasak,text="Võta tagasi", command=undo)
votaTagasi.grid(row=7,column=1,pady=25,padx=10)
votaTagasi["state"]=DISABLED

kinnita = Button(vasak,text="Sisesta", command=run)
kinnita.grid(row=7,column=2,pady=25)

raam.mainloop()
print("VÄLJUN..")
