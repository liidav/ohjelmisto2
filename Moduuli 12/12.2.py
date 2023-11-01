import requests

syote = input("Anna kaupunki: ")

pyynto = f"https://api.openweathermap.org/data/2.5/weather?q={syote}&APPID={APPID}"
vastaus = requests.get(pyynto).json()

lampotila_c = vastaus["main"]["temp"] - 273.15

kuvaus = ""

for x in range (0, len(vastaus["weather"])):
    for tulos in vastaus["weather"][x]["description"]:
        kuvaus = f"{kuvaus}{tulos}"
    kuvaus = f"{kuvaus} "

print(f"Lämpötila: {lampotila_c:.1f} °C\nKuvaus säätilasta: {kuvaus}")

