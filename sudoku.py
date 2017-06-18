import winsound
import time
import random
import os
pausa=[0]
lista_total=[['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','','']]
lista_total_borrar=[['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','',''],['','','','','','','','','']]
nombrejugador=["H"]
partidaactual=[[["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"]],[["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"]],[["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"]],[["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"]],[["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"]],[["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"]],[["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"]],[["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"]],[["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"],["","white"]]]
partidaactualcopia=partidaactual.copy()
pila=[]
estado=[0]#ya se inicio o no el juego
finalizado=[0]#ya se termino el juego=1
color_boton={0:"#8DA641",1:"#F6F7F2"}
import pickle
from tkinter import *
color_boton={0:"#8DA641",1:"#F6F7F2"}#botones de colores seleccionados y no seleccionados, el 0 es el de botones seleccionados
tiempo_reloj={0:["0","30","00"],1:["1","00","00"],2:["2","00","00"]}#tiempo en el reloj, 0 facil, etc
nivel_ahora={0:0}#nivel en el que se esta, se modifica con el cambio de nivel, modifica a reloj y a
reloj_activado={0:"y"}#informacion de si el reloj esta activado, y, n, t=timer
pos_panel={0:1,1:-1}#informacion de donde esta localizado el panel, el 1 es del frame del sudoku
xy_pos_panel={"izquierda":[[10,10],[200,10]],"derecha":[[500,10],[10,10]]}#primero panel y luego sudoku, para cada una/arreglado
color_panel={0:"#8DA641",1:"#E55516"}
cosa={}
imagen_panel={0:1}
imagen_panel_real={1:[["1",color_boton[1]],["2",color_boton[1]],["3",color_boton[1]],["4",color_boton[1]],["5",color_boton[1]],["6",color_boton[1]],["7",color_boton[1]],["8",color_boton[1]],["9",color_boton[1]]],2:[["A",color_boton[1]],["B",color_boton[1]],["C",color_boton[1]],["D",color_boton[1]],["E",color_boton[1]],["F",color_boton[1]],["G",color_boton[1]],["H",color_boton[1]],["I",color_boton[1]]],3:[["♫",color_boton[1]],["╚",color_boton[1]],["§",color_boton[1]],["☻",color_boton[1]],["↕",color_boton[1]],["■",color_boton[1]],["▲",color_boton[1]],["Ä",color_boton[1]],["⌂",color_boton[1]]],4:[["","red"],["","red"],["","blue"],["","yellow"],["","green"],["","orange"],["","purple"],["","pink"],["","black"],["","grey"]]}
imagen_botones_numeros={"":["","white"],"1":["1",color_boton[0]],"2":["2",color_boton[0]],"3":["3",color_boton[0]],"4":["4",color_boton[0]],"5":["5",color_boton[0]],"6":["6",color_boton[0]],"7":["7",color_boton[0]],"8":["8",color_boton[0]],"9":["9",color_boton[0]]}#copia de panel con numeros
imagen_botones_letras={"":["","white"],"1":["A",color_boton[0]],"2":["B",color_boton[0]],"3":["C",color_boton[0]],"4":["D",color_boton[0]],"5":["E",color_boton[0]],"6":["F",color_boton[0]],"7":["G",color_boton[0]],"8":["H",color_boton[0]],"9":["I",color_boton[0]]}#copia del panel con letras
imagen_botones_especiales={"":["","white"],"1":["♫",color_boton[0]],"2":["╚",color_boton[0]],"3":["§",color_boton[0]],"4":["☻",color_boton[0]],"5":["↕",color_boton[0]],"6":["■",color_boton[0]],"7":["▲",color_boton[0]],"8":["Ä",color_boton[0]],"9":["⌂",color_boton[0]]}#copia del panel con especiales
imagen_botones_colores={"":["","white"],"1":["","red"],"2":["","blue"],"3":["","yellow"],"4":["","green"],"5":["","orange"],"6":["","purple"],"7":["","pink"],"8":["","black"],"9":["","grey"]}#copia del panel con colores
imagen_botones={"":["","white"],"1":["1",color_boton[0]],"2":["2",color_boton[0]],"3":["3",color_boton[0]],"4":["4",color_boton[0]],"5":["5",color_boton[0]],"6":["6",color_boton[0]],"7":["7",color_boton[0]],"8":["8",color_boton[0]],"9":["9",color_boton[0]]}#texto y color de los botones del panel
infoahora={0:["1",color_boton[1]]}
def leerpartidasudoku():
    f= open('sudoku2016partidas.dat', 'rb') 
    b = pickle.load(f)
    f.close()
    
    diccionario=list(b)
    
    return diccionario
def leerposiciones():
    f= open('sudoku2016top10.dat', 'rb') 
    b = pickle.load(f)
    f.close()
    diccionario=dict(b)
    
    
    return diccionario
def escribirposiciones(nivel,nombre,tiempo,):
    abcd=leerposiciones()
    
    tiempo2=tiempo
    aj=leerconfigsudoku()
    if aj["tiempo"]=="timer":
        w=int(aj["horas"])*3600+int(aj["minutos"])*60+int(aj["segundos"])
        tiempo2=w-tiempo2
    segundos=(tiempo%60)
    tiempo=tiempo//60
    minutos=tiempo%60
    horas=tiempo//60
    if len(str(horas))==1:
        horas="0"+str(horas)
    if len(str(minutos))==1:
        minutos="0"+str(minutos)
    if len(str(segundos))==1:
        segundos="0"+str(segundos)
    tiempo=str(horas)+":"+str(minutos)+":"+str(segundos)
    lista=abcd[nivel]
    if len(lista)==0:
        lista.append([nombre,tiempo,tiempo2])
    else:
        pruebas=[]
        for i in range(len(lista)):
            pruebas.append(lista[i][2])
        check=0
        for i in range(len(pruebas)):
            if tiempo2>pruebas[i]:
                pass
            else:
                lista.insert(i,[nombre,tiempo,tiempo2])
                break
        else:
            lista.insert(len(pruebas),[nombre,tiempo,tiempo2])
        print(lista)
    print(lista)        
    abcd[nivel]=lista
    if len(lista)>10:
        lista.pop(10)
    f= open('sudoku2016top10.dat', 'wb')
    pickle.dump(abcd, f)
    f.close()
    
        
def print_posiciones():
    abcd=leerposiciones()
    a=""
    for i in abcd:
        j=1
        a=a+"\n"
        a=a+"**Nivel "+i+"**\n\n"
        a=a+"Posicion"+(" "*10)+"Nombre                           "+"Tiempo\n"
        for w in abcd[i]:
            
            a=a+str(j)+(" "*22)+w[0]+(" "*(34-len(w[0])))+(" "*6)+str(w[1])+"\n"
            j+=1
    pausa[0]=0
    y=messagebox.showinfo(title="Posiciones",parent=jugar,message=a)
    if y=="ok":
        pausa[0]=1
        reloj()
        
def guardaractual():
    if estado[0]==0:
        messagebox.showinfo(title="Aviso",parent=jugar,message="Juego no ha iniciado")
    else:
    
        actual=leeractual()
        reloj_horas=leerconfigsudoku()["horas"]
        reloj_minutos=leerconfigsudoku()["minutos"]
        reloj_segundos=leerconfigsudoku()["segundos"]
        reloj_cosa=leerconfigsudoku()["tiempo"]
        imagen=leerconfigsudoku()["imagen"]
        nombre=nombre_jugador.get()
        guardar2enelactual("nombre",nombre)
        guardar2enelactual("partida",actual)
        guardar2enelactual("horas",reloj_horas)
        guardar2enelactual("minutos",reloj_minutos)
        guardar2enelactual("segundos",reloj_segundos)
        guardar2enelactual("tiempo",reloj_cosa)
        guardar2enelactual("imagen",imagen)
def abriractual():
    f= open('sudoku2016juegoactual.dat', 'rb') 
    b = pickle.load(f)
    f.close()
    diccionario=dict(b)
    
    return diccionario
def guardar2enelactual(car,cosa):
    a=abriractual()
    f= open('sudoku2016juegoactual.dat', 'wb')
    a[car]=cosa
    pickle.dump(a, f)
    
def leeractual():
    f= open('sudoku2016actual.dat', 'rb') 
    b = pickle.load(f)
    f.close()
    diccionario=list(b)
    return diccionario
def escribiractual(x,y,cosa):
    a=leeractual()
    f= open('sudoku2016actual.dat', 'wb')
    a[x][y]=cosa
    pickle.dump(a, f)
