import datetime
from datetime import datetime
import random
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkcalendar import Calendar
from tkinter import messagebox
from tkinter import Radiobutton
import babel.numbers
import requests
import json
import secrets
import string
import time
import qrcode
import pywintypes
from tkinter import filedialog
import os


godziny = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
           "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
minuty = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24",
          "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59"]
diet_zagranica = {"Afganistan": ["EUR", 47, 140], "Albania": ["EUR", 41, 120], "Algieria": ["EUR", 50, 200], "Andora": ["EUR", 50, 200], "Angola": ["USD", 61, 180], "Arabia Saudyjska": ["EUR", 50, 200], "Argentyna": ["USD", 50, 150],
                  "Armenia": ["EUR", 42, 145],	"Australia": ["AUD", 95, 270], "Austria": ["EUR", 57, 150], "Azerbejdżan": ["EUR", 43, 150], "Bangladesz": ["USD", 50, 120], "Belgia": ["EUR", 55, 200], "Białoruś": ["EUR", 42, 130],
                  "Bośnia i Hercegowina": ["EUR", 41, 100], "Brazylia": ["EUR", 43, 120], "Bułgaria": ["EUR", 40, 120], "Chile": ["USD", 60, 120], "Chiny": ["EUR", 55, 170], "Chorwacja": ["EUR", 42, 125], "Cypr": ["EUR", 43, 160],
                  "Czechy": ["EUR", 41, 120], "Dania": ["DKK", 446, 1430], "Egipt": ["USD", 55, 150], "Ekwador": ["USD", 44, 110], "Estonia": ["EUR", 45, 110], "Etiopia": ["USD", 55, 300], "Finlandia": ["EUR", 53, 180], "Francja": ["EUR", 55, 200],
                  "Gibraltar": ["GBP", 45, 220], "Grecja": ["EUR", 50, 160], "Gruzja": ["EUR", 48, 160], "Hiszpania": ["EUR", 50, 200], "Hongkong": ["USD", 55, 250], "Indie": ["EUR", 42, 210], "Indonezja": ["EUR", 41, 110], "Irak": ["USD", 60, 120],
                  "Iran": ["EUR", 41, 95], "Irlandia": ["EUR", 52, 160], "Islandia": ["EUR", 56, 160], "Izrael": ["EUR", 70, 200], "Japonia": ["JPY", 7532, 22000], "Jemen": ["USD", 48, 160], "Jordania": ["EUR", 50, 130], "Kambodża": ["USD", 45, 100],
                  "Kanada": ["CAD", 71, 190], "Katar": ["EUR", 41, 200], "Kazachstan": ["EUR", 45, 155], "Kenia": ["EUR", 41, 150], "Kirgistan": ["USD", 41, 150], "Kolumbia": ["USD", 49, 120], "Kongo": ["USD", 66, 220], "Korea Południowa": ["EUR", 46, 170],
                  "Korea Północna": ["EUR", 48, 170], "Kostaryka": ["USD", 50, 140], "Kuba": ["EUR", 50, 140], "Kuwejt": ["EUR", 39, 200], "Laos": ["USD", 54, 100], "Liban": ["USD", 57, 150], "Libia": ["EUR", 52, 100], "Liechtenstein": ["CHF", 88, 220],
                  "Litwa": ["EUR", 45, 150], "Luksemburg": ["EUR", 55, 200], "Łotwa": ["EUR", 57, 132], "Macedonia": ["EUR", 43, 138], "Malezja": ["EUR", 41, 140], "Malta": ["EUR", 43, 180], "Maroko": ["EUR", 41, 130], "Meksyk": ["USD", 58, 154],
                  "Mołdawia": ["EUR", 45, 94], "Monako": ["EUR", 55, 200], "Mongolia": ["EUR", 45, 154], "Niderlandy": ["EUR", 50, 150], "Niemcy": ["EUR", 49, 170], "Nigeria": ["EUR", 46, 240], "Norwegia": ["NOK", 496, 1650],
                  "Nowa Zelandia": ["USD", 58, 180], "Oman": ["EUR", 40, 240], "Pakistan": ["EUR", 38, 200], "Palestyna": ["EUR", 70, 200], "Panama": ["USD", 52, 140], "Państwo spoza listy": ["EUR", 41, 140], "Peru": ["USD", 50, 150],
                  "Portugalia": ["EUR", 49, 150], "Republika Południowej Afryki": ["USD", 52, 275], "Rosja": ["EUR", 48, 200], "Rumunia": ["EUR", 42, 110], "San Marino": ["EUR", 53, 192], "Senegal": ["EUR", 44, 120],
                  "Serbia i Czarnogóra": ["EUR", 40, 110], "Singapur": ["USD", 56, 230], "Słowacja": ["EUR", 47, 132], "Słowenia": ["EUR", 45, 143], "Stany Zjednoczone Ameryki": ["USD", 59, 200], "Syria": ["USD", 50, 150],
                  "Szwajcaria": ["CHF", 88, 220], "Szwecja": ["SEK", 510, 2000], "Tadżykistan": ["EUR", 41, 140], "Tajlandia": ["USD", 42, 110], "Tajwan": ["EUR", 40, 142], "Tanzania": ["USD", 53, 150], "Tunezja": ["EUR", 37, 100],
                  "Turcja": ["USD", 53, 185], "Turkmenistan": ["EUR", 47, 90], "Ukraina": ["EUR", 41, 180], "Urugwaj": ["USD", 50, 80], "Uzbekistan": ["EUR", 41, 140], "Watykan": ["EUR", 53, 192], "Wenezuela": ["USD", 60, 220],
                  "Węgry": ["EUR", 44, 143], "Wielka Brytania": ["GBP", 45, 220], "Wietnam": ["USD", 53, 160], "Włochy": ["EUR", 53, 192], "Wybrzeże Kości Słoniowej": ["EUR", 33, 100], "Zimbabwe": ["EUR", 39, 90], "Zjednoczone Emiraty Arabskie": ["EUR", 43, 220]}
zagranica_odmiana = {"Afganistan": "w Afganistanie", "Albania": "w Albanii", "Algieria": "w Algierii", "Andora": "w Andorze", "Angola": "w Angoli", "Arabia Saudyjska": "w Arabii Saudyjskiej", "Argentyna": "w Argentynie",
                     "Armenia": "w Armenii", "Australia": "w Australii", "Austria": "w Austrii", "Azerbejdżan": "w Azerbejdżanie", "Bangladesz": "w Bangladeszu", "Belgia": "w Belgii", "Białoruś": "na Białorusi",
                     "Bośnia i Hercegowina": "w BiH", "Brazylia": "w Brazylii", "Bułgaria": "w Bułgarii", "Chile": "w Chile", "Chiny": "w Chinach", "Chorwacja": "w Chorwacji", "Cypr": "na Cyprze",
                     "Czechy": "w Czechach", "Dania": "w Danii", "Egipt": "w Egipcie", "Ekwador": "w Ekwadorze", "Estonia": "w Estonii", "Etiopia": "w Etiopii", "Finlandia": "w Finlandii", "Francja": "we Francji",
                     "Gibraltar": "na Gibraltarze", "Grecja": "w Grecji", "Gruzja": "w Gruzji", "Hiszpania": "w Hiszpanii", "Hongkong": "w Hongkongu", "Indie": "w Indiach", "Indonezja": "w Indonezji", "Irak": "w Iraku",
                     "Iran": "w Iranie", "Irlandia": "w Irlandii", "Islandia": "na Islandii", "Izrael": "w Izraelu", "Japonia": "w Japonii", "Jemen": "w Jemenie", "Jordania": "w Jordanii", "Kambodża": "w Kambodży",
                     "Kanada": "w Kanadzie", "Katar": "w Katarze", "Kazachstan": "w Kazachstanie", "Kenia": "w Kenii", "Kirgistan": "w Kirgistanie", "Kolumbia": "w Kolumbii", "Kongo": "w Kongu", "Korea Południowa": "w Korei Południowej",
                     "Korea Północna": "w Korei Północnej", "Kostaryka": "na Kostaryce", "Kuba": "na Kubie", "Kuwejt": "w Kuwejcie", "Laos": "w Laosie", "Liban": "w Libanie", "Libia": "w Libii", "Liechtenstein": "w Liechtensteinie",
                     "Litwa": "na Litwie", "Luksemburg": "w Luksemburgu", "Łotwa": "na Łotwie", "Macedonia": "w Macedonii", "Malezja": "w Malezji", "Malta": "na Malcie", "Maroko": "w Maroku", "Meksyk": "w Meksyku",
                     "Mołdawia": "w Mołdawii", "Monako": "w Monako", "Mongolia": "w Mongolii", "Niderlandy": "w Niderlandach", "Niemcy": "w Niemczech", "Nigeria": "w Nigerii", "Norwegia": "w Norwegii",
                     "Nowa Zelandia": "w Nowej Zelandii", "Oman": "w Omanie", "Pakistan": "w Pakistanie", "Palestyna": "w Palestynie", "Panama": "w Panamie", "Państwo spoza listy": "w dzikim kraju", "Peru": "w Peru",
                     "Portugalia": "w Portugalii", "Republika Południowej Afryki": "w RPA", "Rosja": "w Rosji", "Rumunia": "w Rumunii", "San Marino": "w San Marino", "Senegal": "w Senegalu",
                     "Serbia i Czarnogóra": "w Serbii i Czarnogórze", "Singapur": "w Singapurze", "Słowacja": "na Słowacji", "Słowenia": "w Słowenii", "Stany Zjednoczone Ameryki": "w USA", "Syria": "w Syrii",
                     "Szwajcaria": "w Szwajcarii", "Szwecja": "w Szwecji", "Tadżykistan": "w Tadżykistanie", "Tajlandia": "w Tajlandii", "Tajwan": "na Tajwanie", "Tanzania": "w Tanzanii", "Tunezja": "w Tunezji",
                     "Turcja": "w Turcji", "Turkmenistan": "w Turkmenistanie", "Ukraina": "na Ukrainie", "Urugwaj": "w Urugwaju", "Uzbekistan": "w Uzbekistanie", "Watykan": "w Watykanie", "Wenezuela": "w Wenezueli",
                     "Węgry": "na Węgrzech", "Wielka Brytania": "w Wielkiej Brytanii", "Wietnam": "w Wietnamie", "Włochy": "we Włoszech", "Wybrzeże Kości Słoniowej": "w Wybrzeżu Kości Słoniowej", "Zimbabwe": "w Zimbabwe", "Zjednoczone Emiraty Arabskie": "w ZEA"}
tabela_nbp = {"dolar amerykański [USD]": "USD", "dolar australijski [AUD]": "AUD", "dolar kanadyjski [CAD]": "CAD", "euro [EUR]": "EUR",
              "forint [HUF]": "HUF", "frank szwajcarski [CHF]": "CHF", "funt szterling [GBP]": "GBP", "hrywna [UAH]": "UAH", "jen [JPY]": "JPY",
              "korona czeska [CZK]": "CZK", "korona duńska [DKK]": "DKK", "korona islandzka [ISK]": "ISK", "korona norweska [NOK]": "NOK",
              "korona szwedzka [SEK]": "SEK", "lej rumuński [RON]": "RON", "lira turecka [TRY]": "TRY", "szekel [ILS]": "ILS",
              "dirham ZEA [AED]": "AED", "rubel białoruski [BYN]": "BYN", "rubel rosyjski [RUB]": "RUB"}
options = ["dolar amerykański [USD]", "dolar australijski [AUD]", "dolar kanadyjski [CAD]", "euro [EUR]",
           "forint [HUF]", "frank szwajcarski [CHF]", "funt szterling [GBP]", "hrywna [UAH]", "jen [JPY]",
           "korona czeska [CZK]", "korona duńska [DKK]", "korona islandzka [ISK]", "korona norweska [NOK]",
           "korona szwedzka [SEK]", "lej rumuński [RON]", "lira turecka [TRY]", "szekel [ILS]",
           "dirham ZEA [AED]", "rubel białoruski [BYN]", "rubel rosyjski [RUB]"]


class MenuApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("B130N by Śliwka")
         
        self.button1 = tk.Button(
            self, text="DIETY\n KRAJOWE", command=self.open_diety_krajowe, width=15, height=5)
        self.button1.grid(row=1, column=0, padx=2, pady=2)

        self.button2 = tk.Button(self, text="DIETY\n ZAGRANICZNE",
                                 command=self.open_diety_zagraniczne, width=15, height=5)
        self.button2.grid(row=1, column=2, padx=2, pady=2)

        self.button3 = tk.Button(
            self, text="PESEL", command=self.open_pesel, width=15, height=5)
        self.button3.grid(row=0, column=2, padx=2, pady=2)

        self.button4 = tk.Button(self, text="KALKULATOR\n WALUT",
                                 command=self.open_kalkulator_walut, width=15, height=5)
        self.button4.grid(row=0, column=0, padx=2, pady=2)

        self.button5 = tk.Button(self, text="GENERATOR\n HASEŁ",
                                 command=self.open_generator_hasel, width=15, height=5)
        self.button5.grid(row=2, column=1, padx=2, pady=2)

        self.button6 = tk.Button(self, text="TRANSLITERACJA", command=self.open_transliteracja, width=15, height=5)
        self.button6.grid(row=0, column=1, padx=2, pady=2)

        self.button7 = tk.Button(self, text="KODY QR",
                                 command=self.open_kodyqr, width=15, height=5)
        self.button7.grid(row=2, column=0, padx=2, pady=2)
        
        self.button8 = tk.Button(self, text="POGODA IMGW", command=self.open_pogoda, width=15, height=5)
        self.button8.grid(row=1, column=1, padx=2, pady=2)

        self.button9 = tk.Button(
            self, text="TABLICE\n REJESTRACYJNE", command=self.open_tablice, width=15, height=5)
        self.button9.grid(row=2, column=2, padx=2, pady=2)

        self.current_app = None

    def open_diety_krajowe(self):
        self.hide_menu()
        if self.current_app:
            self.current_app.destroy()
        app1 = DietyKrajowe(self)
        app1.grid()
        self.current_app = app1

    def open_diety_zagraniczne(self):
        self.hide_menu()
        if self.current_app:
            self.current_app.destroy()
        app2 = DietyZagraniczne(self)
        app2.grid()
        self.current_app = app2

    def open_pesel(self):
        self.hide_menu()
        if self.current_app:
            self.current_app.destroy()
        app3 = PESEL(self)
        app3.grid()
        self.current_app = app3

    def open_kalkulator_walut(self):
        self.hide_menu()
        if self.current_app:
            self.current_app.destroy()
        app4 = KalkulatorWalut(self)
        app4.grid()
        self.current_app = app4

    def open_generator_hasel(self):
        self.hide_menu()
        if self.current_app:
            self.current_app.destroy()
        app5 = GeneratorHasel(self)
        app5.grid()
        self.current_app = app5

    def open_transliteracja(self):
        self.hide_menu()
        if self.current_app:
            self.current_app.destroy()
        app6 = Transliteracja(self)
        app6.grid()
        self.current_app = app6

    def open_kodyqr(self):
        self.hide_menu()
        if self.current_app:
            self.current_app.destroy()
        app7 = KodyQR(self)
        app7.grid()
        self.current_app = app7
    
    def open_pogoda(self):
        self.hide_menu()
        if self.current_app:
            self.current_app.destroy()
        app8 = Pogoda(self)
        app8.grid()
        self.current_app = app8

    def open_tablice(self):
        self.hide_menu()
        if self.current_app:
            self.current_app.destroy()
        app9 = Tablice(self)
        app9.grid()
        self.current_app = app9

    def hide_menu(self):
        self.withdraw()

    def show_menu(self):
        self.deiconify()
        
class Pogoda(tk.Toplevel):  
    def __init__(self, menu_app):
        super().__init__()
        self.menu_app = menu_app
        self.title("POGODA IMGW")
        self.protocol("WM_DELETE_WINDOW", self.on_close_window)
        self.current_page = None
        self.strona_pierwsza()

        self.show_page(self.page1)
        
    def strona_pierwsza(self):
        self.miasta = {"Białystok": 12295, "Bielsko Biała": 12600, "Chojnice": 12235, "Częstochowa": 12550, "Elbląg": 12160, "Gdańsk": 12155, "Gorzów": 12300,
          "Hel": 12135, "Jelenia Góra": 12500, "Kalisz": 12435, "Kasprowy Wierch": 12650, "Katowice": 12560, "Kętrzyn": 12185, "Kielce": 12570, "Kłodzko": 12520,
          "Koło": 12345, "Kołobrzeg": 12100, "Koszalin": 12105, "Kozienice": 12488, "Kraków": 12566, "Krosno": 12670, "Legnica": 12415, "Lesko": 12690, "Leszno": 12418,
          "Lębork": 12125, "Lublin": 12495, "Łeba": 12120, "Łódź": 12465, "Mikołajki": 12280, "Mława": 12270, "Nowy Sącz": 12660, "Olsztyn": 12272, "Opole": 12530,
          "Ostrołęka": 12285, "Piła": 12230, "Platforma Baltic Beta": 12001, "Płock": 12360, "Poznań": 12330, "Przemyśl": 12695, "Racibórz": 12540, "Resko": 12210,
          "Rzeszów": 12580, "Sandomierz": 12585, "Siedlce": 12385, "Słubice": 12310, "Sulejów": 12469, "Suwałki": 12195, "Szczecin": 12205, "Szczecinek": 12215,
          "Śnieżka": 12510, "Świnoujście": 12200, "Tarnów": 12575, "Terespol": 12399, "Toruń": 12250, "Ustka": 12115, "Warszawa": 12375, "Wieluń": 12455, "Włodawa": 12497,
          "Wrocław": 12424, "Zakopane": 12625, "Zamość": 12595, "Zielona Góra": 12400}

        self.opcje_miast = sorted(self.miasta.keys())

        self.sila_wiatru = {"cisza": (0, 0.2), "powiew": (0.2, 1.5), "słaby wiatr": (1.6, 3.3), "łagodny wiatr": (3.4, 5.4), "umiarkowany wiatr": (5.5, 7.9), "dość silny wiatr": (8, 10.7),
                "silny wiatr": (10.8, 13.8), "bardzo silny wiatr": (13.9, 17.1), "sztorm": (17.2, 20.7), "silny sztorm": (20.8, 24.4), "bardzo silny sztorm": (24.5, 28.4),
                "gwałtowny sztorm": (28.5, 32.6), "huragan": (32.7, 100)}
        self.kierunki = {"północny": (337.6, 22.5), "północno-wschodni": (22.6, 67.5), "wschodni": (67.6, 112.5), "południowo-wschodni": (112.6, 157.5),
                "południowy": (157.6, 202.5), "południowo-zachodni": (202.6, 247.5), "zachodni": (247.6, 292.5), "północno-zachodni": (292.6, 337.5)}
 
        self.page1 = tk.Frame(self)
        self.top_frame = Frame(self.page1)
        self.top_frame.grid(row=0, column=0, sticky="nsew", padx=10,  pady=10)

        self.label_start = Label(self.top_frame, text="Warunki atmosferyczne\n dla wybranej stacji pomiarowej IMGW")
        self.label_start.grid(row=1, column=0, padx=5, pady=5, sticky=EW, columnspan=3)

        self.option_var = StringVar(self.top_frame)
        self.max_length = max(len(option) for option in self.opcje_miast)

        self.option_menu = OptionMenu(self.top_frame, self.option_var, *self.opcje_miast)
        self.option_menu.grid(row=2, column=1, sticky=NS)
        self.option_menu.config(width=self.max_length + 2)
        self.option_var.set("Wybierz lokalizację")

        self.button = Button(self.top_frame, text='POKAŻ', command=self.pokaz_pogode)
        self.button.grid(row=2, column=2, sticky=NS, padx=5, pady=5)

        self.label1 = Label(self.top_frame)
        self.label1.grid(row=3, column=0, sticky=NS, columnspan=2)
        
        self.back_button = tk.Button(
        self.page1, text="POWRÓT DO MENU", command=self.back_to_menu, compound="right")
        self.back_button.grid(row=4, column=0, sticky=NS, columnspan=2, padx=5, pady=5)
        
    def pokaz_pogode(self):
        miasto = str(self.option_var.get())
        id_stacji = self.miasta[miasto]

        link = ("https://danepubliczne.imgw.pl/api/data/synop/id/xyz")
        link_test = (
            "https://danepubliczne.imgw.pl/api/data/synop/station/warszawa")
        response = requests.get(link_test)

        if response.status_code == 200:
            req = requests.get(link.replace("xyz", str(id_stacji)))
            json_data = req.text
            data = json.loads(json_data)

            stacja = data["stacja"]
            data_pomiaru = data["data_pomiaru"]
            godzina_pomiaru = data["godzina_pomiaru"]
            temperatura = data["temperatura"]
            predkosc_wiatru = data["predkosc_wiatru"]
            kierunek_wiatru = data["kierunek_wiatru"]
            wilgotnosc_wzgledna = data["wilgotnosc_wzgledna"]
            suma_opadu = data["suma_opadu"]
            cisnienie = data["cisnienie"]
            
            for zwrot, (min_wartosc, max_wartosc) in self.sila_wiatru.items():
                if min_wartosc <= int(predkosc_wiatru) <= max_wartosc:
                    x = zwrot
            
            for kierunek, (min_wartosc, max_wartosc) in self.kierunki.items():
                if min_wartosc <= int(kierunek_wiatru) <= max_wartosc:
                    y = kierunek

            info = (f"""
                    Pomiar z dnia {data_pomiaru} 
                    z godz. {godzina_pomiaru}:00 ze stacji {stacja}
                    Temperatura powietrza {temperatura} ℃
                    Wiatr o prędkości {predkosc_wiatru} m/s 
                    ({y} {x})
                    Wilgotność powietrza: {wilgotnosc_wzgledna}%
                    Suma opadów: {suma_opadu} mm
                    Ciśnienie atmosferyczne: {cisnienie} hPa
                    """)
            self.label1.config(text=info)
        else:
            info = (f"Wystąpił problem z połączeniem z Internetem!")
            self.label1.config(text=info)

    def show_page(self, page):
        if self.current_page:
            self.current_page.grid_forget()
        page.grid(row=0, column=0, sticky="nsew")
        self.current_page = page
        
    def on_close_window(self):
        self.back_to_menu()

    def back_to_menu(self):
        self.menu_app.show_menu()
        self.destroy()


