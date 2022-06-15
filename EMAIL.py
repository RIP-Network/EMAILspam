#!/usr/bin/python3

import sys, os, webbrowser, platform, subprocess, time
from colorama import Fore
from importlib_metadata import version

#colores
negro = '\033[30m'
rojo = '\033[31m'
verde = '\033[32m'
amarillo = '\033[33m'
azul = '\033[34m'
rosado = '\033[35m'
calipso= '\033[36m'
blanco = '\033[37m'
cierre = '\033[39m'

#Banner 

banner = Fore.RED + """…………..$……………………………………..$…………..
…………$$……………………………………..$$…………
…………$$……………………………………..$$…………
…………..$$s………………………………s$$…………..
…………….$$$$……………………….$$$$…………….
………………³$$$$..¶¶¶¶¶¶¶¶..$$$$³………………
………………..³$$$$..¶¶¶¶¶¶..$$$$³………………..
………………¶..$$$$$..¶¶¶¶..$$$$$..¶………………
…………….¶¶¶..$$$..¶¶¶¶¶¶..$$$..¶¶………………
…………….¶¶¶….¶¶¶¶¶¶¶¶¶¶….¶¶¶¶………………
…………….¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶………………
………………..¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶………………..
………………..¶¶……..¶¶¶¶……….¶……………………
………………..¶¶……..¶¶¶¶……….¶¶………………….
………………..¶¶¶¶¶¶¶¶..¶¶¶¶¶¶¶¶………………….
………………….¶¶¶¶¶¶……¶¶¶¶¶¶¶………………….
……………………….¶¶¶¶¶¶¶¶¶…………………………
……………………….¶..¶..¶..¶..¶…………………………
…………¶…………..¶…………..¶…………..¶…………..
……….¶¶……………………………………….¶¶…………
……….¶¶……………………………………….¶¶…………
……….¶¶…………..¶¶……….¶¶…………..¶¶…………
……….¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶…………
……¶..¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶..¶……..
….¶¶..¶¶..¶¶..¶¶..¶…………..¶..¶¶..¶¶..¶¶..¶¶……
……¶¶¶¶..¶¶..¶¶………………….¶¶..¶¶..¶¶¶¶……..
"""


print(banner)
print(Fore.GREEN + "              RIP-Network")
print("                 V1.0")
time.sleep(3)
os.system('clear')


def menu():
    while True:
     print(Fore.GREEN + "Opciones\n")        
     print("1) Spam-EMAIL                             RIP-Network                             ")                    
     print("2) Instalar requisitos                  Version 1.0                                     ")
     print("3) Version ")
     print("4) Comunicarte conmigo")
     print("5) Como usar ")
     print("99)Salir")

     d = input(Fore.LIGHTBLUE_EX + "Elige una opcion --> ")

     if d == "1":
        print ("Por favor espere ")
        print ("Nota : No te canses de aprender ")
        webbrowser.open('https://es.pornhub.com/signup')
        time.sleep(2)
        webbrowser.open('https://www.xvideos.com/account')
        time.sleep(2)
        webbrowser.open('https://www.xnxx.com/mobile/login')
        time.sleep(2)
        webbrowser.open('https://signup.fantasyhd.com/?')
        time.sleep(2)
        webbrowser.open('https://signup.exotic4k.com/?')
        time.sleep(2)
        webbrowser.open('https://startwithheartvideos.com/subscriber-account/checkout/?level=10')
        time.sleep(2)
        webbrowser.open('https://www.youx.xxx/register/')
        time.sleep(2)
        webbrowser.open('https://es.xhamster.com/signup?source=menuSignup')
        time.sleep(2)
        webbrowser.open('https://hentaila.com/registro')
        time.sleep(2)
        

     if d == "2":
        print("Vuelva atras del programa y ejecute en la terminal bash install.sh")

     if d == "3":
         print("version 1.0 by RIP-Network")
    

     elif d == "4":
        print("No disponible actualmente pero me puedes seguir en Youtube ;)")
        time.sleep(8)


     elif d == "5":
        print(rojo+"Cuando se habran las paginas deveras poner el correo de la victima en las casillas que te ponga el correo , esta herramienta es muy simple pero peligrosa , la estare actualizando en poco tiempo , gracias por usarla y espero le des una estrella en mi github y te suscribas a mi canal :)"+cierre)

      
     elif d == "99":
         break

     input("Presiona enter para volver como antes")
     os.system('clear')
menu()