def borraractual():
    wxyz=[["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""]]
    f= open('sudoku2016actual.dat', 'wb') 
    b = pickle.dump(wxyz,f)
    f.close()

def leerconfigsudoku():
    f= open('sudoku2016configuracion.dat', 'rb') 
    b = pickle.load(f)
    f.close()
    diccionario=dict(b)
    return diccionario
def escribirconfigsudoku(cosa,car):
    a=leerconfigsudoku()
    f= open('sudoku2016configuracion.dat', 'wb')
    a[cosa]=car
    pickle.dump(a, f)
    
    
#funciones botones en principal

#ventana principal
principal=Tk()
principal.title("Sudoku")
principal.resizable(0,0)
principal.geometry("600x600+0+0")
principal.config(bg="white")
color="#F6F7F2"
def Jugar():#muestra el frame de calculadora y esconde el resto
    jugar.pack()
    acercade.pack_forget()
    ayuda.pack_forget()
    configurar.pack_forget()
    modificar.pack_forget()
    
def Acercade():#muestra el frame de acerca de y esconde el resto
    jugar.pack_forget()
    ayuda.pack_forget()
    acercade.pack()
    configurar.pack_forget()
    modificar.pack_forget()
def Ayuda():#abre el lector depdf y muestra el manual de usuario
    os.startfile("manual_de_usuario_sudoku.mp4")
def Salir():
    principal.quit()# se sale del mainloop

def Configurar():
    jugar.pack_forget()
    acercade.pack_forget()
    ayuda.pack_forget()
    configurar.pack()
    modificar.pack_forget()
def Modificar():
    jugar.pack_forget()
    acercade.pack_forget()
    ayuda.pack_forget()
    configurar.pack_forget()
    modificar.pack()
    imagenes_del_panelc()
    jugar_pos_panelc()


jugar=Label(principal,width=262, height=464, bg=color)
jugar.pack()
configurar=Label(principal,width=262, height=464, bg=color)
acercade=Label(principal,width=262, height=464, bg=color, text="Sudoku\nVersion 1.0\nCreada por Juan F.Villacis")
ayuda=Label(principal,width=262,height=464,bg=color)
modificar=Label(principal,width=262, height=464, bg=color)
barramenu=Menu(principal)
mnuMenu=Menu(barramenu)
barramenu.add_command(label="Jugar",command=Jugar)
barramenu.add_command(label="Acerca de",command=Acercade)
barramenu.add_command(label="Ayuda",command=Ayuda)
barramenu.add_command(label="Configurar", command=Configurar)
barramenu.add_command(label="Modificar", command=Modificar)
barramenu.add_command(label="Salir",command=principal.destroy)#destruye principal
principal.config(menu=barramenu)#se pone para agregarlo a principalS

def actualiza_botones(imagen_botones):
    btn1.config(text=imagen_botones[1][0],bg=imagen_botones[1][1])
    btn2.config(text=imagen_botones[2][0],bg=imagen_botones[2][1])
    btn3.config(text=imagen_botones[3][0],bg=imagen_botones[3][1])
    btn4.config(text=imagen_botones[4][0],bg=imagen_botones[4][1])
    btn5.config(text=imagen_botones[5][0],bg=imagen_botones[5][1])
    btn6.config(text=imagen_botones[6][0],bg=imagen_botones[6][1])
    btn7.config(text=imagen_botones[7][0],bg=imagen_botones[7][1])
    btn8.config(text=imagen_botones[8][0],bg=imagen_botones[8][1])
    btn9.config(text=imagen_botones[9][0],bg=imagen_botones[9][1])
    

        

    



def boton_config_nivel(nivel,cosa): #funciones dentro de configurar
    if cosa=="nivel":#cambia el color del label del nivel, se guardael nivel
        escribirconfigsudoku(cosa,nivel)
        confignivel()
    if cosa=="tiempo":#cambia el color del label del reloj, se guardael reloj, tambien tienen la caja de texto con la info del reloj
        escribirconfigsudoku(cosa,nivel)
        configreloj()
    if cosa=="pos":#cambia el color del label de la posicion, se guarda la posicion
        escribirconfigsudoku(cosa,nivel)
        configpos()
        jugar_pos_panel()
        
        
    if cosa=="panel":#cambia el color del label del objeto del panel, se guarda el que se selecciono
        if nivel=="numeros":
            escribirconfigsudoku(cosa,nivel)
            
        elif nivel=="letras":
            escribirconfigsudoku(cosa,nivel)
            
        elif nivel=="raros":
            escribirconfigsudoku(cosa,nivel)
            
            
        elif nivel=="colores":
            escribirconfigsudoku(cosa,nivel)
            
        configimagenpanel()
        imagenes_del_panel()
       
        
            
    
    
            
        


#botones en configurar

label_info_config=Label(configurar,text="Configurar",bg="#F6F7F2", bd=0,font=("Calibri",14))
label_info_config.place(x=20,y=5)

    #nivel
label_config_nivel=Label(configurar,text="Nivel:",bg="#F6F7F2", bd=0,font=("Calibri",12))
label_config_nivel.place(x=20,y=45)
boton_config_facil=Button(configurar,text="Facil",bd=0,font=("Calibri",12),height=0,width=5,command=lambda:boton_config_nivel("facil","nivel"))
boton_config_facil.place(x=60,y=75)
boton_config_medio=Button(configurar,text="Medio",bd=0,font=("Calibri",12),height=0,width=5,command=lambda:boton_config_nivel("medio","nivel"))
boton_config_medio.place(x=60,y=105)
boton_config_dificil=Button(configurar,text="Dificil",bd=0,font=("Calibri",12),height=0,width=5,command=lambda:boton_config_nivel("dificil","nivel"))
boton_config_dificil.place(x=60,y=135)

    #reloj
label_config_reloj=Label(configurar,text="Reloj:",bg="#F6F7F2", bd=0,font=("Calibri",12))
label_config_reloj.place(x=160,y=45)
boton_config_on=Button(configurar,text="Si",bd=0,font=("Calibri",12),height=0,width=5,command=lambda:boton_config_nivel("si","tiempo"))
boton_config_on.place(x=200,y=75)
boton_config_off=Button(configurar,text="No",bd=0,font=("Calibri",12),height=0,width=5,command=lambda:boton_config_nivel("no","tiempo"))
boton_config_off.place(x=200,y=105)
boton_config_timer=Button(configurar,text="Timer",bd=0,font=("Calibri",12),command=lambda:boton_config_nivel("timer","tiempo"))
boton_config_timer.place(x=200,y=145)
label_config_timer=Label(configurar,text="Horas | Minutos | Segundos",height=1,width=20,bd=3,bg=color_boton[1])
label_config_timer.place(x=310,y=75)

entry_config_horas=Entry(configurar, bd=0,bg=color_boton[1],font=("Calibri",12),width=2)
entry_config_horas.insert(0,tiempo_reloj[nivel_ahora[0]][0])
entry_config_horas.place(x=315,y=100)
entry_config_minutos=Entry(configurar, bd=0,bg=color_boton[1],font=("Calibri",12),width=2)
entry_config_minutos.insert(0,tiempo_reloj[nivel_ahora[0]][1])
entry_config_minutos.place(x=362,y=100)
entry_config_segundos=Entry(configurar, bd=0,bg=color_boton[1],font=("Calibri",12),width=2)
entry_config_segundos.insert(0,tiempo_reloj[nivel_ahora[0]][2])
entry_config_segundos.place(x=420,y=100)
def configreloj():
    dicc=leerconfigsudoku()
    if dicc["tiempo"]=="si":
        bg1=color_boton[0]
        bg2=color_boton[1]
        bg3=color_boton[1]
        
    elif dicc["tiempo"]=="no":
        bg1=color_boton[1]
        bg2=color_boton[0]
        bg3=color_boton[1]
    elif dicc["tiempo"]=="timer":
        bg1=color_boton[1]
        bg2=color_boton[1]
        bg3=color_boton[0]
    boton_config_on.config(bg=bg1)
    boton_config_off.config(bg=bg2)
    boton_config_timer.config(bg=bg3)
configreloj()
def confignivel():
    dicc=leerconfigsudoku()
    entry_config_horas.delete(0,END)
    entry_config_minutos.delete(0,END)
    entry_config_segundos.delete(0,END)
    if dicc["nivel"]=="facil":
        bg1=color_boton[0]
        bg2=color_boton[1]
        bg3=color_boton[1]
        escribirconfigsudoku("minutos","30")
        escribirconfigsudoku("horas","00")
        escribirconfigsudoku("segundos","00")
        
    elif dicc["nivel"]=="medio":
        bg1=color_boton[1]
        bg2=color_boton[0]
        bg3=color_boton[1]
        escribirconfigsudoku("minutos","00")
        escribirconfigsudoku("horas","01")
        escribirconfigsudoku("segundos","00")
    elif dicc["nivel"]=="dificil":
        bg1=color_boton[1]
        bg2=color_boton[1]
        bg3=color_boton[0]
        escribirconfigsudoku("minutos","00")
        escribirconfigsudoku("horas","02")
        escribirconfigsudoku("segundos","00")
    dicc=leerconfigsudoku()
    boton_config_facil.config(bg=bg1,)
    boton_config_medio.config(bg=bg2)
    boton_config_dificil.config(bg=bg3)
    entry_config_horas.insert(0,dicc["horas"])
    entry_config_minutos.insert(0,dicc["minutos"])
    entry_config_segundos.insert(0,dicc["segundos"])
confignivel()
    #posicion del panel
label_config_pospanel=Label(configurar,text="Posicion del panel de elementos:", bg="#F6F7F2", bd=0,font=("Calibri",12))
label_config_pospanel.place(x=20,y=200)
boton_config_izq=Button(configurar,text="izquierda", bd=0,font=("Calibri",12),height=0,width=7,command=lambda:boton_config_nivel("izquierda","pos")) 
boton_config_der=Button(configurar,text="derecha", bd=0,font=("Calibri",12),height=0,width=7,command=lambda:boton_config_nivel("derecha","pos"))
def configpos():
    dicc=leerconfigsudoku()
    if dicc["pos"]=="derecha":
        bg1=color_boton[1]
        bg2=color_boton[0]
        
    elif dicc["pos"]=="izquierda":
        bg1=color_boton[0]
        bg2=color_boton[1]
    boton_config_izq.config(bg=bg1)
    boton_config_der.config(bg=bg2)
configpos()
boton_config_der.place(x=200, y=230)
boton_config_izq.place(x=200, y=270)
    #panel
label_config_panel=Label(configurar,text="Panel de elementos:", bg="#F6F7F2", bd=0,font=("Calibri",12))
label_config_panel.place(x=20,y=310)
boton_numeros_panel=Button(configurar,width=2,bd=0,font=("Calibri",12),text="1\n2\n3\n4\n5\n6\n7\n8\n9",command=lambda:boton_config_nivel("numeros","panel"))
boton_numeros_panel.place(x=220,y=350)
boton_letras_panel=Button(configurar,width=2, bd=0,font=("Calibri",12),text="A\n B\nC\nD\nE\nF\nG\nH\nI",command=lambda:boton_config_nivel("letras","panel"))
boton_letras_panel.place(x=270,y=350)
boton_raros_panel=Button(configurar,width=2, bd=0,font=("Calibri",12),text="♫\n ╚\n§\n☻\n↕\n■\n▲\nÄ\n⌂",command=lambda:boton_config_nivel("raros","panel"))
boton_raros_panel.place(x=320,y=350)
photo1 = PhotoImage(file="imagen1.gif")
boton_colores_panel=Button(configurar,width=50,height=200,bd=0,image=photo1,command=lambda:boton_config_nivel("colores","panel"))
boton_colores_panel.place(x=370,y=340)
def configimagenpanel():
    dicc=leerconfigsudoku()
    if dicc["panel"]=="numeros":
        bg1=color_boton[0]
        bg2=color_boton[1]
        bg3=color_boton[1]
        escribirconfigsudoku("imagen",imagen_botones_numeros)
        
    elif dicc["panel"]=="letras":
        bg1=color_boton[1]
        bg2=color_boton[0]
        bg3=color_boton[1]
        escribirconfigsudoku("imagen",imagen_botones_letras)
    elif dicc["panel"]=="raros":
        bg1=color_boton[1]
        bg2=color_boton[1]
        bg3=color_boton[0]
        escribirconfigsudoku("imagen",imagen_botones_especiales)
    else: #dicc["panel"]=="colores":
        bg1=color_boton[1]
        bg2=color_boton[1]
        bg3=color_boton[1]
        escribirconfigsudoku("imagen",imagen_botones_colores)
        

        
    boton_numeros_panel.config(bg=bg1)
    boton_letras_panel.config(bg=bg2)
    boton_raros_panel.config(bg=bg3)
configimagenpanel()


#botones en jugar
frame_sudoku=Frame(jugar,bg="black",padx=1,pady=1,width=500,height=500)#bg=color_boton[1]
frame_botones=Frame(jugar,bg="#F6F7F2",width=20,height=400)
def jugar_pos_panel():
    dicc=leerconfigsudoku()
    frame_botones.place(x=xy_pos_panel[dicc["pos"]][0][0],y=xy_pos_panel[dicc["pos"]][0][1])
    frame_sudoku.place(x=xy_pos_panel[dicc["pos"]][1][0],y=xy_pos_panel[dicc["pos"]][1][1])
jugar_pos_panel()
btn1=Button(frame_botones,bd=0,width=2,height=2,state="disabled",command=lambda:boton_seleccionado(1))#este tiene que poner ademas la flecha a la par)
btn1.grid(row=0,column=1)
btn2=Button(frame_botones,bd=0,width=2,height=2,state="disabled",command=lambda:boton_seleccionado(2))
btn2.grid(row=1,column=1)
btn3=Button(frame_botones,bd=0,width=2,height=2,state="disabled",command=lambda:boton_seleccionado(3))
btn3.grid(row=2,column=1)
btn4=Button(frame_botones,bd=0,width=2,height=2,state="disabled",command=lambda:boton_seleccionado(4))
btn4.grid(row=3,column=1)
btn5=Button(frame_botones,bd=0,width=2,height=2,state="disabled",command=lambda:boton_seleccionado(5))
btn5.grid(row=4,column=1)
btn6=Button(frame_botones,bd=0,width=2,height=2,state="disabled",command=lambda:boton_seleccionado(6))
btn6.grid(row=5,column=1)
btn7=Button(frame_botones,bd=0,width=2,height=2,state="disabled",command=lambda:boton_seleccionado(7))
btn7.grid(row=6,column=1)
btn8=Button(frame_botones,bd=0,width=2,height=2,state="disabled",command=lambda:boton_seleccionado(8))
btn8.grid(row=7,column=1)
btn9=Button(frame_botones,bd=0,width=2,height=2,state="disabled",command=lambda:boton_seleccionado(9))
btn9.grid(row=8,column=1)
labelflecha=Label(frame_botones,bd=0,width=2,state="disabled",height=2,text="←",bg="#F6F7F2")


def imagenes_del_panel():
    dicc=leerconfigsudoku()
    
    btn1.config(text=dicc["imagen"]["1"][0],bg=dicc["imagen"]["1"][1])
    btn2.config(text=dicc["imagen"]["2"][0],bg=dicc["imagen"]["2"][1])
    btn3.config(text=dicc["imagen"]["3"][0],bg=dicc["imagen"]["3"][1])
    btn4.config(text=dicc["imagen"]["4"][0],bg=dicc["imagen"]["4"][1])
    btn5.config(text=dicc["imagen"]["5"][0],bg=dicc["imagen"]["5"][1])
    btn6.config(text=dicc["imagen"]["6"][0],bg=dicc["imagen"]["6"][1])
    btn7.config(text=dicc["imagen"]["7"][0],bg=dicc["imagen"]["7"][1])
    btn8.config(text=dicc["imagen"]["8"][0],bg=dicc["imagen"]["8"][1])
    btn9.config(text=dicc["imagen"]["9"][0],bg=dicc["imagen"]["9"][1])
    

imagenes_del_panel()
#estas frames crean los bordes gruesos
frame11=Frame(frame_sudoku,bg="black",width=12, height=6,bd=3)
frame11.grid(row=0,column=0)
frame12=Frame(frame_sudoku,bg="black",width=12, height=6,bd=3)
frame12.grid(row=0,column=1)
frame13=Frame(frame_sudoku,bg="black",width=12, height=6,bd=3)
frame13.grid(row=0,column=2)
frame21=Frame(frame_sudoku,bg="black",width=12, height=6,bd=3)
frame21.grid(row=1,column=0)
frame22=Frame(frame_sudoku,bg="black",width=12, height=6,bd=3)
frame22.grid(row=1,column=1)
frame23=Frame(frame_sudoku,bg="black",width=12, height=6,bd=3)
frame23.grid(row=1,column=2)
frame31=Frame(frame_sudoku,bg="black",width=12, height=6,bd=3)
frame31.grid(row=2,column=0)
frame32=Frame(frame_sudoku,bg="black",width=12, height=6,bd=3)
frame32.grid(row=2,column=1)
frame33=Frame(frame_sudoku,bg="black",width=12, height=6,bd=3)
frame33.grid(row=2,column=2)
#fila0
btn00=Button(frame11,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(0,0))
btn00.grid(row=0,column=0)
btn01=Button(frame11,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(0,1))
btn01.grid(row=0,column=1)
btn02=Button(frame11,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(0,2))
btn02.grid(row=0,column=2)
btn03=Button(frame12,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(0,3))
btn03.grid(row=0,column=3)
btn04=Button(frame12,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(0,4))
btn04.grid(row=0,column=4)
btn05=Button(frame12,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(0,5))
btn05.grid(row=0,column=5)
btn06=Button(frame13,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(0,6))
btn06.grid(row=0,column=6)
btn07=Button(frame13,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(0,7))
btn07.grid(row=0,column=7)
btn08=Button(frame13,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(0,8))
btn08.grid(row=0,column=8)
#fila1
btn10=Button(frame11,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(1,0))
btn10.grid(row=1,column=0)
btn11=Button(frame11,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(1,1))
btn11.grid(row=1,column=1)
btn12=Button(frame11,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(1,2))
btn12.grid(row=1,column=2)
btn13=Button(frame12,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(1,3))
btn13.grid(row=1,column=3)
btn14=Button(frame12,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(1,4))
btn14.grid(row=1,column=4)
btn15=Button(frame12,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(1,5))
btn15.grid(row=1,column=5)
btn16=Button(frame13,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(1,6))
btn16.grid(row=1,column=6)
btn17=Button(frame13,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(1,7))
btn17.grid(row=1,column=7)
btn18=Button(frame13,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(1,8))
btn18.grid(row=1,column=8)
#fila2
btn20=Button(frame11,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(2,0))
btn20.grid(row=2,column=0)
btn21=Button(frame11,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(2,1))
btn21.grid(row=2,column=1)
btn22=Button(frame11,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(2,2))
btn22.grid(row=2,column=2)
btn23=Button(frame12,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(2,3))
btn23.grid(row=2,column=3)
btn24=Button(frame12,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(2,4))
btn24.grid(row=2,column=4)
btn25=Button(frame12,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(2,5))
btn25.grid(row=2,column=5)
btn26=Button(frame13,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(2,6))
btn26.grid(row=2,column=6)
btn27=Button(frame13,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(2,7))
btn27.grid(row=2,column=7)
btn28=Button(frame13,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(2,8))
btn28.grid(row=2,column=8)
#fila3
btn30=Button(frame21,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(3,0))
btn30.grid(row=0,column=0)
btn31=Button(frame21,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(3,1))
btn31.grid(row=0,column=1)
btn32=Button(frame21,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(3,2))
btn32.grid(row=0,column=2)
btn33=Button(frame22,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(3,3))
btn33.grid(row=0,column=3)
btn34=Button(frame22,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(3,4))
btn34.grid(row=0,column=4)
btn35=Button(frame22,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(3,5))
btn35.grid(row=0,column=5)
btn36=Button(frame23,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(3,6))
btn36.grid(row=0,column=6)
btn37=Button(frame23,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(3,7))
btn37.grid(row=0,column=7)
btn38=Button(frame23,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(3,8))
btn38.grid(row=0,column=8)
#fila4
btn40=Button(frame21,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(4,0))
btn40.grid(row=1,column=0)
btn41=Button(frame21,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(4,1))
btn41.grid(row=1,column=1)
btn42=Button(frame21,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(4,2))
btn42.grid(row=1,column=2)
btn43=Button(frame22,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(4,3))
btn43.grid(row=1,column=3)
btn44=Button(frame22,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(4,4))
btn44.grid(row=1,column=4)
btn45=Button(frame22,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(4,5))
btn45.grid(row=1,column=5)
btn46=Button(frame23,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(4,6))
btn46.grid(row=1,column=6)
btn47=Button(frame23,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(4,7))
btn47.grid(row=1,column=7)
btn48=Button(frame23,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(4,8))
btn48.grid(row=1,column=8)
#fila5
btn50=Button(frame21,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(5,0))
btn50.grid(row=2,column=0)
btn51=Button(frame21,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(5,1))
btn51.grid(row=2,column=1)
btn52=Button(frame21,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(5,2))
btn52.grid(row=2,column=2)
btn53=Button(frame22,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(5,3))
btn53.grid(row=2,column=3)
btn54=Button(frame22,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(5,4))
btn54.grid(row=2,column=4)
btn55=Button(frame22,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(5,5))
btn55.grid(row=2,column=5)
btn56=Button(frame23,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(5,6))
btn56.grid(row=2,column=6)
btn57=Button(frame23,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(5,7))
btn57.grid(row=2,column=7)
btn58=Button(frame23,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(5,8))
btn58.grid(row=2,column=8)
#fila6
btn60=Button(frame31,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(6,0))
btn60.grid(row=0,column=0)
btn61=Button(frame31,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(6,1))
btn61.grid(row=0,column=1)
btn62=Button(frame31,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(6,2))
btn62.grid(row=0,column=2)
btn63=Button(frame32,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(6,3))
btn63.grid(row=0,column=3)
btn64=Button(frame32,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(6,4))
btn64.grid(row=0,column=4)
btn65=Button(frame32,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(6,5))
btn65.grid(row=0,column=5)
btn66=Button(frame33,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(6,6))
btn66.grid(row=0,column=6)
btn67=Button(frame33,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(6,7))
btn67.grid(row=0,column=7)
btn68=Button(frame33,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(6,8))
btn68.grid(row=0,column=8)
#fia7
btn70=Button(frame31,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(7,0))
btn70.grid(row=1,column=0)
btn71=Button(frame31,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(7,1))
btn71.grid(row=1,column=1)
btn72=Button(frame31,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(7,2))
btn72.grid(row=1,column=2)
btn73=Button(frame32,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(7,3))
btn73.grid(row=1,column=3)
btn74=Button(frame32,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(7,4))
btn74.grid(row=1,column=4)
btn75=Button(frame32,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(7,5))
btn75.grid(row=1,column=5)
btn76=Button(frame33,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(7,6))
btn76.grid(row=1,column=6)
btn77=Button(frame33,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(7,7))
btn77.grid(row=1,column=7)
btn78=Button(frame33,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(7,8))
btn78.grid(row=1,column=8)
#fila8
btn80=Button(frame31,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(8,0))
btn80.grid(row=2,column=0)
btn81=Button(frame31,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(8,1))
btn81.grid(row=2,column=1)
btn82=Button(frame31,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(8,2))
btn82.grid(row=2,column=2)
btn83=Button(frame32,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(8,3))
btn83.grid(row=2,column=3)
btn84=Button(frame32,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(8,4))
btn84.grid(row=2,column=4)
btn85=Button(frame32,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(8,5))
btn85.grid(row=2,column=5)
btn86=Button(frame33,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(8,6))
btn86.grid(row=2,column=6)
btn87=Button(frame33,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(8,7))
btn87.grid(row=2,column=7)
btn88=Button(frame33,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribir(8,8))
btn88.grid(row=2,column=8)
btniniciarjuego=Button(jugar,text="Inciar juego",width=10,height=2,bg=color_boton[0],bd=0,command=lambda:iniciarjuego())
btniniciarjuego.place(x=40,y=450)
btnborrarjugada=Button(jugar,text="Borrar jugada",width=10,height=2,bg=color_boton[0],bd=0,command=lambda:borrarjugada())
btnborrarjugada.place(x=140,y=450)
btnterminarjuego=Button(jugar,text="Terminar juego",width=12,height=2,bg=color_boton[0],bd=0,command=lambda:terminarjuego())
btnterminarjuego.place(x=240,y=450)
btnborrarjuego=Button(jugar,text="Borrar juego",width=10,height=2,bg=color_boton[0],bd=0,command=lambda:borrarjuego(pila))
btnborrarjuego.place(x=350,y=450)
btntop10=Button(jugar,text="Top 10",width=10,height=2,bg=color_boton[0],bd=0,command=lambda:print_posiciones())
btntop10.place(x=450,y=450)
label_nombre_jugador=Label(jugar,width=20,text="Nombre del jugador:",height=1,bg=color_boton[1],bd=0)
label_nombre_jugador.place(x=40,y=400)
nombre_jugador=Entry(jugar,bg="white",font=("Calibri",10),width=30,bd=0)
nombre_jugador.place(x=170,y=400)
label_horas=Label(jugar,bg=color_boton[1],text="Horas",bd=0,height=1,width=8)
label_horas.place(x=40,y=520)
label_minutos=Label(jugar,bg=color_boton[1],text="Minutos",bd=0,height=1,width=8)
label_minutos.place(x=100,y=520)
label_segundos=Label(jugar,bg=color_boton[1],text="Segundos",bd=0,height=1,width=8)
label_segundos.place(x=160,y=520)
label_horas_cont=Label(jugar,bg=color_boton[1],bd=0,height=1,width=8)
label_horas_cont.place(x=40,y=540)
label_minutos_cont=Label(jugar,bg=color_boton[1],bd=0,height=1,width=8)#los cont tienen el contador
label_minutos_cont.place(x=100,y=540)
label_segundos_cont=Label(jugar,bg=color_boton[1],bd=0,height=1,width=8)
label_segundos_cont.place(x=160,y=540)
label_anuncio=Label(width=40, height=5,bg="red")
btn_guardar=Button(jugar,text="Guardar juego",width=10,height=2,bg=color_boton[0],bd=0,command=lambda:guardaractual())
btn_guardar.place(x=350,y=520)
btn_cargar=Button(jugar,text="Cargar juego",width=10,height=2,bg=color_boton[0],bd=0,command=lambda:cargar_partida())
btn_cargar.place(x=450,y=520)
label_config_nivel=Label(jugar,text="Nivel: ",height=1,width=8,bd=3,bg=color_boton[1])
label_config_nivel.place(x=1,y=575)
label_config_mostrarnivel=Label(jugar,text="",height=1,width=5,bd=3,bg=color_boton[1],state="disabled")
label_config_mostrarnivel.place(x=60,y=575)
def boton_seleccionado(num):
    escribirconfigsudoku("boton",str(num))
    #labelflecha.grid(row=num-1,column=2)
    
    
    
    
def checar(x,y,numero):
    print(x,y)
    if btn4.cget("state")=="disabled":
        return (False,"juego no ha iniciado")
    if numero=="":
        return (False,"no se ha seleccionado ficha")
    if lista_total[x][y]!='' and lista_total_borrar[x][y]!=lista_total[x][y]:
        flash_button(x,y)
        return (False, "casilla fija")
    for i in range(9):
        
        if numero in lista_total[i][y]:
            
            flash_button(i,y)
            return (False,"misma columna")
            
        elif numero in lista_total[x][i]:
            flash_button(x,i)
            return (False,"misma fila")
    if x<=2:
        
        if y<=2:
            for i in range(3):
                for j in range(3):
                    if numero in lista_total[i][j]:
                        flash_button(i,j)
                        return (False,"mismo cuadrante")
        elif y<=5:
            for i in range(3):
                for j in range(3,6):
                    if numero in lista_total[i][j]:
                        flash_button(i,j)
                        return (False,"mismo cuadrante")
        elif y<=8:
            for i in range(3):
                for j in range(6,9):
                    if numero in lista_total[i][j]:
                        flash_button(i,j)
                        return (False,"mismo cuadrante")
    elif x<=5:
        
        if y<=2:
            for i in range(3,6):
                for j in range(3):
                    if numero in lista_total[i][j]:
                        flash_button(i,j)
                        return (False,"mismo cuadrante")
        elif y<=5:
            for i in range(3,6):
                for j in range(3,6):
                    if numero in lista_total[i][j]:
                        flash_button(i,j)
                        return (False,"mismo cuadrante")
        elif y<=8:
            for i in range(3,6):
                for j in range(6,9):
                    if numero in lista_total[i][j]:
                        flash_button(i,j)
                        return (False,"mismo cuadrante")
    elif x<=8:
        
        if y<=2:
            for i in range(6,9):
                for j in range(3):
                    if numero in lista_total[i][j]:
                        flash_button(i,j)
                        return (False,"mismo cuadrante")
        elif y<=5:
            for i in range(6,9):
                for j in range(3,6):
                    if numero in lista_total[i][j]:
                        flash_button(i,j)
                        return (False,"mismo cuadrante")
        elif y<=8:
            for i in range(6,9):
                for j in range(6,9):
                    
                    if numero in lista_total[i][j]:
                        flash_button(i,j)
                        return (False,"mismo cuadrante")
    return True

def flash_button(x,y):
    if x==0:
        if y==0:
            btn00.flash()
        elif y==1:
            btn01.flash()
        elif y==2:
            btn02.flash()
        elif y==3:
            btn03.flash()
        elif y==4:
            btn04.flash()
        elif y==5:
            btn05.flash()
        elif y==6:
            btn06.flash()
        elif y==7:
            btn07.flash()
        elif y==8:
            btn08.flash()
    elif x==1:
        if y==0:
            btn10.flash()
        elif y==1:
            btn11.flash()
        elif y==2:
            btn12.flash()
        elif y==3:
            btn13.flash()
        elif y==4:
            btn14.flash()
        elif y==5:
            btn15.flash()
        elif y==6:
            btn16.flash()
        elif y==7:
            btn17.flash()
        elif y==8:
            btn18.flash()
    elif x==2:
        if y==0:
            btn20.flash()
        elif y==1:
            btn21.flash()
        elif y==2:
            btn22.flash()
        elif y==3:
            btn23.flash()
        elif y==4:
            btn24.flash()
        elif y==5:
            btn25.flash()
        elif y==6:
            btn26.flash()
        elif y==7:
            btn27.flash()
        elif y==8:
            btn28.flash()
    elif x==3:
        if y==0:
            btn30.flash()
        elif y==1:
            btn31.flash()
        elif y==2:
            btn32.flash()
        elif y==3:
            btn33.flash()
        elif y==4:
            btn34.flash()
        elif y==5:
            btn35.flash()
        elif y==6:
            btn36.flash()
        elif y==7:
            btn37.flash()
        elif y==8:
            btn38.flash()
    elif x==4:
        if y==0:
            btn40.flash()
        elif y==1:
            btn41.flash()
        elif y==2:
            btn42.flash()
        elif y==3:
            btn43.flash()
        elif y==4:
            btn44.flash()
        elif y==5:
            btn45.flash()
        elif y==6:
            btn46.flash()
        elif y==7:
            btn47.flash()
        elif y==8:
            btn48.flash()
    elif x==5:
        if y==0:
            btn50.flash()
        elif y==1:
            btn51.flash()
        elif y==2:
            btn52.flash()
        elif y==3:
            btn53.flash()
        elif y==4:
            btn54.flash()
        elif y==5:
            btn55.flash()
        elif y==6:
            btn56.flash()
        elif y==7:
            btn57.flash()
        elif y==8:
            btn58.flash()
    elif x==6:
        if y==0:
            btn60.flash()
        elif y==1:
            btn61.flash()
        elif y==2:
            btn62.flash()
        elif y==3:
            btn63.flash()
        elif y==4:
            btn64.flash()
        elif y==5:
            btn65.flash()
        elif y==6:
            btn66.flash()
        elif y==7:
            btn67.flash()
        elif y==8:
            btn68.flash()
    elif x==7:
        if y==0:
            btn70.flash()
        elif y==1:
            btn71.flash()
        elif y==2:
            btn72.flash()
        elif y==3:
            btn73.flash()
        elif y==4:
            btn74.flash()
        elif y==5:
            btn75.flash()
        elif y==6:
            btn76.flash()
        elif y==7:
            btn77.flash()
        elif y==8:
            btn78.flash()
    elif x==8:
        if y==0:
            btn80.flash()
        elif y==1:
            btn81.flash()
        elif y==2:
            btn82.flash()
        elif y==3:
            btn83.flash()
        elif y==4:
            btn84.flash()
        elif y==5:
            btn85.flash()
        elif y==6:
            btn86.flash()
        elif y==7:
            btn87.flash()
        elif y==8:
           btn88.flash()
def buscar_gane():
    par=leeractual()
    for i in range(9):
        for j in range(9):
            if par[i][j]=="":
                return False
    ajd=leerconfigsudoku()
    if ajd["tiempo"]=="no":
        pass
    else:
        tiempo=int(ajd["horas"])*3600+int(ajd["minutos"])*60+int(ajd["segundos"])
        escribirposiciones(ajd["nivel"],nombre_jugador.get(),tiempo)
    pausa[0]=0
    
    return True


    
def escribir(x,y):
    
    numero=leerconfigsudoku()["boton"]
    
    
    if numero=="0":
        pass
    else:
        if checar(x,y,numero)==True:
        
            texto=leerconfigsudoku()["imagen"][numero][0]
            
            bg1=leerconfigsudoku()["imagen"][numero][1]
            lista_total[x][y]=numero
            lista_total_borrar[x][y]=numero
            
            
            if bg1=="#8DA641":
                bg1="white"
                
            if x==0:
                if y==0:
                    btn00.config(bg=bg1,text=texto)
                elif y==1:
                    btn01.config(bg=bg1,text=texto)
                elif y==2:
                    btn02.config(bg=bg1,text=texto)
                elif y==3:
                    btn03.config(bg=bg1,text=texto)
                elif y==4:
                    btn04.config(bg=bg1,text=texto)
                elif y==5:
                    btn05.config(bg=bg1,text=texto)
                elif y==6:
                    btn06.config(bg=bg1,text=texto)
                elif y==7:
                    btn07.config(bg=bg1,text=texto)
                elif y==8:
                    btn08.config(bg=bg1,text=texto)
            elif x==1:
                if y==0:
                    btn10.config(bg=bg1,text=texto)
                elif y==1:
                    btn11.config(bg=bg1,text=texto)
                elif y==2:
                    btn12.config(bg=bg1,text=texto)
                elif y==3:
                    btn13.config(bg=bg1,text=texto)
                elif y==4:
                    btn14.config(bg=bg1,text=texto)
                elif y==5:
                    btn15.config(bg=bg1,text=texto)
                elif y==6:
                    btn16.config(bg=bg1,text=texto)
                elif y==7:
                    btn17.config(bg=bg1,text=texto)
                elif y==8:
                    btn18.config(bg=bg1,text=texto)
            elif x==2:
                if y==0:
                    btn20.config(bg=bg1,text=texto)
                elif y==1:
                    btn21.config(bg=bg1,text=texto)
                elif y==2:
                    btn22.config(bg=bg1,text=texto)
                elif y==3:
                    btn23.config(bg=bg1,text=texto)
                elif y==4:
                    btn24.config(bg=bg1,text=texto)
                elif y==5:
                    btn25.config(bg=bg1,text=texto)
                elif y==6:
                    btn26.config(bg=bg1,text=texto)
                elif y==7:
                    btn27.config(bg=bg1,text=texto)
                elif y==8:
                    btn28.config(bg=bg1,text=texto)
            elif x==3:
                if y==0:
                    btn30.config(bg=bg1,text=texto)
                elif y==1:
                    btn31.config(bg=bg1,text=texto)
                elif y==2:
                    btn32.config(bg=bg1,text=texto)
                elif y==3:
                    btn33.config(bg=bg1,text=texto)
                elif y==4:
                    btn34.config(bg=bg1,text=texto)
                elif y==5:
                    btn35.config(bg=bg1,text=texto)
                elif y==6:
                    btn36.config(bg=bg1,text=texto)
                elif y==7:
                    btn37.config(bg=bg1,text=texto)
                elif y==8:
                    btn38.config(bg=bg1,text=texto)
            elif x==4:
                if y==0:
                    btn40.config(bg=bg1,text=texto)
                elif y==1:
                    btn41.config(bg=bg1,text=texto)
                elif y==2:
                    btn42.config(bg=bg1,text=texto)
                elif y==3:
                    btn43.config(bg=bg1,text=texto)
                elif y==4:
                    btn44.config(bg=bg1,text=texto)
                elif y==5:
                    btn45.config(bg=bg1,text=texto)
                elif y==6:
                    btn46.config(bg=bg1,text=texto)
                elif y==7:
                    btn47.config(bg=bg1,text=texto)
                elif y==8:
                    btn48.config(bg=bg1,text=texto)
            elif x==5:
                if y==0:
                    btn50.config(bg=bg1,text=texto)
                elif y==1:
                    btn51.config(bg=bg1,text=texto)
                elif y==2:
                    btn52.config(bg=bg1,text=texto)
                elif y==3:
                    btn53.config(bg=bg1,text=texto)
                elif y==4:
                    btn54.config(bg=bg1,text=texto)
                elif y==5:
                    btn55.config(bg=bg1,text=texto)
                elif y==6:
                    btn56.config(bg=bg1,text=texto)
                elif y==7:
                    btn57.config(bg=bg1,text=texto)
                elif y==8:
                    btn58.config(bg=bg1,text=texto)
            elif x==6:
                if y==0:
                    btn60.config(bg=bg1,text=texto)
                elif y==1:
                    btn61.config(bg=bg1,text=texto)
                elif y==2:
                    btn62.config(bg=bg1,text=texto)
                elif y==3:
                    btn63.config(bg=bg1,text=texto)
                elif y==4:
                    btn64.config(bg=bg1,text=texto)
                elif y==5:
                    btn65.config(bg=bg1,text=texto)
                elif y==6:
                    btn66.config(bg=bg1,text=texto)
                elif y==7:
                    btn67.config(bg=bg1,text=texto)
                elif y==8:
                    btn68.config(bg=bg1,text=texto)
            elif x==7:
                if y==0:
                    btn70.config(bg=bg1,text=texto)
                elif y==1:
                    btn71.config(bg=bg1,text=texto)
                elif y==2:
                    btn72.config(bg=bg1,text=texto)
                elif y==3:
                    btn73.config(bg=bg1,text=texto)
                elif y==4:
                    btn74.config(bg=bg1,text=texto)
                elif y==5:
                    btn75.config(bg=bg1,text=texto)
                elif y==6:
                    btn76.config(bg=bg1,text=texto)
                elif y==7:
                    btn77.config(bg=bg1,text=texto)
                elif y==8:
                    btn78.config(bg=bg1,text=texto)
            elif x==8:
                if y==0:
                    btn80.config(bg=bg1,text=texto)
                elif y==1:
                    btn81.config(bg=bg1,text=texto)
                elif y==2:
                    btn82.config(bg=bg1,text=texto)
                elif y==3:
                    btn83.config(bg=bg1,text=texto)
                elif y==4:
                    btn84.config(bg=bg1,text=texto)
                elif y==5:
                    btn85.config(bg=bg1,text=texto)
                elif y==6:
                    btn86.config(bg=bg1,text=texto)
                elif y==7:
                    btn87.config(bg=bg1,text=texto)
                elif y==8:
                    btn88.config(bg=bg1,text=texto)
            escribirconfigsudoku("boton","0")
            escribiractual(x,y,numero)
            if buscar_gane()==True:
                pausa[0]=0
                btniniciarjuego.config(state="normal")
                sonido="cartoon005.wav"
                messagebox.showinfo(title="Aviso",parent=jugar,message="Juego terminado")
                winsound.PlaySound(sonido,winsound.SND_FILENAME)
                btniniciarjuego.config(state="normal")
                barramenu.entryconfig("Configurar",state="normal")
                btn1.config(state="disabled")
                btn2.config(state="disabled")
                btn3.config(state="disabled")
                btn4.config(state="disabled")
                btn5.config(state="disabled")
                btn6.config(state="disabled")
                btn7.config(state="disabled")
                btn8.config(state="disabled")
                btn9.config(state="disabled")
                finalizado[0]=1
            partidaactual[x][y][0]=texto
            partidaactual[x][y][1]=bg1
            escribirconfigsudoku("boton","")
            if [x,y] in pila:
                pila.remove([x,y])
            
            pila.append([x,y])
        elif checar(x,y,numero)[0]==False :
            messagebox.showinfo(title="Aviso",parent=jugar,message="Jugada no valida: "+checar(x,y,numero)[1])
        


def cargarbotones():
    w=leerconfigsudoku()["imagen"]
    partidaactual=leeractual()
    btn00.config(text=w[partidaactual[0][0]][0],bg=w[partidaactual[0][0]][1])
    btn01.config(text=partidaactual[0][1][0],bg=partidaactual[0][1][1])
    btn02.config(text=partidaactual[0][2][0],bg=partidaactual[0][2][1])
    btn03.config(text=partidaactual[0][3][0],bg=partidaactual[0][3][1])
    btn04.config(text=partidaactual[0][4][0],bg=partidaactual[0][4][1])
    btn05.config(text=partidaactual[0][5][0],bg=partidaactual[0][5][1])
    btn06.config(text=partidaactual[0][6][0],bg=partidaactual[0][6][1])
    btn07.config(text=partidaactual[0][7][0],bg=partidaactual[0][7][1])
    btn08.config(text=partidaactual[0][8][0],bg=partidaactual[0][8][1])

    btn10.config(text=partidaactual[1][0][0],bg=partidaactual[1][0][1])
    btn11.config(text=partidaactual[1][1][0],bg=partidaactual[1][1][1])
    btn12.config(text=partidaactual[1][2][0],bg=partidaactual[1][2][1])
    btn13.config(text=partidaactual[1][3][0],bg=partidaactual[1][3][1])
    btn14.config(text=partidaactual[1][4][0],bg=partidaactual[1][4][1])
    btn15.config(text=partidaactual[1][5][0],bg=partidaactual[1][5][1])
    btn16.config(text=partidaactual[1][6][0],bg=partidaactual[1][6][1])
    btn17.config(text=partidaactual[1][7][0],bg=partidaactual[1][7][1])
    btn18.config(text=partidaactual[1][8][0],bg=partidaactual[1][8][1])

    btn20.config(text=partidaactual[2][0][0],bg=partidaactual[2][0][1])
    btn21.config(text=partidaactual[2][1][0],bg=partidaactual[2][1][1])
    btn22.config(text=partidaactual[2][2][0],bg=partidaactual[2][2][1])
    btn23.config(text=partidaactual[2][3][0],bg=partidaactual[2][3][1])
    btn24.config(text=partidaactual[2][4][0],bg=partidaactual[2][4][1])
    btn25.config(text=partidaactual[2][5][0],bg=partidaactual[2][5][1])
    btn26.config(text=partidaactual[2][6][0],bg=partidaactual[2][6][1])
    btn27.config(text=partidaactual[2][7][0],bg=partidaactual[2][7][1])
    btn28.config(text=partidaactual[2][8][0],bg=partidaactual[2][8][1])

    btn30.config(text=partidaactual[3][0][0],bg=partidaactual[3][0][1])
    btn31.config(text=partidaactual[3][1][0],bg=partidaactual[3][1][1])
    btn32.config(text=partidaactual[3][2][0],bg=partidaactual[3][2][1])
    btn33.config(text=partidaactual[3][3][0],bg=partidaactual[3][3][1])
    btn34.config(text=partidaactual[3][4][0],bg=partidaactual[3][4][1])
    btn35.config(text=partidaactual[3][5][0],bg=partidaactual[3][5][1])
    btn36.config(text=partidaactual[3][6][0],bg=partidaactual[3][6][1])
    btn37.config(text=partidaactual[3][7][0],bg=partidaactual[3][7][1])
    btn38.config(text=partidaactual[3][8][0],bg=partidaactual[3][8][1])

    btn40.config(text=partidaactual[4][0][0],bg=partidaactual[4][0][1])
    btn41.config(text=partidaactual[4][1][0],bg=partidaactual[4][1][1])
    btn42.config(text=partidaactual[4][2][0],bg=partidaactual[4][2][1])
    btn43.config(text=partidaactual[4][3][0],bg=partidaactual[4][3][1])
    btn44.config(text=partidaactual[4][4][0],bg=partidaactual[4][4][1])
    btn45.config(text=partidaactual[4][5][0],bg=partidaactual[4][5][1])
    btn46.config(text=partidaactual[4][6][0],bg=partidaactual[4][6][1])
    btn47.config(text=partidaactual[4][7][0],bg=partidaactual[4][7][1])
    btn48.config(text=partidaactual[4][8][0],bg=partidaactual[4][8][1])

    btn50.config(text=partidaactual[5][0][0],bg=partidaactual[5][0][1])
    btn51.config(text=partidaactual[5][1][0],bg=partidaactual[5][1][1])
    btn52.config(text=partidaactual[5][2][0],bg=partidaactual[5][2][1])
    btn53.config(text=partidaactual[5][3][0],bg=partidaactual[5][3][1])
    btn54.config(text=partidaactual[5][4][0],bg=partidaactual[5][4][1])
    btn55.config(text=partidaactual[5][5][0],bg=partidaactual[5][5][1])
    btn56.config(text=partidaactual[5][6][0],bg=partidaactual[5][6][1])
    btn57.config(text=partidaactual[5][7][0],bg=partidaactual[5][7][1])
    btn58.config(text=partidaactual[5][8][0],bg=partidaactual[5][8][1])

    btn60.config(text=partidaactual[6][0][0],bg=partidaactual[6][0][1])
    btn61.config(text=partidaactual[6][1][0],bg=partidaactual[6][1][1])
    btn62.config(text=partidaactual[6][2][0],bg=partidaactual[6][2][1])
    btn63.config(text=partidaactual[6][3][0],bg=partidaactual[6][3][1])
    btn64.config(text=partidaactual[6][4][0],bg=partidaactual[6][4][1])
    btn65.config(text=partidaactual[6][5][0],bg=partidaactual[6][5][1])
    btn66.config(text=partidaactual[6][6][0],bg=partidaactual[6][6][1])
    btn67.config(text=partidaactual[6][7][0],bg=partidaactual[6][7][1])
    btn68.config(text=partidaactual[6][8][0],bg=partidaactual[6][8][1])

    btn70.config(text=partidaactual[7][0][0],bg=partidaactual[7][0][1])
    btn71.config(text=partidaactual[7][1][0],bg=partidaactual[7][1][1])
    btn72.config(text=partidaactual[7][2][0],bg=partidaactual[7][2][1])
    btn73.config(text=partidaactual[7][3][0],bg=partidaactual[7][3][1])
    btn74.config(text=partidaactual[7][4][0],bg=partidaactual[7][4][1])
    btn75.config(text=partidaactual[7][5][0],bg=partidaactual[7][5][1])
    btn76.config(text=partidaactual[7][6][0],bg=partidaactual[7][6][1])
    btn77.config(text=partidaactual[7][7][0],bg=partidaactual[7][7][1])
    btn78.config(text=partidaactual[7][8][0],bg=partidaactual[7][8][1])

    btn80.config(text=partidaactual[8][0][0],bg=partidaactual[8][0][1])
    btn81.config(text=partidaactual[8][1][0],bg=partidaactual[8][1][1])
    btn82.config(text=partidaactual[8][2][0],bg=partidaactual[8][2][1])
    btn83.config(text=partidaactual[8][3][0],bg=partidaactual[8][3][1])
    btn84.config(text=partidaactual[8][4][0],bg=partidaactual[8][4][1])
    btn85.config(text=partidaactual[8][5][0],bg=partidaactual[8][5][1])
    btn86.config(text=partidaactual[8][6][0],bg=partidaactual[8][6][1])
    btn87.config(text=partidaactual[8][7][0],bg=partidaactual[8][7][1])
    btn88.config(text=partidaactual[8][8][0],bg=partidaactual[8][8][1])
   

def cargar_botones_borrar(x,y):
    bg1="white"
    texto=''
    if x==0:
        if y==0:
            btn00.config(bg=bg1,text=texto)
        elif y==1:
            btn01.config(bg=bg1,text=texto)
        elif y==2:
            btn02.config(bg=bg1,text=texto)
        elif y==3:
            btn03.config(bg=bg1,text=texto)
        elif y==4:
            btn04.config(bg=bg1,text=texto)
        elif y==5:
            btn05.config(bg=bg1,text=texto)
        elif y==6:
            btn06.config(bg=bg1,text=texto)
        elif y==7:
            btn07.config(bg=bg1,text=texto)
        elif y==8:
            btn08.config(bg=bg1,text=texto)
    elif x==1:
        if y==0:
            btn10.config(bg=bg1,text=texto)
        elif y==1:
            btn11.config(bg=bg1,text=texto)
        elif y==2:
            btn12.config(bg=bg1,text=texto)
        elif y==3:
            btn13.config(bg=bg1,text=texto)
        elif y==4:
            btn14.config(bg=bg1,text=texto)
        elif y==5:
            btn15.config(bg=bg1,text=texto)
        elif y==6:
            btn16.config(bg=bg1,text=texto)
        elif y==7:
            btn17.config(bg=bg1,text=texto)
        elif y==8:
            btn18.config(bg=bg1,text=texto)
    elif x==2:
        if y==0:
            btn20.config(bg=bg1,text=texto)
        elif y==1:
            btn21.config(bg=bg1,text=texto)
        elif y==2:
            btn22.config(bg=bg1,text=texto)
        elif y==3:
            btn23.config(bg=bg1,text=texto)
        elif y==4:
            btn24.config(bg=bg1,text=texto)
        elif y==5:
            btn25.config(bg=bg1,text=texto)
        elif y==6:
            btn26.config(bg=bg1,text=texto)
        elif y==7:
            btn27.config(bg=bg1,text=texto)
        elif y==8:
            btn28.config(bg=bg1,text=texto)
    elif x==3:
        if y==0:
            btn30.config(bg=bg1,text=texto)
        elif y==1:
            btn31.config(bg=bg1,text=texto)
        elif y==2:
            btn32.config(bg=bg1,text=texto)
        elif y==3:
            btn33.config(bg=bg1,text=texto)
        elif y==4:
            btn34.config(bg=bg1,text=texto)
        elif y==5:
            btn35.config(bg=bg1,text=texto)
        elif y==6:
            btn36.config(bg=bg1,text=texto)
        elif y==7:
            btn37.config(bg=bg1,text=texto)
        elif y==8:
            btn38.config(bg=bg1,text=texto)
    elif x==4:
        if y==0:
            btn40.config(bg=bg1,text=texto)
        elif y==1:
            btn41.config(bg=bg1,text=texto)
        elif y==2:
            btn42.config(bg=bg1,text=texto)
        elif y==3:
            btn43.config(bg=bg1,text=texto)
        elif y==4:
            btn44.config(bg=bg1,text=texto)
        elif y==5:
            btn45.config(bg=bg1,text=texto)
        elif y==6:
            btn46.config(bg=bg1,text=texto)
        elif y==7:
            btn47.config(bg=bg1,text=texto)
        elif y==8:
            btn48.config(bg=bg1,text=texto)
    elif x==5:
        if y==0:
            btn50.config(bg=bg1,text=texto)
        elif y==1:
            btn51.config(bg=bg1,text=texto)
        elif y==2:
            btn52.config(bg=bg1,text=texto)
        elif y==3:
            btn53.config(bg=bg1,text=texto)
        elif y==4:
            btn54.config(bg=bg1,text=texto)
        elif y==5:
            btn55.config(bg=bg1,text=texto)
        elif y==6:
            btn56.config(bg=bg1,text=texto)
        elif y==7:
            btn57.config(bg=bg1,text=texto)
        elif y==8:
            btn58.config(bg=bg1,text=texto)
    elif x==6:
        if y==0:
            btn60.config(bg=bg1,text=texto)
        elif y==1:
            btn61.config(bg=bg1,text=texto)
        elif y==2:
            btn62.config(bg=bg1,text=texto)
        elif y==3:
            btn63.config(bg=bg1,text=texto)
        elif y==4:
            btn64.config(bg=bg1,text=texto)
        elif y==5:
            btn65.config(bg=bg1,text=texto)
        elif y==6:
            btn66.config(bg=bg1,text=texto)
        elif y==7:
            btn17.config(bg=bg1,text=texto)
        elif y==8:
            btn68.config(bg=bg1,text=texto)
    elif x==7:
        if y==0:
            btn70.config(bg=bg1,text=texto)
        elif y==1:
            btn71.config(bg=bg1,text=texto)
        elif y==2:
            btn72.config(bg=bg1,text=texto)
        elif y==3:
            btn73.config(bg=bg1,text=texto)
        elif y==4:
            btn74.config(bg=bg1,text=texto)
        elif y==5:
            btn75.config(bg=bg1,text=texto)
        elif y==6:
            btn76.config(bg=bg1,text=texto)
        elif y==7:
            btn77.config(bg=bg1,text=texto)
        elif y==8:
            btn78.config(bg=bg1,text=texto)
    elif x==8:
        if y==0:
            btn80.config(bg=bg1,text=texto)
        elif y==1:
            btn81.config(bg=bg1,text=texto)
        elif y==2:
            btn82.config(bg=bg1,text=texto)
        elif y==3:
            btn83.config(bg=bg1,text=texto)
        elif y==4:
            btn84.config(bg=bg1,text=texto)
        elif y==5:
            btn85.config(bg=bg1,text=texto)
        elif y==6:
            btn86.config(bg=bg1,text=texto)
        elif y==7:
            btn87.config(bg=bg1,text=texto)
        elif y==8:
            btn88.config(bg=bg1,text=texto)




    
def borrarjugada():
    if estado[0]==0:
        messagebox.showinfo(title="Aviso",parent=jugar,message="No se ha inciado el juego")

    elif len(pila)==0:
        messagebox.showinfo(title="Aviso",parent=jugar,message="No hay jugadas anteriores")
             
        
        
        
    else:
        posiciones=pila[len(pila)-1]
        
        lista_total[posiciones[0]][posiciones[1]]=""
        lista_total_borrar[posiciones[0]][posiciones[1]]=""
        
        pila.pop()
        cargar_botones_borrar(posiciones[0],posiciones[1])


def update_minutes_positivo(horas,minutos,segundos):
    if minutos==59 and segundos==60:
        
        minutos=0
        horas=horas+1
    if segundos==60:
        segundos=0
    return (horas,minutos,segundos)
def update_seconds_positivo(horas,minutos,segundos):
    
    if segundos==59:
        segundos=60
        minutos=minutos+1
    else:
        
        segundos=segundos+1
        
        
    
    
    abc=update_minutes_positivo(horas,minutos,segundos)
    
    return (abc[0],abc[1],abc[2])
    
def reloj():
    if pausa[0]==0:
        return
    datos=leerconfigsudoku()
    horas=int(datos["horas"])
    minutos=int(datos["minutos"])
    segundos=int(datos["segundos"])
    if datos["tiempo"]=="si":
        tiempos=update_seconds_positivo(horas,minutos,segundos)
    elif datos["tiempo"]=="timer":
        tiempos=update_seconds_negativo(horas,minutos,segundos)
    escribirconfigsudoku("horas",str(tiempos[0]))
    escribirconfigsudoku("minutos",str(tiempos[1]))
    escribirconfigsudoku("segundos",str(tiempos[2]))                     
    label_segundos_cont.config(text=str(tiempos[2]))
    label_minutos_cont.config(text=str(tiempos[1]))
    label_horas_cont.config(text=str(tiempos[0]))
    principal.after(1000,reloj)
         

def update_minutes_negativo(horas,minutos,segundos):
    if minutos==-1:
        minutos=59
        horas=horas-1
    return(horas,minutos,segundos)
def update_seconds_negativo(horas,minutos,segundos):
    if segundos==0:
        if horas==0 and minutos==0 and segundos==0:
            respuesta=messagebox.askyesno(title="Aviso",parent=jugar,message="Tiempos se ha acabado. Continuar jugando")
            
            if respuesta==True:
                escribirconfigsudoku("tiempo","si")
                horas=entry_config_horas.get()
                minutos=entry_config_minutos.get()
                segundos=entry_config_segundos.get()
                escribirconfigsudoku("horas",horas)
                escribirconfigsudoku("minutos",minutos)
                escribirconfigsudoku("segundos",segundos)
        else:
            segundos=59
            minutos=minutos-1        
            update=update_minutes_negativo(horas,minutos,segundos)
            horas=update[0]
            minutos=update[1]
            segundos=update[2]
    else:
        segundos=segundos-1
    return (horas,minutos,segundos)
    


def iniciarjuego():
    pausa[0]=1
    
    a=int(entry_config_segundos.get())
    b=int(entry_config_minutos.get())
    c=int(entry_config_horas.get())
    nombrejugador[0]=nombre_jugador.get()
    if a>59 or a<0 or b>59 or b<0 or c>4 or c<0:
        messagebox.showinfo(title="Aviso",parent=jugar,message="Entradas de tiempo no validas")
    elif len(nombrejugador[0])<2 or len(nombrejugador[0])>30:
        messagebox.showinfo(title="Aviso",parent=jugar,message="Nombre no valido")
    else:
        bmw=leerconfigsudoku()
        label_config_mostrarnivel.config(state="normal",text=bmw["nivel"])
        barramenu.entryconfig("Configurar",state="disabled")
        escribirconfigsudoku("horas",str(c))
        escribirconfigsudoku("minutos",str(b))
        escribirconfigsudoku("segundos",str(a))
        estado[0]=1
        borraractual()
        numeros_en_las_cajas()
        btniniciarjuego.config(state="disabled")
        dicc=leerconfigsudoku()
        if dicc["tiempo"]=="si":
            escribirconfigsudoku("horas","0")
            escribirconfigsudoku("minutos","0")
            escribirconfigsudoku("segundos","0")
            reloj()
        elif dicc["tiempo"]=="timer":
            reloj()
        elif dicc["tiempo"]=="no":
            pass
        
        btn1.config(state="normal")
        btn2.config(state="normal")
        btn3.config(state="normal")
        btn4.config(state="normal")
        btn5.config(state="normal")
        btn6.config(state="normal")
        btn7.config(state="normal")
        btn8.config(state="normal")
        btn9.config(state="normal")


def borrarjuego(pila):#borra las jugadas
    
    if estado[0]==0:
        messagebox.showinfo(title="Aviso",parent=jugar,message="El juego no ha iniciado")
    else:
        respuesta=messagebox.askquestion(title="Aviso",parent=jugar,message="Borrar el juego")
        if respuesta=="yes":
            partidaactual=partidaactualcopia.copy()
            while len(pila)>0:
                borrarjugada()
            


def terminarjuego():#nuevo juego
    
    
    if estado[0]==0:
        messagebox.showinfo(title="Aviso",parent=jugar,message="El juego no ha iniciado")
    else:
        
        respuesta=messagebox.askquestion(title="Aviso",parent=jugar,message="Terminar el juego")
        if respuesta=="yes":
            
            iniciarjuego()
            btniniciarjuego.config(state="normal")
            barramenu.entryconfig("Configurar",state="normal")
            numeros_en_las_cajas()
            nombre_jugador.delete(0,END)
            nombre_jugador.insert(0,"")
            pausa[0]=0
            pila=[]
            
            btn1.config(state="disabled")
            btn2.config(state="disabled")
            btn3.config(state="disabled")
            btn4.config(state="disabled")
            btn5.config(state="disabled")
            btn6.config(state="disabled")
            btn7.config(state="disabled")
            btn8.config(state="disabled")
            btn9.config(state="disabled")
            
estado_botones={"":"normal","1":"normal","2":"normal","3":"normal","4":"normal","5":"normal","6":"normal","7":"normal","8":"normal","9":"normal"}
def cargarbotones_inicio(partida):
    
    escribirconfigsudoku("boton","")
    w=leerconfigsudoku()["imagen"]
    pila=[]#si hay errores esta aqui
    for i in range(9):
        for j in range(9):
            escribiractual(i,j,str(partida[i][j]))
            lista_total[i][j]=(str(partida[i][j]))
    
    if w["1"][0]!="":
        for i in range(1,10):
            w[str(i)][1]="white"
    
    z=leeractual()

    btn00.config(text=w[z[0][0]][0],bg=w[z[0][0]][1],state=estado_botones[z[0][0]])
    btn01.config(text=w[z[0][1]][0],bg=w[z[0][1]][1],state=estado_botones[z[0][1]])
    btn02.config(text=w[z[0][2]][0],bg=w[z[0][2]][1],state=estado_botones[z[0][2]])
    btn03.config(text=w[z[0][3]][0],bg=w[z[0][3]][1],state=estado_botones[z[0][3]])
    btn04.config(text=w[z[0][4]][0],bg=w[z[0][4]][1],state=estado_botones[z[0][4]])
    btn05.config(text=w[z[0][5]][0],bg=w[z[0][5]][1],state=estado_botones[z[0][5]])
    btn06.config(text=w[z[0][6]][0],bg=w[z[0][6]][1],state=estado_botones[z[0][6]])
    btn07.config(text=w[z[0][7]][0],bg=w[z[0][7]][1],state=estado_botones[z[0][7]])
    btn08.config(text=w[z[0][8]][0],bg=w[z[0][8]][1],state=estado_botones[z[0][8]])

    btn10.config(text=w[z[1][0]][0],bg=w[z[1][0]][1],state=estado_botones[z[1][0]])
    btn11.config(text=w[z[1][1]][0],bg=w[z[1][1]][1],state=estado_botones[z[1][1]])
    btn12.config(text=w[z[1][2]][0],bg=w[z[1][2]][1],state=estado_botones[z[1][2]])
    btn13.config(text=w[z[1][3]][0],bg=w[z[1][3]][1],state=estado_botones[z[1][3]])
    btn14.config(text=w[z[1][4]][0],bg=w[z[1][4]][1],state=estado_botones[z[1][4]])
    btn15.config(text=w[z[1][5]][0],bg=w[z[1][5]][1],state=estado_botones[z[1][5]])
    btn16.config(text=w[z[1][6]][0],bg=w[z[1][6]][1],state=estado_botones[z[1][6]])
    btn17.config(text=w[z[1][7]][0],bg=w[z[1][7]][1],state=estado_botones[z[1][7]])
    btn18.config(text=w[z[1][8]][0],bg=w[z[1][8]][1],state=estado_botones[z[1][8]])

    btn20.config(text=w[z[2][0]][0],bg=w[z[2][0]][1],state=estado_botones[z[2][0]])
    btn21.config(text=w[z[2][1]][0],bg=w[z[2][1]][1],state=estado_botones[z[2][1]])
    btn22.config(text=w[z[2][2]][0],bg=w[z[2][2]][1],state=estado_botones[z[2][2]])
    btn23.config(text=w[z[2][3]][0],bg=w[z[2][3]][1],state=estado_botones[z[2][3]])
    btn24.config(text=w[z[2][4]][0],bg=w[z[2][4]][1],state=estado_botones[z[2][4]])
    btn25.config(text=w[z[2][5]][0],bg=w[z[2][5]][1],state=estado_botones[z[2][5]])
    btn26.config(text=w[z[2][6]][0],bg=w[z[2][6]][1],state=estado_botones[z[2][6]])
    btn27.config(text=w[z[2][7]][0],bg=w[z[2][7]][1],state=estado_botones[z[2][7]])
    btn28.config(text=w[z[2][8]][0],bg=w[z[2][8]][1],state=estado_botones[z[2][8]])

    btn30.config(text=w[z[3][0]][0],bg=w[z[3][0]][1],state=estado_botones[z[3][0]])
    btn31.config(text=w[z[3][1]][0],bg=w[z[3][1]][1],state=estado_botones[z[3][1]])
    btn32.config(text=w[z[3][2]][0],bg=w[z[3][2]][1],state=estado_botones[z[3][2]])
    btn33.config(text=w[z[3][3]][0],bg=w[z[3][3]][1],state=estado_botones[z[3][3]])
    btn34.config(text=w[z[3][4]][0],bg=w[z[3][4]][1],state=estado_botones[z[3][4]])
    btn35.config(text=w[z[3][5]][0],bg=w[z[3][5]][1],state=estado_botones[z[3][5]])
    btn36.config(text=w[z[3][6]][0],bg=w[z[3][6]][1],state=estado_botones[z[3][6]])
    btn37.config(text=w[z[3][7]][0],bg=w[z[3][7]][1],state=estado_botones[z[3][7]])
    btn38.config(text=w[z[3][8]][0],bg=w[z[3][8]][1],state=estado_botones[z[3][8]])

    btn40.config(text=w[z[4][0]][0],bg=w[z[4][0]][1],state=estado_botones[z[4][0]])
    btn41.config(text=w[z[4][1]][0],bg=w[z[4][1]][1],state=estado_botones[z[4][1]])
    btn42.config(text=w[z[4][2]][0],bg=w[z[4][2]][1],state=estado_botones[z[4][2]])
    btn43.config(text=w[z[4][3]][0],bg=w[z[4][3]][1],state=estado_botones[z[4][3]])
    btn44.config(text=w[z[4][4]][0],bg=w[z[4][4]][1],state=estado_botones[z[4][4]])
    btn45.config(text=w[z[4][5]][0],bg=w[z[4][5]][1],state=estado_botones[z[4][5]])
    btn46.config(text=w[z[4][6]][0],bg=w[z[4][6]][1],state=estado_botones[z[4][6]])
    btn47.config(text=w[z[4][7]][0],bg=w[z[4][7]][1],state=estado_botones[z[4][7]])
    btn48.config(text=w[z[4][8]][0],bg=w[z[4][8]][1],state=estado_botones[z[4][8]])

    btn50.config(text=w[z[5][0]][0],bg=w[z[5][0]][1],state=estado_botones[z[5][0]])
    btn51.config(text=w[z[5][1]][0],bg=w[z[5][1]][1],state=estado_botones[z[5][1]])
    btn52.config(text=w[z[5][2]][0],bg=w[z[5][2]][1],state=estado_botones[z[5][2]])
    btn53.config(text=w[z[5][3]][0],bg=w[z[5][3]][1],state=estado_botones[z[5][3]])
    btn54.config(text=w[z[5][4]][0],bg=w[z[5][4]][1],state=estado_botones[z[5][4]])
    btn55.config(text=w[z[5][5]][0],bg=w[z[5][5]][1],state=estado_botones[z[5][5]])
    btn56.config(text=w[z[5][6]][0],bg=w[z[5][6]][1],state=estado_botones[z[5][6]])
    btn57.config(text=w[z[5][7]][0],bg=w[z[5][7]][1],state=estado_botones[z[5][7]])
    btn58.config(text=w[z[5][8]][0],bg=w[z[5][8]][1],state=estado_botones[z[5][8]])

    btn60.config(text=w[z[6][0]][0],bg=w[z[6][0]][1],state=estado_botones[z[6][0]])
    btn61.config(text=w[z[6][1]][0],bg=w[z[6][1]][1],state=estado_botones[z[6][1]])
    btn62.config(text=w[z[6][2]][0],bg=w[z[6][2]][1],state=estado_botones[z[6][2]])
    btn63.config(text=w[z[6][3]][0],bg=w[z[6][3]][1],state=estado_botones[z[6][3]])
    btn64.config(text=w[z[6][4]][0],bg=w[z[6][4]][1],state=estado_botones[z[6][4]])
    btn65.config(text=w[z[6][5]][0],bg=w[z[6][5]][1],state=estado_botones[z[6][5]])
    btn66.config(text=w[z[6][6]][0],bg=w[z[6][6]][1],state=estado_botones[z[6][6]])
    btn67.config(text=w[z[6][7]][0],bg=w[z[6][7]][1],state=estado_botones[z[6][7]])
    btn68.config(text=w[z[6][8]][0],bg=w[z[6][8]][1],state=estado_botones[z[6][8]])

    btn70.config(text=w[z[7][0]][0],bg=w[z[7][0]][1],state=estado_botones[z[7][0]])
    btn71.config(text=w[z[7][1]][0],bg=w[z[7][1]][1],state=estado_botones[z[7][1]])
    btn72.config(text=w[z[7][2]][0],bg=w[z[7][2]][1],state=estado_botones[z[7][2]])
    btn73.config(text=w[z[7][3]][0],bg=w[z[7][3]][1],state=estado_botones[z[7][3]])
    btn74.config(text=w[z[7][4]][0],bg=w[z[7][4]][1],state=estado_botones[z[7][4]])
    btn75.config(text=w[z[7][5]][0],bg=w[z[7][5]][1],state=estado_botones[z[7][5]])
    btn76.config(text=w[z[7][6]][0],bg=w[z[7][6]][1],state=estado_botones[z[7][6]])
    btn77.config(text=w[z[7][7]][0],bg=w[z[7][7]][1],state=estado_botones[z[7][7]])
    btn78.config(text=w[z[7][8]][0],bg=w[z[7][8]][1],state=estado_botones[z[7][8]])

    btn80.config(text=w[z[8][0]][0],bg=w[z[8][0]][1],state=estado_botones[z[8][0]])
    btn81.config(text=w[z[8][1]][0],bg=w[z[8][1]][1],state=estado_botones[z[8][1]])
    btn82.config(text=w[z[8][2]][0],bg=w[z[8][2]][1],state=estado_botones[z[8][2]])
    btn83.config(text=w[z[8][3]][0],bg=w[z[8][3]][1],state=estado_botones[z[8][3]])
    btn84.config(text=w[z[8][4]][0],bg=w[z[8][4]][1],state=estado_botones[z[8][4]])
    btn85.config(text=w[z[8][5]][0],bg=w[z[8][5]][1],state=estado_botones[z[8][5]])
    btn86.config(text=w[z[8][6]][0],bg=w[z[8][6]][1],state=estado_botones[z[8][6]])
    btn87.config(text=w[z[8][7]][0],bg=w[z[8][7]][1],state=estado_botones[z[8][7]])
    btn88.config(text=w[z[8][8]][0],bg=w[z[8][8]][1],state=estado_botones[z[8][8]])
def numeros_en_las_cajas():
    p=leerpartidasudoku()
    j=leerconfigsudoku()
    
    
    if j["nivel"]=="facil":
        
        numero=random.randint(0,len(p[0])-1)
        partida=p[0][numero]
    elif j["nivel"]=="medio":
        numero=random.randint(0,len(p[1])-1)
        partida=p[1][numero]

    elif j["nivel"]=="dificil":
        numero=random.randint(0,len(p[2])-1)
        partida=p[2][numero]
    cargarbotones_inicio(partida)


def cargar_partida():
    datos=abriractual()
    nombre_jugador.delete(0,END)
    nombre_jugador.insert(0,datos["nombre"])
    escribirconfigsudoku("tiempo",datos["tiempo"])
    escribirconfigsudoku("horas",datos["horas"])
    escribirconfigsudoku("minutos",datos["minutos"])
    escribirconfigsudoku("segundos",datos["segundos"])
    escribirconfigsudoku("imagen",datos["imagen"])
    partida=datos["partida"]
    cargarbotones_inicio(partida)
            
    btn1.config(state="normal")
    btn2.config(state="normal")
    btn3.config(state="normal")
    btn4.config(state="normal")
    btn5.config(state="normal")
    btn6.config(state="normal")
    btn7.config(state="normal")
    btn8.config(state="normal")
    btn9.config(state="normal")
    reloj()
    
    
    
###
frame_sudokuc=Frame(modificar,bg="black",padx=1,pady=1,width=500,height=500)#bg=color_boton[1]
frame_botonesc=Frame(modificar,bg="#F6F7F2",width=20,height=400)
def jugar_pos_panelc():
    dicc=leerconfigsudoku()
    frame_botonesc.place(x=xy_pos_panel[dicc["pos"]][0][0],y=xy_pos_panel[dicc["pos"]][0][1])
    frame_sudokuc.place(x=xy_pos_panel[dicc["pos"]][1][0],y=xy_pos_panel[dicc["pos"]][1][1])
jugar_pos_panelc()

frame11c=Frame(frame_sudokuc,bg="black",width=12, height=6,bd=3)
frame11c.grid(row=0,column=0)
frame12c=Frame(frame_sudokuc,bg="black",width=12, height=6,bd=3)
frame12c.grid(row=0,column=1)
frame13c=Frame(frame_sudokuc,bg="black",width=12, height=6,bd=3)
frame13c.grid(row=0,column=2)
frame21c=Frame(frame_sudokuc,bg="black",width=12, height=6,bd=3)
frame21c.grid(row=1,column=0)
frame22c=Frame(frame_sudokuc,bg="black",width=12, height=6,bd=3)
frame22c.grid(row=1,column=1)
frame23c=Frame(frame_sudokuc,bg="black",width=12, height=6,bd=3)
frame23c.grid(row=1,column=2)
frame31c=Frame(frame_sudokuc,bg="black",width=12, height=6,bd=3)
frame31c.grid(row=2,column=0)
frame32c=Frame(frame_sudokuc,bg="black",width=12, height=6,bd=3)
frame32c.grid(row=2,column=1)
frame33c=Frame(frame_sudokuc,bg="black",width=12, height=6,bd=3)
frame33c.grid(row=2,column=2)
#fila0
btn00c=Button(frame11c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(0,0))
btn00c.grid(row=0,column=0)
btn01c=Button(frame11c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(0,1))
btn01c.grid(row=0,column=1)
btn02c=Button(frame11c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(0,2))
btn02c.grid(row=0,column=2)
btn03c=Button(frame12c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(0,3))
btn03c.grid(row=0,column=3)
btn04c=Button(frame12c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(0,4))
btn04c.grid(row=0,column=4)
btn05c=Button(frame12c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(0,5))
btn05c.grid(row=0,column=5)
btn06c=Button(frame13c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(0,6))
btn06c.grid(row=0,column=6)
btn07c=Button(frame13c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(0,7))
btn07c.grid(row=0,column=7)
btn08c=Button(frame13c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(0,8))
btn08c.grid(row=0,column=8)
#filacc1
btn10c=Button(frame11c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(1,0))
btn10c.grid(row=1,column=0)
btn11c=Button(frame11c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(1,1))
btn11c.grid(row=1,column=1)
btn12c=Button(frame11c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(1,2))
btn12c.grid(row=1,column=2)
btn13c=Button(frame12c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(1,3))
btn13c.grid(row=1,column=3)
btn14c=Button(frame12c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(1,4))
btn14c.grid(row=1,column=4)
btn15c=Button(frame12c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(1,5))
btn15c.grid(row=1,column=5)
btn16c=Button(frame13c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(1,6))
btn16c.grid(row=1,column=6)
btn17c=Button(frame13c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(1,7))
btn17c.grid(row=1,column=7)
btn18c=Button(frame13c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(1,8))
btn18c.grid(row=1,column=8)
#filac2
btn20c=Button(frame11c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(2,0))
btn20c.grid(row=2,column=0)
btn21c=Button(frame11c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(2,1))
btn21c.grid(row=2,column=1)
btn22c=Button(frame11c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(2,2))
btn22c.grid(row=2,column=2)
btn23c=Button(frame12c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(2,3))
btn23c.grid(row=2,column=3)
btn24c=Button(frame12c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(2,4))
btn24c.grid(row=2,column=4)
btn25c=Button(frame12c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(2,5))
btn25c.grid(row=2,column=5)
btn26c=Button(frame13c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(2,6))
btn26c.grid(row=2,column=6)
btn27c=Button(frame13c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(2,7))
btn27c.grid(row=2,column=7)
btn28c=Button(frame13c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(2,8))
btn28c.grid(row=2,column=8)
#filacc3
btn30c=Button(frame21c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(3,0))
btn30c.grid(row=0,column=0)
btn31c=Button(frame21c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(3,1))
btn31c.grid(row=0,column=1)
btn32c=Button(frame21c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(3,2))
btn32c.grid(row=0,column=2)
btn33c=Button(frame22c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(3,3))
btn33c.grid(row=0,column=3)
btn34c=Button(frame22c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(3,4))
btn34c.grid(row=0,column=4)
btn35c=Button(frame22c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(3,5))
btn35c.grid(row=0,column=5)
btn36c=Button(frame23c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(3,6))
btn36c.grid(row=0,column=6)
btn37c=Button(frame23c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(3,7))
btn37c.grid(row=0,column=7)
btn38c=Button(frame23c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(3,8))
btn38c.grid(row=0,column=8)
#fila4
btn40c=Button(frame21c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(4,0))
btn40c.grid(row=1,column=0)
btn41c=Button(frame21c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(4,1))
btn41c.grid(row=1,column=1)
btn42c=Button(frame21c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(4,2))
btn42c.grid(row=1,column=2)
btn43c=Button(frame22c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(4,3))
btn43c.grid(row=1,column=3)
btn44c=Button(frame22c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(4,4))
btn44c.grid(row=1,column=4)
btn45c=Button(frame22c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(4,5))
btn45c.grid(row=1,column=5)
btn46c=Button(frame23c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(4,6))
btn46c.grid(row=1,column=6)
btn47c=Button(frame23c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(4,7))
btn47c.grid(row=1,column=7)
btn48c=Button(frame23c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(4,8))
btn48c.grid(row=1,column=8)
#filacc5
btn50c=Button(frame21c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(5,0))
btn50c.grid(row=2,column=0)
btn51c=Button(frame21c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(5,1))
btn51c.grid(row=2,column=1)
btn52c=Button(frame21c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(5,2))
btn52c.grid(row=2,column=2)
btn53c=Button(frame22c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(5,3))
btn53c.grid(row=2,column=3)
btn54c=Button(frame22c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(5,4))
btn54c.grid(row=2,column=4)
btn55c=Button(frame22c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(5,5))
btn55c.grid(row=2,column=5)
btn56c=Button(frame23c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(5,6))
btn56c.grid(row=2,column=6)
btn57c=Button(frame23c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(5,7))
btn57c.grid(row=2,column=7)
btn58c=Button(frame23c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(5,8))
btn58c.grid(row=2,column=8)
#filacc6
btn60c=Button(frame31c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(6,0))
btn60c.grid(row=0,column=0)
btn61c=Button(frame31c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(6,1))
btn61c.grid(row=0,column=1)
btn62c=Button(frame31c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(6,2))
btn62c.grid(row=0,column=2)
btn63c=Button(frame32c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(6,3))
btn63c.grid(row=0,column=3)
btn64c=Button(frame32c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(6,4))
btn64c.grid(row=0,column=4)
btn65c=Button(frame32c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(6,5))
btn65c.grid(row=0,column=5)
btn66c=Button(frame33c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(6,6))
btn66c.grid(row=0,column=6)
btn67c=Button(frame33c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(6,7))
btn67c.grid(row=0,column=7)
btn68c=Button(frame33c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(6,8))
btn68c.grid(row=0,column=8)
#fiac7
btn70c=Button(frame31c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(7,0))
btn70c.grid(row=1,column=0)
btn71c=Button(frame31c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(7,1))
btn71c.grid(row=1,column=1)
btn72c=Button(frame31c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(7,2))
btn72c.grid(row=1,column=2)
btn73c=Button(frame32c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(7,3))
btn73c.grid(row=1,column=3)
btn74c=Button(frame32c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(7,4))
btn74c.grid(row=1,column=4)
btn75c=Button(frame32c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(7,5))
btn75c.grid(row=1,column=5)
btn76c=Button(frame33c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(7,6))
btn76c.grid(row=1,column=6)
btn77c=Button(frame33c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(7,7))
btn77c.grid(row=1,column=7)
btn78c=Button(frame33c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(7,8))
btn78c.grid(row=1,column=8)
#filac8
btn80c=Button(frame31c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(8,0))
btn80c.grid(row=2,column=0)
btn81c=Button(frame31c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(8,1))
btn81c.grid(row=2,column=1)
btn82c=Button(frame31c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(8,2))
btn82c.grid(row=2,column=2)
btn83c=Button(frame32c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(8,3))
btn83c.grid(row=2,column=3)
btn84c=Button(frame32c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(8,4))
btn84c.grid(row=2,column=4)
btn85c=Button(frame32c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(8,5))
btn85c.grid(row=2,column=5)
btn86c=Button(frame33c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(8,6))
btn86c.grid(row=2,column=6)
btn87c=Button(frame33c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(8,7))
btn87c.grid(row=2,column=7)
btn88c=Button(frame33c,bg=color_boton[1],text="",width=4,height=2,bd=1,command=lambda:escribirc(8,8))
btn88c.grid(row=2,column=8)

partidacosas=[["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""]]
def checar2(x,y,numero):
    for i in range(9):
        if partidacosas[x][i]==numero:
            return False
    for i in range(9):
        if partidacosas[i][y]==numero:
            return False
    if x<=2:
        if y<=2:
            for i in range(3):
                for j in range(3):
                    if numero in partidacosas[i][j]:
                        
                        return False
        elif y<=5:
            for i in range(3):
                for j in range(3,6):
                    if numero in partidacosas[i][j]:
                        
                        return False
        elif y<=8:
            for i in range(3):
                for j in range(6,9):
                    if numero in partidacosas[i][j]:
                        
                        return False
    elif x<=5:
        if y<=2:
            for i in range(3,6):
                for j in range(3):
                    if numero in partidacosas[i][j]:
                        
                        return False
        elif y<=5:
            for i in range(3,6):
                for j in range(3,6):
                    if numero in partidacosas[i][j]:
                       
                        return False
        elif y<=8:
            for i in range(3,6):
                for j in range(6,9):
                    if numero in partidacosas[i][j]:
                       
                            return False
    elif x<=8:
        if y<=2:
            for i in range(6,9):
                for j in range(3):
                    if numero in partidacosas[i][j]:
                        
                        return False
        elif y<=5:
            for i in range(6,9):
                for j in range(3,6):
                    if numero in partidacosas[i][j]:
                        
                        return False
        elif y<=8:
            for i in range(6,9):
                for j in range(6,9):
                    if numero in partidacosas[i][j]:
                        
                        return False
    return True

boton_ahora=[0]
def boton_seleccionadoc(num):
    boton_ahora[0]=str(num)
def escribirc(x,y):
    try:
        if checar2(x,y,boton_ahora[0])==True:
            if boton_ahora[0]=="0":
                boton_ahora[0]=""
                
            partidacosas[x][y]=boton_ahora[0]
            if boton_ahora[0]=="":
                texto=""
                bg1="white"
            else:
                texto=leerconfigsudoku()["imagen"][boton_ahora[0]][0]
                    
                bg1=leerconfigsudoku()["imagen"][boton_ahora[0]][1]
            if x==0:
                if y==0:
                    btn00c.config(bg=bg1,text=texto)
                elif y==1:
                    btn01c.config(bg=bg1,text=texto)
                elif y==2:
                    btn02c.config(bg=bg1,text=texto)
                elif y==3:
                    btn03c.config(bg=bg1,text=texto)
                elif y==4:
                    btn04c.config(bg=bg1,text=texto)
                elif y==5:
                    btn05c.config(bg=bg1,text=texto)
                elif y==6:
                    btn06c.config(bg=bg1,text=texto)
                elif y==7:
                    btn07c.config(bg=bg1,text=texto)
                elif y==8:
                    btn08c.config(bg=bg1,text=texto)
            elif x==1:
                if y==0:
                    btn10c.config(bg=bg1,text=texto)
                elif y==1:
                    btn11c.config(bg=bg1,text=texto)
                elif y==2:
                    btn12c.config(bg=bg1,text=texto)
                elif y==3:
                    btn13c.config(bg=bg1,text=texto)
                elif y==4:
                    btn14c.config(bg=bg1,text=texto)
                elif y==5:
                    btn15c.config(bg=bg1,text=texto)
                elif y==6:
                    btn16c.config(bg=bg1,text=texto)
                elif y==7:
                    btn17c.config(bg=bg1,text=texto)
                elif y==8:
                    btn18c.config(bg=bg1,text=texto)
            elif x==2:
                if y==0:
                    btn20c.config(bg=bg1,text=texto)
                elif y==1:
                    btn21c.config(bg=bg1,text=texto)
                elif y==2:
                    btn22c.config(bg=bg1,text=texto)
                elif y==3:
                    btn23c.config(bg=bg1,text=texto)
                elif y==4:
                    btn24c.config(bg=bg1,text=texto)
                elif y==5:
                    btn25c.config(bg=bg1,text=texto)
                elif y==6:
                    btn26c.config(bg=bg1,text=texto)
                elif y==7:
                    btn27c.config(bg=bg1,text=texto)
                elif y==8:
                    btn28c.config(bg=bg1,text=texto)
            elif x==3:
                if y==0:
                    btn30c.config(bg=bg1,text=texto)
                elif y==1:
                    btn31c.config(bg=bg1,text=texto)
                elif y==2:
                    btn32c.config(bg=bg1,text=texto)
                elif y==3:
                    btn33c.config(bg=bg1,text=texto)
                elif y==4:
                    btn34c.config(bg=bg1,text=texto)
                elif y==5:
                    btn35c.config(bg=bg1,text=texto)
                elif y==6:
                    btn36c.config(bg=bg1,text=texto)
                elif y==7:
                    btn37c.config(bg=bg1,text=texto)
                elif y==8:
                    btn38c.config(bg=bg1,text=texto)
            elif x==4:
                if y==0:
                    btn40c.config(bg=bg1,text=texto)
                elif y==1:
                    btn41c.config(bg=bg1,text=texto)
                elif y==2:
                    btn42c.config(bg=bg1,text=texto)
                elif y==3:
                    btn43c.config(bg=bg1,text=texto)
                elif y==4:
                    btn44c.config(bg=bg1,text=texto)
                elif y==5:
                    btn45c.config(bg=bg1,text=texto)
                elif y==6:
                    btn46c.config(bg=bg1,text=texto)
                elif y==7:
                    btn47c.config(bg=bg1,text=texto)
                elif y==8:
                    btn48c.config(bg=bg1,text=texto)
            elif x==5:
                if y==0:
                    btn50c.config(bg=bg1,text=texto)
                elif y==1:
                    btn51c.config(bg=bg1,text=texto)
                elif y==2:
                    btn52c.config(bg=bg1,text=texto)
                elif y==3:
                    btn53c.config(bg=bg1,text=texto)
                elif y==4:
                    btn54c.config(bg=bg1,text=texto)
                elif y==5:
                    btn55c.config(bg=bg1,text=texto)
                elif y==6:
                    btn56c.config(bg=bg1,text=texto)
                elif y==7:
                    btn57c.config(bg=bg1,text=texto)
                elif y==8:
                    btn58c.config(bg=bg1,text=texto)
            elif x==6:
                if y==0:
                    btn60c.config(bg=bg1,text=texto)
                elif y==1:
                    btn61c.config(bg=bg1,text=texto)
                elif y==2:
                    btn62c.config(bg=bg1,text=texto)
                elif y==3:
                    btn63c.config(bg=bg1,text=texto)
                elif y==4:
                    btn64c.config(bg=bg1,text=texto)
                elif y==5:
                    btn65c.config(bg=bg1,text=texto)
                elif y==6:
                    btn66c.config(bg=bg1,text=texto)
                elif y==7:
                    btn67c.config(bg=bg1,text=texto)
                elif y==8:
                    btn68c.config(bg=bg1,text=texto)
            elif x==7:
                if y==0:
                    btn70c.config(bg=bg1,text=texto)
                elif y==1:
                    btn71c.config(bg=bg1,text=texto)
                elif y==2:
                    btn72c.config(bg=bg1,text=texto)
                elif y==3:
                    btn73c.config(bg=bg1,text=texto)
                elif y==4:
                    btn74c.config(bg=bg1,text=texto)
                elif y==5:
                    btn75c.config(bg=bg1,text=texto)
                elif y==6:
                    btn76c.config(bg=bg1,text=texto)
                elif y==7:
                    btn77c.config(bg=bg1,text=texto)
                elif y==8:
                    btn78c.config(bg=bg1,text=texto)
            elif x==8:
                if y==0:
                    btn80c.config(bg=bg1,text=texto)
                elif y==1:
                    btn81c.config(bg=bg1,text=texto)
                elif y==2:
                    btn82c.config(bg=bg1,text=texto)
                elif y==3:
                    btn83c.config(bg=bg1,text=texto)
                elif y==4:
                    btn84c.config(bg=bg1,text=texto)
                elif y==5:
                    btn85c.config(bg=bg1,text=texto)
                elif y==6:
                    btn86c.config(bg=bg1,text=texto)
                elif y==7:
                    btn87c.config(bg=bg1,text=texto)
                elif y==8:
                    btn88c.config(bg=bg1,text=texto)
    except:
        pass
        
    
    
btn1c=Button(frame_botonesc,bd=0,width=2,height=2,state="normal",command=lambda:boton_seleccionadoc(1))#este tiene que poner ademas la flecha a la par)
btn1c.grid(row=0,column=1)
btn2c=Button(frame_botonesc,bd=0,width=2,height=2,state="normal",command=lambda:boton_seleccionadoc(2))
btn2c.grid(row=1,column=1)
btn3c=Button(frame_botonesc,bd=0,width=2,height=2,state="normal",command=lambda:boton_seleccionadoc(3))
btn3c.grid(row=2,column=1)
btn4c=Button(frame_botonesc,bd=0,width=2,height=2,state="normal",command=lambda:boton_seleccionadoc(4))
btn4c.grid(row=3,column=1)
btn5c=Button(frame_botonesc,bd=0,width=2,height=2,state="normal",command=lambda:boton_seleccionadoc(5))
btn5c.grid(row=4,column=1)
btn6c=Button(frame_botonesc,bd=0,width=2,height=2,state="normal",command=lambda:boton_seleccionadoc(6))
btn6c.grid(row=5,column=1)
btn7c=Button(frame_botonesc,bd=0,width=2,height=2,state="normal",command=lambda:boton_seleccionadoc(7))
btn7c.grid(row=6,column=1)
btn8c=Button(frame_botonesc,bd=0,width=2,height=2,state="normal",command=lambda:boton_seleccionadoc(8))
btn8c.grid(row=7,column=1)
btn9c=Button(frame_botonesc,bd=0,width=2,height=2,state="normal",command=lambda:boton_seleccionadoc(9))
btn9c.grid(row=8,column=1)
btnvacioc=Button(frame_botonesc,bd=0,width=2,height=2,state="normal",command=lambda:boton_seleccionadoc(0))
btnvacioc.grid(row=9,column=1)

def imagenes_del_panelc():
    dicc=leerconfigsudoku()
    btn1c.config(text=dicc["imagen"]["1"][0],bg=dicc["imagen"]["1"][1])
    btn2c.config(text=dicc["imagen"]["2"][0],bg=dicc["imagen"]["2"][1])
    btn3c.config(text=dicc["imagen"]["3"][0],bg=dicc["imagen"]["3"][1])
    btn4c.config(text=dicc["imagen"]["4"][0],bg=dicc["imagen"]["4"][1])
    btn5c.config(text=dicc["imagen"]["5"][0],bg=dicc["imagen"]["5"][1])
    btn6c.config(text=dicc["imagen"]["6"][0],bg=dicc["imagen"]["6"][1])
    btn7c.config(text=dicc["imagen"]["7"][0],bg=dicc["imagen"]["7"][1])
    btn8c.config(text=dicc["imagen"]["8"][0],bg=dicc["imagen"]["8"][1])
    btn9c.config(text=dicc["imagen"]["9"][0],bg=dicc["imagen"]["9"][1])
    btnvacioc.config(text="clr",bg="light grey")
    
imagenes_del_panelc()
btnincluir=Button(modificar,text="Incluir partida",width=12,height=2,bg=color_boton[0],bd=0,command=lambda:incluir())
btnincluir.place(x=40,y=450)
btnmodificar=Button(modificar,text="Guardar cambios",width=13,height=2,bg=color_boton[0],bd=0,command=lambda:guardar())
btnmodificar.place(x=210,y=450)
btnconsultar=Button(modificar,text="Consultar partida",width=14,height=2,bg=color_boton[0],bd=0,command=lambda:consultar())
btnconsultar.place(x=400,y=450)
entry_partida=Entry(modificar, bd=0,bg="white",font=("Calibri",12),width=2)
entry_partida.insert(0,"#")
entry_partida.place(x=520,y=460)
def incluir():
    a=leerpartidasudoku()
    nivel=leerconfigsudoku()["nivel"]
    
    if nivel=="facil":
        indice=0
    elif nivel=="medio":
        indice=1
    elif nivel=="dificil":
        indice=2
    if partidacosas in a[indice]:
        return False
    f= open('sudoku2016partidas.dat', 'wb')
    a[indice].append(partidacosas)
    pickle.dump(a, f)
        
def consultar():
    
    try:
        indice=int(entry_partida.get())
        a=leerpartidasudoku()
        nivel=leerconfigsudoku()["nivel"]
        if nivel=="facil":
            nivel=0
        elif nivel=="medio":
            nivel=1
        elif nivel=="dificil":
            nivel=2
        partida_cargar=a[nivel][indice]
        partidacosas=partida_cargar
        z=partida_cargar
        w=leerconfigsudoku()["imagen"]
        btn00c.config(text=w[z[0][0]][0],bg=w[z[0][0]][1])
        btn01c.config(text=w[z[0][1]][0],bg=w[z[0][1]][1])
        btn02c.config(text=w[z[0][2]][0],bg=w[z[0][2]][1])
        btn03c.config(text=w[z[0][3]][0],bg=w[z[0][3]][1])
        btn04c.config(text=w[z[0][4]][0],bg=w[z[0][4]][1])
        btn05c.config(text=w[z[0][5]][0],bg=w[z[0][5]][1])
        btn06c.config(text=w[z[0][6]][0],bg=w[z[0][6]][1])
        btn07c.config(text=w[z[0][7]][0],bg=w[z[0][7]][1])
        btn08c.config(text=w[z[0][8]][0],bg=w[z[0][8]][1])

        btn10c.config(text=w[z[1][0]][0],bg=w[z[1][0]][1])
        btn11c.config(text=w[z[1][1]][0],bg=w[z[1][1]][1])
        btn12c.config(text=w[z[1][2]][0],bg=w[z[1][2]][1])
        btn13c.config(text=w[z[1][3]][0],bg=w[z[1][3]][1])
        btn14c.config(text=w[z[1][4]][0],bg=w[z[1][4]][1])
        btn15c.config(text=w[z[1][5]][0],bg=w[z[1][5]][1])
        btn16c.config(text=w[z[1][6]][0],bg=w[z[1][6]][1])
        btn17c.config(text=w[z[1][7]][0],bg=w[z[1][7]][1])
        btn18c.config(text=w[z[1][8]][0],bg=w[z[1][8]][1])

        btn20c.config(text=w[z[2][0]][0],bg=w[z[2][0]][1])
        btn21c.config(text=w[z[2][1]][0],bg=w[z[2][1]][1])
        btn22c.config(text=w[z[2][2]][0],bg=w[z[2][2]][1])
        btn23c.config(text=w[z[2][3]][0],bg=w[z[2][3]][1])
        btn24c.config(text=w[z[2][4]][0],bg=w[z[2][4]][1])
        btn25c.config(text=w[z[2][5]][0],bg=w[z[2][5]][1])
        btn26c.config(text=w[z[2][6]][0],bg=w[z[2][6]][1])
        btn27c.config(text=w[z[2][7]][0],bg=w[z[2][7]][1])
        btn28c.config(text=w[z[2][8]][0],bg=w[z[2][8]][1])

        btn30c.config(text=w[z[3][0]][0],bg=w[z[3][0]][1])
        btn31c.config(text=w[z[3][1]][0],bg=w[z[3][1]][1])
        btn32c.config(text=w[z[3][2]][0],bg=w[z[3][2]][1])
        btn33c.config(text=w[z[3][3]][0],bg=w[z[3][3]][1])
        btn34c.config(text=w[z[3][4]][0],bg=w[z[3][4]][1])
        btn35c.config(text=w[z[3][5]][0],bg=w[z[3][5]][1])
        btn36c.config(text=w[z[3][6]][0],bg=w[z[3][6]][1])
        btn37c.config(text=w[z[3][7]][0],bg=w[z[3][7]][1])
        btn38c.config(text=w[z[3][8]][0],bg=w[z[3][8]][1])

        btn40c.config(text=w[z[4][0]][0],bg=w[z[4][0]][1])
        btn41c.config(text=w[z[4][1]][0],bg=w[z[4][1]][1])
        btn42c.config(text=w[z[4][2]][0],bg=w[z[4][2]][1])
        btn43c.config(text=w[z[4][3]][0],bg=w[z[4][3]][1])
        btn44c.config(text=w[z[4][4]][0],bg=w[z[4][4]][1])
        btn45c.config(text=w[z[4][5]][0],bg=w[z[4][5]][1])
        btn46c.config(text=w[z[4][6]][0],bg=w[z[4][6]][1])
        btn47c.config(text=w[z[4][7]][0],bg=w[z[4][7]][1])
        btn48c.config(text=w[z[4][8]][0],bg=w[z[4][8]][1])

        btn50c.config(text=w[z[5][0]][0],bg=w[z[5][0]][1])
        btn51c.config(text=w[z[5][1]][0],bg=w[z[5][1]][1])
        btn52c.config(text=w[z[5][2]][0],bg=w[z[5][2]][1])
        btn53c.config(text=w[z[5][3]][0],bg=w[z[5][3]][1])
        btn54c.config(text=w[z[5][4]][0],bg=w[z[5][4]][1])
        btn55c.config(text=w[z[5][5]][0],bg=w[z[5][5]][1])
        btn56c.config(text=w[z[5][6]][0],bg=w[z[5][6]][1])
        btn57c.config(text=w[z[5][7]][0],bg=w[z[5][7]][1])
        btn58c.config(text=w[z[5][8]][0],bg=w[z[5][8]][1])

        btn60c.config(text=w[z[6][0]][0],bg=w[z[6][0]][1])
        btn61c.config(text=w[z[6][1]][0],bg=w[z[6][1]][1])
        btn62c.config(text=w[z[6][2]][0],bg=w[z[6][2]][1])
        btn63c.config(text=w[z[6][3]][0],bg=w[z[6][3]][1])
        btn64c.config(text=w[z[6][4]][0],bg=w[z[6][4]][1])
        btn65c.config(text=w[z[6][5]][0],bg=w[z[6][5]][1])
        btn66c.config(text=w[z[6][6]][0],bg=w[z[6][6]][1])
        btn67c.config(text=w[z[6][7]][0],bg=w[z[6][7]][1])
        btn68c.config(text=w[z[6][8]][0],bg=w[z[6][8]][1])

        btn70c.config(text=w[z[7][0]][0],bg=w[z[7][0]][1])
        btn71c.config(text=w[z[7][1]][0],bg=w[z[7][1]][1])
        btn72c.config(text=w[z[7][2]][0],bg=w[z[7][2]][1])
        btn73c.config(text=w[z[7][3]][0],bg=w[z[7][3]][1])
        btn74c.config(text=w[z[7][4]][0],bg=w[z[7][4]][1])
        btn75c.config(text=w[z[7][5]][0],bg=w[z[7][5]][1])
        btn76c.config(text=w[z[7][6]][0],bg=w[z[7][6]][1])
        btn77c.config(text=w[z[7][7]][0],bg=w[z[7][7]][1])
        btn78c.config(text=w[z[7][8]][0],bg=w[z[7][8]][1])

        btn80c.config(text=w[z[8][0]][0],bg=w[z[8][0]][1])
        btn81c.config(text=w[z[8][1]][0],bg=w[z[8][1]][1])
        btn82c.config(text=w[z[8][2]][0],bg=w[z[8][2]][1])
        btn83c.config(text=w[z[8][3]][0],bg=w[z[8][3]][1])
        btn84c.config(text=w[z[8][4]][0],bg=w[z[8][4]][1])
        btn85c.config(text=w[z[8][5]][0],bg=w[z[8][5]][1])
        btn86c.config(text=w[z[8][6]][0],bg=w[z[8][6]][1])
        btn87c.config(text=w[z[8][7]][0],bg=w[z[8][7]][1])
        btn88c.config(text=w[z[8][8]][0],bg=w[z[8][8]][1])
    except:
         messagebox.showinfo(title="Aviso",parent=jugar,message="Indice no valido. Introduzca el indice en la caja de texto donde esta el numeral")
        
def guardar():
    try:
        indice=int(entry_partida.get())
        a=leerpartidasudoku()
        nivel=leerconfigsudoku()["nivel"]
        if nivel=="facil":
            nivel=0
        elif nivel=="medio":
            nivel=1
        elif nivel=="dificil":
            nivel=2
        f= open('sudoku2016partidas.dat', 'wb')
        a[nivel][indice]=partidacosas
        pickle.dump(a, f)
        messagebox.showinfo(title="Aviso",parent=jugar,message="Partida se ha guardado con exito")
    except:
        messagebox.showinfo(title="Aviso",parent=jugar,message="Indice no valido. Introduzca el indice en la caja de texto donde esta el numeral")
        
    
        
        
principal.mainloop()

