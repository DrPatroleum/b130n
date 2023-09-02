import datetime
from datetime import datetime
import random
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from tkcalendar import Calendar
from tkinter import messagebox
from tkinter import simpledialog, Radiobutton
import requests
import json
import secrets
import string
import time

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
tabela_nbp = {"dolar amerykański [USD]":"USD","dolar australijski [AUD]":"AUD", "dolar kanadyjski [CAD]":"CAD","euro [EUR]":"EUR",
              "forint [HUF]":"HUF","frank szwajcarski [CHF]":"CHF","funt szterling [GBP]":"GBP","hrywna [UAH]":"UAH","jen [JPY]":"JPY",
              "korona czeska [CZK]":"CZK","korona duńska [DKK]":"DKK","korona islandzka [ISK]":"ISK","korona norweska [NOK]":"NOK",
              "korona szwedzka [SEK]":"SEK","lej rumuński [RON]":"RON","lira turecka [TRY]":"TRY","szekel [ILS]":"ILS",
              "dirham ZEA [AED]":"AED","rubel białoruski [BYN]":"BYN","rubel rosyjski [RUB]":"RUB"}
options = ["dolar amerykański [USD]", "dolar australijski [AUD]", "dolar kanadyjski [CAD]", "euro [EUR]",
              "forint [HUF]","frank szwajcarski [CHF]","funt szterling [GBP]","hrywna [UAH]","jen [JPY]",
              "korona czeska [CZK]","korona duńska [DKK]","korona islandzka [ISK]","korona norweska [NOK]",
              "korona szwedzka [SEK]","lej rumuński [RON]","lira turecka [TRY]","szekel [ILS]",
              "dirham ZEA [AED]","rubel białoruski [BYN]","rubel rosyjski [RUB]"]


class MenuApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("B!30N")
        self.button1 = tk.Button(self, text="DIETY\n KRAJOWE", command=self.open_diety_krajowe, width=15, height=5)
        self.button1.grid(row=0,column=0, padx=2, pady=2)

        self.button2 = tk.Button(self, text="DIETY\n ZAGRANICZNE", command=self.open_diety_zagraniczne, width=15, height=5)
        self.button2.grid(row=0,column=1, padx=2, pady=2)
        
        self.button3 = tk.Button(self, text="PESEL", command=self.open_pesel, width=15, height=5)
        self.button3.grid(row=0,column=2, padx=2, pady=2)

        self.button4 = tk.Button(self, text="KALKULATOR\n WALUT", command=self.open_kalkulator_walut, width=15, height=5)
        self.button4.grid(row=1,column=0, padx=2, pady=2)
        
        self.button5 = tk.Button(self, text="GENERATOR\n HASEŁ", command=self.open_generator_hasel, width=15, height=5)
        self.button5.grid(row=1,column=1, padx=2, pady=2)
        
        self.button6 = tk.Button(self, text="TRANSLITERACJA", command=self.open_transliteracja, width=15, height=5)
        self.button6.grid(row=1,column=2, padx=2, pady=2)

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
        
    def hide_menu(self):
        self.withdraw()

    def show_menu(self):
        self.deiconify()

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
        label_start = Label(self.page1, text="Wybierz datę i godzinę rozpoczęcia delegacji")
        label_start.grid(row=0, column=0, sticky=EW, padx=5, pady=5, columnspan=8)
        
        label_godzina_startu = Label(self.page1, text="GODZINA")
        label_godzina_startu.grid(row=1, column=3, padx=5, pady=5, sticky=S)
        label_minuta_startu = Label(self.page1, text="MINUTA")
        label_minuta_startu.grid(row=1, column=4, padx=5, pady=5, sticky=S)
        
        self.cal_start = Calendar(self.page1, selectmode='day',
                            date_pattern='dd/mm/yyyy', locale='pl_PL')
        self.date = self.cal_start.datetime.today()
        self.cal_start.grid(row=1, column=0, padx=5, pady=5,
                    sticky=N, rowspan=3, columnspan=3)
        
        self.godzinysk = IntVar()
        self.wybor_godziny_startu = Spinbox(self.page1, width=5, wrap=True, values=godziny)
        self.wybor_godziny_startu.grid(row=2, column=3, padx=5, pady=5, sticky=N)
        self.minutysk = IntVar()
        self.wybor_minuty_startu = Spinbox(self.page1, width=5, wrap=True, values=minuty)
        self.wybor_minuty_startu.grid(row=2, column=4, padx=5, pady=5, sticky=N)

        button_container = tk.Frame(self.page1)
        button_container.grid(row=4, column=0, padx=5, pady=5, columnspan=8)   

        self.back_button = tk.Button(button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=0)
        
        self.button_next_page2 = tk.Button(button_container, text="DALEJ", command=self.next_page1)
        self.button_next_page2.grid(row=0, column=1)
        
    
    def strona_druga(self):
        self.page2 = tk.Frame(self)
        label_start = Label(self.page2, text="Wybierz datę i godzinę zakończenia delegacji")
        label_start.grid(row=0, column=0, sticky=EW, padx=5, pady=5, columnspan=8)
        
        self.cal_koniec = Calendar(self.page2, selectmode='day',
                            date_pattern='dd/mm/yyyy', locale='pl_PL')
        self.date = self.cal_koniec.datetime.today()
        self.cal_koniec.grid(row=1, column=0, padx=5, pady=5,
                        sticky=N, rowspan=3, columnspan=3)
        
        self.label_godzina_konca = Label(self.page2, text="GODZINA")
        self.label_godzina_konca.grid(row=1, column=3, padx=5, pady=5, sticky=S)
        label_minuta_konca = Label(self.page2, text="MINUTA")
        label_minuta_konca.grid(row=1, column=4, padx=5, pady=5, sticky=S)
        
        self.godzinykk = IntVar()
        self.wybor_godziny_konca = Spinbox(self.page2, width=5, wrap=True, values=godziny)
        self.wybor_godziny_konca.grid(row=2, column=3, padx=5, pady=5, sticky=N)
        self.minutykk = IntVar()
        self.wybor_minuty_konca = Spinbox(self.page2, width=5, wrap=True, values=minuty)
        self.wybor_minuty_konca.grid(row=2, column=4, padx=5, pady=5, sticky=N)
    
        button_container = tk.Frame(self.page2)
        button_container.grid(row=4, column=0, padx=5, pady=5, columnspan=8)     

        self.button_back_page2 = tk.Button(button_container, text="WSTECZ", command=self.back_page2)
        self.button_back_page2.grid(row=0, column=0)
        
        self.back_button = tk.Button(button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=1)

        self.button_next_page2 = tk.Button(button_container, text="DALEJ", command=self.next_page2)
        self.button_next_page2.grid(row=0, column=2, columnspan=2)
        
    def strona_trzecia(self):
        self.page3 = tk.Frame(self)
        self.label_posilki = Label(self.page3, text="Wskaż posiłki zapewnione podczas delegacji")
        self.label_posilki.grid(row=0, column=0, sticky=EW, padx=5, pady=5, columnspan=8)
        
        self.var1dk = IntVar()
        self.check_sniadaniedk = Checkbutton(self.page3, text="ŚNIADANIE", onvalue=1,
                                    offvalue=0, command=self.checking_sniadaniedk, variable=self.var1dk)
        self.check_sniadaniedk.grid(row=1, column=0, padx=50, pady=5, sticky=W, columnspan=2)
        self.label_sniadanie = Label(self.page3, text="w ilości")
        self.label_sniadanie.grid(row=1, column=2, sticky=E, padx=5, pady=5)
        self.ilosc_sniadaniedk = Entry(self.page3, width=5, state=DISABLED)
        self.ilosc_sniadaniedk.grid(row=1, column=3, sticky=W, padx=5, pady=5)
        
        self.var2dk = IntVar()
        self.check_obiaddk = Checkbutton(self.page3, text="OBIAD", onvalue=1,
                                offvalue=0, command=self.checking_obiaddk, variable=self.var2dk)
        self.check_obiaddk.grid(row=2, column=0, padx=50, pady=5, sticky=W, columnspan=2)
        self.label_obiad = Label(self.page3, text="w ilości")
        self.label_obiad.grid(row=2, column=2, sticky=E, padx=5, pady=5)
        self.ilosc_obiaddk = Entry(self.page3, width=5, state=DISABLED)
        self.ilosc_obiaddk.grid(row=2, column=3, sticky=W, padx=5, pady=5)
        
        self.var3dk = IntVar()
        self.check_kolacjadk = Checkbutton(self.page3, text="KOLACJA", onvalue=1,
                                    offvalue=0, command=self.checking_kolacjadk, variable=self.var3dk)
        self.check_kolacjadk.grid(row=3, column=0, padx=50, pady=5, sticky=W, columnspan=2)
        self.label_kolacja = Label(self.page3, text="w ilości")
        self.label_kolacja.grid(row=3, column=2, sticky=E, padx=5, pady=5)
        self.ilosc_kolacjadk = Entry(self.page3, width=5, state=DISABLED)
        self.ilosc_kolacjadk.grid(row=3, column=3, sticky=W, padx=5, pady=5)
                
        self.label_dodatki = Label(self.page3, text="Wskaż przysługujące ci ryczałty")
        self.label_dodatki.grid(row=4, column=0, sticky=EW, padx=5, pady=5, columnspan=8)
        
        self.nocleg_var1 = tk.BooleanVar()
        self.auto_var2 = tk.BooleanVar()
        self.komunikacja_var3 = tk.BooleanVar()
        
        self.checkframe = Frame(self.page3)
        self.checkframe.grid(row=5, column=0, columnspan=8)
        
        self.check_nocleg = Checkbutton(self.checkframe, text="NOCLEG", variable=self.nocleg_var1, command=self.rycz_nocleg)
        self.check_auto = Checkbutton(self.checkframe, text="PRYWATNE AUTO", variable=self.auto_var2, command=self.rycz_auto)
        self.check_komunikacja = Checkbutton(self.checkframe, text="KOMUNIKACJA MIEJSCOWA", variable=self.komunikacja_var3, command=self.rycz_komunikacja)
        self.check_nocleg.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.check_auto.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.check_komunikacja.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        self.button_container = tk.Frame(self.page3)
        self.button_container.grid(row=8, column=0, padx=5, pady=5, columnspan=8)       
                
        self.button_back_page2 = tk.Button(self.button_container, text="WSTECZ", command=self.back_page3)
        self.button_back_page2.grid(row=0, column=0, sticky=E)
        
        self.back_button = tk.Button(self.button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=1)

        self.button_next_page2 = tk.Button(self.button_container, text="DALEJ", command=self.next_page3)
        self.button_next_page2.grid(row=0, column=2, sticky=W)
        
    def strona_czwarta(self):
        self.page4 = tk.Frame(self)
        
        button_container = tk.Frame(self.page4)
        button_container.grid(row=1, column=0, padx=5, pady=5, columnspan=8)

        self.label_wynik = Label(self.page4)
        self.label_wynik.grid(row=0, column=0, padx=5, pady=5, columnspan=8, sticky=W)
        
        self.button_back_page2 = tk.Button(button_container, text="WSTECZ", command=self.back_page4)
        self.button_back_page2.grid(row=0, column=0, sticky=E)

        self.back_button = tk.Button(button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=1, sticky=W)
   
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
            data_startu = datetime(s_rok, s_miesiac, s_dzien, s_godzina, s_minuta)
            data_konca = datetime(k_rok, k_miesiac, k_dzien, k_godzina, k_minuta)
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

        label = tk.Label(self.top, text="Wprowadź liczbę przejechanych kilometrów:")
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

        option1 = Radiobutton(self.top, text="Auto z silnikiem o poj. do 900 cm3", variable=option_var, value=self.auto_do_900)
        option2 = Radiobutton(self.top, text="Auto z silnikiem o poj. ponad 900 cm3", variable=option_var, value=self.auto_ponad_900)
        option3 = Radiobutton(self.top, text="Motocykl", variable=option_var, value=self.motocykl)
        option4 = Radiobutton(self.top, text="Motorower", variable=option_var, value=self.motorower)
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
                messagebox.showerror("Wystąpił błąd", "Aby przejść dalej musisz wprowadzić kilometry i wybrać środek transportu.")

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
            data_startu = datetime(s_rok, s_miesiac, s_dzien, s_godzina, s_minuta)
            data_konca = datetime(k_rok, k_miesiac, k_dzien, k_godzina, k_minuta)
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
            s_miesiac = int(self.cal_start.get_date()[4:5])
            s_dzien = int(self.cal_start.get_date()[:2])
            s_godzina = int(self.wybor_godziny_startu.get())
            s_minuta = int(self.wybor_minuty_startu.get())
        except ValueError:
            info = ("Wprowadzono złą wartość godziny i/lub minuty")
            self.label_wynik.config(text=info)
    
        try:
            k_rok = int(self.cal_koniec.get_date()[-4:])
            k_miesiac = int(self.cal_koniec.get_date()[4:5])
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
            ryc_noc_info = (f"Za ryczałt za nocleg należy ci się dodatkowo {round(self.ryczalt_nocleg,2)} PLN.")
        else:
            self.ryczalt_nocleg = 0   
            ryc_noc_info = (f"Nie uwzględniono ryczałtu za nocleg.")

            
        if self.auto_var2.get():
            self.ryczalt_auto
            ryc_auto_info = (f"Za ryczałt za pozdróż prywatnym środkiem transportu\n należy ci się dodatkowo {round(self.ryczalt_auto,2)} PLN.")
        else:
            self.ryczalt_auto = 0
            ryc_auto_info = (f"Nie uwzględniono ryczałtu za pozdróż prywatnym środkiem transportu.")

            
        if self.komunikacja_var3.get():
            self.ryczalt_komunikacja
            ryc_kom_info = (f"Za ryczałt za dojazd środkami komunikacji miejscowej\n należy ci sie dodatkowo {round(self.ryczalt_komunikacja,2)} PLN.")
        else:
            self.ryczalt_komunikacja = 0
            ryc_kom_info = (f"Nie uwzględniono ryczałtu za przejazd środkami komunikacji miejscowej.")

    
        zarcie = sniadanie + obiad + kolacja
        
        if zarcie != 0:
            zarcie_info = (f"Za zapewnione posiłki należy odjąć {round(zarcie,2)} PLN.")
        else:
            zarcie_info = (f"Podczas delegacji nie zapewniono zadnych posiłków.")

        
        nalezna_dieta = nalezna_dieta_dzien + \
            nalezna_dieta_godz - sniadanie - obiad - kolacja + self.ryczalt_nocleg + self.ryczalt_komunikacja + self.ryczalt_auto
        
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
    
        result = (f"""
            Delegacja krajowa trwała \n{int(liczba_dni)} {wersja_dzien}, {int(liczba_godzin)} {wersja_godzin} i {int(liczba_minut)} {wersja_minut} ({round(nalezna_dieta_dzien,2)} PLN + {round(nalezna_dieta_godz,2)} PLN).\n
            {zarcie_info}\n
            {ryc_noc_info}
            {ryc_kom_info}
            {ryc_auto_info}\n
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
        
        label_wybierz_kraj = Label(kraj_container, text="Wskaż kraj docelowy delegacji: ")
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
                
        zlabel_start = Label(self.page1, text="Wybierz datę i godzinę opuszczenia Polski")
        zlabel_start.grid(row=1, column=0, sticky=EW, padx=5, pady=5, columnspan=5)
        
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
        self.zwybor_godziny_startu = Spinbox(self.page1, width=5, wrap=True, values=godziny)
        self.zwybor_godziny_startu.grid(row=3, column=3, padx=5, pady=5, sticky=N)
        self.minutysz = IntVar()
        self.zwybor_minuty_startu = Spinbox(self.page1, width=5, wrap=True, values=minuty)
        self.zwybor_minuty_startu.grid(row=3, column=4, padx=5, pady=5, sticky=N)
        
        button_container = tk.Frame(self.page1)
        button_container.grid(row=5, column=0, padx=5, pady=5, columnspan=5)   

        self.back_button = tk.Button(button_container, text="STAWKI DIET ZAGRANICZNYCH", command=self.stawki_diet_zagra)
        self.back_button.grid(row=0, column=0, padx=10, columnspan=2)

        self.back_button = tk.Button(button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=1, column=0, sticky=E)
        
        self.button_next_page2 = tk.Button(button_container, text="DALEJ", command=self.next_page1)
        self.button_next_page2.grid(row=1, column=1, sticky=W)
        
    def strona_druga(self):
        self.page2 = tk.Frame(self)
        zlabel_start = Label(self.page2, text="Wybierz datę i godzinę powrotu do Polski")
        zlabel_start.grid(row=0, column=0, sticky=EW, padx=5, pady=5, columnspan=8)
        
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
        self.zwybor_godziny_konca = Spinbox(self.page2, width=5, wrap=True, values=godziny)
        self.zwybor_godziny_konca.grid(row=2, column=3, padx=5, pady=5, sticky=N)
        self.minutykz = IntVar()
        self.zwybor_minuty_konca = Spinbox(self.page2, width=5, wrap=True, values=minuty)
        self.zwybor_minuty_konca.grid(row=2, column=4, padx=5, pady=5, sticky=N)
        
        button_container = tk.Frame(self.page2)
        button_container.grid(row=4, column=0, padx=5, pady=5, columnspan=8)     

        self.button_back_page2 = tk.Button(button_container, text="WSTECZ", command=self.back_page2)
        self.button_back_page2.grid(row=0, column=0)
        
        self.back_button = tk.Button(button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=1)

        self.button_next_page2 = tk.Button(button_container, text="DALEJ", command=self.next_page2)
        self.button_next_page2.grid(row=0, column=2, columnspan=2)
        
    def strona_trzecia(self):
        self.page3 = tk.Frame(self)
        self.zlabel_posilki = Label(self.page3, text="Wskaż posiłki zapewnione podczas delegacji zagranicznej")
        self.zlabel_posilki.grid(row=0, column=0, sticky=EW, padx=5, pady=5, columnspan=8)
        
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
        self.zcheck_obiad.grid(row=2, column=0, padx=50, pady=5, sticky=W, columnspan=2)
        self.zlabel_obiad = Label(self.page3, text="w ilości")
        self.zlabel_obiad.grid(row=2, column=2, sticky=E, padx=5, pady=5)
        self.zilosc_obiad = Entry(self.page3, width=5, state=DISABLED)
        self.zilosc_obiad.grid(row=2, column=3, sticky=W, padx=5, pady=5)
        
        self.zvar3 = IntVar()
        self.zcheck_kolacja = Checkbutton(self.page3, text="KOLACJA", onvalue=1,
                                    offvalue=0, command=self.zchecking_kolacja, variable=self.zvar3)
        self.zcheck_kolacja.grid(row=3, column=0, padx=50, pady=5, sticky=W, columnspan=2)
        self.zlabel_kolacja = Label(self.page3, text="w ilości")
        self.zlabel_kolacja.grid(row=3, column=2, sticky=E, padx=5, pady=5)
        self.zilosc_kolacja = Entry(self.page3, width=5, state=DISABLED)
        self.zilosc_kolacja.grid(row=3, column=3, sticky=W, padx=5, pady=5)
        
        self.label_dodatki = Label(self.page3, text="Wskaż przysługujące ci ryczałty")
        self.label_dodatki.grid(row=4, column=0, sticky=EW, padx=5, pady=5, columnspan=8)
        
        self.nocleg_var1 = tk.BooleanVar()
        self.auto_var2 = tk.BooleanVar()
        self.komunikacja_var3 = tk.BooleanVar()
        self.dojazd_do_var4 = tk.BooleanVar()
        self.dojazd_z_var5 = tk.BooleanVar()
        
        self.checkframe = Frame(self.page3)
        self.checkframe.grid(row=5, column=0, columnspan=8)
        
        self.check_nocleg = Checkbutton(self.checkframe, text="NOCLEG", variable=self.nocleg_var1, command=self.rycz_nocleg)
        self.check_auto = Checkbutton(self.checkframe, text="PRYWATNE AUTO", variable=self.auto_var2, command=self.rycz_auto)
        self.check_komunikacja = Checkbutton(self.checkframe, text="KOMUNIKACJA MIEJSCOWA", variable=self.komunikacja_var3, command=self.rycz_komunikacja)
        self.check_dojazd_do= Checkbutton(self.checkframe, text="DOJAZD DO LOTNISKA", variable=self.dojazd_do_var4, command=self.rycz_dojazd_do)
        self.check_dojazd_z = Checkbutton(self.checkframe, text="DOJAZD Z LOTNISKA", variable=self.dojazd_z_var5, command=self.rycz_dojazd_z)
        self.check_nocleg.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.check_auto.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.check_komunikacja.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        self.check_dojazd_do.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        self.check_dojazd_z.grid(row=4, column=0, padx=5, pady=5, sticky=W)
        
        self.button_container = tk.Frame(self.page3)
        self.button_container.grid(row=8, column=0, padx=5, pady=5, columnspan=8)       
                
        self.button_back_page2 = tk.Button(self.button_container, text="WSTECZ", command=self.back_page3)
        self.button_back_page2.grid(row=0, column=0, sticky=E)
        
        self.back_button = tk.Button(self.button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=1)

        self.button_next_page2 = tk.Button(self.button_container, text="DALEJ", command=self.next_page3)
        self.button_next_page2.grid(row=0, column=2, sticky=W)
        
    def strona_czwarta(self):
        self.page4 = tk.Frame(self)
        
        self.zlabel_wynik = Label(self.page4)
        self.zlabel_wynik.grid(row=0, column=0, padx=5, pady=5, columnspan=8)
        
        button_container = tk.Frame(self.page4)
        button_container.grid(row=1, column=0, padx=5, pady=5, columnspan=8)
        
        self.button_back_page2 = tk.Button(button_container, text="WSTECZ", command=self.back_page4)
        self.button_back_page2.grid(row=0, column=0, sticky=E)

        self.back_button = tk.Button(button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=1, sticky=W)

    def stawki_diet_zagra(self):
        self.window = Toplevel()
        self.window.title("STAWKI DIET ZAGRANICZNYCH")
        self.window.resizable(True, True)

        self.frame = ttk.Frame(self.window, padding=5)
        self.frame.pack(fill="both", expand=True)
        
        self.table = ttk.Treeview(self.frame, columns=("Kraj", "Stawka", "Limity"), show="headings")
        self.table.heading("Kraj", text="Kraj")
        self.table.heading("Stawka", text="Stawka diety")
        self.table.heading("Limity", text="Limity hotelowe")

        self.table.column("Kraj", width=180)
        self.table.column("Stawka", width=100)
        self.table.column("Limity", width=100)

        for kraj, (waluta, stawka, limit) in diet_zagranica.items():
            self.table.insert("", "end", values=(kraj, f"{stawka} {waluta}", f"{limit} {waluta} "))
        
        self.scroll = ttk.Scrollbar(self.frame, orient="vertical", command=self.table.yview)
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
            s_miesiac = int(self.zcal_start.get_date()[4:5])
            s_dzien = int(self.zcal_start.get_date()[:2])
            s_godzina = int(self.zwybor_godziny_startu.get())
            s_minuta = int(self.zwybor_minuty_startu.get())
            k_rok = int(self.zcal_koniec.get_date()[-4:])
            k_miesiac = int(self.zcal_koniec.get_date()[4:5])
            k_dzien = int(self.zcal_koniec.get_date()[:2])
            k_godzina = int(self.zwybor_godziny_konca.get())
            k_minuta = int(self.zwybor_minuty_konca.get())
            data_startu = datetime(s_rok, s_miesiac, s_dzien, s_godzina, s_minuta)
            data_konca = datetime(k_rok, k_miesiac, k_dzien, k_godzina, k_minuta)
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

        label = tk.Label(self.top, text="Wprowadź liczbę przejechanych kilometrów:")
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

        option1 = Radiobutton(self.top, text="Auto z silnikiem o poj. do 900 cm3", variable=option_var, value=self.auto_do_900)
        option2 = Radiobutton(self.top, text="Auto z silnikiem o poj. ponad 900 cm3", variable=option_var, value=self.auto_ponad_900)
        option3 = Radiobutton(self.top, text="Motocykl", variable=option_var, value=self.motocykl)
        option4 = Radiobutton(self.top, text="Motorower", variable=option_var, value=self.motorower)
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
                messagebox.showerror("Wystąpił błąd", "Aby przejść dalej musisz wprowadzić kilometry i wybrać środek transportu.")

        submit_button = tk.Button(self.top, text="POTWIERDŹ", command=submit)
        submit_button.pack(padx=10, pady=10)

    def rycz_komunikacja(self):
        try:
            zet = str(self.wybor_kraju.get(ACTIVE))
            igrek = diet_zagranica[zet]
            dieta = igrek[1]
            s_rok = int(self.zcal_start.get_date()[-4:])
            s_miesiac = int(self.zcal_start.get_date()[4:5])
            s_dzien = int(self.zcal_start.get_date()[:2])
            s_godzina = int(self.zwybor_godziny_startu.get())
            s_minuta = int(self.zwybor_minuty_startu.get())
            k_rok = int(self.zcal_koniec.get_date()[-4:])
            k_miesiac = int(self.zcal_koniec.get_date()[4:5])
            k_dzien = int(self.zcal_koniec.get_date()[:2])
            k_godzina = int(self.zwybor_godziny_konca.get())
            k_minuta = int(self.zwybor_minuty_konca.get())
            data_startu = datetime(s_rok, s_miesiac, s_dzien, s_godzina, s_minuta)
            data_konca = datetime(k_rok, k_miesiac, k_dzien, k_godzina, k_minuta)
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
            s_miesiac = int(self.zcal_start.get_date()[4:5])
            s_dzien = int(self.zcal_start.get_date()[:2])
            s_godzina = int(self.zwybor_godziny_startu.get())
            s_minuta = int(self.zwybor_minuty_startu.get())
        except ValueError:
            info = ("Wprowadzono złą wartość godziny i/lub minuty")
            self.zlabel_wynik.config(text=info)
    
        try:
            k_rok = int(self.zcal_koniec.get_date()[-4:])
            k_miesiac = int(self.zcal_koniec.get_date()[4:5])
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
            ryc_noc_info = (f"Za ryczałt za nocleg należy ci się dodatkowo {round(self.ryczalt_nocleg,2)} PLN.")
        else:
            self.ryczalt_nocleg = 0   
            ryc_noc_info = (f"Nie uwzględniono ryczałtu za nocleg.")
        
        if self.auto_var2.get():
            self.ryczalt_auto
            ryc_auto_info = (f"Za ryczałt za pozdróż prywatnym środkiem transportu\n należy ci się dodatkowo {round(self.ryczalt_auto,2)} PLN.")
        else:
            self.ryczalt_auto = 0
            ryc_auto_info = (f"Nie uwzględniono ryczałtu za pozdróż prywatnym środkiem transportu.")

            
        if self.komunikacja_var3.get():
            self.ryczalt_komunikacja
            ryc_kom_info = (f"Za ryczałt za dojazd środkami komunikacji miejscowej\n należy ci sie dodatkowo {round(self.ryczalt_komunikacja,2)} PLN.")
        else:
            self.ryczalt_komunikacja = 0
            ryc_kom_info = (f"Nie uwzględniono ryczałtu za przejazd środkami komunikacji miejscowej.")

        if self.dojazd_do_var4.get():
            self.ryczalt_dojazd_do
            ryc_dojazd_do = (f"Za ryczałt za dojazd do lotniska należy ci sie dodatkowo {round(self.ryczalt_dojazd_do,2)} PLN.")
        else:
            self.ryczalt_dojazd_do = 0
            ryc_dojazd_do = (f"Nie uwzględniono ryczałtu za dojazd do lotniska.")
            
        if self.dojazd_z_var5.get():
            self.ryczalt_dojazd_z
            ryc_dojazd_z = (f"Za ryczałt za dojazd z lotniska należy ci sie dodatkowo {round(self.ryczalt_dojazd_z,2)} PLN.")
        else:
            self.ryczalt_dojazd_z = 0
            ryc_dojazd_z = (f"Nie uwzględniono ryczałtu za dojazd z lotniska.")
    
    
        zarcie = sniadanie + obiad + kolacja
        
        if zarcie != 0:
            zarcie_info = (f"Za zapewnione posiłki należy odjąć {round(zarcie,2)} PLN.")
        else:
            zarcie_info = (f"Podczas delegacji nie zapewniono zadnych posiłków.")

        
        nalezna_dieta = nalezna_dieta_dzien + \
            nalezna_dieta_godz - sniadanie - obiad - kolacja + self.ryczalt_nocleg + self.ryczalt_komunikacja + self.ryczalt_auto
        
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
    
        result = (f"""
            Delegacja {gamma} trwała \n{int(liczba_dni)} {wersja_dzien}, {int(liczba_godzin)} {wersja_godzin} i {int(liczba_minut)} {wersja_minut} ({round(nalezna_dieta_dzien,2)} {omega} + {round(nalezna_dieta_godz,2)} {omega}).\n
            {zarcie_info}\n
            {ryc_noc_info}
            {ryc_kom_info}
            {ryc_auto_info}
            {ryc_dojazd_do}
            {ryc_dojazd_z}\n
            Finalnie należy ci się {round(nalezna_dieta,2)} PLN.
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
    months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    days = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20","21", "22", "23", "24", "25", "26", "27", "28"]
    zodiac_signs = {("01", 20): "KOZIOROŻEC",("02", 19): "WODNIK",("03", 21): "RYBY",("04", 20): "BARAN",("05", 21): "BYK",
        ("06", 21): "BLIŹNIĘTA",("07", 23): "RAK",("08", 23): "LEW",("09", 23): "PANNA",("10", 23): "WAGA",("11", 22): "SKORPION",("12", 22): "STRZELEC"}

    
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
        L1.grid(row=0,column=0, padx=5, pady=5, columnspan=3)

        self.kalendarz = Calendar(self.tab1_gen, selectmode='day', date_pattern='dd/mm/yyyy', locale='pl_PL')
        date = self.kalendarz.datetime.today()
        self.kalendarz.grid(row=1,column=0, columnspan=3)

        self.plec_frame = Frame(self.tab1_gen)
        self.plec_frame.grid(row=2,column=0, padx=5, pady=5, columnspan=3)

        L2 = Label(self.plec_frame, text="Wybierz płeć:")
        L2.grid(row=0,column=0, padx=5, pady=5)

        self.man = IntVar()
        self.check_man = Checkbutton(self.plec_frame,
                                text="MĘŻCZYZNA",
                                variable=self.man,
                                command=self.checkbutton_man_selected)
        self.check_man.grid(row=0,column=1, padx=5, pady=5)


        self.woman = IntVar()
        self.check_woman = Checkbutton(self.plec_frame,
                                text="KOBIETA",
                                variable=self.woman,
                                command=self.checkbutton_woman_selected)
        self.check_woman.grid(row=0,column=2, padx=5, pady=5)

        self.przyciski_frame = Frame(self.tab1_gen)
        self.przyciski_frame.grid(row=3,column=0, padx=5, pady=5, columnspan=3)

        self.back_button0 = Button(self.przyciski_frame,
                            text="POWRÓT DO MENU",
                            command=self.back_to_menu,
                            state=ACTIVE,
                            compound=LEFT)
        self.back_button0.grid(row=0,column=0, sticky=W, padx=5, pady=5)
        
        self.gen_button = Button(self.przyciski_frame,
                            text="GENERUJ",
                            command=self.generate_pesel,
                            state=ACTIVE)
        self.gen_button.grid(row=0,column=1, sticky=E, padx=5, pady=5)

        self.copy_button0 = Button(self.przyciski_frame,
                            text="KOPIUJ",
                            command=self.copy_result,
                            state=DISABLED)
        self.copy_button0.grid(row=0,column=2, sticky=W, padx=5, pady=5)


        self.L4 = Label(self.tab1_gen)
        self.L4.grid(row=4,column=0, padx=5, pady=5, columnspan=3)


        self.L4a = Label(self.tab1_gen)
        self.L4a.grid(row=5,column=0, padx=5, pady=5, columnspan=3)


        # Zakładka numer 2 SPRAWDZANIE PESEL

        self.tab2_check = ttk.Frame(self.tabGeneral)
        self.tabGeneral.add(self.tab2_check, text='Sprawdź PESEL')

        self.Lab1 = Label(self.tab2_check, text="Wprowadź PESEL")
        self.Lab1.grid(row=0,column=0, padx=100, pady=5, sticky=N)

        self.Enter1 = Entry(self.tab2_check, width=15)
        self.Enter1.grid(row=1,column=0, padx=100, pady=5)

        self.przycisk_frame = Frame(self.tab2_check)
        self.przycisk_frame.grid(row=2,column=0, padx=5, pady=5)

        self.back_button1 = Button(self.przycisk_frame,
                            text="POWRÓT DO MENU",
                            command=self.back_to_menu,
                            state=ACTIVE,
                            compound=LEFT)
        self.back_button1.grid(row=0,column=0, sticky=W, padx=5, pady=5)

        self.check_button = Button(self.przycisk_frame,
                            text="SPRAWDŹ",
                            command=self.check_pesel,
                            state=ACTIVE)
        self.check_button.grid(row=0,column=1, padx=5, pady=5)

        self.Lab4 = Label(self.tab2_check)
        self.Lab4.grid(row=3,column=0, padx=5, pady=5)

        # Zakładka numer 3 TWORZENIE TOZSAMOSCI

        self.tab3_check = ttk.Frame(self.tabGeneral)
        self.tabGeneral.add(self.tab3_check, text='Stwórz tożsamość')

        self.Ldsd2 = Label(self.tab3_check, text="Wybierz płeć:")
        self.Ldsd2.grid(row=0,column=0, padx=5, pady=5)

        self.man_opt = IntVar()
        self.option_man = Checkbutton(self.tab3_check,
                                text="Mężczyzna",
                                variable=self.man_opt,
                                command=self.checkbutton_man_opt_selected)
        self.option_man.grid(row=0,column=1, padx=5, pady=5)

        self.woman_opt = IntVar()
        self.option_woman = Checkbutton(self.tab3_check,
                                text="Kobieta",
                                variable=self.woman_opt,
                                command=self.checkbutton_woman_opt_selected)
        self.option_woman.grid(row=0,column=2, padx=5, pady=5)

        self.L7 = Label(self.tab3_check, text="Podaj wiek w latach:")
        self.L7.grid(row=1,column=0, padx=5, pady=5)

        self.EE = Entry(self.tab3_check, width=15)
        self.EE.grid(row=1,column=1, columnspan=2, padx=5, pady=5, sticky=W)

        self.przycis_frame = Frame(self.tab3_check)
        self.przycis_frame.grid(row=2,column=0, padx=5, pady=5, columnspan=3)

        self.back_button1 = Button(self.przycis_frame,
                            text="POWRÓT DO MENU",
                            command=self.back_to_menu,
                            state=ACTIVE,
                            compound=LEFT)
        self.back_button1.grid(row=0,column=0, sticky=W, padx=5, pady=5)

        self.makenew_button = Button(self.przycis_frame,
                                text="STWÓRZ",
                                command=self.generate_identity,
                                state=ACTIVE,
                                compound=LEFT)
        self.makenew_button.grid(row=0,column=1, padx=5, pady=5, sticky=E)

        self.copy_button01 = Button(self.przycis_frame,
                            text="KOPIUJ",
                            command=self.copy_result2,
                            state=DISABLED,
                            compound=RIGHT)
        self.copy_button01.grid(row=0,column=2, padx=5, pady=5, sticky=W)

        self.Lab6 = Label(self.tab3_check)
        self.Lab6.grid(row=4,column=0, padx=5, pady=5, columnspan=3)

        self.Lab7 = Label(self.tab3_check)
        self.Lab7.grid(row=5,column=0, padx=5, pady=5, columnspan=3)
    
    def dob_from_pesel(self):
        #global dob_confirm
        if int(self.Enter1.get()[2]) == 1 or int(self.Enter1.get()[2]) == 0:
            self.dob_confirm = ("Data urodzenia to " + str(self.Enter1.get()[4:6]) + "-" + str(
                self.Enter1.get()[2:4]) + "-19" + (str(self.Enter1.get()[0:2])))
        if int(self.Enter1.get()[2]) == 8:
            self.dob_confirm = ("Data urodzenia to " + str(self.Enter1.get()
                        [4:6]) + "-0" + str(self.Enter1.get()[3]) + "-18" + (str(self.Enter1.get()[0:2])))
        if int(self.Enter1.get()[2]) == 9:
            self.dob_confirm = ("Data urodzenia to " + str(self.Enter1.get()
                        [4:6]) + "-1" + str(self.Enter1.get()[3]) + "-18" + (str(self.Enter1.get()[0:2])))
        if int(self.Enter1.get()[2]) == 2:
            self.dob_confirm = ("Data urodzenia to " + str(self.Enter1.get()
                        [4:6]) + "-0" + str(self.Enter1.get()[3]) + "-20" + (str(self.Enter1.get()[0:2])))
        if int(self.Enter1.get()[2]) == 3:
            self.dob_confirm = ("Data urodzenia to " + str(self.Enter1.get()
                        [4:6]) + "-1" + str(self.Enter1.get()[3]) + "-20" + (str(self.Enter1.get()[0:2])))
        if int(self.Enter1.get()[2]) == 4:
            self.dob_confirm = ("Data urodzenia to " + str(self.Enter1.get()
                        [4:6]) + "-0" + str(self.Enter1.get()[3]) + "-21" + (str(self.Enter1.get()[0:2])))
        if int(self.Enter1.get()[2]) == 5:
            self.dob_confirm = ("Data urodzenia to " + str(self.Enter1.get()
                        [4:6]) + "-1" + str(self.Enter1.get()[3]) + "-21" + (str(self.Enter1.get()[0:2])))
        if int(self.Enter1.get()[2]) == 6:
            self.dob_confirm = ("Data urodzenia to " + str(self.Enter1.get()
                        [4:6]) + "-0" + str(self.Enter1.get()[3]) + "-22" + (str(self.Enter1.get()[0:2])))
        if int(self.Enter1.get()[2]) == 7:
            self.dob_confirm = ("Data urodzenia to " + str(self.Enter1.get()
                        [4:6]) + "-1" + str(self.Enter1.get()[3]) + "-21" + (str(self.Enter1.get()[0:2])))
        return self.dob_confirm

    def sex_from_pesel(self):
        #global sex
        if int(self.Enter1.get()[9]) % 2 == 0:
            self.sex = "PESEL należy do kobiety."
            return self.sex
        else:
            self.sex = "PESEL należy do mężczyzny."
            return self.sex

    def check_pesel(self):
        #global result
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
                    result = "PESEL poprawny (zgadza się suma kontrolna)"
                else:
                    result = "PESEL niepoprawny (niewłaściwa suma kontrolna)"
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
            while True:
                position_1 = self.kalendarz.get_date()[8]
                position_2 = self.kalendarz.get_date()[9]
                if self.kalendarz.get_date()[6] == "1" and self.kalendarz.get_date()[7] == "8" and self.kalendarz.get_date()[3] == "0":
                    position_3 = 8
                if self.kalendarz.get_date()[6] == "1" and self.kalendarz.get_date()[7] == "8" and self.kalendarz.get_date()[3] == "1":
                    position_3 = 9
                if self.kalendarz.get_date()[6] == "2" and self.kalendarz.get_date()[7] == "0" and self.kalendarz.get_date()[3] == "0":
                    position_3 = 2
                if self.kalendarz.get_date()[6] == "2" and self.kalendarz.get_date()[7] == "0" and self.kalendarz.get_date()[3] == "1":
                    position_3 = 3
                if self.kalendarz.get_date()[6] == "2" and self.kalendarz.get_date()[7] == "1" and self.kalendarz.get_date()[3] == "0":
                    position_3 = 4
                if self.kalendarz.get_date()[6] == "2" and self.kalendarz.get_date()[7] == "1" and self.kalendarz.get_date()[3] == "1":
                    position_3 = 5
                if self.kalendarz.get_date()[6] == "2" and self.kalendarz.get_date()[7] == "2" and self.kalendarz.get_date()[3] == "0":
                    position_3 = 6
                if self.kalendarz.get_date()[6] == "2" and self.kalendarz.get_date()[7] == "2" and self.kalendarz.get_date()[3] == "1":
                    position_3 = 7
                if self.kalendarz.get_date()[6] == "1" and self.kalendarz.get_date()[7] == "9" and self.kalendarz.get_date()[3] == "0":
                    position_3 = self.kalendarz.get_date()[3]
                if self.kalendarz.get_date()[6] == "1" and self.kalendarz.get_date()[7] == "9" and self.kalendarz.get_date()[3] == "1":
                    position_3 = self.kalendarz.get_date()[3]
                position_4 = self.kalendarz.get_date()[4]
                position_5 = self.kalendarz.get_date()[0]
                position_6 = self.kalendarz.get_date()[1]
                position_7 = random.randint(0, 9)
                position_8 = random.randint(0, 9)
                position_9 = str(random.randint(0, 9))
                position_10 = random.choice(num_list)
                p_2 = str(position_2 * 3)
                p_3 = str(position_3 * 7)
                p_4 = str(position_4 * 9)
                p_6 = str(position_6 * 3)
                p_7 = str(position_7 * 7)
                p_8 = str(position_8 * 9)
                p_10 = str(position_10 * 3)
                sum = str(int(position_1[-1]) + int(p_2[-1]) + int(p_3[-1]) + int(p_4[-1]) + int(position_5[-1]) +
                        int(p_6[-1]) + int(p_7[-1]) + int(p_8[-1]) + int(position_9[-1]) + int(p_10[-1]))
                if int(sum[-1]) != 0:
                    break
            control_sum = 10 - int(sum[-1])
            self.generated_pesel = str(position_1) + str(position_2) + str(position_3) + str(position_4) + str(position_5) + str(position_6) + \
                str(position_7) + str(position_8) + str(position_9) + str(position_10) + str(control_sum)
            inf = ""
            self.L4.config(text=self.generated_pesel)
            self.L4a.config(text=inf)
            self.copy_button0.config(state=ACTIVE)
        elif self.woman.get() == 1:
            num_list = [0, 2, 4, 6, 8]
            while True:
                position_1 = self.kalendarz.get_date()[8]
                position_2 = self.kalendarz.get_date()[9]
                if self.kalendarz.get_date()[6] == "1" and self.kalendarz.get_date()[7] == "8" and self.kalendarz.get_date()[3] == "0":
                    position_3 = 8
                if self.kalendarz.get_date()[6] == "1" and self.kalendarz.get_date()[7] == "8" and self.kalendarz.get_date()[3] == "1":
                    position_3 = 9
                if self.kalendarz.get_date()[6] == "2" and self.kalendarz.get_date()[7] == "0" and self.kalendarz.get_date()[3] == "0":
                    position_3 = 2
                if self.kalendarz.get_date()[6] == "2" and self.kalendarz.get_date()[7] == "0" and self.kalendarz.get_date()[3] == "1":
                    position_3 = 3
                if self.kalendarz.get_date()[6] == "2" and self.kalendarz.get_date()[7] == "1" and self.kalendarz.get_date()[3] == "0":
                    position_3 = 4
                if self.kalendarz.get_date()[6] == "2" and self.kalendarz.get_date()[7] == "1" and self.kalendarz.get_date()[3] == "1":
                    position_3 = 5
                if self.kalendarz.get_date()[6] == "2" and self.kalendarz.get_date()[7] == "2" and self.kalendarz.get_date()[3] == "0":
                    position_3 = 6
                if self.kalendarz.get_date()[6] == "2" and self.kalendarz.get_date()[7] == "2" and self.kalendarz.get_date()[3] == "1":
                    position_3 = 7
                if self.kalendarz.get_date()[6] == "1" and self.kalendarz.get_date()[7] == "9" and self.kalendarz.get_date()[3] == "0":
                    position_3 = self.kalendarz.get_date()[3]
                if self.kalendarz.get_date()[6] == "1" and self.kalendarz.get_date()[7] == "9" and self.kalendarz.get_date()[3] == "1":
                    position_3 = self.kalendarz.get_date()[3]
                position_4 = self.kalendarz.get_date()[4]
                position_5 = self.kalendarz.get_date()[0]
                position_6 = self.kalendarz.get_date()[1]
                position_7 = random.randint(0, 9)
                position_8 = random.randint(0, 9)
                position_9 = str(random.randint(0, 9))
                position_10 = random.choice(num_list)
                p_2 = str(position_2 * 3)
                p_3 = str(position_3 * 7)
                p_4 = str(position_4 * 9)
                p_6 = str(position_6 * 3)
                p_7 = str(position_7 * 7)
                p_8 = str(position_8 * 9)
                p_10 = str(position_10 * 3)
                sum = str(int(position_1[-1]) + int(p_2[-1]) + int(p_3[-1]) + int(p_4[-1]) + int(position_5[-1]) +
                        int(p_6[-1]) + int(p_7[-1]) + int(p_8[-1]) + int(position_9[-1]) + int(p_10[-1]))
                if int(sum[-1]) != 0:
                    break
            control_sum = 10 - int(sum[-1])
            self.generated_pesel = str(position_1) + str(position_2) + str(position_3) + str(position_4) + str(position_5) + str(position_6) + \
                str(position_7) + str(position_8) + str(position_9) + \
                str(position_10) + str(control_sum)
            inf = ""
            self.L4.config(text=self.generated_pesel)
            self.L4a.config(text=inf)
            self.copy_button0.config(state=ACTIVE)


    def zodiaq(self):
        z_month = str(self.date_of_birth[3:5])
        z_day = int(self.date_of_birth[:2])

        for (month, day_limit), self.sign in self.zodiac_signs.items():
            if z_month == month and z_day <= day_limit:
                return self.sign
        
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
            if not self.EE.get().isdigit():
                generated_personality = "Wprowadzono niewłaściwy wiek!"
                self.Lab6.config(text=generated_personality)
                break
            if self.man_opt.get() == 1:
                name = random.choice(self.men_names)
                last_name = random.choice(self.men_surnames)
                year_of_birth = int(local_time.tm_year) - int(self.EE.get())
                month_of_birth = random.choice(self.months)
                day_of_birth = random.choice(self.days)
                self.date_of_birth = str(day_of_birth) + "-" + \
                    str(month_of_birth) + "-" + str(year_of_birth)
                dob_for_pesel = str(day_of_birth) + \
                    str(month_of_birth) + str(year_of_birth)
                num_list = [1, 3, 5, 7, 9]
                while True:
                    position_1 = dob_for_pesel[6]
                    position_2 = dob_for_pesel[7]
                    if dob_for_pesel[4] == "1" and dob_for_pesel[5] == "8" and dob_for_pesel[2] == "0":
                        position_3 = 8
                    if dob_for_pesel[4] == "1" and dob_for_pesel[5] == "8" and dob_for_pesel[2] == "1":
                        position_3 = 9
                    if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "0" and dob_for_pesel[2] == "0":
                        position_3 = 2
                    if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "0" and dob_for_pesel[2] == "1":
                        position_3 = 3
                    if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "1" and dob_for_pesel[2] == "0":
                        position_3 = 4
                    if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "1" and dob_for_pesel[2] == "1":
                        position_3 = 5
                    if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "2" and dob_for_pesel[2] == "0":
                        position_3 = 6
                    if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "2" and dob_for_pesel[2] == "1":
                        position_3 = 7
                    if dob_for_pesel[4] == "1" and dob_for_pesel[5] == "9" and dob_for_pesel[2] == "0":
                        position_3 = dob_for_pesel[2]
                    if dob_for_pesel[4] == "1" and dob_for_pesel[5] == "9" and dob_for_pesel[2] == "1":
                        position_3 = dob_for_pesel[2]
                    position_4 = dob_for_pesel[3]
                    position_5 = dob_for_pesel[0]
                    position_6 = dob_for_pesel[1]
                    position_7 = random.randint(0, 9)
                    position_8 = random.randint(0, 9)
                    position_9 = str(random.randint(0, 9))
                    position_10 = random.choice(num_list)
                    p_2 = position_2 * 3
                    p_3 = str(position_3 * 7)
                    p_4 = position_4 * 9
                    p_6 = position_6 * 3
                    p_7 = str(position_7 * 7)
                    p_8 = str(position_8 * 9)
                    p_10 = str(position_10 * 3)
                    sum = str(int(position_1[-1]) + int(p_2[-1]) + int(p_3[-1]) + int(p_4[-1]) + int(position_5[-1]) +
                            int(p_6[-1]) + int(p_7[-1]) + int(p_8[-1]) + int(position_9[-1]) + int(p_10[-1]))
                    if int(sum[-1]) != 0:
                        break
                control_sum = 10 - int(sum[-1])
                self.generated_pesel = str(position_1) + str(position_2) + str(position_3) + str(position_4) + str(position_5) + str(position_6) + \
                    str(position_7) + str(position_8) + str(position_9) + \
                    str(position_10) + str(control_sum)
                self.zodiaq()
                self.generated_identity = "Wygenerowana tożsamość:\n" + \
                    name + " " + last_name + "\nData urodzenia: " + \
                    self.date_of_birth + "\nPESEL: " + self.generated_pesel + "\nZnak zodiaku: " + self.sign
                self.Lab6.config(text=self.generated_identity)
                self.copy_button01.config(state=ACTIVE)
                break
            if self.woman_opt.get() == 1:
                name = random.choice(self.women_names)
                last_name = random.choice(self.women_surnames)
                year_of_birth = int(local_time.tm_year) - int(self.EE.get())
                month_of_birth = random.choice(self.months)
                day_of_birth = random.choice(self.days)
                self.date_of_birth = str(day_of_birth) + "-" + \
                    str(month_of_birth) + "-" + str(year_of_birth)
                dob_for_pesel = str(day_of_birth) + \
                    str(month_of_birth) + str(year_of_birth)
                num_list = [0, 2, 4, 6, 8]
                while True:
                    position_1 = dob_for_pesel[6]
                    position_2 = dob_for_pesel[7]
                    if dob_for_pesel[4] == "1" and dob_for_pesel[5] == "8" and dob_for_pesel[2] == "0":
                        position_3 = 8
                    if dob_for_pesel[4] == "1" and dob_for_pesel[5] == "8" and dob_for_pesel[2] == "1":
                        position_3 = 9
                    if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "0" and dob_for_pesel[2] == "0":
                        position_3 = 2
                    if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "0" and dob_for_pesel[2] == "1":
                        position_3 = 3
                    if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "1" and dob_for_pesel[2] == "0":
                        position_3 = 4
                    if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "1" and dob_for_pesel[2] == "1":
                        position_3 = 5
                    if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "2" and dob_for_pesel[2] == "0":
                        position_3 = 6
                    if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "2" and dob_for_pesel[2] == "1":
                        position_3 = 7
                    if dob_for_pesel[4] == "1" and dob_for_pesel[5] == "9" and dob_for_pesel[2] == "0":
                        position_3 = dob_for_pesel[2]
                    if dob_for_pesel[4] == "1" and dob_for_pesel[5] == "9" and dob_for_pesel[2] == "1":
                        position_3 = dob_for_pesel[2]
                    position_4 = dob_for_pesel[3]
                    position_5 = dob_for_pesel[0]
                    position_6 = dob_for_pesel[1]
                    position_7 = random.randint(0, 9)
                    position_8 = random.randint(0, 9)
                    position_9 = str(random.randint(0, 9))
                    position_10 = random.choice(num_list)
                    p_2 = position_2 * 3
                    p_3 = str(position_3 * 7)
                    p_4 = position_4 * 9
                    p_6 = position_6 * 3
                    p_7 = str(position_7 * 7)
                    p_8 = str(position_8 * 9)
                    p_10 = str(position_10 * 3)
                    sum = str(int(position_1[-1]) + int(p_2[-1]) + int(p_3[-1]) + int(p_4[-1]) + int(position_5[-1]) +
                            int(p_6[-1]) + int(p_7[-1]) + int(p_8[-1]) + int(position_9[-1]) + int(p_10[-1]))
                    if int(sum[-1]) != 0:
                        break
                control_sum = 10 - int(sum[-1])
                self.generated_pesel = str(position_1) + str(position_2) + str(position_3) + str(position_4) + str(position_5) + str(position_6) + \
                    str(position_7) + str(position_8) + str(position_9) + \
                    str(position_10) + str(control_sum)
                self.zodiaq()
                self.generated_identity = "Wygenerowana tożsamość::\n" + \
                    name + " " + last_name + "\nData urodzenia: " + \
                    self.date_of_birth + "\nPESEL: " + self.generated_pesel + "\nZnak zodiaku: " + self.sign
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

        #OBCE NA PLN
         
        self.label_start = Label(self.page1, text="Przeliczanie z waluty obcej na złotówki")
        self.label_start.grid(row=1, column=0, padx=5,pady=5, sticky=W, columnspan=3)
        
        self.kwota = Entry(self.page1)
        self.kwota.grid(row=2, column=0, sticky=NS, padx=5,pady=5)

        self.option_var = StringVar(self.page1)
        self.max_length = max(len(option) for option in options)

        self.option_menu = OptionMenu(self.page1, self.option_var, *options)
        self.option_menu.grid(row=2, column=1, sticky=NS)
        self.option_menu.config(width=self.max_length + 2)
        self.option_var.set("Wybierz walutę")

        self.button = Button(self.page1, text='Przelicz', command=self.konwertuj_do_pln)
        self.button.grid(row=2, column=2, sticky=NS, padx=5,pady=5)

        self.label1 = Label(self.page1)
        self.label1.grid(row=3, column=0, sticky=NS, columnspan=3, padx=5,pady=5)

        #PLN NA OBCE

        self.olabel_start = Label(self.page1, text="Przeliczanie ze złotówek na walutę obcą")
        self.olabel_start.grid(row=4, column=0, padx=5,pady=5, sticky=W, columnspan=3)
        
        self.okwota = Entry(self.page1)
        self.okwota.grid(row=5, column=0, sticky=NS, padx=5,pady=5)

        self.ooption_var = StringVar(self.page1)
        self.omax_length = max(len(option) for option in options)

        self.ooption_menu = OptionMenu(self.page1, self.ooption_var, *options)
        self.ooption_menu.grid(row=5, column=1, sticky=NS)
        self.ooption_menu.config(width=self.omax_length + 2)
        self.ooption_var.set("Wybierz walutę")

        self.obutton = Button(self.page1, text='Przelicz', command=self.konwertuj_z_pln)
        self.obutton.grid(row=5, column=2, sticky=NS, padx=5,pady=5)

        self.olabel1 = Label(self.page1)
        self.olabel1.grid(row=6, column=0, sticky=NS, columnspan=3, padx=5,pady=5)

        self.buttonframe = Frame(self.page1)
        self.buttonframe.grid(row=7, column=0, padx=10, pady=10, columnspan=3)

        self.back_button = tk.Button(self.buttonframe, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=0, padx=10, pady=10)
        
        self.tabela_button = tk.Button(self.buttonframe, text="KURS WALUT", command=self.tabela)
        self.tabela_button.grid(row=0, column=1, padx=10, pady=10)
  
    def tabela(self):
        self.table_window = tk.Toplevel(self)
        self.table_window.title("KURS WALUT")

        self.table = ttk.Treeview(self.table_window, columns=("Waluta", "Kurs"), show="headings")
        self.table.heading("Waluta", text="Waluta")
        self.table.heading("Kurs", text="Aktualny kurs")
        self.table.column("Waluta", width=180)
        self.table.column("Kurs", width=100)

        for waluta, skrot in tabela_nbp.items():
            kurs = self.kurs_walut(skrot)
            self.table.insert("", "end", values=(waluta, f"{kurs} PLN"))

        self.table.grid(row=0, column=0, padx=10, pady=10)
        self.table["height"] = len(tabela_nbp) 

        
    def kurs_walut(self,skrot):
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

                info = (f"{ilosc} {skrot} po kursie NBP z dnia {kurs_z_dnia} jest warte {round(calc,2)} PLN")
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

                info = (f"{ilosc} PLN po kursie NBP z dnia {kurs_z_dnia} jest warte {round(calc,2)} {skrot}")
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
        self.label1.pack()

        self.check_numbers = IntVar()
        self.check_button_numbers = Checkbutton(self.page1,
                                        text="Liczby",
                                        variable=self.check_numbers)
        self.check_button_numbers.pack()

        self.check_letters = IntVar()
        self.check_button_letters = Checkbutton(self.page1,
                                        text="Litery",
                                        variable=self.check_letters)
        self.check_button_letters.pack()

        self.check_special_characters = IntVar()
        self.check_button_special = Checkbutton(self.page1,
                                        text="Znaki specjalne",
                                        variable=self.check_special_characters)
        self.check_button_special.pack()

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
        self.scale.pack()

        self.gen_button = Button(self.page1,
                            text="GENERUJ",
                            command=self.click,
                            state=ACTIVE,
                            compound="left")
        self.gen_button.pack()
        
        self.back_button = tk.Button(self.page1, text="POWRÓT DO MENU", command=self.back_to_menu, compound="right")
        self.back_button.pack()

        self.label2 = Label(self.page1)
        self.label2.pack()

        self.label3 = Label(self.page1)
        self.label3.pack()
    
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
        
        self.input_label = tk.Label(self.page1, text="Wprowadź tekst do tłumaczenia")
        self.input_label.pack(padx=5, pady=5)

        self.input_text = tk.Text(self.page1, height=4)
        self.input_text.pack(padx=5, pady=5)

        self.translate_button = tk.Button(self.page1, text="TŁUMACZ", command=self.translate)
        self.translate_button.pack(padx=5, pady=5)

        self.output_label = tk.Label(self.page1, text="Tłumaczenie:")
        self.output_label.pack(padx=5, pady=5)

        self.output_text = tk.Text(self.page1, height=4)
        self.output_text.pack(padx=5, pady=5)
    
    def translate(self):
        all_chars = {"Й":"Y", "Ц":"TS","У":"U", "К":"K", "Е":"E", "Н":"N", "Г":"G", "Ш":"SH", "Ё":"E",
           "Щ":"SHCH", "З":"Z", "Х":"H", "Ъ":"", "Ф":"F", "Ы":"Y", "В":"V", "А":"A",
           "П":"P", "Р":"R", "О":"O", "Л":"L", "Д":"D", "Ж":"ZH", "Э":"E", "Я":"YA", 
           "Ч":"CH", "С":"S", "М":"M", "И":"I", "Т":"T", "Ь":"", "Б":"B", "Ю":"YU",  
           "й":"y",  "ц":"ts",  "у":"u",  "к":"k",  "е":"e",  "н":"n",  "г":"g",  
           "ш":"sh",  "щ":"shch",  "з":"z",  "х":"h",  "ъ":"",  "ф":"f",  "ы":"y",  
           "в":"v",  "а":"a",  "п":"p", "р":"r",  "о":"o",  "л":"l",  "д":"d", "ё":"e",  
           "ж":"zh",  "э":"e",  "я":"ya",  "ч":"ch",  "с":"s",  "м":"m",  "и":"i",  
           "т":"t",  "ь":"",  "б":"b",  "ю":"yu", " ":" "}
    
        text_to_translate = self.input_text.get("1.0", "end-1c")
        self.lista = [] 
        
        for char in text_to_translate:
            translated_char = all_chars.get(char, char)
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



"""
Diety krajowe:
- 

Diety zagraniczne:
- 

PESEL:
-

Kalkulator walut:
-

Transliteracja:
- klawiatura ekranowa z rosyjska klawiatura
- ogarnac to wizualnie

Generator haseł:
-

dodac planer podrozy
dodac genrator qrcodow 
"""