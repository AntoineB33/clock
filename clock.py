from datetime import datetime
from datetime import timedelta
import threading
from pynput.keyboard import Key, Listener
import keyboard
from tkinter import *
from time import sleep as s
import pyttsx3
import atexit,osfrom win10toast import ToastNotifier
n = ToastNotifier()
engine = pyttsx3.init()
clock = Tk()
clock.title("Clock")
clock.geometry("800x300")
pf='C:/Users/comma/Desktop/fichier_clock/'
comb=[]
class AsyncZip4(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global key,exo,comb,shift
        k=str(key)
        if k not in comb:
            comb.append(k)
        if"'w'"in comb and"'x'"in comb and"'c'"in comb:
            fecran()
        print(comb)
        if"'w'"in comb and"'x'"in comb and"'f'"in comb and"'v'"in comb:
            print(allum.cget('text'))
            if allum.cget('text')!="écran allumé ?":
                fecran()
            os.system('shutdown -s')
def on_press(k):
    global key,background4
    key=k
    try:
        background4.join()
    except:
        1
    background4 = AsyncZip4()
    background4.start()
def on_release(k):
    global comb,background4
    try:
        background4.join()
    except:
        1
    comb=[]
class AsyncZip(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        with Listener(on_press=on_press,on_release=on_release) as listener:
            listener.join()
background = AsyncZip()
background.start()
def fecran():
    global allum,yeux,quart,mat,now
    if allum.cget('text')=="écran allumé ?":
        now = datetime.now()
        with open(pf+'clock.txt','r')as f:
            c=f.read().splitlines()
            if c:
                save=datetime.strptime(c[0],"%Y:%b:%d:%H:%M:%S:%f")
                diffe=datetime.strptime(c[3],"%Y:%b:%d:%H:%M:%S:%f")-save
                print('mat',mat,diffe,diffe.seconds,diffe.microseconds)
                mat=now+timedelta(seconds=diffe.seconds,microseconds=diffe.microseconds)
                print(mat)
            else:
                mat=now+timedelta(hours=2)
            if c:
                print(c==[], save,now-timedelta(seconds=20))
            if c==[]or save<=now-timedelta(seconds=20):
                yeux=now+timedelta(minutes=20)
                if c==[]or save<=now-timedelta(minutes=15):
                    quart=now+timedelta(hours=2)
                else:
                    quart=datetime.strptime(c[2],"%Y:%b:%d:%H:%M:%S:%f")
                    if now+timedelta(minutes=20)<quart and now+timedelta(minutes=20,seconds=20)>quart:
                        yeux=now+timedelta(days=1)
            else:
                yeux=datetime.strptime(c[1],"%Y:%b:%d:%H:%M:%S:%f")
                quart=datetime.strptime(c[2],"%Y:%b:%d:%H:%M:%S:%f")
        with open(pf+'clock.txt','w')as f:
            f.write('')
        allum.config(text="éteindre l'écran ?")
        allum.config(bg='green')
        print(yeux)
        print(quart)
        print(mat,'\n')
    else:
        with open(pf+'clock.txt','w')as f:
            print('rrrrr',now.strftime("%Y:%b:%d:%H:%M:%S:%f"))
            f.write(now.strftime("%Y:%b:%d:%H:%M:%S:%f")+'\n'+yeux.strftime("%Y:%b:%d:%H:%M:%S:%f")
                    +'\n'+quart.strftime("%Y:%b:%d:%H:%M:%S:%f")+'\n'+mat.strftime("%Y:%b:%d:%H:%M:%S:%f"))
        allum.config(text="écran allumé ?")
        allum.config(bg='red')
allum = Button(clock,text = "écran allumé ?",fg="white",width = 15,command = fecran)
allum.place(x =120,y=30)
def fsuiv():
    global mat,quart,liste,po,li
    now=datetime.now()
    d=mat-now
    if mat>quart+timedelta(seconds=15):
        d-=timedelta(minutes=15)
    po+=1
    if po<len(li):
        mat0=now+li[po]
        li[po-1]=d
    else:
        mat0=now+timedelta(hours=2)
        li.append(d)
    if mat0>quart:
        mat0+=timedelta(minutes=15)
    mat=mat0
    d=d.seconds
    bef=liste.cget("text")
    if bef:
        bef+='    '
    if d//3600:
        bef+=f'{d//3600}h '
        d=d%3600
    if d//60:
        bef+=f'{d//60}min '
        d=d%60
    liste.config(text=bef+f'{d}s')
suiv = Button(clock,text = "suivant",fg='white',bg='black',width = 15,command = fsuiv)
suiv.place(x =240,y=30)
ug=1
fecran()
def fprec():
    global li,liste,po,quart,mat
    if po:
        now=datetime.now()
        po-=1
        print(liste.cget("text").rsplit('s',2)[0]+'s')
        texte=liste.cget("text")
        if texte.count('s')>1:
            texte=liste.cget("text").rsplit('s',2)[0]+'s'
        else:
            texte=''
        liste.config(text=texte)
        mat0=now+li[po]
        if mat0>quart:
            mat0+=timedelta(minutes=15)
        mat=mat0
prec = Button(clock,text = "précédant",fg='white',bg='black',width = 15,command = fprec)
prec.place(x =360,y=30)
liste = Label(clock,fg='blue')
liste.place(x =0,y=0)
def arrf(sv):
    global arrh
    t=sv.get()
    sp=t.split(':')
    print(sp)
    if len(sp)==3 and min([len(x)==2 for x in sp]):
        print('!!!',sp)
        now=datetime.now()
        arrh=datetime.strptime(f'{now.year}:{now.month}:{now.day}:'+t,"%Y:%m:%d:%H:%M:%S")
sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: arrf(sv))
arr = Entry(clock,fg='blue',textvariable=sv)
arr.place(x =150,y=100)
arrt = Label(clock,text='arrêter à : ')
arrt.place(x =0,y=100)
li=[]
po=0
arrh=0
class AsyncZip(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global yeux,quart,mat,arrh,allum,now,n
        try:
            quart
        except NameError:
            print('erreur!!')
            input()
            quit()
        now=datetime.now()
        co=1
        inter=0
        while 1:
            if allum.cget('text')=="éteindre l'écran ?"or inter:
                if not inter:
                    if yeux<now:
                        n.show_toast("Ferme les yeux","pendant 20 secondes")
                        engine.say("ferme les yeux")
                        engine.runAndWait()
                        fecran()
                        s(20)
                        engine.say("rouvre les yeux")
                        engine.runAndWait()
                        fecran()
                        mat+=timedelta(seconds=20)
                        co=0
                    if quart<now:
                        re=now+timedelta(minutes=15)
                        n.show_toast(f"mets en veille jusqu'à {re.hour} heures et {re.minute+bool(re.second!=0)} minutes")
                        engine.say(f"mets en veille jusqu'à {re.hour} heures et {re.minute+bool(re.second!=0)} minutes")
                        engine.runAndWait()
                        quart+=timedelta(days=1)
                    if mat<now:
                        n.show_toast("change de matière")
                        engine.say("change de matière")
                        engine.runAndWait()
                        mat=now+timedelta(hours=2)
                        print(mat)
                    if arrh and arrh<now:
                        n.show_toast("arrêt demandé")
                        engine.say("arrêt demandé")
                        engine.runAndWait()
                        arr.delete(0,"end")
                        arrh=datetime.strptime(now.strftime("%Y:%b:%d"),"%Y:%b:%d")+timedelta(days=1)
                now0 = datetime.now()
                di=(datetime.now()-now).seconds
                if co and di>15 or di>25:
                    mat+=timedelta(seconds=di)
                    if di>20:
                        print(di)
                        inter=1
                        fecran()
                elif inter and allum.cget('text')=="écran allumé ?":
                    print('inter')
                    fecran()
                    inter=0
                co=1
                now=now0
            s(10)
now1=datetime.now()
nowl=[datetime.strptime((now1+timedelta(days=x)).strftime("%Y:%m:%d"),"%Y:%m:%d")for x in range(4)]
with open(pf+'clock_autre.txt')as f:
    c=f.read().splitlines()
with open(pf+'clock_autre.txt','w')as f:
    da=[datetime.strptime(x,"%Y:%m:%d")for x in c]
    ta=[['changer de serviette',3],['changer de pantalon',4],
        ['changer de veste',3],['se laver les cheveux',4],['changer de pyjama',7],['changer de tapis de bain',7]]
    txt=['']*len(ta)
    for i in range(len(ta)):
        while nowl[0]>da[i]:
            da[i]+=timedelta(days=ta[i][1])
            c=c[:i]+[da[i].strftime("%Y:%m:%d")]+c[i+1:]
    for i in range(len(ta)):
        for j in range(len(nowl)):
            if nowl[j]==da[i]:
                aj='- '+ta[i][0]
            else:
                aj='-'
            txt[i]+=aj.ljust(40)
    f.write('\n'.join(c))
    print('\n'.join(txt))
lab = Label(clock,text='\n'.join(txt))
lab.place(x =0,y=150)
background = AsyncZip()
background.start()
clock.mainloop()
