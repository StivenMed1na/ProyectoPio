# -*- coding: utf-8 -*-
"""Funciones&Procedimientos.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1c3cY16ZcBvaws0bwUdk2StfWJS3c53SY

##Funcion
Es un bloque que al realizar una tarea especifica y devuelve (return) un resultado. Se utilizan en tareas respetitivas.

##Procedimiento

Es similar a una funcion pero No devuelve un valor.
"""

def sumaDosNumeros(num1, num2):
  return num1 + num2

#Llamada a la funcion

print("la suma es: ", sumaDosNumeros(4,5))

#Pidanle al usuario los numeros

numero1 = int(input("Ingrese el primer numero: "))

numero2 = int(input("Ingrese el segundo numero: "))

print(f"La suma de los numeros {numero1} y {numero2} es ", sumaDosNumeros(numero1, numero2))

def saludar(nombre):
  print("Hola ", nombre, "Bienvenido a mi codigo")

  saludar("Camila")

#Pidanle el nombre al usuario

nombreUsuario= int(input("Ingrese su nombre: "))

#Mini calculadora

def sumar(num1, num2):
  return num1 + num2

def resta(num1, num2):
  return num1 - num2

def multi(num1, num2):
  return num1*num2

def dividir(num1, num2):
  return num1/num2


num1= 20
num2= 15

print("Suma: ", sumar(num1, num2))

#def calculadora (operador, num1, num2):


#Pidanle los numeros al usuario

numero1 = int(input("Ingrese el primer numero: "))

numero2 = int(input("Ingrese el segundo numero: "))