class KodyQR(tk.Toplevel):
    def __init__(self, menu_app):
        super().__init__()
        self.menu_app = menu_app
        self.title("GENERATOR KODÓW QR")
        self.protocol("WM_DELETE_WINDOW", self.on_close_window)
        self.current_page = None
        self.strona_pierwsza()

        self.show_page(self.page1)

    def strona_pierwsza(self):
        self.page1 = tk.Frame(self)
        self.data_label = Label(self.page1, text="Wprowadź dane do wygenerowania kodu QR:")
        self.data_label.grid(row=0, column=0, columnspan=2)

        self.data_entry = Entry(self.page1, width=40)
        self.data_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.box_size_label = Label(self.page1, text="Wybierz rozmiar kwadratu (1-10):")
        self.box_size_label.grid(row=2, column=0, sticky=EW)

        self.box_size_var = StringVar()
        self.box_size_var.set("5")
        self.box_size_option_menu = OptionMenu(self.page1, self.box_size_var, *map(str, range(1, 11)))
        self.box_size_option_menu.grid(row=2, column=1)

        self.border_label = Label(self.page1, text="Wybierz grubość ramki (0-10):")
        self.border_label.grid(row=3, column=0, sticky=EW)

        self.border_var = StringVar()
        self.border_var.set("2")
        self.border_option_menu = OptionMenu(self.page1, self.border_var, *map(str, range(11)))
        self.border_option_menu.grid(row=3, column=1)

        self.browse_button = Button(self.page1, text="GDZIE ZAPISAĆ PLIK?", command=self.browse_folder)
        self.browse_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        self.generate_button = Button(self.page1, text="GENERUJ QR", command=self.generate_qr, state=DISABLED)
        self.generate_button.grid(row=5, column=0, sticky=EW, padx=5, pady=5)
        
        self.back_button = Button(self.page1, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=5, column=1, sticky=EW, padx=5, pady=5)

        self.result_label = Label(self.page1)
        self.result_label.grid(row=6, column=0, columnspan=2)
    
    def generate_unique_filename(self, folder, base_filename):
        unique_filename = base_filename
        counter = 1
        while os.path.exists(os.path.join(folder, unique_filename)):
            unique_filename = f"qr_code_{counter}.jpg"
            counter += 1
        return os.path.join(folder, unique_filename)


    def qr_generate(self, data, box_size, border, save_folder):
        filename = "qr_code.jpg"
        save_path = os.path.join(save_folder, filename)

        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        if os.path.exists(save_path):
            save_path = self.generate_unique_filename(save_folder, "qr_code.jpg")

        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=box_size,
            border=border)
        
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color='black', back_color='white')
        img.save(save_path)
        info = f"Kod QR wygenerowano pomyślnie!"
        messagebox.showinfo('Śliwka Coding Center ©', info)


    def browse_folder(self):
        global folder_path
        folder_path = filedialog.askdirectory()
        self.generate_button.config(state=ACTIVE)


    def generate_qr(self):
        data = self.data_entry.get()
        box_size = int(self.box_size_var.get())
        border = int(self.border_var.get())

        if data:
            if box_size >= 1 and box_size <= 10:
                if border >= 0 and border <= 10:
                    self.qr_generate(data,box_size, border, folder_path)
                else:
                    self.result_label.config(
                        text="Wprowadź poprawny border (od 0 do 10).")
            else:
                self.result_label.config(
                    text="Wprowadź poprawny box size (od 1 do 10).")
        else:
            self.result_label.config(text="Wprowadź dane do wygenerowania kodu QR.")
        
    def show_page(self, page):
        if self.current_page:
            self.current_page.grid_forget()
        page.grid(row=0, column=0, sticky="nsew")
        self.current_page = page
        
    def on_close_window(self):
        self.back_to_menu()

    def back_to_menu(self):
        self.menu_app.show_menu()
        self.destroy()


