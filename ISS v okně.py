"Zeměpišná šířka a délka ISS(vesmírná stanice)"

# http://api.open-notify.org/iss-now.json

# Request (žádost)
# Response (odpověd)¨

# Chyby
# 1xx = Ještě není konec
# 2xx = vše ok, tady máš data
# 3xx = přesměrovávání 
# 4xx = chyba na straně uživatele
# 5xx = chyba na straně poskytovatele

import requests
from tkinter import *

# Okno 
window = Tk()
window.minsize(700, 400)
window.resizable(False, False)
window.title("ISS - aplikace ukazuje aktuální polohu mezinárodní vesmírné stanice")
window.iconbitmap("C:/Users/tslac/OneDrive/Plocha/Projekty/API základy/Poloha-ISS-s-API/iss.ico")

# Funkce 
def iss_coordinates():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status() # pokud je chyba, detailněji popíše chybu !!
    data = response.json()
    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    longitude_label.config(text=f"Zeměpisná délka ISS je: {longitude}")
    latitude_label.config(text=f"Zeměpisná šířka ISS je: {latitude}")

# Obrázek - Vytvoření canvasu
canvas = Canvas(window, width=500, height=280,)
canvas.pack()
iss_img = PhotoImage(file="C:/Users/tslac/OneDrive/Plocha/Projekty/API základy/Poloha-ISS-s-API/gif.gif")
canvas.create_image(0, 0, image=iss_img, anchor= "nw")

# Tlačítko ve Frame 
coordinates_frame = Frame(window)
coordinates_frame.pack()

recount_button = Button(coordinates_frame, text="Současné souřadnice ISS", command=iss_coordinates)
recount_button.pack()

# Labels 
latitude_label = Label()
latitude_label.pack()

longitude_label = Label()
longitude_label.pack()

# Hlavní okno 
window.mainloop()