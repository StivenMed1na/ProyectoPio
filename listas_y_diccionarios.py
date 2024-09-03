# -*- coding: utf-8 -*-
"""Listas y Diccionarios.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LQ5jPtapXjZjoIeF-fvvE7KbgApzCUgw

Es una coleccion ordenada
Manzanas, Peras,Leche,Carne,Pollo
Diccionarios-Objetos

Es una coleccion de datos desordenada almacenada con clave-valor.
clave valor paula ej : 3014567898 Pedro:3105678998 Stiven: 3155874569
"""

#Lista

frutas=["Manzana","Pera","Naranja"]
print(frutas[1])#Acceder a un elemento de la lista

frutas[2]="Fresas"#Modificar un elemento de la lista
print(frutas[2])

print(*frutas) #Muestra toda la lista de fruta. * quita los simbolos de la lista

frutas.append("Uva") #append() me permite agregar un elemento a lista , en la ultima posicion

print(*frutas)

frutas.pop(0)#Elimina el ultimo elemento de la lista, o agregando la posicion
print(*frutas)

frutas.remove("Pera")#Elimina un elemento en especifico
print(*frutas)

print(len(frutas))#Longitud de la lista

#Diccionarios

contactos={
    "Pedro":"319-532-4706",
    "Paula":"315-547-4811", #Clave --- Valor
    "Stiven": "319-371-5618",
}

print("El contacto de pedro es: ",contactos["Pedro"]) #Llamo un elemento por medio de su clave

contactos["Camila"]="310-567-7458" #AGREGANDO UN NUEVO CONTACTO AL DICCIONARIO , si ya existe la clave , se sobreescribe el numero de telefono o si no existe se agrega una nueva
print(contactos)

del contactos["Pedro"]#Eliminar un contacto(clave)
print(contactos)

contactos={
    "Sofia": {
    "Telefono": ["312-500-8854", 313696465],
    "Correo": ["sofia2001@gmai1.com","sofia2@gmail.com","sofia3@gmail.com"],
    "Direccion": {
       "Calle": "calle 24N",
       "Barrio": "San vicente",
       "Ciudad": "Popayan"
    }
},
    "Stiven":{
    "Telefono": ["3105472862", "3008563274", "3195324706"],
    "Correo": "stiven2007@gmail.com",
    "Direccion":{
        "Calle": "Calle 40Oeste",
        "Barrio": "Terror",
        "Ciudad": "Cali"
        }
 }
}
print(contactos)


contactos["Tatiana"]={
    "telefono":["315-425-7896", "350-896-1140"],
    "correo":"tatiana@gmail.com"

}


print(contactos)
print(*contactos)

print("El contacto de Stiven es: ", contactos["Stiven"]["Telefono"])

print("El segundo telefono de Tatiana es: ", contactos["Tatiana"]["telefono"][1])

print("La ciudad de Stiven es: ", contactos["Stiven"]["Direccion"]["Ciudad"])

telefonosStiven= contactos["Stiven"]["Telefono"]

#for telefono in telefonosStiven:
#for i, telefono in enumerate(telefonosStiven, start =1):
    #print(f"Telefonos {i}", telefono)

correoSofia=contactos["Sofia"]["Correo"]
print(correoSofia)

for i, correo in enumerate(correoSofia, start =1):
    print(f"Correo {i}", correo)