import network # import des fonctions liées au wifi
import urequests # import des fonctions liées aux requettes http
import utime # import des fonctions liées au temps 
import ujson # import des fonctions liées à la conversion en json

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client
wlan.active(True) # active le mode client wifi

ssid = "IIM_Private"
password = "Creative_Lab_2023"
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "http://date.jsontest.com/"

while(True):
    try:
        print("GET")
        r = urequests.get(url) # lance une requete sur l'url
        print(r.json()) # traite sa reponse en Json
        r.close() #ferme la demande
        utime.sleep(1)
    except Exception as e:
        print (e)