import requests
import json

syote = input("Paina mitä tahansa näppäintä saadaksesi Chuck Norris -vitsin tai 0 lopettaaksesi: ")

while syote != "0":
    pyynto = "https://api.chucknorris.io/jokes/random"
    vastaus = requests.get(pyynto).json()
    dict = json.dumps(vastaus, indent=2)

    print(vastaus["value"])

    syote = input("Paina mitä tahansa näppäintä saadaksesi Chuck Norris -vitsin tai ENTER lopettaaksesi: ")