class Tablice(tk.Toplevel):
    def __init__(self, menu_app):
        super().__init__()
        self.menu_app = menu_app
        self.title("TABLICE REJESTRACYJNE")
        self.protocol("WM_DELETE_WINDOW", self.on_close_window)
        self.current_page = None
        self.strona_pierwsza()

        self.show_page(self.page1)

    def strona_pierwsza(self):
        self.page1 = tk.Frame(self)

        self.label = tk.Label(self.page1, text="Wprowadź numer tablicy rejestracyjnej")
        self.label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.entry = tk.Entry(self.page1)
        self.entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.check_button = tk.Button(self.page1, text="SPRAWDŹ", command=self.check_tablica)
        self.check_button.grid(row=2, column=0, padx=5, pady=5)
        
        self.back_to_menu_button = tk.Button(self.page1, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_to_menu_button.grid(row=2, column=1, padx=5, pady=5)

        self.result_label = tk.Label(self.page1, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
        
    def check_tablica(self):
        tablice_dyplomatyczne_funkcja = {(0,199): "Prywatny pojazd personelu dyplomatycznego ambasady",
                                        (200,299): "Prywatny pojazd attaché wojskowego",
                                        (300,499): "Prywatny pojazd personelu niedyplomatycznego ambasady",
                                        (500,501): "Służbowy pojazd ambasadora",
                                        (502,699): "Służbowy pojazd ambasady",
                                        (700,799): "Prywatny pojazd personelu dyplomatycznego konsulatu generalnego",
                                        (800,899): "Prywatny pojazd personelu niedyplomatycznego konsulatu generalnego",
                                        (900,901): "Służbowy pojazd konsula generalnego",
                                        (902,999): "Służbowy pojazd konsulatu generalnego"}
                                        
        tablice_wojewodztwa = {"B": "podlaskie", "C": "kujawsko-pomorskie", "D": "dolnośląskie", "E": "łódzkie", "F": "lubuskie",
                            "G": "pomorskie", "X": "pomorskie", "K": "małopolskie", "L": "lubelskie", "N": "warmińsko-mazurskie",
                            "O": "opolskie", "P": "wielkopolskie", "R": "podkarpackie", "S": "śląskie", "T": "świętokrzyskie", "W": "mazowieckie",
                            "Z": "zachodniopomorskie", "I": "śląskie", "J": "małopolskie", "M": "wielkopolskie", "Y": "podkarpackie",
                            "V": "dolnośląskie", "A": "mazowieckie"}

        tablice_dyplomatyczne_kraj = {"001": "USA", "002": "Wielka Brytania", "003": "Francja", "004": "Kanada",
            "005": "Niemcy","006": "Holandia","007": "Włochy","008": "Austria","009": "Japonia",
            "010": "Turcja","011": "Belgia","012": "Dania","013": "Norwegia","014": "Grecja",
            "015": "Australia","016": "Algieria","017": "Afganistan","018": "Argentyna",
            "019": "Brazylia","020": "Bangladesz","021": "Egipt","022": "Ekwador","023": "Finlandia",
            "024": "Hiszpania","025": "Irak","026": "Iran","027": "Indie","028": "Indonezja",
            "029": "Kolumbia","030": "Malezja","031": "Libia","032": "Maroko","033": "Meksyk",
            "034": "Nigeria","035": "Pakistan","036": "Portugalia","037": "Palestyna","038": "Syria",
            "039": "Szwecja","040": "Szwajcaria","041": "Tunezja","042": "Tajlandia","043": "Wenezuela",
            "044": "Urugwaj","045": "Peru","046": "Jemen","047": "Kostaryka","048": "Kongo",
            "049": "Izrael","050": "Nikaragua","051": "Chile","052": "Watykan","053": "Korea Południowa",
            "054": "Przedstawicielstwo Komisji Wspólnot Europejskich","055": "Irlandia","056": "Bank Światowy",
            "057": "Międzynarodowy Fundusz Walutowy","058": "Filipiny","059": "Międzynarodowa Korporacja Finansowa",
            "060": "RPA","061": "Biuro Instytucji Demokratycznych i Praw Człowieka OBWE","062": "Cypr",
            "063": "Kuwejt","064": "Organizacja Narodów Zjednoczonych","065": "Rosja","066": "Słowacja",
            "067": "Czechy","068": "Bułgaria","069": "Węgry","070": "Rumunia","071": "Wietnam",
            "072": "Serbia","073": "Korea Północna","074": "Kuba","075": "Albania","076": "Chiny",
            "077": "Mongolia","078": "Międzynarodowa Organizacja Pracy","079": "Organizacja Kooperacyjna ds. Kolei",
            "080": "Klub Dyplomatyczny","081": "Laos","082": "Angola","083": "Ukraina","084": "Europejski Bank Odbudowy i Rozwoju",
            "085": "Litwa","086": "Białoruś","087": "Łotwa","088": "Chorwacja","089": "Liban",
            "090": "Słowenia","091": "Gwatemala","092": "Estonia","093": "Macedonia","094": "Mołdawia",
            "095": "Izrael","096": "Armenia","097": "Sri Lanka","098": "Kazachstan","099": "Arabia Saudyjska",
            "100": "Gruzja","101": "Uzbekistan","102": "UN-HABITAT","103": "Nowa Zelandia","104": "Azerbejdżan",
            "105": "Suwerenny Wojskowy Zakon Maltański","106": "Kambodża","107": "Frontex","108": "Luksemburg",
            "109": "Bośnia i Hercegowina","110": "Panama","111": "Katar","112": "Malta",
            "113": "Zjednoczone Emiraty Arabskie","114": "Czarnogóra","115": "Senegal"}

        polskie_tablice_rejestracyjne = {"UA": "Siły zbrojne RP:\n samochód osobowy, osobowo-terenowy\n lub specjalny na podwoziu osobowym",
        "UB": "Siły zbrojne RP:\n transporter opancerzony","UC": "Siły zbrojne RP:\n samochód dostawczy",
        "UD": "Siły zbrojne RP:\n autobus","UE": "Siły zbrojne RP:\n samochód ciężarowy lub ciężarowo-terenowy\n o przeznaczeniu transportowym",
        "UG": "Siły zbrojne RP:\n pojazd specjalny\n na podwoziu ciężarowym","UI": "Siły zbrojne RP:\n przyczepa transportowa",
        "UJ": "Siły zbrojne RP:\n przyczepa specjalna","UK": "Siły zbrojne RP:\n motocykl","HSB": "Kontrola skarbowa\n woj. podlaskie","HSC": "Kontrola skarbowa\n woj. kujawsko-pomorskie","HSD": "Kontrola skarbowa\n woj. dolnośląskie",
        "HSE": "Kontrola skarbowa\n woj. łódzkie","HSF": "Kontrola skarbowa\n woj. lubuskie",
        "HSG": "Kontrola skarbowa\n woj. pomorskie","HSK": "Kontrola skarbowa\n woj. małopolskie",
        "HSL": "Kontrola skarbowa\n woj. lubelskie","HSN": "Kontrola skarbowa\n woj. warmińsko-mazurskie",
        "HSO": "Kontrola skarbowa\n woj. opolskie","HSP": "Kontrola skarbowa\n woj. wielkopolskie",
        "HSR": "Kontrola skarbowa\n woj. podkarpackie","HSS": "Kontrola skarbowa\n woj. śląskie",
        "HST": "Kontrola skarbowa\n woj. świętokrzyskie","HSW": "Kontrola skarbowa\n woj. mazowieckie",
        "HSZ": "Kontrola skarbowa\n woj. zachodniopomorskie","HCA": "Służba celna Olsztyn",
        "HCB": "Służba celna Białystok","HCC": "Służba celna Biała Podlaska",
        "HCD": "Służba celna Przemyśl","HCE": "Służba celna Kraków","HCF": "Służba celna Katowice",
        "HCG": "Służba celna Wrocław","HCH": "Służba celna Rzepin","HCJ": "Służba celna Szczecin",
        "HCK": "Służba celna Gdynia","HCL": "Służba celna Warszawa","HCM": "Służba celna Toruń",
        "HCN": "Służba celna Łódź","HCO": "Służba celna Poznań","HCP": "Służba celna Opole",
        "HCR": "Służba celna Kielce","HPA": "Komenda Główna Policji","HPB": "Policja woj. dolnośląskie",
        "HPC": "Policja woj. kujawsko-pomorskie","HPD": "Policja woj. lubelskie",
        "HPE": "Policja woj. lubuskie","HPF": "Policja woj. łódzkie","HPG": "Policja woj. małopolskie",
        "HPH": "Policja woj. mazowieckie","HPJ": "Policja woj. opolskie","HPK": "Policja woj. podkarpackie", "HPL": "Szkoła Policji w Szczytnie/Pile/Słupsku/Katowicach\n lub Centrum Szkolenia Policji w Legionowie",
        "HPM": "Policja woj. podlaskie","HPN": "Policja woj. pomorskie","HPP": "Policja woj. śląskie",
        "HPS": "Policja woj. świętokrzyskie","HPT": "Policja woj. warmińsko-mazurskie",
        "HPU": "Policja woj. wielkopolskie","HPW": "Policja woj. zachodniopomorskie",
        "HPZ": "Komenda Stołeczna Policji","HA": "Centralne Biuro Antykorupcyjne",
        "HB": "Służba Ochrony Państwa","HK": "Agencja Bezpieczeństwa Wewnętrznego\n lub Agencja Wywiadu",
        "HW": "Straż Graniczna","HM": "Służba Wywiadu Wojskowego\n lub Służba Kontrwywiadu Wojskowego", "BI":"Białystok","BS":"Suwałki","BL":"Łomża","BAU":"powiat augustowski",
        "BIA":"powiat białostocki","BBI":"powiat bielski","BGR":"powiat grajewski","BHA":"powiat hajnowski",
        "BKL":"powiat kolneński","BMN":"powiat moniecki","BSE":"powiat sejneński","BSI":"powiat siemiatycki",
        "BSK":"powiat sokólski","BSU":"powiat suwalski","BWM":"powiat wysokomazowiecki","BZA":"powiat zambrowski",
        "BLM":"powiat łomżyński","CB":"Bydgoszcz","CG":"Grudziądz","CT":"Toruń","CW":"Włocławek","CAL":"powiat aleksandrowski",
        "CBR":"powiat brodnicki","CBY":"powiat bydgoski","CCH":"powiat chełmiński","CGD":"powiat golubsko-dobrzyński",
        "CGR":"powiat grudziądzki","CIN":"powiat inowrocławski","CLI":"powiat lipnowski","CMG":"powiat mogileński",
        "CNA":"powiat nakielski","CRA":"powiat radziejowski","CRY":"powiat rypiński","CSE":"powiat sępoleński",
        "CSW":"powiat świecki","CTR":"powiat toruński","CTU":"powiat tucholski","CWA":"powiat wąbrzeski",
        "CWL":"powiat włocławski","CZN":"powiat żniński","DJ":"Jelenia Góra","VJ":"Jelenia Góra","DL":"Legnica","DB":"Wałbrzych","VL":"Legnica","VB":"Wałbrzych","DW":"Wrocław", "DX":"Wrocław", "VW":"Wrocław", "VX":"Wrocław", "VBL":"powiat bolesławiecki",
        "DBL":"powiat bolesławiecki", "VBL":"powiat bolesławiecki","DDZ":"powiat dzierżoniowski","VDZ":"powiat dzierżoniowski",
        "DGR":"powiat górowski","VGR":"powiat górowski","DGL":"powiat głogowski","VGL":"powiat głogowski",
        "DGL":"powiat głogowski", "VGL":"powiat głogowski","DJE":"powiat jeleniogórski", "VJE":"powiat jeleniogórski",
        "DKA":"powiat kamiennogórski", "VKA":"powiat kamiennogórski","DKL":"powiat kłodzki", "VKL":"powiat kłodzki", 
        "DLE":"powiat legnicki","VLE":"powiat legnicki","DLB":"powiat lubański","VLB":"powiat lubański",
        "DLU":"powiat lubiński","VLU":"powiat lubiński","DLW":"powiat lwówecki","VLW":"powiat lwówecki",
        "DMI":"powiat milicki","VMI":"powiat milicki","DOL":"powiat oleśnicki","VOL":"powiat oleśnicki",
        "DOA":"powiat oławski","VOA":"powiat oławski","DPL":"powiat polkowicki","VPL":"powiat polkowicki",
        "DSR":"powiat średzki","VSR":"powiat średzki","DST":"powiat strzeliński","VST":"powiat strzeliński",
        "DSW":"powiat świdnicki","VSW":"powiat świdnicki","DTR":"powiat trzebnicki","VTR":"powiat trzebnicki",
        "DBA":"powiat wałbrzyski","VBA":"powiat wałbrzyski","DWL":"powiat wołowski","VWL":"powiat wołowski",
        "DWR":"powiat wrocławski","VWR":"powiat wrocławski","DZA":"powiat ząbkowicki","VZA":"powiat ząbkowicki",
        "DZG":"powiat zgorzelecki","VZG":"powiat zgorzelecki","DZL":"powiat złotoryjski","VZL":"powiat złotoryjski", "ED":"Łódź",
        "EP":"Piotrków Trybunalski","ES":"Skierniewice","EL":"Łódź","EBE":"powiat bełchatowski","EBR":"powiat brzeziński","EKU":"powiat kutnowski","EOP":"powiat opoczyński","EPA":"powiat pabianicki","EPJ":"powiat pajęczański","EPI":"powiat piotrkowski",
        "EPD":"powiat poddębicki","ERA":"powiat radomszczański","ERW":"powiat rawski","ESI":"powiat sieradzki",
        "ESK":"powiat skierniewicki","ETM":"powiat tomaszowski","EWI":"powiat wieluński","EWE":"powiat wieruszowski",
        "EZD":"powiat zduńskowolski","EZG":"powiat zgierski","ELA":"powiat łaski","ELE":"powiat łęczycki",
        "ELW":"powiat łódzki wschodni","ELC":"powiat łowicki","FG":"Gorzów Wielkopolski","FZ":"Zielona Góra",
        "FGW":"powiat gorzowski","FKR":"powiat krośnieński","FMI":"powiat międzyrzecki","FNW":"powiat nowosolski",
        "FSD":"powiat strzelecko-drezdenecki","FSU":"powiat sulęciński","FSW":"powiat świebodziński",
        "FSL":"powiat słubicki","FWS":"powiat wschowski","FZG":"powiat żagański","FZA":"powiat żarski",
        "FZI":"powiat zielonogórski","GD":"Gdańsk","XD":"Gdańsk","GA":"Gdynia","XA":"Gdynia",
        "GSP":"Sopot","XSP":"Sopot","GS":"Słupsk","XS":"Słupsk","GBY":"powiat bytowski","XBY":"powiat bytowski",
        "GCH":"powiat chojnicki","XCH":"powiat chojnicki","GCZ":"powiat człuchowski","XCZ":"powiat człuchowski",
        "GDA":"powiat gdański","XDA":"powiat gdański","GKA":"powiat kartuski","GKY":"powiat kartuski","GKZ":"powiat kartuski",
        "XKA":"powiat kartuski","XKY":"powiat kartuski","XKZ":"powiat kartuski","GKS":"powiat kościerski","XKS":"powiat kościerski",
        "GKW":"powiat kwidzyński","XKW":"powiat kwidzyński","GLE":"powiat lęborski","XLE":"powiat lęborski",
        "GMB":"powiat malborski","XMB":"powiat malborski","GND":"powiat nowodworski","XND":"powiat nowodworski",
        "GPU":"powiat pucki","XPU":"powiat pucki","GST":"powiat starogardzki","XST":"powiat starogardzki",
        "GSZ":"powiat sztumski","XSZ":"powiat sztumski","GSL":"powiat słupski","XSL":"powiat słupski",
        "GTC":"powiat tczewski","XTC":"powiat tczewski","GWE":"powiat wejherowski","GWO":"powiat wejherowski",
        "XWE":"powiat wejherowski","XWO":"powiat wejherowski","KK":"Kraków","KR":"Kraków", "JK":"Kraków","JR":"Kraków",
        "KN":"Nowy Sącz","JN":"Nowy Sącz","KT":"Tarnów","JT":"Tarnów","KBC":"powiat bocheński","JBC":"powiat bocheński",
        "KBA":"powiat bocheński","JBA":"powiat bocheński","KBR":"powiat brzeski","JBR":"powiat brzeski",
        "KCH":"powiat chrzanowski","JCH":"powiat chrzanowski","KDA":"powiat dąbrowski","JDA":"powiat dąbrowski",
        "KGR":"powiat gorlicki","JGR":"powiat gorlicki","KRA":"powiat krakowski","JRA":"powiat krakowski",
        "KLI":"powiat limanowski","JLI":"powiat limanowski","KMI":"powiat miechowski","JMI":"powiat miechowski",
        "KMY":"powiat myślenicki","JMY":"powiat myślenicki","KNS":"powiat nowosądecki","JNS":"powiat nowosądecki",
        "KNT":"powiat nowotarski","JNT":"powiat nowotarski","KOL":"powiat olkuski","JOL":"powiat olkuski",
        "KOS":"powiat oświęcimski","JOS":"powiat oświęcimski","KPR":"powiat proszowicki","JPR":"powiat proszowicki",
        "KSU":"powiat suski","JSU":"powiat suski","KTA":"powiat tarnowski","JTA":"powiat tarnowski",
        "KTT":"powiat tatrzański","JTT":"powiat tatrzański","KWA":"powiat wadowicki", "JWA":"powiat wadowicki",
        "KWI":"powiat wielicki", "JWI":"powiat wielicki","LB":"Biała Podlaska","LC":"Chełm","LU":"Lublin","LZ":"Zamość","LBI":"powiat bialski","LBL":"powiat biłgorajski","LCH":"powiat chełmski","LHR":"powiat hrubieszowski","LJA":"powiat janowski","LKR":"powiat kraśnicki",
        "LKS":"powiat krasnostawski","LLB":"powiat lubartowski","LUB":"powiat lubelski","LOP":"powiat opolski",
        "LPA":"powiat parczewski","LPU":"powiat puławski","LRA":"powiat radzyński","LRY":"powiat rycki",
        "LSW":"powiat świdnicki","LTM":"powiat tomaszowski","LWL":"powiat włodawski","LZA":"powiat zamojski",
        "LLE":"powiat łęczyński","LLU":"powiat łukowski","NE":"Elbląg","NO":"Olsztyn","NBA":"powiat bartoszycki",
        "NBR":"powiat braniewski","NDZ":"powiat działdowski","NEB":"powiat elbląski","NEL":"powiat ełcki",
        "NGI":"powiat giżycki","NGO":"powiat gołdapski","NIL":"powiat iławski","NKE":"powiat kętrzyński",
        "NLI":"powiat lidzbarski","NMR":"powiat mrągowski","NNI":"powiat nidzicki","NNM":"powiat nowomiejski",
        "NOE":"powiat olecki","NOL":"powiat olsztyński","NOS":"powiat ostródzki","NPI":"powiat piski",
        "NSZ":"powiat szczycieński","NWE":"powiat węgorzewski","OP":"Opole","OB":"powiat brzeski","OGL":"powiat głubczycki",
        "OK":"powiat kędzierzyńsko-kozielski","OKL":"powiat kluczborski","OKR":"powiat krapkowicki",
        "ONA":"powiat namysłowski","ONY":"powiat nyski","OOL":"powiat oleski","OPO":"powiat opolski",
        "OPR":"powiat prudnicki","OST":"powiat strzelecki","PK":"Kalisz","PA":"Kalisz","MK":"Kalisz","MA":"Kalisz",
        "PN":"Konin","PKO":"Konin","MN":"Konin","MKO":"Konin","PL":"Leszno","ML":"Leszno","PO":"Poznań","MO":"Poznań",
        "PY":"Poznań","MY":"Poznań","PCH":"powiat chodzieski","MCH":"powiat chodzieski",
        "PCT":"powiat czarnkowsko-trzcianecki","MCT":"powiat czarnkowsko-trzcianecki",
        "PGN":"powiat gnieźnieński","MGN":"powiat gnieźnieński","PGS":"powiat gostyński","MGS":"powiat gostyński",
        "PGO":"powiat grodziski","MGO":"powiat grodziski","PJA":"powiat jarociński","MJA":"powiat jarociński",
        "PKA":"powiat kaliski","MKA":"powiat kaliski","PKE":"powiat kępiński","MKE":"powiat kępiński",
        "PKL":"powiat kolski","MKL":"powiat kolski","PKN":"powiat koniński","MKN":"powiat koniński",
        "PKS":"powiat kościański","MKS":"powiat kościański","PKR":"powiat krotoszyński","MKR":"powiat krotoszyński",
        "PLE":"powiat leszczyński","MLE":"powiat leszczyński","PMI":"powiat międzychodzki","MMI":"powiat międzychodzki",
        "PNT":"powiat nowotomyski","MNT":"powiat nowotomyski","POB":"powiat obornicki","MOB":"powiat obornicki",
        "POS":"powiat ostrowski","MOS":"powiat ostrowski","POT":"powiat ostrzeszowski","MOT":"powiat ostrzeszowski",
        "PP":"powiat pilski","MP":"powiat pilski","PPL":"powiat pleszewski","MPL":"powiat pleszewski",
        "PZ":"powiat poznański","POZ":"powiat poznański","MZ":"powiat poznański","MOZ":"powiat poznański",
        "PRA":"powiat rawicki","MRA":"powiat rawicki","PSR":"powiat średzki","MSR":"powiat średzki",
        "PSE":"powiat śremski","MSE":"powiat śremski","PSZ":"powiat szamotulski","MSZ":"powiat szamotulski",
        "PSL":"powiat słupecki","MSL":"powiat słupecki","PTU":"powiat turecki","MTU":"powiat turecki",
        "PWA":"powiat wągrowiecki","MWA":"powiat wągrowiecki","PWL":"powiat wolsztyński","MWL":"powiat wolsztyński",
        "PWR":"powiat wrzesiński","MWR":"powiat wrzesiński","PZL":"powiat złotowski","MZL":"powiat złotowski",
        "RK":"Krosno","YK":"Krosno","RP":"Przemyśl","YP":"Przemyśl","RZ":"Rzeszów","YZ":"Rzeszów",
        "RT":"Tarnobrzeg", "YT":"Tarnobrzeg","RBI":"powiat bieszczadzki","YBI":"powiat bieszczadzki",
        "RBR":"powiat brzozowski","YBR":"powiat brzozowski","RDE":"powiat dębicki","YDE":"powiat dębicki",
        "RJA":"powiat jarosławski","YJA":"powiat jarosławski","RJS":"powiat jasielski","YJS":"powiat jasielski",
        "RKL":"powiat kolbuszowski","YKL":"powiat kolbuszowski","RKR":"powiat krośnieński","YKR":"powiat krośnieński",
        "RLS":"powiat leski","YLS":"powiat leski","RLE":"powiat leżajski","YLE":"powiat leżajski",
        "RLU":"powiat lubaczowski","YLU":"powiat lubaczowski","RMI":"powiat mielecki","YMI":"powiat mielecki",
        "RNI":"powiat niżański","YNI":"powiat niżański","RPR":"powiat przemyski","YPR":"powiat przemyski",
        "RPZ":"powiat przeworski","YPZ":"powiat przeworski","RRS":"powiat ropczycko-sędziszowski","YRS":"powiat ropczycko-sędziszowski",
        "RZE":"powiat rzeszowski","RZZ":"powiat rzeszowski","RZR":"powiat rzeszowski","YZE":"powiat rzeszowski","YZZ":"powiat rzeszowski","YZR":"powiat rzeszowski","RSA":"powiat sanocki","YSA":"powiat sanocki","RST":"powiat stalowowolski","YST":"powiat stalowowolski",
        "RSR":"powiat strzyżowski","YSR":"powiat strzyżowski","RTA":"powiat tarnobrzeski","YTA":"powiat tarnobrzeski",
        "RLA":"powiat łańcucki","YLA":"powiat łańcucki","SB":"Bielsko-Biała","IB":"Bielsko-Biała",
        "SY":"Bytom","IY":"Bytom","SH":"Chorzów","IH":"Chorzów","SC":"Częstochowa","IC":"Częstochowa",
        "SD":"Dąbrowa Górnicza","ID":"Dąbrowa Górnicza","SG":"Gliwice","IG":"Gliwice","SJZ":"Jastrzębie-Zdrój","IJZ":"Jastrzębie-Zdrój",
        "SJ":"Jaworzno","IJ":"Jaworzno","SK":"Katowice","IK":"Katowice","SM":"Mysłowice","IM":"Mysłowice",
        "SPI":"Piekary Śląskie","IPI":"Piekary Śląskie","SL":"Ruda Śląska","SRS":"Ruda Śląska","IL":"Ruda Śląska","IRS":"Ruda Śląska",
        "SR":"Rybnik","IR":"Rybnik","SI":"Siemianowice Śląskie","II":"Siemianowice Śląskie","SO":"Sosnowiec","IO":"Sosnowiec",
        "SW":"Świętochłowice","IW":"Świętochłowice","ST":"Tychy","IT":"Tychy","SZ":"Zabrze","IZ":"Zabrze","SZO":"Żory","IZO":"Żory",
        "SBE":"powiat będziński","SE":"powiat będziński","SBN":"powiat będziński","IBE":"powiat będziński","IE":"powiat będziński","IBN":"powiat będziński","SBI":"powiat bielski","IBI":"powiat bielski","SBL":"powiat bieruńsko-lędziński","IBL":"powiat bieruńsko-lędziński","SCI":"powiat cieszyński","SCN":"powiat cieszyński","ICI":"powiat cieszyński","ICN":"powiat cieszyński",
        "SCZ":"powiat częstochowski","ICZ":"powiat częstochowski","SGL":"powiat gliwicki","IGL":"powiat gliwicki",
        "SKL":"powiat kłobucki","IKL":"powiat kłobucki","SLU":"powiat lubliniecki","ILU":"powiat lubliniecki",
        "SMI":"powiat mikołowski","IMI":"powiat mikołowski","SMY":"powiat myszkowski","IMY":"powiat myszkowski",
        "SPS":"powiat pszczyński","IPS":"powiat pszczyński","SRC":"powiat raciborski","IRC":"powiat raciborski",
        "SRB":"powiat rybnicki","IRB":"powiat rybnicki","STA":"powiat tarnogórski","ITA":"powiat tarnogórski",
        "IWD":"powiat wodzisławski","IWZ":"powiat wodzisławski","SWD":"powiat wodzisławski","SWZ":"powiat wodzisławski",
        "SZA":"powiat zawierciański","IZA":"powiat zawierciański","SZY":"powiat żywiecki","IZY":"powiat żywiecki",
        "TK":"Kielce","TBU":"powiat buski","TJE":"powiat jędrzejowski","TKA":"powiat kazimierski","TKI":"powiat kielecki",
        "TKN":"powiat konecki","TOP":"powiat opatowski","TOS":"powiat ostrowiecki","TPI":"powiat pińczowski",
        "TSA":"powiat sandomierski","TSK":"powiat skarżyski","TST":"powiat starachowicki","TSZ":"powiat staszowski",
        "TLW":"powiat włoszczowski","WO":"Ostrołęka", "AO":"Ostrołęka","WP":"Płock","AP":"Płock","WR":"Radom","AR":"Radom",
        "WS":"Siedlce", "AS":"Siedlce","WB":"Warszawa Bemowo", "AB":"Warszawa Bemowo",
        "WA":"Warszawa Białołęka", "AA":"Warszawa Białołęka","WD":"Warszawa Bielany", "AD":"Warszawa Bielany",
        "WE":"Warszawa Mokotów", "AE":"Warszawa Mokotów","WU":"Warszawa Ochota","AU":"Warszawa Ochota",
        "WH":"Warszawa Praga Północ","AH":"Warszawa Praga Północ","WF":"Warszawa Praga Południe", "AF":"Warszawa Praga Południe",
        "WI":"Warszawa Śródmieście", "AI":"Warszawa Śródmieście","WJ":"Warszawa Targówek","AJ":"Warszawa Targówek",
        "WK":"Warszawa Ursus","AK":"Warszawa Ursus","WN":"Warszawa Ursynów","AN":"Warszawa Ursynów",
        "WT":"Warszawa Wawer","AT":"Warszawa Wawer","WBR":"powiat białobrzeski","ABR":"powiat białobrzeski",
        "WCI":"powiat ciechanowski","ACI":"powiat ciechanowski","WG":"powiat garwoliński","AG":"powiat garwoliński",
        "WGS":"powiat gostyniński","AGS":"powiat gostyniński","WGM":"powiat grodziski","AGM":"powiat grodziski",
        "WGR":"powiat grójecki","AGR":"powiat grójecki","WKZ":"powiat kozienicki","AKZ":"powiat kozienicki",
        "WL":"powiat legionowski","AL":"powiat legionowski","WLI":"powiat lipski","ALI":"powiat lipski",
        "WMA":"powiat makowski","AMA":"powiat makowski","WM":"powiat miński","AM":"powiat miński",
        "WML":"powiat mławski","AML":"powiat mławski","WND":"powiat nowodworski","AND":"powiat nowodworski",
        "WOR":"powiat ostrowski","AOR":"powiat ostrowski","WOS":"powiat ostrołęcki","AOS":"powiat ostrołęcki",
        "WOT":"powiat otwocki","AOT":"powiat otwocki","WPI":"powiat piaseczyński", "WPA":"powiat piaseczyński", "WPW":"powiat piaseczyński", "WPX":"powiat piaseczyński","API":"powiat piaseczyński", "APA":"powiat piaseczyński", "APW":"powiat piaseczyński", "APX":"powiat piaseczyński","WPS":"powiat pruszkowski", "WPR":"powiat pruszkowski", "WPP":"powiat pruszkowski",
        "APS":"powiat pruszkowski", "APR":"powiat pruszkowski", "APP":"powiat pruszkowski",
        "WPZ":"powiat przasnyski","APZ":"powiat przasnyski","WPY":"powiat przysuski","APY":"powiat przysuski",
        "WPU":"powiat pułtuski","APU":"powiat pułtuski","WPL":"powiat płocki","APL":"powiat płocki",
        "WPN":"powiat płoński","APN":"powiat płoński","WRA":"powiat radomski","ARA":"powiat radomski",
        "WSI":"powiat siedlecki","ASI":"powiat siedlecki","WSE":"powiat sierpecki","ASE":"powiat sierpecki",
        "WSC":"powiat sochaczewski","ASC":"powiat sochaczewski","WSK":"powiat sokołowski","ASK":"powiat sokołowski",
        "WSZ":"powiat szydłowiecki","ASZ":"powiat szydłowiecki","WZ":"powiat warszawski zachodni","AZ":"powiat warszawski zachodni",
        "WWE":"powiat węgrowski","AWE":"powiat węgrowski","WWL":"powiat wołomiński","AWL":"powiat wołomiński",
        "WV":"powiat wołomiński","AV":"powiat wołomiński","WWY":"powiat wyszkowski","AWY":"powiat wyszkowski",
        "WZU":"powiat żuromiński","AZU":"powiat żuromiński","WZW":"powiat zwoleński","AZW":"powiat zwoleński",
        "WZY":"powiat żyrardowski","AZY":"powiat żyrardowski","WLS":"powiat łosicki","ALS":"powiat łosicki",
        "ZK":"Koszalin","ZSW":"Świnoujście","ZS":"Szczecin","ZZ":"Szczecin","ZBI":"powiat białogardzki",
        "ZCH":"powiat choszczeński","ZDR":"powiat drawski","ZGL":"powiat goleniowski","ZGY":"powiat gryficki",
        "ZGR":"powiat gryfiński","ZKA":"powiat kamieński","ZKO":"powiat koszaliński","ZKL":"powiat kołobrzeski",
        "ZMY":"powiat myśliborski","ZPL":"powiat policki","ZPY":"powiat pyrzycki","ZST":"powiat stargardzki",
        "ZSD":"powiat świdwiński","ZSZ":"powiat szczecinecki","ZSL":"powiat sławieński","ZWA":"powiat wałecki",
        "ZLO":"powiat łobeski"}

        numer_tablicy = self.entry.get().upper() 
        
        if numer_tablicy.startswith("W") and numer_tablicy[1:].isdigit() and len(numer_tablicy) == 7:
            kraj_numer = numer_tablicy[1:4]
            stanowisko_numer = int(numer_tablicy[4:])
            
            kraj = tablice_dyplomatyczne_kraj.get(kraj_numer, "Nieznany kraj")
            
            for key_range, description in tablice_dyplomatyczne_funkcja.items():
                if key_range[0] <= stanowisko_numer <= key_range[1]:
                    stanowisko = description
                    break
            else:
                stanowisko = "Nieznane stanowisko"
            
            self.result_label.config(text=f"Tablica dyplomatyczna:\nKraj: {kraj}\n{stanowisko}")
        
        elif numer_tablicy.startswith("WX") or numer_tablicy.startswith("AX"):
            if numer_tablicy.endswith("YV") or numer_tablicy.endswith("YZ") or numer_tablicy[-2] == "Y":
                self.result_label.config(text=f"Przynależność: Warszawa Wesoła")
            else:
                self.result_label.config(text=f"Przynależność: Warszawa Żoliborz")
        elif numer_tablicy.startswith("WY") or numer_tablicy.startswith("AY"):
            if numer_tablicy[-1] == "Y":
                self.result_label.config(text=f"Samochód służbowy warszawskiego urzędu miasta\n lub pojazd cudzoziemca zameldowanego w stolicy.")
                if numer_tablicy[-2:] == "YY":
                    self.result_label.config(text=f"Przynależność: Sulejówek")
            else:
                self.result_label.config(text=f"Przynależność: Warszawa Wola")
                
        elif numer_tablicy[:1].isalpha() and numer_tablicy[1].isdigit():
            znaki = numer_tablicy[:1]
            if znaki in tablice_wojewodztwa:
                self.result_label.config(text=f"Województwo {tablice_wojewodztwa[znaki]},\n tablica indywidualna")
            else:
                self.result_label.config(text="Brak informacji dla tego rodzaju tablicy rejestracyjnej.")
                
        elif numer_tablicy[:3].isalpha():
            znaki = numer_tablicy[:3]
            wojewodztwo = numer_tablicy[:1]
            if znaki in polskie_tablice_rejestracyjne:
                if wojewodztwo in tablice_wojewodztwa:
                    self.result_label.config(text=f"Przynależność: {polskie_tablice_rejestracyjne[znaki]},\n województwo {tablice_wojewodztwa[wojewodztwo]}")
                else:
                    self.result_label.config(text=f"Przynależność: {polskie_tablice_rejestracyjne[znaki]}")

            else:
                self.result_label.config(text="Brak informacji dla tego rodzaju tablicy rejestracyjnej.")
        
        elif numer_tablicy.startswith("WW") or numer_tablicy.startswith("AW") and numer_tablicy[1].isdigit():
            rembertow = ["A", "C", "E", "X", "Y"]
            wilanow = ["F","G","H","J","W"]
            wlochy = ["K","L","M","N","V"]
            if numer_tablicy[-1] in rembertow:
                self.result_label.config(text=f"Przynależność: Warszawa Rembertów")
            elif numer_tablicy[-1] in wilanow:
                self.result_label.config(text=f"Przynależność: Warszawa Wilanów")
            elif numer_tablicy[-1] in wlochy:
                self.result_label.config(text=f"Przynależność: Warszawa Włochy")
                
        elif numer_tablicy[:2].isalpha():
            znaki = numer_tablicy[:2]
            wojewodztwo = numer_tablicy[:1]
            if znaki in polskie_tablice_rejestracyjne:
                if wojewodztwo in tablice_wojewodztwa:
                    self.result_label.config(text=f"Przynależność: {polskie_tablice_rejestracyjne[znaki]},\n województwo {tablice_wojewodztwa[wojewodztwo]}")
                else:
                    self.result_label.config(text=f"Przynależność: {polskie_tablice_rejestracyjne[znaki]}")
            else:
                self.result_label.config(text="Brak informacji dla tego rodzaju tablicy rejestracyjnej.")
        
        else:
            self.result_label.config(text="Nieznany format numeru tablicy.")  
        
    def show_page(self, page):
        if self.current_page:
            self.current_page.grid_forget()
        page.grid(row=0, column=0, sticky="nsew")
        self.current_page = page
        
    def on_close_window(self):
        self.back_to_menu()

    def back_to_menu(self):
        self.menu_app.show_menu()
        self.destroy()


class DietyKrajowe(tk.Toplevel):
    def __init__(self, menu_app):
        super().__init__()
        self.menu_app = menu_app
        self.title("DIETY KRAJOWE")
        self.protocol("WM_DELETE_WINDOW", self.on_close_window)
        self.current_page = None
        self.strona_pierwsza()
        self.strona_druga()
        self.strona_trzecia()
        self.strona_czwarta()

        self.show_page(self.page1)

    def strona_pierwsza(self):
        self.page1 = tk.Frame(self)
        label_start = tk.Label(
            self.page1, text="Wybierz datę i godzinę rozpoczęcia delegacji")
        label_start.grid(row=0, column=0, sticky="EW",
                         padx=5, pady=5, columnspan=8)

        label_godzina_startu = tk.Label(self.page1, text="GODZINA")
        label_godzina_startu.grid(row=1, column=3, padx=5, pady=5, sticky=S)
        label_minuta_startu = tk.Label(self.page1, text="MINUTA")
        label_minuta_startu.grid(row=1, column=4, padx=5, pady=5, sticky=S)

        self.cal_start = Calendar(self.page1, selectmode='day',
                                  date_pattern='dd/mm/yyyy', locale='pl_PL')
        self.date = self.cal_start.datetime.today()
        self.cal_start.grid(row=1, column=0, padx=5, pady=5,
                            sticky="N", rowspan=3, columnspan=3)

        self.godzinysk = tk.IntVar()
        self.wybor_godziny_startu = tk.Spinbox(
            self.page1, width=5, wrap=True, values=godziny)
        self.wybor_godziny_startu.grid(
            row=2, column=3, padx=5, pady=5, sticky="N")
        self.minutysk = tk.IntVar()
        self.wybor_minuty_startu = tk.Spinbox(
            self.page1, width=5, wrap=True, values=minuty)
        self.wybor_minuty_startu.grid(
            row=2, column=4, padx=5, pady=5, sticky="N")

        button_container = tk.Frame(self.page1)
        button_container.grid(row=4, column=0, padx=5, pady=5, columnspan=8)

        self.back_button = tk.Button(
            button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=0, padx=5, pady=5)

        self.button_next_page2 = tk.Button(
            button_container, text="DALEJ", command=self.next_page1)
        self.button_next_page2.grid(row=0, column=1, padx=5, pady=5)

    def strona_druga(self):
        self.page2 = tk.Frame(self)
        label_start = tk.Label(
            self.page2, text="Wybierz datę i godzinę zakończenia delegacji")
        label_start.grid(row=0, column=0, sticky="EW",
                         padx=5, pady=5, columnspan=8)

        self.cal_koniec = Calendar(self.page2, selectmode='day',
                                   date_pattern='dd/mm/yyyy', locale='pl_PL')
        self.date = self.cal_koniec.datetime.today()
        self.cal_koniec.grid(row=1, column=0, padx=5, pady=5,
                             sticky="N", rowspan=3, columnspan=3)

        self.label_godzina_konca = tk.Label(self.page2, text="GODZINA")
        self.label_godzina_konca.grid(
            row=1, column=3, padx=5, pady=5, sticky=S)
        label_minuta_konca = tk.Label(self.page2, text="MINUTA")
        label_minuta_konca.grid(row=1, column=4, padx=5, pady=5, sticky=S)

        self.godzinykk = tk.IntVar()
        self.wybor_godziny_konca = tk.Spinbox(
            self.page2, width=5, wrap=True, values=godziny)
        self.wybor_godziny_konca.grid(
            row=2, column=3, padx=5, pady=5, sticky="N")
        self.minutykk = tk.IntVar()
        self.wybor_minuty_konca = tk.Spinbox(
            self.page2, width=5, wrap=True, values=minuty)
        self.wybor_minuty_konca.grid(row=2, column=4, padx=5, pady=5, sticky=N)

        button_container = tk.Frame(self.page2)
        button_container.grid(row=4, column=0, padx=5, pady=5, columnspan=8)

        self.button_back_page2 = tk.Button(
            button_container, text="WSTECZ", command=self.back_page2)
        self.button_back_page2.grid(row=0, column=0, padx=5, pady=5)

        self.back_button = tk.Button(
            button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=1, padx=5, pady=5)

        self.button_next_page2 = tk.Button(
            button_container, text="DALEJ", command=self.next_page2)
        self.button_next_page2.grid(row=0, column=2, columnspan=2, padx=5, pady=5)

    def strona_trzecia(self):
        self.page3 = tk.Frame(self)
        self.label_posilki = tk.Label(
            self.page3, text="Wskaż posiłki zapewnione podczas delegacji")
        self.label_posilki.grid(
            row=0, column=0, sticky="EW", padx=5, pady=5, columnspan=8)

        self.var1dk = tk.IntVar()
        self.check_sniadaniedk = tk.Checkbutton(self.page3, text="ŚNIADANIE", onvalue=1,
                                                offvalue=0, command=self.checking_sniadaniedk, variable=self.var1dk)
        self.check_sniadaniedk.grid(
            row=1, column=0, padx=50, pady=5, sticky="W", columnspan=2)
        self.label_sniadanie = tk.Label(self.page3, text="w ilości")
        self.label_sniadanie.grid(row=1, column=2, sticky="E", padx=5, pady=5)
        self.ilosc_sniadaniedk = tk.Entry(self.page3, width=5, state=DISABLED)
        self.ilosc_sniadaniedk.grid(
            row=1, column=3, sticky="W", padx=5, pady=5)

        self.var2dk = IntVar()
        self.check_obiaddk = Checkbutton(self.page3, text="OBIAD", onvalue=1,
                                         offvalue=0, command=self.checking_obiaddk, variable=self.var2dk)
        self.check_obiaddk.grid(row=2, column=0, padx=50,
                                pady=5, sticky=W, columnspan=2)
        self.label_obiad = Label(self.page3, text="w ilości")
        self.label_obiad.grid(row=2, column=2, sticky=E, padx=5, pady=5)
        self.ilosc_obiaddk = Entry(self.page3, width=5, state=DISABLED)
        self.ilosc_obiaddk.grid(row=2, column=3, sticky=W, padx=5, pady=5)

        self.var3dk = IntVar()
        self.check_kolacjadk = Checkbutton(self.page3, text="KOLACJA", onvalue=1,
                                           offvalue=0, command=self.checking_kolacjadk, variable=self.var3dk)
        self.check_kolacjadk.grid(
            row=3, column=0, padx=50, pady=5, sticky=W, columnspan=2)
        self.label_kolacja = Label(self.page3, text="w ilości")
        self.label_kolacja.grid(row=3, column=2, sticky=E, padx=5, pady=5)
        self.ilosc_kolacjadk = Entry(self.page3, width=5, state=DISABLED)
        self.ilosc_kolacjadk.grid(row=3, column=3, sticky=W, padx=5, pady=5)

        self.label_dodatki = Label(
            self.page3, text="Wskaż przysługujące ci ryczałty")
        self.label_dodatki.grid(
            row=4, column=0, sticky=EW, padx=5, pady=5, columnspan=8)

        self.nocleg_var1 = tk.BooleanVar()
        self.auto_var2 = tk.BooleanVar()
        self.komunikacja_var3 = tk.BooleanVar()

        self.checkframe = Frame(self.page3)
        self.checkframe.grid(row=5, column=0, columnspan=8)

        self.check_nocleg = Checkbutton(
            self.checkframe, text="NOCLEG", variable=self.nocleg_var1, command=self.rycz_nocleg)
        self.check_auto = Checkbutton(
            self.checkframe, text="PRYWATNE AUTO", variable=self.auto_var2, command=self.rycz_auto)
        self.check_komunikacja = Checkbutton(
            self.checkframe, text="KOMUNIKACJA MIEJSCOWA", variable=self.komunikacja_var3, command=self.rycz_komunikacja)
        self.check_nocleg.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.check_auto.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.check_komunikacja.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        self.button_container = tk.Frame(self.page3)
        self.button_container.grid(
            row=8, column=0, padx=5, pady=5, columnspan=8)

        self.button_back_page2 = tk.Button(
            self.button_container, text="WSTECZ", command=self.back_page3)
        self.button_back_page2.grid(row=0, column=0, sticky=E, padx=5, pady=5)

        self.back_button = tk.Button(
            self.button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=1, padx=5, pady=5)

        self.button_next_page2 = tk.Button(
            self.button_container, text="DALEJ", command=self.next_page3)
        self.button_next_page2.grid(row=0, column=2, sticky=W, padx=5, pady=5)

    def strona_czwarta(self):
        self.page4 = tk.Frame(self)

        button_container = tk.Frame(self.page4)
        button_container.grid(row=1, column=0, padx=5, pady=5, columnspan=8)

        self.label_wynik = Label(self.page4)
        self.label_wynik.grid(row=0, column=0, padx=5,
                              pady=5, columnspan=8, sticky=W)

        self.button_back_page2 = tk.Button(
            button_container, text="WSTECZ", command=self.back_page4)
        self.button_back_page2.grid(row=0, column=0, sticky=E, padx=5, pady=5)

        self.back_button = tk.Button(
            button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=1, sticky=W, padx=5, pady=5)

    def rycz_nocleg(self):
        try:
            s_rok = int(self.cal_start.get_date()[-4:])
            s_miesiac = int(self.cal_start.get_date()[4:5])
            s_dzien = int(self.cal_start.get_date()[:2])
            s_godzina = int(self.wybor_godziny_startu.get())
            s_minuta = int(self.wybor_minuty_startu.get())
            k_rok = int(self.cal_koniec.get_date()[-4:])
            k_miesiac = int(self.cal_koniec.get_date()[4:5])
            k_dzien = int(self.cal_koniec.get_date()[:2])
            k_godzina = int(self.wybor_godziny_konca.get())
            k_minuta = int(self.wybor_minuty_konca.get())
            data_startu = datetime(
                s_rok, s_miesiac, s_dzien, s_godzina, s_minuta)
            data_konca = datetime(
                k_rok, k_miesiac, k_dzien, k_godzina, k_minuta)
            czas_delegacji = data_konca - data_startu
            tsecs = czas_delegacji.total_seconds()
            thrs = tsecs/(60*60)
            self.liczba_dni = int(thrs // 24)
            self.ryczalt_nocleg = self.liczba_dni * 45 * 1.5

            return self.ryczalt_nocleg
        except Exception as e:
            self.info = ("Wystąpił błąd:", e)
            messagebox.showinfo('Śliwka Coding Center ©', self.info)

    def rycz_auto(self):
        self.top = tk.Toplevel(self.page3)
        self.top.title("Kilometrówka")

        label = tk.Label(
            self.top, text="Wprowadź liczbę przejechanych kilometrów:")
        label.pack(padx=10, pady=10)

        entry = tk.Entry(self.top)
        entry.pack(padx=10, pady=10)

        self.auto_do_900 = 0.89
        self.auto_ponad_900 = 1.15
        self.motocykl = 0.69
        self.motorower = 0.42

        label2 = tk.Label(self.top, text="Wybierz środek transportu:")
        label2.pack(padx=10, pady=10)

        option_var = tk.DoubleVar()

        option1 = Radiobutton(self.top, text="Auto z silnikiem o poj. do 900 cm3",
                              variable=option_var, value=self.auto_do_900)
        option2 = Radiobutton(self.top, text="Auto z silnikiem o poj. ponad 900 cm3",
                              variable=option_var, value=self.auto_ponad_900)
        option3 = Radiobutton(self.top, text="Motocykl",
                              variable=option_var, value=self.motocykl)
        option4 = Radiobutton(self.top, text="Motorower",
                              variable=option_var, value=self.motorower)
        option1.pack(padx=10, pady=5)
        option2.pack(padx=10, pady=5)
        option3.pack(padx=10, pady=5)
        option4.pack(padx=10, pady=5)

        def submit():
            try:
                self.kilometry = float(entry.get())
                self.stawka = option_var.get()
                self.ryczalt_auto = self.kilometry * self.stawka
                self.top.destroy()
            except ValueError:
                messagebox.showerror(
                    "Wystąpił błąd", "Aby przejść dalej musisz wprowadzić kilometry i wybrać środek transportu.")

        submit_button = tk.Button(self.top, text="POTWIERDŹ", command=submit)
        submit_button.pack(padx=10, pady=10)

    def rycz_komunikacja(self):
        try:
            s_rok = int(self.cal_start.get_date()[-4:])
            s_miesiac = int(self.cal_start.get_date()[4:5])
            s_dzien = int(self.cal_start.get_date()[:2])
            s_godzina = int(self.wybor_godziny_startu.get())
            s_minuta = int(self.wybor_minuty_startu.get())
            k_rok = int(self.cal_koniec.get_date()[-4:])
            k_miesiac = int(self.cal_koniec.get_date()[4:5])
            k_dzien = int(self.cal_koniec.get_date()[:2])
            k_godzina = int(self.wybor_godziny_konca.get())
            k_minuta = int(self.wybor_minuty_konca.get())
            data_startu = datetime(
                s_rok, s_miesiac, s_dzien, s_godzina, s_minuta)
            data_konca = datetime(
                k_rok, k_miesiac, k_dzien, k_godzina, k_minuta)
            czas_delegacji = data_konca - data_startu
            tsecs = czas_delegacji.total_seconds()
            self.thrs = tsecs/(60*60)
            self.full_days = self.thrs // 24
            remainder_hours = self.thrs % 24

            if remainder_hours > 0:
                self.full_days += 1

            self.ryczalt_komunikacja = self.full_days * 45 * 0.2

            return self.ryczalt_komunikacja
        except Exception as e:
            self.info = ("Wystąpił błąd:", e)
            messagebox.showinfo('Śliwka Coding Center ©', self.info)

    def checking_sniadaniedk(self):
        if self.var1dk.get():
            self.ilosc_sniadaniedk.config(state=NORMAL)
        else:
            self.ilosc_sniadaniedk.config(state=DISABLED)

    def checking_obiaddk(self):
        if self.var2dk.get():
            self.ilosc_obiaddk.config(state=NORMAL)
        else:
            self.ilosc_obiaddk.config(state=DISABLED)

    def checking_kolacjadk(self):
        if self.var3dk.get():
            self.ilosc_kolacjadk.config(state=NORMAL)
        else:
            self.ilosc_kolacjadk.config(state=DISABLED)

    def licz_diete(self):
        try:
            s_rok = int(self.cal_start.get_date()[-4:])
            s_miesiac = int(self.cal_start.get_date()[3:5])
            s_dzien = int(self.cal_start.get_date()[:2])
            s_godzina = int(self.wybor_godziny_startu.get())
            s_minuta = int(self.wybor_minuty_startu.get())
        except ValueError:
            info = ("Wprowadzono złą wartość godziny i/lub minuty")
            self.label_wynik.config(text=info)

        try:
            k_rok = int(self.cal_koniec.get_date()[-4:])
            k_miesiac = int(self.cal_koniec.get_date()[3:5])
            k_dzien = int(self.cal_koniec.get_date()[:2])
            k_godzina = int(self.wybor_godziny_konca.get())
            k_minuta = int(self.wybor_minuty_konca.get())
        except ValueError:
            info = ("Wprowadzono złą wartość godziny i/lub minuty")
            self.label_wynik.config(text=info)

        data_startu = datetime(s_rok, s_miesiac, s_dzien, s_godzina, s_minuta)
        data_konca = datetime(k_rok, k_miesiac, k_dzien, k_godzina, k_minuta)
        czas_delegacji = data_konca - data_startu
        tsecs = czas_delegacji.total_seconds()
        thrs = tsecs/(60*60)
        tmins = tsecs/60
        liczba_dni = int(thrs // 24)
        liczba_godzin = int(thrs) - int(liczba_dni*24)

        dieta = 45

        if liczba_dni == 0:
            liczba_minut = tmins - (liczba_godzin*60)
            nalezna_dieta_dzien = 0
            if liczba_godzin < 8:
                nalezna_dieta_godz = 0
            if 8 <= liczba_godzin < 12:
                nalezna_dieta_godz = 22.5
            if liczba_godzin >= 12:
                nalezna_dieta_godz = 45
        else:
            liczba_minut = tmins - (liczba_godzin*60) - (liczba_dni*24*60)
            nalezna_dieta_dzien = liczba_dni*dieta
            if liczba_godzin == 0:
                nalezna_dieta_godz = 0
            if 0 < liczba_godzin < 8:
                nalezna_dieta_godz = 22.5
            if liczba_godzin >= 8:
                nalezna_dieta_godz = 45

        try:
            sniadanie = int(self.ilosc_sniadaniedk.get()) * 11.25
        except ValueError:
            sniadanie = 0

        try:
            obiad = int(self.ilosc_obiaddk.get()) * 22.50
        except ValueError:
            obiad = 0

        try:
            kolacja = int(self.ilosc_kolacjadk.get()) * 11.25
        except ValueError:
            kolacja = 0

        if self.nocleg_var1.get():
            self.ryczalt_nocleg
            ryc_noc_info = (
                f"Za ryczałt za nocleg należy ci się dodatkowo {round(self.ryczalt_nocleg,2)} PLN.")
        else:
            self.ryczalt_nocleg = 0
            ryc_noc_info = ("")

        if self.auto_var2.get():
            self.ryczalt_auto
            ryc_auto_info = (
                f"Za ryczałt za pozdróż prywatnym środkiem transportu\n należy ci się dodatkowo {round(self.ryczalt_auto,2)} PLN.")
        else:
            self.ryczalt_auto = 0
            ryc_auto_info = ("")

        if self.komunikacja_var3.get():
            self.ryczalt_komunikacja
            ryc_kom_info = (
                f"Za ryczałt za dojazd środkami komunikacji miejscowej\n należy ci sie dodatkowo {round(self.ryczalt_komunikacja,2)} PLN.")
        else:
            self.ryczalt_komunikacja = 0
            ryc_kom_info = ("")

        zarcie = sniadanie + obiad + kolacja

        if zarcie != 0:
            zarcie_info = (
                f"Za zapewnione posiłki należy odjąć {round(zarcie,2)} PLN.")
        else:
            zarcie_info = ("")

        nalezna_dieta = nalezna_dieta_dzien + \
            nalezna_dieta_godz - sniadanie - obiad - kolacja + \
            self.ryczalt_nocleg + self.ryczalt_komunikacja + self.ryczalt_auto

        if int(liczba_dni) == 1:
            wersja_dzien = "dzień"
        else:
            wersja_dzien = "dni"

        if int(liczba_godzin) == 1:
            wersja_godzin = "godzinę"
        elif int(liczba_godzin) in range(2, 4):
            wersja_godzin = "godziny"
        else:
            wersja_godzin = "godzin"

        if int(liczba_minut) == 1:
            wersja_minut = "minutę"
        elif int(liczba_minut) in range(2, 4):
            wersja_minut = "minuty"
        else:
            wersja_minut = "minut"

        dodatki = zarcie + self.komunikacja_var3.get() + self.auto_var2.get() + \
            self.nocleg_var1.get()

        if dodatki != 0:
            result = (f"""
                Delegacja krajowa trwała \n{int(liczba_dni)} {wersja_dzien}, {int(liczba_godzin)} {wersja_godzin} i {int(liczba_minut)} {wersja_minut} ({round(nalezna_dieta_dzien,2)} PLN + {round(nalezna_dieta_godz,2)} PLN).\n
                {zarcie_info}
                {ryc_noc_info}
                {ryc_kom_info}
                {ryc_auto_info}
                Finalnie należy ci się {round(nalezna_dieta,2)} PLN.
                """)
        else:
            result = (f"""
                Delegacja krajowa trwała \n{int(liczba_dni)} {wersja_dzien}, {int(liczba_godzin)} {wersja_godzin} i {int(liczba_minut)} {wersja_minut} ({round(nalezna_dieta_dzien,2)} PLN + {round(nalezna_dieta_godz,2)} PLN).\n
                Finalnie należy ci się {round(nalezna_dieta,2)} PLN.
                """)

        self.label_wynik.config(text=result)

    def show_page(self, page):
        if self.current_page:
            self.current_page.grid_forget()
        page.grid(row=0, column=0, sticky="nsew")
        self.current_page = page

    def next_page1(self):
        self.show_page(self.page2)
        
    def back_page2(self):
        self.show_page(self.page1)

    def next_page2(self):
        self.show_page(self.page3)

    def next_page3(self):
        self.licz_diete()
        self.next_page4()

    def next_page4(self):
        self.show_page(self.page4)

    def back_page4(self):
        self.show_page(self.page3)

    def back_page3(self):
        self.show_page(self.page2)

    def on_close_window(self):
        self.back_to_menu()

    def back_to_menu(self):
        self.menu_app.show_menu()
        self.destroy()


class DietyZagraniczne(tk.Toplevel):
    def __init__(self, menu_app):
        super().__init__()
        self.menu_app = menu_app
        self.title("DIETY ZAGRANICZNE")
        self.protocol("WM_DELETE_WINDOW", self.on_close_window)
        self.current_page = None

        self.strona_pierwsza()
        self.strona_druga()
        self.strona_trzecia()
        self.strona_czwarta()

        self.show_page(self.page1)

    def on_close_window(self):
        self.back_to_menu()

    def back_to_menu(self):
        self.menu_app.show_menu()
        self.destroy()

    def strona_pierwsza(self):
        self.page1 = tk.Frame(self)

        kraj_container = tk.Frame(self.page1)
        kraj_container.grid(row=0, column=0, padx=5, pady=5, columnspan=5)

        label_wybierz_kraj = Label(
            kraj_container, text="Wskaż kraj docelowy delegacji: ")
        label_wybierz_kraj.grid(row=0, column=0, padx=5,
                                pady=5, sticky=E, columnspan=3)

        scrollbar = Scrollbar(kraj_container)
        scrollbar.grid(row=0, column=5, sticky=NS)

        self.wybor_kraju = Listbox(kraj_container, yscrollcommand=scrollbar.set,
                                   height=5, width=15, selectmode=SINGLE)
        for key in diet_zagranica:
            self.wybor_kraju.insert(END, str(key))

        self.wybor_kraju.grid(row=0, column=3, sticky=E, columnspan=2)
        scrollbar.config(command=self.wybor_kraju.yview)

        zlabel_start = Label(
            self.page1, text="Wybierz datę i godzinę opuszczenia Polski")
        zlabel_start.grid(row=1, column=0, sticky=EW,
                          padx=5, pady=5, columnspan=5)

        zlabel_godzina_startu = Label(self.page1, text="GODZINA")
        zlabel_godzina_startu.grid(row=2, column=3, padx=5, pady=5, sticky=S)
        zlabel_minuta_startu = Label(self.page1, text="MINUTA")
        zlabel_minuta_startu.grid(row=2, column=4, padx=5, pady=5, sticky=S)

        self.zcal_start = Calendar(self.page1, selectmode='day',
                                   date_pattern='dd/mm/yyyy', locale='pl_PL')
        self.date = self.zcal_start.datetime.today()
        self.zcal_start.grid(row=2, column=0, padx=5, pady=5,
                             sticky=N, rowspan=3, columnspan=3)

        self.godzinysz = IntVar()
        self.zwybor_godziny_startu = Spinbox(
            self.page1, width=5, wrap=True, values=godziny)
        self.zwybor_godziny_startu.grid(
            row=3, column=3, padx=5, pady=5, sticky=N)
        self.minutysz = IntVar()
        self.zwybor_minuty_startu = Spinbox(
            self.page1, width=5, wrap=True, values=minuty)
        self.zwybor_minuty_startu.grid(
            row=3, column=4, padx=5, pady=5, sticky=N)

        button_container = tk.Frame(self.page1)
        button_container.grid(row=5, column=0, padx=5, pady=5, columnspan=5)

        self.back_button = tk.Button(
            button_container, text="STAWKI DIET ZAGRANICZNYCH", command=self.stawki_diet_zagra)
        self.back_button.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.back_button = tk.Button(
            button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=1, column=0, sticky=E, padx=5, pady=5)

        self.button_next_page2 = tk.Button(
            button_container, text="DALEJ", command=self.next_page1)
        self.button_next_page2.grid(row=1, column=1, sticky=W, padx=5, pady=5)

    def strona_druga(self):
        self.page2 = tk.Frame(self)
        zlabel_start = Label(
            self.page2, text="Wybierz datę i godzinę powrotu do Polski")
        zlabel_start.grid(row=0, column=0, sticky=EW,
                          padx=5, pady=5, columnspan=8)

        self.zcal_koniec = Calendar(self.page2, selectmode='day',
                                    date_pattern='dd/mm/yyyy', locale='pl_PL')
        self.date = self.zcal_koniec.datetime.today()
        self.zcal_koniec.grid(row=1, column=0, padx=5, pady=5,
                              sticky=N, rowspan=3, columnspan=3)

        zlabel_godzina_konca = Label(self.page2, text="GODZINA")
        zlabel_godzina_konca.grid(row=1, column=3, padx=5, pady=5, sticky=S)
        zlabel_minuta_konca = Label(self.page2, text="MINUTA")
        zlabel_minuta_konca.grid(row=1, column=4, padx=5, pady=5, sticky=S)

        self.godzinykz = IntVar()
        self.zwybor_godziny_konca = Spinbox(
            self.page2, width=5, wrap=True, values=godziny)
        self.zwybor_godziny_konca.grid(
            row=2, column=3, padx=5, pady=5, sticky=N)
        self.minutykz = IntVar()
        self.zwybor_minuty_konca = Spinbox(
            self.page2, width=5, wrap=True, values=minuty)
        self.zwybor_minuty_konca.grid(
            row=2, column=4, padx=5, pady=5, sticky=N)

        button_container = tk.Frame(self.page2)
        button_container.grid(row=4, column=0, padx=5, pady=5, columnspan=8)

        self.button_back_page2 = tk.Button(
            button_container, text="WSTECZ", command=self.back_page2)
        self.button_back_page2.grid(row=0, column=0, padx=5, pady=5)

        self.back_button = tk.Button(
            button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=1, padx=5, pady=5)

        self.button_next_page2 = tk.Button(
            button_container, text="DALEJ", command=self.next_page2)
        self.button_next_page2.grid(row=0, column=2, columnspan=2, padx=5, pady=5)

    def strona_trzecia(self):
        self.page3 = tk.Frame(self)
        self.zlabel_posilki = Label(
            self.page3, text="Wskaż posiłki zapewnione podczas delegacji zagranicznej")
        self.zlabel_posilki.grid(
            row=0, column=0, sticky=EW, padx=5, pady=5, columnspan=8)

        self.zvar1 = IntVar()
        self.zcheck_sniadanie = Checkbutton(self.page3, text="ŚNIADANIE", onvalue=1,
                                            offvalue=0, command=self.zchecking_sniadanie, variable=self.zvar1)
        self.zcheck_sniadanie.grid(row=1, column=0, padx=50,
                                   pady=5, sticky=W, columnspan=2)
        self.zlabel_sniadanie = Label(self.page3, text="w ilości")
        self.zlabel_sniadanie.grid(row=1, column=2, sticky=E, padx=5, pady=5)
        self.zilosc_sniadanie = Entry(self.page3, width=5, state=DISABLED)
        self.zilosc_sniadanie.grid(row=1, column=3, sticky=W, padx=5, pady=5)

        self.zvar2 = IntVar()
        self.zcheck_obiad = Checkbutton(self.page3, text="OBIAD", onvalue=1,
                                        offvalue=0, command=self.zchecking_obiad, variable=self.zvar2)
        self.zcheck_obiad.grid(row=2, column=0, padx=50,
                               pady=5, sticky=W, columnspan=2)
        self.zlabel_obiad = Label(self.page3, text="w ilości")
        self.zlabel_obiad.grid(row=2, column=2, sticky=E, padx=5, pady=5)
        self.zilosc_obiad = Entry(self.page3, width=5, state=DISABLED)
        self.zilosc_obiad.grid(row=2, column=3, sticky=W, padx=5, pady=5)

        self.zvar3 = IntVar()
        self.zcheck_kolacja = Checkbutton(self.page3, text="KOLACJA", onvalue=1,
                                          offvalue=0, command=self.zchecking_kolacja, variable=self.zvar3)
        self.zcheck_kolacja.grid(
            row=3, column=0, padx=50, pady=5, sticky=W, columnspan=2)
        self.zlabel_kolacja = Label(self.page3, text="w ilości")
        self.zlabel_kolacja.grid(row=3, column=2, sticky=E, padx=5, pady=5)
        self.zilosc_kolacja = Entry(self.page3, width=5, state=DISABLED)
        self.zilosc_kolacja.grid(row=3, column=3, sticky=W, padx=5, pady=5)

        self.label_dodatki = Label(
            self.page3, text="Wskaż przysługujące ci ryczałty")
        self.label_dodatki.grid(
            row=4, column=0, sticky=EW, padx=5, pady=5, columnspan=8)

        self.nocleg_var1 = tk.BooleanVar()
        self.auto_var2 = tk.BooleanVar()
        self.komunikacja_var3 = tk.BooleanVar()
        self.dojazd_do_var4 = tk.BooleanVar()
        self.dojazd_z_var5 = tk.BooleanVar()

        self.checkframe = Frame(self.page3)
        self.checkframe.grid(row=5, column=0, columnspan=8)

        self.check_nocleg = Checkbutton(
            self.checkframe, text="NOCLEG", variable=self.nocleg_var1, command=self.rycz_nocleg)
        self.check_auto = Checkbutton(
            self.checkframe, text="PRYWATNE AUTO", variable=self.auto_var2, command=self.rycz_auto)
        self.check_komunikacja = Checkbutton(
            self.checkframe, text="KOMUNIKACJA MIEJSCOWA", variable=self.komunikacja_var3, command=self.rycz_komunikacja)
        self.check_dojazd_do = Checkbutton(
            self.checkframe, text="DOJAZD DO LOTNISKA", variable=self.dojazd_do_var4, command=self.rycz_dojazd_do)
        self.check_dojazd_z = Checkbutton(
            self.checkframe, text="DOJAZD Z LOTNISKA", variable=self.dojazd_z_var5, command=self.rycz_dojazd_z)
        self.check_nocleg.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.check_auto.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.check_komunikacja.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        self.check_dojazd_do.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        self.check_dojazd_z.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        self.button_container = tk.Frame(self.page3)
        self.button_container.grid(
            row=8, column=0, padx=5, pady=5, columnspan=8)

        self.button_back_page2 = tk.Button(
            self.button_container, text="WSTECZ", command=self.back_page3)
        self.button_back_page2.grid(row=0, column=0, sticky=E, padx=5, pady=5)

        self.back_button = tk.Button(
            self.button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=1, padx=5, pady=5)

        self.button_next_page2 = tk.Button(
            self.button_container, text="DALEJ", command=self.next_page3)
        self.button_next_page2.grid(row=0, column=2, sticky=W, padx=5, pady=5)

    def strona_czwarta(self):
        self.page4 = tk.Frame(self)

        self.zlabel_wynik = Label(self.page4)
        self.zlabel_wynik.grid(row=0, column=0, padx=5, pady=5, columnspan=8)

        button_container = tk.Frame(self.page4)
        button_container.grid(row=1, column=0, padx=5, pady=5, columnspan=8)

        self.button_back_page2 = tk.Button(
            button_container, text="WSTECZ", command=self.back_page4)
        self.button_back_page2.grid(row=0, column=0, sticky=E, padx=5, pady=5)

        self.back_button = tk.Button(
            button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=1, sticky=W, padx=5, pady=5)

    def stawki_diet_zagra(self):
        self.window = Toplevel()
        self.window.title("STAWKI DIET ZAGRANICZNYCH")
        self.window.resizable(True, True)

        self.frame = ttk.Frame(self.window, padding=5)
        self.frame.pack(fill="both", expand=True)

        self.table = ttk.Treeview(self.frame, columns=(
            "Kraj", "Stawka", "Limity"), show="headings")
        self.table.heading("Kraj", text="Kraj")
        self.table.heading("Stawka", text="Stawka diety")
        self.table.heading("Limity", text="Limity hotelowe")

        self.table.column("Kraj", width=180)
        self.table.column("Stawka", width=100)
        self.table.column("Limity", width=100)

        for kraj, (waluta, stawka, limit) in diet_zagranica.items():
            self.table.insert("", "end", values=(
                kraj, f"{stawka} {waluta}", f"{limit} {waluta} "))

        self.scroll = ttk.Scrollbar(
            self.frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=self.scroll.set)
        self.scroll.pack(side="right", fill="y")
        self.table.pack(fill="both", expand=True)

    def rycz_dojazd_do(self):
        try:
            zet = str(self.wybor_kraju.get(ACTIVE))
            igrek = diet_zagranica[zet]
            dieta = igrek[1]
            self.ryczalt_dojazd_do = dieta/2
            return self.ryczalt_dojazd_do
        except Exception as e:
            self.info = ("Wystąpił błąd:", e)
            messagebox.showinfo('Śliwka Coding Center ©', self.info)

    def rycz_dojazd_z(self):
        try:
            zet = str(self.wybor_kraju.get(ACTIVE))
            igrek = diet_zagranica[zet]
            dieta = igrek[1]
            self.ryczalt_dojazd_z = dieta/2
            return self.ryczalt_dojazd_z
        except Exception as e:
            self.info = ("Wystąpił błąd:", e)
            messagebox.showinfo('Śliwka Coding Center ©', self.info)

    def rycz_nocleg(self):
        try:
            zet = str(self.wybor_kraju.get(ACTIVE))
            igrek = diet_zagranica[zet]
            hotel = igrek[2]
            s_rok = int(self.zcal_start.get_date()[-4:])
            s_miesiac = int(self.zcal_start.get_date()[3:5])
            s_dzien = int(self.zcal_start.get_date()[:2])
            s_godzina = int(self.zwybor_godziny_startu.get())
            s_minuta = int(self.zwybor_minuty_startu.get())
            k_rok = int(self.zcal_koniec.get_date()[-4:])
            k_miesiac = int(self.zcal_koniec.get_date()[3:5])
            k_dzien = int(self.zcal_koniec.get_date()[:2])
            k_godzina = int(self.zwybor_godziny_konca.get())
            k_minuta = int(self.zwybor_minuty_konca.get())
            data_startu = datetime(
                s_rok, s_miesiac, s_dzien, s_godzina, s_minuta)
            data_konca = datetime(
                k_rok, k_miesiac, k_dzien, k_godzina, k_minuta)
            czas_delegacji = data_konca - data_startu
            tsecs = czas_delegacji.total_seconds()
            thrs = tsecs/(60*60)
            self.liczba_dni = int(thrs // 24)
            self.ryczalt_nocleg = self.liczba_dni * hotel * 0.25
            return self.ryczalt_nocleg
        except Exception as e:
            self.info = ("Wystąpił błąd:", e)
            messagebox.showinfo('Śliwka Coding Center ©', self.info)

    def rycz_auto(self):
        self.top = tk.Toplevel(self.page3)
        self.top.title("Kilometrówka")

        label = tk.Label(
            self.top, text="Wprowadź liczbę przejechanych kilometrów:")
        label.pack(padx=10, pady=10)

        entry = tk.Entry(self.top)
        entry.pack(padx=10, pady=10)

        self.auto_do_900 = 0.89
        self.auto_ponad_900 = 1.15
        self.motocykl = 0.69
        self.motorower = 0.42

        label2 = tk.Label(self.top, text="Wybierz środek transportu:")
        label2.pack(padx=10, pady=10)

        option_var = tk.DoubleVar()

        option1 = Radiobutton(self.top, text="Auto z silnikiem o poj. do 900 cm3",
                              variable=option_var, value=self.auto_do_900)
        option2 = Radiobutton(self.top, text="Auto z silnikiem o poj. ponad 900 cm3",
                              variable=option_var, value=self.auto_ponad_900)
        option3 = Radiobutton(self.top, text="Motocykl",
                              variable=option_var, value=self.motocykl)
        option4 = Radiobutton(self.top, text="Motorower",
                              variable=option_var, value=self.motorower)
        option1.pack(padx=10, pady=5)
        option2.pack(padx=10, pady=5)
        option3.pack(padx=10, pady=5)
        option4.pack(padx=10, pady=5)

        def submit():
            try:
                self.kilometry = float(entry.get())
                self.stawka = option_var.get()
                self.ryczalt_auto = self.kilometry * self.stawka
                self.top.destroy()
            except ValueError:
                messagebox.showerror(
                    "Wystąpił błąd", "Aby przejść dalej musisz wprowadzić kilometry i wybrać środek transportu.")

        submit_button = tk.Button(self.top, text="POTWIERDŹ", command=submit)
        submit_button.pack(padx=10, pady=10)

    def rycz_komunikacja(self):
        try:
            zet = str(self.wybor_kraju.get(ACTIVE))
            igrek = diet_zagranica[zet]
            dieta = igrek[1]
            s_rok = int(self.zcal_start.get_date()[-4:])
            s_miesiac = int(self.zcal_start.get_date()[3:5])
            s_dzien = int(self.zcal_start.get_date()[:2])
            s_godzina = int(self.zwybor_godziny_startu.get())
            s_minuta = int(self.zwybor_minuty_startu.get())
            k_rok = int(self.zcal_koniec.get_date()[-4:])
            k_miesiac = int(self.zcal_koniec.get_date()[3:5])
            k_dzien = int(self.zcal_koniec.get_date()[:2])
            k_godzina = int(self.zwybor_godziny_konca.get())
            k_minuta = int(self.zwybor_minuty_konca.get())
            data_startu = datetime(
                s_rok, s_miesiac, s_dzien, s_godzina, s_minuta)
            data_konca = datetime(
                k_rok, k_miesiac, k_dzien, k_godzina, k_minuta)
            czas_delegacji = data_konca - data_startu
            tsecs = czas_delegacji.total_seconds()
            self.thrs = tsecs/(60*60)
            self.full_days = self.thrs // 24
            remainder_hours = self.thrs % 24

            if remainder_hours > 0:
                self.full_days += 1

            self.ryczalt_komunikacja = self.full_days * dieta * 0.1

            return self.ryczalt_komunikacja
        except Exception as e:
            self.info = ("Wystąpił błąd:", e)
            messagebox.showinfo('Śliwka Coding Center ©', self.info)

    def licz_diete_zagra(self):
        zet = str(self.wybor_kraju.get(ACTIVE))
        igrek = diet_zagranica[zet]
        omega = igrek[0]
        beta = igrek[1]
        dieta = int(beta)
        gamma = zagranica_odmiana[zet]

        try:
            s_rok = int(self.zcal_start.get_date()[-4:])
            s_miesiac = int(self.zcal_start.get_date()[3:5])
            s_dzien = int(self.zcal_start.get_date()[:2])
            s_godzina = int(self.zwybor_godziny_startu.get())
            s_minuta = int(self.zwybor_minuty_startu.get())
        except ValueError:
            info = ("Wprowadzono złą wartość godziny i/lub minuty")
            self.zlabel_wynik.config(text=info)

        try:
            k_rok = int(self.zcal_koniec.get_date()[-4:])
            k_miesiac = int(self.zcal_koniec.get_date()[3:5])
            k_dzien = int(self.zcal_koniec.get_date()[:2])
            k_godzina = int(self.zwybor_godziny_konca.get())
            k_minuta = int(self.zwybor_minuty_konca.get())
        except ValueError:
            info = ("Wprowadzono złą wartość godziny i/lub minuty")
            self.zlabel_wynik.config(text=info)
        data_startu = datetime(s_rok, s_miesiac, s_dzien, s_godzina, s_minuta)
        data_konca = datetime(k_rok, k_miesiac, k_dzien, k_godzina, k_minuta)
        czas_delegacji = data_konca - data_startu
        tsecs = czas_delegacji.total_seconds()
        thrs = tsecs/(60*60)
        tmins = tsecs/60
        liczba_dni = int(thrs // 24)
        liczba_godzin = int(thrs) - int(liczba_dni*24)

        if liczba_dni == 0:
            liczba_minut = tmins - (liczba_godzin*60)
            nalezna_dieta_dzien = 0
        else:
            liczba_minut = tmins - (liczba_godzin*60) - (liczba_dni*24*60)
            nalezna_dieta_dzien = liczba_dni*dieta

        if liczba_godzin == 0:
            nalezna_dieta_godz = 0
        if 0 < liczba_godzin < 8:
            nalezna_dieta_godz = dieta/3
        if 8 <= liczba_godzin < 12:
            nalezna_dieta_godz = dieta * 0.5
        if liczba_godzin >= 12:
            nalezna_dieta_godz = dieta

        try:
            sniadanie = int(self.zilosc_sniadanie.get()) * (dieta * 0.15)
        except ValueError:
            sniadanie = 0

        try:
            obiad = int(self.zilosc_obiad.get()) * (dieta * 0.3)
        except ValueError:
            obiad = 0

        try:
            kolacja = int(self.zilosc_kolacja.get()) * (dieta * 0.3)
        except ValueError:
            kolacja = 0

        if self.nocleg_var1.get():
            self.ryczalt_nocleg
            ryc_noc_info = (
                f"Za ryczałt za nocleg należy ci się dodatkowo {round(self.ryczalt_nocleg,2)} PLN.")
        else:
            self.ryczalt_nocleg = 0
            ryc_noc_info = ("")

        if self.auto_var2.get():
            self.ryczalt_auto
            ryc_auto_info = (
                f"Za ryczałt za pozdróż prywatnym środkiem transportu\n należy ci się dodatkowo {round(self.ryczalt_auto,2)} PLN.")
        else:
            self.ryczalt_auto = 0
            ryc_auto_info = ("")

        if self.komunikacja_var3.get():
            self.ryczalt_komunikacja
            ryc_kom_info = (
                f"Za ryczałt za dojazd środkami komunikacji miejscowej\n należy ci sie dodatkowo {round(self.ryczalt_komunikacja,2)} PLN.")
        else:
            self.ryczalt_komunikacja = 0
            ryc_kom_info = ("")

        if self.dojazd_do_var4.get():
            self.ryczalt_dojazd_do
            ryc_dojazd_do = (
                f"Za ryczałt za dojazd do lotniska należy ci sie dodatkowo {round(self.ryczalt_dojazd_do,2)} PLN.")
        else:
            self.ryczalt_dojazd_do = 0
            ryc_dojazd_do = ("")

        if self.dojazd_z_var5.get():
            self.ryczalt_dojazd_z
            ryc_dojazd_z = (
                f"Za ryczałt za dojazd z lotniska należy ci sie dodatkowo {round(self.ryczalt_dojazd_z,2)} PLN.")
        else:
            self.ryczalt_dojazd_z = 0
            ryc_dojazd_z = ("")

        zarcie = sniadanie + obiad + kolacja

        if zarcie != 0:
            zarcie_info = (
                f"Za zapewnione posiłki należy odjąć {round(zarcie,2)} PLN.")
        else:
            zarcie_info = ("")

        nalezna_dieta = nalezna_dieta_dzien + \
            nalezna_dieta_godz - sniadanie - obiad - kolacja + \
            self.ryczalt_nocleg + self.ryczalt_komunikacja + self.ryczalt_auto

        if int(liczba_dni) == 1:
            wersja_dzien = "dzień"
        else:
            wersja_dzien = "dni"

        if int(liczba_godzin) == 1:
            wersja_godzin = "godzinę"
        elif int(liczba_godzin) in range(2, 4):
            wersja_godzin = "godziny"
        else:
            wersja_godzin = "godzin"

        if int(liczba_minut) == 1:
            wersja_minut = "minutę"
        elif int(liczba_minut) in range(2, 4):
            wersja_minut = "minuty"
        else:
            wersja_minut = "minut"

        dodatki = zarcie + self.dojazd_z_var5.get() + self.dojazd_do_var4.get() + \
            self.komunikacja_var3.get() + self.auto_var2.get() + self.nocleg_var1.get()

        if dodatki != 0:
            result = (f"""
                Delegacja {gamma} trwała \n{int(liczba_dni)} {wersja_dzien}, {int(liczba_godzin)} {wersja_godzin} i {int(liczba_minut)} {wersja_minut} ({round(nalezna_dieta_dzien,2)} {omega} + {round(nalezna_dieta_godz,2)} {omega}).\n
                {zarcie_info}
                {ryc_noc_info}
                {ryc_kom_info}
                {ryc_auto_info}
                {ryc_dojazd_do}
                {ryc_dojazd_z}
                Finalnie należy ci się {round(nalezna_dieta,2)} {omega}.
                """)
        else:
            result = (f"""
                Delegacja {gamma} trwała \n{int(liczba_dni)} {wersja_dzien}, {int(liczba_godzin)} {wersja_godzin} i {int(liczba_minut)} {wersja_minut} ({round(nalezna_dieta_dzien,2)} {omega} + {round(nalezna_dieta_godz,2)} {omega}).\n
                Finalnie należy ci się {round(nalezna_dieta,2)} {omega}.
                """)

        self.zlabel_wynik.config(text=result)

    def zchecking_sniadanie(self):
        if self.zvar1.get():
            self.zilosc_sniadanie.config(state=NORMAL)
        else:
            self.zilosc_sniadanie.config(state=DISABLED)

    def zchecking_obiad(self):
        if self.zvar2.get():
            self.zilosc_obiad.config(state=NORMAL)
        else:
            self.zilosc_obiad.config(state=DISABLED)

    def zchecking_kolacja(self):
        if self.zvar3.get():
            self.zilosc_kolacja.config(state=NORMAL)
        else:
            self.zilosc_kolacja.config(state=DISABLED)

    def show_page(self, page):
        if self.current_page:
            self.current_page.grid_forget()
        page.grid(row=0, column=0, sticky="nsew")
        self.current_page = page

    def next_page1(self):
        self.show_page(self.page2)

    def back_page2(self):
        self.show_page(self.page1)

    def next_page2(self):
        self.show_page(self.page3)

    def next_page3(self):
        self.licz_diete_zagra()
        self.next_page4()

    def next_page4(self):
        self.show_page(self.page4)

    def back_page4(self):
        self.show_page(self.page3)

    def back_page3(self):
        self.show_page(self.page2)

    def on_close_window(self):
        self.back_to_menu()

    def back_to_menu(self):
        self.menu_app.show_menu()
        self.destroy()


class PESEL(tk.Toplevel):
    data = ''
    women_names = ["ANNA", "KATARZYNA", "MARIA", "MAŁGORZATA", "AGNIESZKA", "BARBARA", "EWA", "MAGDALENA", "ELŻBIETA", "KRYSTYNA", "JOANNA",
                   "ALEKSANDRA", "MONIKA", "ZOFIA", "TERESA", "NATALIA", "JULIA", "DANUTA", "KAROLINA", "MARTA", "BEATA", "DOROTA", "ALICJA", "HALINA",
                   "JADWIGA", "JOLANTA", "IWONA", "GRAŻYNA", "JANINA", "PAULINA", "ZUZANNA", "JUSTYNA", "IRENA", "HANNA", "WIKTORIA",
                   "BOŻENA", "RENATA", "URSZULA", "AGATA", "SYLWIA", "MAJA", "PATRYCJA", "HELENA", "IZABELA", "EMILIA", "OLIWIA", "ANETA", "WERONIKA",
                   "EWELINA", "MARTYNA", "KLAUDIA", "GABRIELA", "MARZENA", "LENA", "DOMINIKA", "MARIANNA", "AMELIA", "KINGA",
                   "STANISŁAWA", "EDYTA", "KAMILA", "WIESŁAWA", "ALINA", "WANDA", "DARIA", "LIDIA", "MARIOLA", "LUCYNA", "NIKOLA", "MILENA", "WIOLETTA",
                   "MIROSŁAWA", "LAURA", "ANTONINA", "ANGELIKA", "OLGA", "KAZIMIERA", "BOGUMIŁA", "ILONA", "MICHALINA", "SANDRA", "GENOWEFA", "KORNELIA",
                   "MARLENA", "HENRYKA", "ŁUCJA", "SABINA", "BOGUSŁAWA", "NINA", "JÓZEFA", "ANITA", "STEFANIA", "IGA", "LILIANA", "REGINA", "POLA",
                   "MARCELINA", "JAGODA", "CZESŁAWA", "ANIELA", "WŁADYSŁAWA", "KARINA", "WIOLETA", "ADRIANNA", "DIANA", "ROKSANA",
                   "DAGMARA", "SARA", "MALWINA", "ELIZA", "CECYLIA", "ŻANETA", "ZDZISŁAWA", "KLARA", "RÓŻA", "KAJA", "LEOKADIA", "BLANKA", "ANASTAZJA", "BRONISŁAWA",
                   "EUGENIA", "JULITA", "ALDONA", "ROZALIA", "DANIELA", "LILIANNA", "MAGDA", "CELINA", "MATYLDA", "ADRIANA", "HONORATA", "VERONIKA",
                   "NELA", "PAULA", "BRYGIDA", "AURELIA", "KALINA", "MARIKA", "GERTRUDA", "MIECZYSŁAWA", "SONIA", "ELWIRA", "ANDŻELIKA", "POLINA",
                   "ARLETA", "LUIZA", "ADELA", "JUDYTA", "NICOLE", "FRANCISZKA", "MARIANA", "NICOLA", "LIWIA", "JOWITA", "VANESSA", "ALFREDA"]
    women_surnames = ["NOWAK", "KOWALSKA", "WIŚNIEWSKA", "WÓJCIK", "KOWALCZYK", "KAMIŃSKA", "LEWANDOWSKA", "ZIELIŃSKA", "SZYMAŃSKA", "DĄBROWSKA",
                      "WOŹNIAK", "KOZŁOWSKA", "MAZUR", "JANKOWSKA", "KWIATKOWSKA", "WOJCIECHOWSKA", "KRAWCZYK", "KACZMAREK", "PIOTROWSKA", "GRABOWSKA", "PAWŁOWSKA",
                      "MICHALSKA", "KRÓL", "ZAJĄC", "WIECZOREK", "JABŁOŃSKA", "WRÓBEL", "NOWAKOWSKA", "MAJEWSKA", "OLSZEWSKA", "ADAMCZYK", "JAWORSKA", "MALINOWSKA",
                      "STĘPIEŃ", "DUDEK", "GÓRSKA", "NOWICKA", "WITKOWSKA", "PAWLAK", "SIKORA", "WALCZAK", "RUTKOWSKA", "MICHALAK", "SZEWCZYK", "OSTROWSKA", "BARAN",
                      "TOMASZEWSKA", "ZALEWSKA", "WRÓBLEWSKA", "PIETRZAK", "JASIŃSKA", "MARCINIAK", "SADOWSKA", "JAKUBOWSKA", "ZAWADZKA", "DUDA", "WŁODARCZYK",
                      "CHMIELEWSKA", "BORKOWSKA", "BĄK", "WILK", "SOKOŁOWSKA", "SZCZEPAŃSKA", "SAWICKA", "LIS", "KUCHARSKA", "KALINOWSKA", "MACIEJEWSKA", "MAZUREK",
                      "WYSOCKA", "KUBIAK", "KOŁODZIEJ", "CZARNECKA", "KAŹMIERCZAK", "URBAŃSKA", "SIKORSKA", "KRUPA", "SOBCZAK", "KRAJEWSKA", "GŁOWACKA", "ZAKRZEWSKA",
                      "WASILEWSKA", "LASKOWSKA", "ZIÓŁKOWSKA", "GAJEWSKA", "KOZAK", "SZULC", "MRÓZ", "MAKOWSKA", "BRZEZIŃSKA", "PRZYBYLSKA", "KACZMARCZYK",
                      "BARANOWSKA", "SZYMCZAK", "ADAMSKA", "BŁASZCZYK", "BOROWSKA", "GÓRECKA", "SZCZEPANIAK", "KANIA", "LESZCZYŃSKA", "JANIK", "CZERWIŃSKA",
                      "CHOJNACKA", "LIPIŃSKA", "ANDRZEJEWSKA", "WESOŁOWSKA", "KOWALEWSKA", "MIKOŁAJCZYK", "MUCHA", "CIEŚLAK", "JAROSZ", "ZIĘBA", "KONIECZNA",
                      "KOZIOŁ", "MARKOWSKA", "KOWALIK", "KOŁODZIEJCZYK", "MUSIAŁ", "BRZOZOWSKA", "DOMAŃSKA", "TOMCZYK", "ORŁOWSKA", "PAWLIK", "PIĄTEK", "NOWACKA",
                      "KOPEĆ", "TOMCZAK", "KRUK", "KUREK", "ŻAK", "CIESIELSKA", "KOT", "MARKIEWICZ", "POLAK", "WAWRZYNIAK", "WOLSKA", "WÓJTOWICZ", "STANKIEWICZ",
                      "JASTRZĘBSKA", "SOWA", "URBANIAK", "KARPIŃSKA", "CZAJKOWSKA", "STASIAK", "WIERZBICKA", "ŁUCZAK", "NAWROCKA", "PIASECKA", "KLIMEK", "DZIEDZIC",
                      "SOSNOWSKA", "JANICKA", "BEDNAREK", "BIELECKA", "MILEWSKA", "GAJDA", "STEFAŃSKA", "MADEJ", "MAJCHRZAK", "LEŚNIAK", "JÓŹWIAK", "MAJ", "URBAN",
                      "KOWAL", "ŚLIWIŃSKA", "SKIBA", "MAŁECKA", "BEDNARCZYK", "SOCHA", "DOBROWOLSKA", "MICHALIK", "ROMANOWSKA", "DOMAGAŁA", "RATAJCZAK", "WRONA",
                      "WILCZYŃSKA", "KASPRZAK", "MATUSZEWSKA", "ORZECHOWSKA", "ŚWIĄTEK", "OLEJNICZAK", "PAJĄK", "RYBAK", "KUROWSKA", "BUKOWSKA", "SOBOLEWSKA",
                      "OWCZAREK", "MAZURKIEWICZ", "ŁUKASIK", "ROGOWSKA", "OLEJNIK", "GRZELAK", "KĘDZIERSKA", "KOSIŃSKA", "BARAŃSKA", "MATUSIAK", "SOBCZYK"]
    men_names = ["PIOTR", "KRZYSZTOF", "ANDRZEJ", "TOMASZ", "PAWEŁ", "MICHAŁ", "JAN", "MARCIN", "JAKUB", "ADAM", "ŁUKASZ", "MAREK", "GRZEGORZ",
                 "MATEUSZ", "STANISŁAW", "WOJCIECH", "MARIUSZ", "DARIUSZ", "MACIEJ", "ZBIGNIEW", "RAFAŁ", "ROBERT", "KAMIL", "JERZY", "DAWID",
                 "SZYMON", "JACEK", "KACPER", "JÓZEF", "RYSZARD", "TADEUSZ", "BARTOSZ", "ARTUR", "JAROSŁAW", "SŁAWOMIR", "SEBASTIAN", "JANUSZ",
                 "DAMIAN", "MIROSŁAW", "PATRYK", "ROMAN", "DANIEL", "FILIP", "HENRYK", "ANTONI", "PRZEMYSŁAW", "KAROL", "ALEKSANDER", "ADRIAN",
                 "KAZIMIERZ", "WIESŁAW", "MARIAN", "ARKADIUSZ", "DOMINIK", "FRANCISZEK", "MIKOŁAJ", "BARTŁOMIEJ", "LESZEK", "WIKTOR", "KRYSTIAN",
                 "WALDEMAR", "RADOSŁAW", "BOGDAN", "ZDZISŁAW", "KONRAD", "IGOR", "HUBERT", "EDWARD", "MIECZYSŁAW", "OSKAR", "MARCEL", "WŁADYSŁAW",
                 "CZESŁAW", "MAKSYMILIAN", "EUGENIUSZ", "MIŁOSZ", "BOGUSŁAW", "IRENEUSZ", "NIKODEM", "STEFAN", "WITOLD", "LEON", "OLIWIER", "SYLWESTER",
                 "ZYGMUNT", "ALAN", "WŁODZIMIERZ", "CEZARY", "ZENON", "GABRIEL", "IGNACY", "JULIAN", "NORBERT", "TYMON", "TYMOTEUSZ", "FABIAN", "BŁAŻEJ",
                 "ERYK", "EMIL", "LECH", "BRONISŁAW", "WACŁAW", "NATAN", "KSAWERY", "BORYS", "BOLESŁAW", "REMIGIUSZ", "OLAF", "BERNARD", "KAJETAN", "KUBA",
                 "EDMUND", "LUCJAN", "BRUNO", "ALBERT", "TOBIASZ", "ROMUALD", "GRACJAN", "SEWERYN", "SZCZEPAN", "ALFRED", "ERNEST", "JOACHIM", "LUDWIK",
                 "LESŁAW", "BOGUMIŁ", "JĘDRZEJ", "GERARD", "FELIKS", "LEONARD", "JULIUSZ", "KLAUDIUSZ", "DORIAN", "TEODOR"]
    men_surnames = ["NOWAK", "KOWALSKI", "WIŚNIEWSKI", "WÓJCIK", "KOWALCZYK", "KAMIŃSKI", "LEWANDOWSKI", "ZIELIŃSKI", "WOŹNIAK", "ZYMAŃSKI", "DĄBROWSKI",
                    "KOZŁOWSKI", "MAZUR", "JANKOWSKI", "KWIATKOWSKI", "WOJCIECHOWSKI", "KRAWCZYK", "KACZMAREK", "PIOTROWSKI", "GRABOWSKI", "ZAJĄC",
                    "PAWŁOWSKI", "KRÓL", "MICHALSKI", "WRÓBEL", "WIECZOREK", "JABŁOŃSKI", "NOWAKOWSKI", "MAJEWSKI", "OLSZEWSKI", "DUDEK", "JAWORSKI",
                    "STĘPIEŃ", "MALINOWSKI", "ADAMCZYK", "GÓRSKI", "PAWLAK", "SIKORA", "NOWICKI", "WITKOWSKI", "RUTKOWSKI", "WALCZAK", "BARAN", "MICHALAK",
                    "SZEWCZYK", "OSTROWSKI", "TOMASZEWSKI", "ZALEWSKI", "WRÓBLEWSKI", "PIETRZAK", "JASIŃSKI", "DUDA", "MARCINIAK", "SADOWSKI", "BĄK",
                    "ZAWADZKI", "JAKUBOWSKI", "WILK", "CHMIELEWSKI", "BORKOWSKI", "WŁODARCZYK", "SOKOŁOWSKI", "SZCZEPAŃSKI", "SAWICKI", "LIS", "KUCHARSKI",
                    "KALINOWSKI", "WYSOCKI", "MAZUREK", "KUBIAK", "MACIEJEWSKI", "KOŁODZIEJ", "KAŹMIERCZAK", "CZARNECKI", "KONIECZNY", "SOBCZAK", "KRUPA",
                    "GŁOWACKI", "URBAŃSKI", "MRÓZ", "ZAKRZEWSKI", "WASILEWSKI", "KRAJEWSKI", "KOZAK", "LASKOWSKI", "SIKORSKI", "ZIÓŁKOWSKI", "GAJEWSKI", "SZULC",
                    "MAKOWSKI", "KACZMARCZYK", "BRZEZIŃSKI", "BARANOWSKI", "PRZYBYLSKI", "KANIA", "SZYMCZAK", "JANIK", "BOROWSKI", "BŁASZCZYK", "ADAMSKI",
                    "GÓRECKI", "SZCZEPANIAK", "CHOJNACKI", "LESZCZYŃSKI", "KOZIOŁ", "MUCHA", "KOWALEWSKI", "LIPIŃSKI", "ANDRZEJEWSKI", "CZERWIŃSKI",
                    "WESOŁOWSKI", "MIKOŁAJCZYK", "ZIĘBA", "JAROSZ", "CIEŚLAK", "MUSIAŁ", "KOWALIK", "MARKOWSKI", "KOŁODZIEJCZYK", "KOPEĆ", "BRZOZOWSKI",
                    "NOWACKI", "PIĄTEK", "ŻAK", "DOMAŃSKI", "PAWLIK", "ORŁOWSKI", "KUREK", "CIESIELSKI", "KOT", "WÓJTOWICZ", "TOMCZYK", "TOMCZAK", "KRUK",
                    "WAWRZYNIAK", "POLAK", "WOLSKI", "MARKIEWICZ", "SOWA", "STASIAK", "JASTRZĘBSKI", "KARPIŃSKI", "STANKIEWICZ", "URBANIAK", "KLIMEK", "PIASECKI",
                    "ŁUCZAK", "CZAJKOWSKI", "WIERZBICKI", "NAWROCKI", "GAJDA", "BIELECKI", "DZIEDZIC", "STEFAŃSKI", "BEDNAREK", "MADEJ", "MILEWSKI", "JANICKI",
                    "SOSNOWSKI", "SKIBA", "KOWAL", "LEŚNIAK", "MAJ", "MAJCHRZAK", "JÓŹWIAK", "URBAN", "ŚLIWIŃSKI", "SOCHA", "MAŁECKI", "MAREK", "DOMAGAŁA",
                    "BEDNARCZYK", "KASPRZAK", "DOBROWOLSKI", "WRONA", "PAJĄK", "MICHALIK", "MATUSZEWSKI", "RATAJCZAK", "OLEJNICZAK", "ORZECHOWSKI", "ŚWIĄTEK",
                    "WILCZYŃSKI", "ROMANOWSKI", "KUROWSKI", "OLEJNIK", "ŁUKASIK", "ROGOWSKI", "RYBAK", "GRZELAK", "MAZURKIEWICZ", "BUKOWSKI", "OWCZAREK", "SROKA",
                    "SOBOLEWSKI", "KOSIŃSKI", "KĘDZIERSKI", "BARAŃSKI", "ZYCH"]
    cities = ["Warszawa", "Kraków", "Szczecin", "Łódź", "Wrocław", "Zielona Góra", "Gdańsk", "Gdynia", "Poznań",
              "Katowice", "Białystok", "Kielce", "Bydgoszcz", "Toruń", "Częstochowa", "Lublin", "Rzeszów",
              "Radom", "Gorzów Wielkopolski", "Koszalin", "Elbląg", "Olsztyn", "Łomża", "Siedlce", "Kalisz",
              "Piotrków Trybunalski", "Nowy Sącz", "Opole", "Lubin", "Legnica", "Piła", "Płock"]
    months = ["01", "02", "03", "04", "05",
              "06", "07", "08", "09", "10", "11", "12"]
    days = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13",
            "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28"]

    def __init__(self, menu_app):
        super().__init__()
        self.menu_app = menu_app
        self.title("PESEL")
        self.protocol("WM_DELETE_WINDOW", self.on_close_window)
        self.current_page = None
        self.strona_pierwsza()

        self.show_page(self.page1)

    def strona_pierwsza(self):
        self.page1 = tk.Frame(self)

        self.tabGeneral = ttk.Notebook(self.page1)
        self.tabGeneral.grid()

        # Zakładka numer 1 GENEROWANIE PESEL

        self.tab1_gen = ttk.Frame(self.tabGeneral)
        self.tabGeneral.add(self.tab1_gen, text='Wygeneruj PESEL')

        L1 = Label(self.tab1_gen, text="Wskaż datę urodzenia")
        L1.grid(row=0, column=0, padx=5, pady=5, columnspan=3)

        self.kalendarz = Calendar(
            self.tab1_gen, selectmode='day', date_pattern='dd/mm/yyyy', locale='pl_PL')
        date = self.kalendarz.datetime.today()
        self.kalendarz.grid(row=1, column=0, columnspan=3)

        self.plec_frame = Frame(self.tab1_gen)
        self.plec_frame.grid(row=2, column=0, padx=5, pady=5, columnspan=3)

        L2 = Label(self.plec_frame, text="Wybierz płeć:")
        L2.grid(row=0, column=0, padx=5, pady=5)

        self.man = IntVar()
        self.check_man = Checkbutton(self.plec_frame,
                                     text="MĘŻCZYZNA",
                                     variable=self.man,
                                     command=self.checkbutton_man_selected)
        self.check_man.grid(row=0, column=1, padx=5, pady=5)

        self.woman = IntVar()
        self.check_woman = Checkbutton(self.plec_frame,
                                       text="KOBIETA",
                                       variable=self.woman,
                                       command=self.checkbutton_woman_selected)
        self.check_woman.grid(row=0, column=2, padx=5, pady=5)

        self.przyciski_frame = Frame(self.tab1_gen)
        self.przyciski_frame.grid(
            row=3, column=0, padx=5, pady=5, columnspan=3)

        self.back_button0 = Button(self.przyciski_frame,
                                   text="POWRÓT DO MENU",
                                   command=self.back_to_menu,
                                   state=ACTIVE,
                                   compound=LEFT)
        self.back_button0.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.gen_button = Button(self.przyciski_frame,
                                 text="GENERUJ",
                                 command=self.generate_pesel,
                                 state=ACTIVE)
        self.gen_button.grid(row=0, column=1, sticky=E, padx=5, pady=5)

        self.copy_button0 = Button(self.przyciski_frame,
                                   text="KOPIUJ",
                                   command=self.copy_result,
                                   state=DISABLED)
        self.copy_button0.grid(row=0, column=2, sticky=W, padx=5, pady=5)

        self.L4 = Label(self.tab1_gen)
        self.L4.grid(row=4, column=0, padx=5, pady=5, columnspan=3)

        self.L4a = Label(self.tab1_gen)
        self.L4a.grid(row=5, column=0, padx=5, pady=5, columnspan=3)

        # Zakładka numer 2 SPRAWDZANIE PESEL

        self.tab2_check = ttk.Frame(self.tabGeneral)
        self.tabGeneral.add(self.tab2_check, text='Sprawdź PESEL')

        self.Lab1 = Label(self.tab2_check, text="Wprowadź PESEL")
        self.Lab1.grid(row=0, column=0, padx=100, pady=5, sticky=N)

        self.Enter1 = Entry(self.tab2_check, width=15)
        self.Enter1.grid(row=1, column=0, padx=100, pady=5)

        self.przycisk_frame = Frame(self.tab2_check)
        self.przycisk_frame.grid(row=2, column=0, padx=5, pady=5)

        self.back_button1 = Button(self.przycisk_frame,
                                   text="POWRÓT DO MENU",
                                   command=self.back_to_menu,
                                   state=ACTIVE,
                                   compound=LEFT)
        self.back_button1.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.check_button = Button(self.przycisk_frame,
                                   text="SPRAWDŹ",
                                   command=self.check_pesel,
                                   state=ACTIVE)
        self.check_button.grid(row=0, column=1, padx=5, pady=5)

        self.Lab4 = Label(self.tab2_check)
        self.Lab4.grid(row=3, column=0, padx=5, pady=5)

        # Zakładka numer 3 TWORZENIE TOZSAMOSCI

        self.tab3_check = ttk.Frame(self.tabGeneral)
        self.tabGeneral.add(self.tab3_check, text='Stwórz tożsamość')

        self.Ldsd2 = Label(self.tab3_check, text="Wybierz płeć:")
        self.Ldsd2.grid(row=0, column=0, padx=5, pady=5)

        self.man_opt = IntVar()
        self.option_man = Checkbutton(self.tab3_check,
                                      text="Mężczyzna",
                                      variable=self.man_opt,
                                      command=self.checkbutton_man_opt_selected)
        self.option_man.grid(row=0, column=1, padx=5, pady=5)

        self.woman_opt = IntVar()
        self.option_woman = Checkbutton(self.tab3_check,
                                        text="Kobieta",
                                        variable=self.woman_opt,
                                        command=self.checkbutton_woman_opt_selected)
        self.option_woman.grid(row=0, column=2, padx=5, pady=5)

        self.L7 = Label(self.tab3_check, text="Podaj wiek w latach:")
        self.L7.grid(row=1, column=0, padx=5, pady=5)

        self.EE = Entry(self.tab3_check, width=15)
        self.EE.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky=W)

        self.przycis_frame = Frame(self.tab3_check)
        self.przycis_frame.grid(row=2, column=0, padx=5, pady=5, columnspan=3)

        self.back_button1 = Button(self.przycis_frame,
                                   text="POWRÓT DO MENU",
                                   command=self.back_to_menu,
                                   state=ACTIVE,
                                   compound=LEFT)
        self.back_button1.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.makenew_button = Button(self.przycis_frame,
                                     text="STWÓRZ",
                                     command=self.generate_identity,
                                     state=ACTIVE,
                                     compound=LEFT)
        self.makenew_button.grid(row=0, column=1, padx=5, pady=5, sticky=E)

        self.copy_button01 = Button(self.przycis_frame,
                                    text="KOPIUJ",
                                    command=self.copy_result2,
                                    state=DISABLED,
                                    compound=RIGHT)
        self.copy_button01.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        self.wynik_frame = Frame(self.tab3_check)
        self.wynik_frame.grid(row=4, column=0, padx=5, pady=5, columnspan=5)

        self.Lab6 = Label(self.wynik_frame)
        self.Lab6.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        self.Lab7 = Label(self.wynik_frame)
        self.Lab7.grid(row=1, column=0, padx=5, pady=5, sticky=NS)

    def dob_from_pesel(self):
        lista = {0: [0, 19], 1: [1, 19], 2: [0, 20], 3: [1, 20], 4: [
            0, 21], 5: [1, 21], 6: [0, 22], 7: [1, 22], 8: [0, 18], 9: [1, 18]}

        dzien = self.Enter1.get()[4:6]
        miesiac = f"""{lista[int(self.Enter1.get()[2])][0]}{self.Enter1.get()[3]}"""
        rok = f"""{lista[int(self.Enter1.get()[2])][1]}{self.Enter1.get()[0:2]}"""

        self.dob_confirm = f"""Data urodzenia to {dzien}-{miesiac}-{rok}"""
        return self.dob_confirm

    def sex_from_pesel(self):
        if int(self.Enter1.get()[9]) % 2 == 0:
            self.sex = "PESEL należy do kobiety."
            return self.sex
        else:
            self.sex = "PESEL należy do mężczyzny."
            return self.sex

    def check_pesel(self):
        while True:
            if not self.Enter1.get():
                result = "Wprowadź PESEL!"
                self.Lab4.config(text=result)
                break
            if not self.Enter1.get().isdigit():
                result = "Wprowadono niewłaściwe znaki!"
                self.Lab4.config(text=result)
                break
            if len(self.Enter1.get()) != 11:
                result = "Niewłaściwa ilość cyfr w numerze PESEL!"
                self.Lab4.config(text=result)
                break
            if len(self.Enter1.get()) == 11:
                p0 = str(int(self.Enter1.get()[0]) * 1)
                p1 = str(int(self.Enter1.get()[1]) * 3)
                p2 = str(int(self.Enter1.get()[2]) * 7)
                p3 = str(int(self.Enter1.get()[3]) * 9)
                p4 = str(int(self.Enter1.get()[4]) * 1)
                p5 = str(int(self.Enter1.get()[5]) * 3)
                p6 = str(int(self.Enter1.get()[6]) * 7)
                p7 = str(int(self.Enter1.get()[7]) * 9)
                p8 = str(int(self.Enter1.get()[8]) * 1)
                p9 = str(int(self.Enter1.get()[9]) * 3)
                sum = str(int(p0[-1]) + int(p1[-1]) + int(p2[-1]) + int(p3[-1]) + int(p4[-1]) +
                          int(p5[-1]) + int(p6[-1]) + int(p7[-1]) + int(p8[-1]) + int(p9[-1]))
                control_sum = 10 - int(sum[-1])
                if control_sum == int(self.Enter1.get()[10]):
                    result = "PESEL poprawny\n (zgadza się suma kontrolna)"
                else:
                    result = "PESEL niepoprawny\n (niewłaściwa suma kontrolna)"
                self.dob_from_pesel()
                self.sex_from_pesel()
                final_result = result + "\n" + self.dob_confirm + "\n" + self.sex + "\n"
                self.Lab4.config(text=final_result)
                break

    def checkbutton_man_opt_selected(self):
        if self.man_opt.get() == 1:
            self.option_woman.config(state=tk.DISABLED)
        else:
            self.option_woman.config(state=tk.NORMAL)

    def checkbutton_woman_opt_selected(self):
        if self.woman_opt.get() == 1:
            self.option_man.config(state=tk.DISABLED)
        else:
            self.option_man.config(state=tk.NORMAL)

    def checkbutton_man_selected(self):
        if self.man.get() == 1:
            self.check_woman.config(state=tk.DISABLED)
        else:
            self.check_woman.config(state=tk.NORMAL)

    def checkbutton_woman_selected(self):
        if self.woman.get() == 1:
            self.check_man.config(state=tk.DISABLED)
        else:
            self.check_man.config(state=tk.NORMAL)

    def copy_result(self):
        self.page1.clipboard_clear()
        self.page1.clipboard_append(self.generated_pesel)
        info = "Skopiowano PESEL!"
        self.L4a.config(text=info)

    def copy_result2(self):
        self.page1.clipboard_clear()
        self.page1.clipboard_append(self.generated_identity)
        info = "Skopiowano wygenerowany tekst!"
        self.Lab7.config(text=info)

    def generate_pesel(self):
        if self.man.get() == 0 and self.woman.get() == 0:
            info = "Wybierz płeć!"
            self.L4.config(text=info)
        if self.man.get() == 1:
            num_list = [1, 3, 5, 7, 9]
            position_1 = int(self.kalendarz.get_date()[8])
            position_2 = int(self.kalendarz.get_date()[9])
            if self.kalendarz.get_date()[6:8] == "18":
                position_3 = int(self.kalendarz.get_date()[3]) + 8
            if self.kalendarz.get_date()[6:8] == "20":
                position_3 = int(self.kalendarz.get_date()[3]) + 2
            if self.kalendarz.get_date()[6:8] == "21":
                position_3 = int(self.kalendarz.get_date()[3]) + 4
            if self.kalendarz.get_date()[6:8] == "22":
                position_3 = int(self.kalendarz.get_date()[3]) + 6
            if self.kalendarz.get_date()[6:8] == "19":
                position_3 = int(self.kalendarz.get_date()[3])
            position_4 = int(self.kalendarz.get_date()[4])
            position_5 = int(self.kalendarz.get_date()[0])
            position_6 = int(self.kalendarz.get_date()[1])
            position_7 = random.randint(0, 9)
            position_8 = random.randint(0, 9)
            position_10 = int(random.choice(num_list))
            control_sum = position_1 + (position_2 * 3) + (position_3 * 7) + (position_4 * 9) + position_5 + (position_6 * 3) + (position_7 * 7) + (position_8 * 9) + (position_10 * 3)
            ctrl_sum = control_sum
            while control_sum % 10 == 0:
                position_9 = random.randint(0, 9)                
                control_sum += position_9
            last_sign = str(control_sum)[-1]
            position_9 = control_sum - ctrl_sum
            position_11 = 10 - int(last_sign)
            list_of_numbers = [position_1, position_2, position_3, position_4, position_5, position_6,
                               position_7, position_8, position_9, position_10, position_11]
            self.generated_pesel = ''.join(map(str, list_of_numbers))
            self.L4.config(text=self.generated_pesel)
            self.copy_button0.config(state=ACTIVE)
        elif self.woman.get() == 1:
            num_list = [0, 2, 4, 6, 8]
            position_1 = int(self.kalendarz.get_date()[8])
            position_2 = int(self.kalendarz.get_date()[9])
            if self.kalendarz.get_date()[6:8] == "18":
                position_3 = int(self.kalendarz.get_date()[3]) + 8
            if self.kalendarz.get_date()[6:8] == "20":
                position_3 = int(self.kalendarz.get_date()[3]) + 2
            if self.kalendarz.get_date()[6:8] == "21":
                position_3 = int(self.kalendarz.get_date()[3]) + 4
            if self.kalendarz.get_date()[6:8] == "22":
                position_3 = int(self.kalendarz.get_date()[3]) + 6
            if self.kalendarz.get_date()[6:8] == "19":
                position_3 = int(self.kalendarz.get_date()[3])
            position_4 = int(self.kalendarz.get_date()[4])
            position_5 = int(self.kalendarz.get_date()[0])
            position_6 = int(self.kalendarz.get_date()[1])
            position_7 = random.randint(0, 9)
            position_8 = random.randint(0, 9)
            position_10 = int(random.choice(num_list))
            control_sum = position_1 + (position_2 * 3) + (position_3 * 7) + (position_4 * 9) + position_5 + (position_6 * 3) + (position_7 * 7) + (position_8 * 9) + (position_10 * 3)
            ctrl_sum = control_sum
            while control_sum % 10 == 0:
                position_9 = random.randint(0, 9)                
                control_sum += position_9
            last_sign = str(control_sum)[-1]
            position_9 = control_sum - ctrl_sum
            position_11 = 10 - int(last_sign)
            list_of_numbers = [position_1, position_2, position_3, position_4, position_5, position_6,
                               position_7, position_8, position_9, position_10, position_11]
            self.generated_pesel = ''.join(map(str, list_of_numbers))
            self.L4.config(text=self.generated_pesel)
            self.copy_button0.config(state=ACTIVE)

    def zodiaq(self):
        self.zodiac_signs = {("01", 1, 19): "KOZIOROŻEC", ("12", 22, 31): "KOZIOROŻEC", ("01", 20, 31): "WODNIK", ("02", 1, 18): "WODNIK",
                             ("02", 19, 31): "RYBY", ("03", 1, 20): "RYBY", ("03", 21, 31): "BARAN", ("04", 1, 19): "BARAN",
                             ("04", 20, 31): "BYK", ("05", 1, 20): "BYK", ("05", 21, 31): "BLIŹNIĘTA", ("06", 1, 20): "BLIŹNIĘTA",
                             ("06", 21, 31): "RAK", ("07", 1, 22): "RAK", ("07", 23, 31): "LEW", ("08", 1, 22): "LEW",
                             ("08", 23, 31): "PANNA", ("09", 1, 22): "PANNA", ("09", 23, 31): "WAGA", ("10", 1, 22): "WAGA",
                             ("10", 23, 31): "SKORPION", ("11", 1, 21): "SKORPION", ("11", 22, 31): "STRZELEC", ("12", 1, 21): "STRZELEC"}

        z_month = str(self.date_of_birth[3:5])
        z_day = int(self.date_of_birth[:2])

        for (month, day_start, day_end), self.sign in self.zodiac_signs.items():
            if z_month == month and day_start <= z_day <= day_end:
                return self.sign

    def telefon(self):
        start_numeru = [45, 50, 51, 53, 57, 60, 66, 69, 72, 73, 78, 79, 88]
        self.numer_telefonu = (
            f"""+48 {random.choice(start_numeru)}{random.randint(0, 9)} {random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)} {random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}""")
        return self.numer_telefonu

    def mail(self):
        skrzynka = ["gmail.com", "wp.pl", "o2.pl", "onet.eu",
                    "onet.pl", "interia.pl", "gazeta.pl", "proton.me"]
        zamiana_liter = {"ą": "a", "ć": "c", "ę": "e", "ł": "l",
                         "ń": "n", "ó": "o", "ś": "s", "ź": "z", "ż": "z"}
        self.name_new = []
        self.last_name_new = []

        for char in self.name.lower():
            translated_char = zamiana_liter.get(char, char)
            self.name_new.append(translated_char)
            self.result_name = ''.join(self.name_new)

        for char in self.last_name.lower():
            translated_char = zamiana_liter.get(char, char)
            self.last_name_new.append(translated_char)
            self.result_last_name = ''.join(self.last_name_new)

        znak = [".", "-", "_"]
        opt1 = (
            f"""{self.result_name}{random.choice(znak)}{self.result_last_name}""")
        opt2 = (
            f"""{self.result_last_name}{random.choice(znak)}{self.result_name}""")
        opt3 = (
            f"""{self.result_name}{random.choice(znak)}{self.result_last_name}{random.randint(0, 9)}{random.randint(0, 9)}""")
        opt4 = (
            f"""{self.result_last_name}{random.choice(znak)}{self.result_name}{random.randint(0, 9)}{random.randint(0, 9)}""")
        opcje = [opt1, opt2, opt3, opt4]

        self.adres_email = (
            f"""{random.choice(opcje)}@{random.choice(skrzynka)}""")
        return self.adres_email

    def generate_identity(self):
        local_time = time.localtime()
        while True:
            if self.man_opt.get() == 0 and self.woman_opt.get() == 0:
                generated_personality = "Wybierz płeć!"
                self.Lab6.config(text=generated_personality)
                break
            if not self.EE.get():
                generated_personality = "Wprowadź wiek!"
                self.Lab6.config(text=generated_personality)
                break
            if int(self.EE.get()) >= 100:
                generated_personality = "Bez przesady, zejdź poniżej 100 lat..."
                self.Lab6.config(text=generated_personality)
                break
            if not self.EE.get().isdigit():
                generated_personality = "Wprowadzono niewłaściwy wiek!"
                self.Lab6.config(text=generated_personality)
                break
            if self.man_opt.get() == 1:
                self.name = random.choice(self.men_names)
                self.last_name = random.choice(self.men_surnames)
                year_of_birth = int(local_time.tm_year) - int(self.EE.get())
                month_of_birth = random.choice(self.months)
                day_of_birth = random.choice(self.days)
                self.date_of_birth = str(day_of_birth) + "-" + \
                    str(month_of_birth) + "-" + str(year_of_birth)
                dob_for_pesel = str(day_of_birth) + \
                    str(month_of_birth) + str(year_of_birth)
                num_list = [1, 3, 5, 7, 9]
                position_1 = int(dob_for_pesel[6])
                position_2 = int(dob_for_pesel[7])
                if dob_for_pesel[4:6] == "18":
                    position_3 = int(dob_for_pesel[2]) + 8
                if dob_for_pesel[4:6] == "20":
                    position_3 = int(dob_for_pesel[2]) + 2
                if dob_for_pesel[4:6] == "21":
                    position_3 = int(dob_for_pesel[2]) + 4
                if dob_for_pesel[4:6] == "22":
                    position_3 = int(dob_for_pesel[2]) + 6
                if dob_for_pesel[4:6] == "19":
                    position_3 = int(dob_for_pesel[2])    
                position_4 = int(dob_for_pesel[3])
                position_5 = int(dob_for_pesel[0])
                position_6 = int(dob_for_pesel[1])
                position_7 = random.randint(0, 9)
                position_8 = random.randint(0, 9)
                position_10 = int(random.choice(num_list))
                control_sum = position_1 + (position_2 * 3) + (position_3 * 7) + (position_4 * 9) + position_5 + (position_6 * 3) + (position_7 * 7) + (position_8 * 9) + (position_10 * 3)
                ctrl_sum = control_sum
                while control_sum % 10 == 0:
                    position_9 = random.randint(0, 9)                
                    control_sum += position_9
                last_sign = str(control_sum)[-1]
                position_9 = control_sum - ctrl_sum
                position_11 = 10 - int(last_sign)
                list_of_numbers = [position_1, position_2, position_3, position_4, position_5, position_6,
                                position_7, position_8, position_9, position_10, position_11]
                self.generated_pesel = ''.join(map(str, list_of_numbers))
                self.zodiaq()
                self.telefon()
                self.mail()
                self.generated_identity = (f"""
                    Wygenerowana tożsamość:
                    {self.name} {self.last_name} 
                    {self.date_of_birth} {random.choice(self.cities)}
                    PESEL: {self.generated_pesel}
                    Znak zodiaku: {self.sign}
                    Numer telefonu: {self.numer_telefonu}
                    Adres mailowy: {self.adres_email}
                    """)
                self.Lab6.config(text=self.generated_identity)
                self.copy_button01.config(state=ACTIVE)
                break
            if self.woman_opt.get() == 1:
                self.name = random.choice(self.women_names)
                self.last_name = random.choice(self.women_surnames)
                year_of_birth = int(local_time.tm_year) - int(self.EE.get())
                month_of_birth = random.choice(self.months)
                day_of_birth = random.choice(self.days)
                self.date_of_birth = str(day_of_birth) + "-" + \
                    str(month_of_birth) + "-" + str(year_of_birth)
                dob_for_pesel = str(day_of_birth) + \
                    str(month_of_birth) + str(year_of_birth)
                num_list = [0, 2, 4, 6, 8]
                position_1 = dob_for_pesel[6]
                position_2 = dob_for_pesel[7]
                if dob_for_pesel[4:6] == "18":
                    position_3 = dob_for_pesel[2] + 8
                if dob_for_pesel[4:6] == "20":
                    position_3 = dob_for_pesel[2] + 2
                if dob_for_pesel[4:6] == "21":
                    position_3 = dob_for_pesel[2] + 4
                if dob_for_pesel[4:6] == "22":
                    position_3 = dob_for_pesel[2] + 6
                if dob_for_pesel[4:6] == "19":
                    position_3 = dob_for_pesel[2]    
                position_4 = dob_for_pesel[3]
                position_5 = dob_for_pesel[0]
                position_6 = dob_for_pesel[1]
                position_7 = random.randint(0, 9)
                position_8 = random.randint(0, 9)
                position_10 = int(random.choice(num_list))
                control_sum = position_1 + (position_2 * 3) + (position_3 * 7) + (position_4 * 9) + position_5 + (position_6 * 3) + (position_7 * 7) + (position_8 * 9) + (position_10 * 3)
                ctrl_sum = control_sum
                while control_sum % 10 == 0:
                    position_9 = random.randint(0, 9)                
                    control_sum += position_9
                last_sign = str(control_sum)[-1]
                position_9 = control_sum - ctrl_sum
                position_11 = 10 - int(last_sign)
                list_of_numbers = [position_1, position_2, position_3, position_4, position_5, position_6,
                                position_7, position_8, position_9, position_10, position_11]
                self.generated_pesel = ''.join(map(str, list_of_numbers))
                self.zodiaq()
                self.telefon()
                self.mail()
                self.generated_identity = (f"""
                    Wygenerowana tożsamość:
                    {self.name} {self.last_name} 
                    {self.date_of_birth} {random.choice(self.cities)}
                    PESEL: {self.generated_pesel}
                    Znak zodiaku: {self.sign}
                    Numer telefonu: {self.numer_telefonu}
                    Adres mailowy: {self.adres_email}
                    """)
                self.Lab6.config(text=self.generated_identity)
                self.copy_button01.config(state=ACTIVE)
                break
                    
    def show_page(self, page):
        if self.current_page:
            self.current_page.grid_forget()
        page.grid(row=0, column=0, sticky="nsew")
        self.current_page = page

    def on_close_window(self):
        self.back_to_menu()

    def back_to_menu(self):
        self.menu_app.show_menu()
        self.destroy()            

class KalkulatorWalut(tk.Toplevel):
    def __init__(self, menu_app):
        super().__init__()
        self.menu_app = menu_app
        self.title("KALKULATOR WALUT")
        self.protocol("WM_DELETE_WINDOW", self.on_close_window)
        self.current_page = None
        self.strona_pierwsza()

        self.show_page(self.page1)

    def strona_pierwsza(self):
        self.page1 = tk.Frame(self)

        # OBCE NA PLN

        self.label_start = Label(
            self.page1, text="Przeliczanie z waluty obcej na złotówki")
        self.label_start.grid(row=1, column=0, padx=5,
                              pady=5, sticky=W, columnspan=3)

        self.kwota = Entry(self.page1)
        self.kwota.grid(row=2, column=0, sticky=NS, padx=5, pady=5)

        self.option_var = StringVar(self.page1)
        self.max_length = max(len(option) for option in options)

        self.option_menu = OptionMenu(self.page1, self.option_var, *options)
        self.option_menu.grid(row=2, column=1, sticky=NS)
        self.option_menu.config(width=self.max_length + 2)
        self.option_var.set("Wybierz walutę")

        self.button = Button(self.page1, text='Przelicz',
                             command=self.konwertuj_do_pln)
        self.button.grid(row=2, column=2, sticky=NS, padx=5, pady=5)

        self.label1 = Label(self.page1)
        self.label1.grid(row=3, column=0, sticky=NS,
                         columnspan=3, padx=5, pady=5)

        # PLN NA OBCE

        self.olabel_start = Label(
            self.page1, text="Przeliczanie ze złotówek na walutę obcą")
        self.olabel_start.grid(row=4, column=0, padx=5,
                               pady=5, sticky=W, columnspan=3)

        self.okwota = Entry(self.page1)
        self.okwota.grid(row=5, column=0, sticky=NS, padx=5, pady=5)

        self.ooption_var = StringVar(self.page1)
        self.omax_length = max(len(option) for option in options)

        self.ooption_menu = OptionMenu(self.page1, self.ooption_var, *options)
        self.ooption_menu.grid(row=5, column=1, sticky=NS)
        self.ooption_menu.config(width=self.omax_length + 2)
        self.ooption_var.set("Wybierz walutę")

        self.obutton = Button(self.page1, text='Przelicz',
                              command=self.konwertuj_z_pln)
        self.obutton.grid(row=5, column=2, sticky=NS, padx=5, pady=5)

        self.olabel1 = Label(self.page1)
        self.olabel1.grid(row=6, column=0, sticky=NS,
                          columnspan=3, padx=5, pady=5)

        self.buttonframe = Frame(self.page1)
        self.buttonframe.grid(row=7, column=0, padx=10, pady=10, columnspan=3)

        self.back_button = tk.Button(
            self.buttonframe, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=0, padx=10, pady=10)

        self.tabela_button = tk.Button(
            self.buttonframe, text="KURS WALUT", command=self.tabela)
        self.tabela_button.grid(row=0, column=1, padx=10, pady=10)

    def tabela(self):
        self.table_window = tk.Toplevel(self)
        self.table_window.title("KURS WALUT")

        self.table = ttk.Treeview(self.table_window, columns=(
            "Waluta", "Kurs"), show="headings")
        self.table.heading("Waluta", text="Waluta")
        self.table.heading("Kurs", text="Aktualny kurs")
        self.table.column("Waluta", width=180)
        self.table.column("Kurs", width=100)

        for waluta, skrot in tabela_nbp.items():
            kurs = self.kurs_walut(skrot)
            self.table.insert("", "end", values=(waluta, f"{kurs} PLN"))

        self.table.grid(row=0, column=0, padx=10, pady=10)
        self.table["height"] = len(tabela_nbp)

    def kurs_walut(self, skrot):
        link = f"http://api.nbp.pl/api/exchangerates/rates/a/{skrot}/"
        response = requests.get(link)
        link2 = f"http://api.nbp.pl/api/exchangerates/rates/b/{skrot}/"
        response2 = requests.get(link2)

        if response.status_code == 200:
            try:
                data = response.json()
                mid_value = data["rates"][0]["mid"]
                return mid_value
            except json.decoder.JSONDecodeError:
                info = f"Brak danych dla waluty o skrócie {skrot}"
                return info
        if response2.status_code == 200:
            try:
                data = response2.json()
                mid_value = data["rates"][0]["mid"]
                return mid_value
            except json.decoder.JSONDecodeError:
                info = f"Brak danych dla waluty o skrócie {skrot}"
                return info
        else:
            info = "Wystąpił problem z połączeniem z Internetem!"
            return info

    def konwertuj_do_pln(self):
        try:
            waluta = str(self.option_var.get())
            skrot = tabela_nbp[waluta]
            ilosc = int(self.kwota.get())
            link_1 = ("http://api.nbp.pl/api/exchangerates/rates/a/xyz/")
            link_2 = ("http://api.nbp.pl/api/exchangerates/rates/b/xyz/")
            response = requests.get(link_1.replace("xyz", "usd"))
            if response.status_code == 200:
                try:
                    req = requests.get(link_1.replace("xyz", skrot.lower()))
                    json_data = req.text
                    data = json.loads(json_data)
                except json.decoder.JSONDecodeError:
                    req = requests.get(link_2.replace("xyz", skrot.lower()))
                    json_data = req.text
                    data = json.loads(json_data)

                mid_value = data["rates"][0]["mid"]
                kurs_z_dnia = data["rates"][0]["effectiveDate"]

                calc = ilosc * mid_value

                info = (
                    f"{ilosc} {skrot} po kursie NBP z dnia {kurs_z_dnia} jest warte {round(calc,2)} PLN")
                self.label1.config(text=info)
            else:
                info = (f"Wystąpił problem z połączeniem z Internetem!")
                self.label1.config(text=info)
        except KeyError:
            info = (f"Musisz wybrać walutę!")
            self.label1.config(text=info)
        except ValueError:
            info = (f"Wskaż kwotę do przeliczenia!")
            self.label1.config(text=info)

    def konwertuj_z_pln(self):
        try:
            waluta = str(self.ooption_var.get())
            skrot = tabela_nbp[waluta]
            ilosc = int(self.okwota.get())
            link_1 = ("http://api.nbp.pl/api/exchangerates/rates/a/xyz/")
            link_2 = ("http://api.nbp.pl/api/exchangerates/rates/b/xyz/")
            response = requests.get(link_1.replace("xyz", "usd"))
            if response.status_code == 200:
                try:
                    req = requests.get(link_1.replace("xyz", skrot.lower()))
                    json_data = req.text
                    data = json.loads(json_data)
                except json.decoder.JSONDecodeError:
                    req = requests.get(link_2.replace("xyz", skrot.lower()))
                    json_data = req.text
                    data = json.loads(json_data)

                mid_value = data["rates"][0]["mid"]
                kurs_z_dnia = data["rates"][0]["effectiveDate"]

                calc = ilosc / mid_value

                info = (
                    f"{ilosc} PLN po kursie NBP z dnia {kurs_z_dnia} jest warte {round(calc,2)} {skrot}")
                self.olabel1.config(text=info)
            else:
                info = (f"Wystąpił problem z połączeniem z Internetem!")
                self.olabel1.config(text=info)
        except KeyError:
            info = (f"Musisz wybrać walutę!")
            self.olabel1.config(text=info)
        except ValueError:
            info = (f"Wskaż kwotę do przeliczenia!")
            self.olabel1.config(text=info)

    def show_page(self, page):
        if self.current_page:
            self.current_page.grid_forget()
        page.grid(row=0, column=0, sticky="nsew")
        self.current_page = page

    def on_close_window(self):
        self.back_to_menu()

    def back_to_menu(self):
        self.menu_app.show_menu()
        self.destroy()


class GeneratorHasel(tk.Toplevel):
    def __init__(self, menu_app):
        super().__init__()
        self.menu_app = menu_app
        self.title("GENERATOR HASEŁ")
        self.protocol("WM_DELETE_WINDOW", self.on_close_window)
        self.current_page = None
        self.strona_pierwsza()
        self.password = ''

        self.letters = string.ascii_letters
        self.digits = string.digits
        self.special_chars = string.punctuation

        self.full_alphabet = self.letters + self.digits + self.special_chars
        self.letters_num = self.letters + self.digits
        self.num_spec = self.digits + self.special_chars
        self.letters_spec = self.letters + self.special_chars

        self.show_page(self.page1)

    def strona_pierwsza(self):
        self.page1 = tk.Frame(self)
        self.label1 = Label(self.page1,
                            text="Z jakich znaków ma składać się hasło?")
        self.label1.grid(row=0, column=0, columnspan=2)

        self.check_numbers = IntVar()
        self.check_button_numbers = Checkbutton(self.page1,
                                                text="Liczby",
                                                variable=self.check_numbers)
        self.check_button_numbers.grid(row=1, column=0, columnspan=2)

        self.check_letters = IntVar()
        self.check_button_letters = Checkbutton(self.page1,
                                                text="Litery",
                                                variable=self.check_letters)
        self.check_button_letters.grid(row=2, column=0, columnspan=2)

        self.check_special_characters = IntVar()
        self.check_button_special = Checkbutton(self.page1,
                                                text="Znaki specjalne",
                                                variable=self.check_special_characters)
        self.check_button_special.grid(row=3, column=0, columnspan=2)

        self.pass_len = IntVar()
        self.scale = Scale(self.page1,
                           from_=8,
                           to=18,
                           length=250,
                           orient=HORIZONTAL,
                           tickinterval=2,
                           showvalue=1,
                           resolution=1,
                           variable=self.pass_len)
        self.scale.grid(row=4, column=0, columnspan=2)

        self.gen_button = Button(self.page1,
                                 text="GENERUJ",
                                 command=self.click,
                                 state=ACTIVE,
                                 compound="left")
        self.gen_button.grid(row=5, column=0)

        self.back_button = tk.Button(
            self.page1, text="POWRÓT DO MENU", command=self.back_to_menu, compound="right")
        self.back_button.grid(row=5, column=1)

        self.label2 = Label(self.page1)
        self.label2.grid(row=6, column=0, columnspan=2)

        self.label3 = Label(self.page1)
        self.label3.grid(row=7, column=0, columnspan=2)

    def click(self):
        if self.check_numbers.get() == 0 and self.check_letters.get() == 0 and self.check_special_characters.get() == 0:
            self.msgbox = 'Hasło nie zostało wygenerowane, ponieważ nie wybrano żadnych możliwych do użycia znaków!'
            messagebox.showinfo('Śliwka Coding Center ©', self.msgbox)
            return

        charset = ""

        if self.check_numbers.get() == 1:
            charset += self.digits
        if self.check_letters.get() == 1:
            charset += self.letters
        if self.check_special_characters.get() == 1:
            charset += self.special_chars

        self.generate_password(charset)

    def create_result(self, password):
        self.page1.clipboard_clear()
        self.page1.clipboard_append(password)

    def generate_password(self, charset):
        for _ in range(self.pass_len.get()):
            self.password += ''.join(secrets.choice(charset))
        self.create_result(self.password)
        self.check_passwd_power()

    def check_password_strength(self):
        if len(self.password) < 8:
            self.power = "Hasło jest za krótkie. Minimalna długość to 8 znaków."
            return self.power
        if len(set(self.password)) < 4:
            self.power = "Hasło jest zbyt słabe. Powinno zawierać co najmniej 4 różne znaki."
            return self.power
        if self.password.isdigit():
            self.power = "Hasło składające się wyłącznie z cyfr jest bardzo słabe."
            return self.power
        else:
            self.power = "Hasło jest wystarczająco silne!"
            return self.power

    def check_passwd_power(self):
        self.check_password_strength()
        self.msgbox = (f"""
            Wygenerowane hasło to:\n
            {str(self.password)}\n
            {self.power}
            Hasło zostało skopiowane do schowka!
                """)
        messagebox.showinfo('Śliwka Coding Center ©', self.msgbox)

    def show_page(self, page):
        if self.current_page:
            self.current_page.grid_forget()
        page.grid(row=0, column=0, sticky="nsew")
        self.current_page = page

    def on_close_window(self):
        self.back_to_menu()

    def back_to_menu(self):
        self.menu_app.show_menu()
        self.destroy()

class Transliteracja(tk.Toplevel):
    def __init__(self, menu_app):
        super().__init__()
        self.menu_app = menu_app
        self.title("TRANSLITERACJA")
        self.protocol("WM_DELETE_WINDOW", self.on_close_window)
        self.current_page = None
        self.strona_pierwsza()

        self.show_page(self.page1)

    def strona_pierwsza(self):
        self.page1 = tk.Frame(self)

        self.input_label = tk.Label(
            self.page1, text="Wprowadź tekst do transliteracji\n z języka rosyjskiego na alfabet łaciński")
        self.input_label.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

        self.input_text = tk.Text(self.page1, height=4, width=50)
        self.input_text.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        self.translate_button = tk.Button(
            self.page1, text="TRANSLITERACJA", command=self.translate)
        self.translate_button.grid(row=2, column=0, padx=5, pady=5)
        
        self.back_button = tk.Button(
        self.page1, text="POWRÓT DO MENU", command=self.back_to_menu, compound="right")
        self.back_button.grid(row=2, column=1, padx=5, pady=5)

        self.output_text = tk.Text(self.page1, height=4, width=50)
        self.output_text.grid(row=4, column=0, padx=5, pady=5, columnspan=2)

    def translate(self):
        self.all_chars_rus = {"Й": "Y", "Ц": "TS", "У": "U", "К": "K", "Е": "E", "Н": "N", "Г": "G", "Ш": "SH", "Ё": "E",
                              "Щ": "SHCH", "З": "Z", "Х": "H", "Ъ": "", "Ф": "F", "Ы": "Y", "В": "V", "А": "A",
                              "П": "P", "Р": "R", "О": "O", "Л": "L", "Д": "D", "Ж": "ZH", "Э": "E", "Я": "YA",
                              "Ч": "CH", "С": "S", "М": "M", "И": "I", "Т": "T", "Ь": "", "Б": "B", "Ю": "YU",
                              "й": "y",  "ц": "ts",  "у": "u",  "к": "k",  "е": "e",  "н": "n",  "г": "g",
                              "ш": "sh",  "щ": "shch",  "з": "z",  "х": "h",  "ъ": "",  "ф": "f",  "ы": "y",
                              "в": "v",  "а": "a",  "п": "p", "р": "r",  "о": "o",  "л": "l",  "д": "d", "ё": "e",
                              "ж": "zh",  "э": "e",  "я": "ya",  "ч": "ch",  "с": "s",  "м": "m",  "и": "i",
                              "т": "t",  "ь": "",  "б": "b",  "ю": "yu", " ": " "}
        text_to_translate = self.input_text.get("1.0", "end-1c")
        self.lista = []

        for char in text_to_translate:
            translated_char = self.all_chars_rus.get(char, char)
            self.lista.append(translated_char)

        self.output_text.delete("1.0", "end")
        self.output_text.insert("end", ''.join(self.lista))

    def show_page(self, page):
        if self.current_page:
            self.current_page.grid_forget()
        page.grid(row=0, column=0, sticky="nsew")
        self.current_page = page

    def on_close_window(self):
        self.back_to_menu()

    def back_to_menu(self):
        self.menu_app.show_menu()
        self.destroy()


if __name__ == "__main__":
    app = MenuApp()
    app.mainloop()