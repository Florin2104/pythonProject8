"""
Resurse folosite:
https://stackoverflow.com/questions/19377262/regex-for-youtube-url
https://pypi.org/project/pywhatkit/
"""
#Am dat import la libraria pywhatkit
import pywhatkit as kit
from Functii import playonyt


print("Mesaj pe whatsapp:1\nInformatii despre o tema:2\nCautare pe google:3\nDati play pe youtube:4")
decizie = input("Ce doriti sa faceti?")
#Am creat un if ca programul sa urmeze o anumita ramura in functie de decizia utilizatorului.
if decizie =='1':
    #Am folosit niste variabile ca sa stochez parametrii necesari functiei sendwhatmsg
    numar = input("Formati numarul la care doriti sa trimiteti mesaj:")
    mesaj = input("Mesajul pe care doriti sa il trimiteti:")
    ora = int(input("Scrieti ora la care doriti sa trimiteti mesajul:"))
    minut = int(input("Scrieti minutul la care doriti sa trimiteti mesajul: "))
    kit.sendwhatmsg(numar, mesaj, ora, minut)
elif decizie=='2':
    #Am folosit niste variabile ca sa stochez parametrii necesari functiei info
    infomartie = input("Scrieti despre ce doriti sa aflati informatii:")
    linii = int(input("Cate linii de cod doriti sa afiseze:"))
    kit.info(infomartie, linii)
elif decizie=='3':
    #Am folosit o variabila ca sa stochez un parametru necesar functiei search
    cautare_google = input("Scrieti ce doriti sa cautati pe google:")
    kit.search(cautare_google)
elif decizie=='4':
    #Am apelat functia playonyt folosind o variabila citita de la tastatura.
    youtube=input("Scrieti ce doriti sa urmariti pe youtube:")
    playonyt(youtube)

