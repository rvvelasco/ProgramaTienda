from tkinter import *
from tkinter import ttk
import mysql.connector



root=Tk()   

def ingresar():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tienda",
     )

    mycursor = mydb.cursor()
    nombre = nombreEntry.get()
    codigo = codigoEntry.get()
    precio = precioEntry.get()
    cantidad = cantidadEntry.get()
    sql = "INSERT INTO productos (codigo,nombre,precio,cantidad) VALUES (%s, %s, %s, %s)"
    val = (codigo,nombre,precio,cantidad)
    mycursor.execute(sql, val)
    mydb.commit()
    mycursor.close()

def Buscar():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tienda"
    )

    mycursor = mydb.cursor()
    codigobuscado = buscarCodEntry.get()
    mycursor.execute("SELECT * FROM productos WHERE codigo =  '"+codigobuscado+"'")

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    mycursor.close
        
root.title("Titulo del programa")
root.minsize(500,400)
root.wm_iconbitmap("")

    
    
tituloLbl=Label(root,text="Nombre de la tienda")
tituloLblFont=('times',20,'bold')
tituloLbl.config(font=tituloLblFont)
tituloLbl.grid(column=3,row=0)

#labels 

ingresarLbl=Label(text="Ingresar producto: ")
ingresarLblFont=('times',15,'bold')
ingresarLbl.config(font=ingresarLbl)
ingresarLbl.grid(column=2,row=1)

codigoLbl=Label(text="Código: ")
codigoLbl.grid(column=2,row=5)

nombreLbl=Label(text="Nombre: ")
nombreLbl.grid(column=2,row=6)

precioLbl=Label(text="Precio: ")
precioLbl.grid(column=2,row=7)

cantidadLbl=Label(text="Cantidad: ")
cantidadLbl.grid(column=2,row=8)

buscarLbl=Label(text="buscar: ")
buscarLblFont=('times',15,'bold')
buscarLbl.config(font=buscarLbl)
buscarLbl.grid(column=2,row=10)

ingresaCodlbl=Label(text="ingresa codigo del producto")
ingresaCodlbl.grid(column=2,row=11)

#entry
        
codigoEntry=Entry()
codigoEntry.grid(column=3,row=5)

nombreEntry=Entry()
nombreEntry.grid(column=3,row=6)
        
precioEntry=Entry()
precioEntry.grid(column=3,row=7)

cantidadEntry=Entry()
cantidadEntry.grid(column=3,row=8) 

buscarCodEntry=Entry()
buscarCodEntry.grid(column=3,row=11)
        
ingresarBtn=Button(text="Ingresar",command=ingresar)
ingresarBtn.grid(column=4,row=8) 

buscarbtn=Button(text="buscar",command=Buscar)
buscarbtn.grid(column=4,row=11)




 

       

    



   

    



root=root()
root.mainloop()
