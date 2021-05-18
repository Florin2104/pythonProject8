#Am dat import la librariile folosite pentru a realiza un url care urmareste sablonul de la youtube.
import webbrowser
import re
import urllib.request

#Am urmarit sablonul de la youtube pentru a crea un url bazat pe un anumit text.
def playonyt(text):
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + text.replace("play",'').replace(" ",''))
    #Am cautat ' watch\?v=(\S{11}) ' si am decodatat textul .
    video_ids = re.findall(r"watch\?v=(\S{11})",html.read().decode())
    #Am creat noul url folosind 'video_ids[0]' pentru a accesa primul rezultat gasit pe youtube.
    video_url = "https://www.youtube.com/watch?v=" + video_ids[0]
    #Am dat open la url-ul finalizat.
    webbrowser.open(video_url)
