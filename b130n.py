import datetime
from datetime import datetime, timedelta
import random
import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, filedialog, Radiobutton
import tkinter.ttk as ttk
from tkcalendar import Calendar
import babel.numbers
import requests
import json
import secrets
import string
import time
import qrcode
import os
import math
import psutil
import feedparser


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
              "dirham ZEA [AED]": "AED", "rubel białoruski [BYN]": "BYN", "rubel rosyjski [RUB]": "RUB", "bat tajski [THB]": "THB", "dolar nowozelandzki [NZD]": "NZD", 
              "dolar singapurski [SGD]": "SGD", "lew bułgarski [BGN]": "BGN", "real brazylijski [BRL]": "BRL", "rupia indonezyjska [IDR]": "IDR", 
              "rupia indyjska [INR]": "INR", "won południowokoreański [KRW]": "KRW", "juan renminbi [CNY]": "CNY", "dong wietnamski [VND]": "VND", "nowy dolar tajwański [TWD]": "TWD"}
options = ["dolar amerykański [USD]", "dolar australijski [AUD]", "dolar kanadyjski [CAD]", "euro [EUR]",
           "forint [HUF]", "frank szwajcarski [CHF]", "funt szterling [GBP]", "hrywna [UAH]", "jen [JPY]",
           "korona czeska [CZK]", "korona duńska [DKK]", "korona islandzka [ISK]", "korona norweska [NOK]",
           "korona szwedzka [SEK]", "lej rumuński [RON]", "lira turecka [TRY]", "szekel [ILS]",
           "dirham ZEA [AED]", "rubel białoruski [BYN]", "rubel rosyjski [RUB]", "bat tajski [THB]", "dolar nowozelandzki [NZD]",
           "dolar singapurski [SGD]", "lew bułgarski [BGN]", "real brazylijski [BRL]", "rupia indonezyjska [IDR]",
           "rupia indyjska [INR]","won południowokoreański [KRW]","juan renminbi [CNY]","dong wietnamski [VND]","nowy dolar tajwański [TWD]"]
tablice_dyplomatyczne_kraj = {"001": "USA", "002": "Wielka Brytania", "003": "Francja", "004": "Kanada",
                                      "005": "Niemcy", "006": "Holandia", "007": "Włochy", "008": "Austria", "009": "Japonia",
                                      "010": "Turcja", "011": "Belgia", "012": "Dania", "013": "Norwegia", "014": "Grecja",
                                      "015": "Australia", "016": "Algieria", "017": "Afganistan", "018": "Argentyna",
                                      "019": "Brazylia", "020": "Bangladesz", "021": "Egipt", "022": "Ekwador", "023": "Finlandia",
                                      "024": "Hiszpania", "025": "Irak", "026": "Iran", "027": "Indie", "028": "Indonezja",
                                      "029": "Kolumbia", "030": "Malezja", "031": "Libia", "032": "Maroko", "033": "Meksyk",
                                      "034": "Nigeria", "035": "Pakistan", "036": "Portugalia", "037": "Palestyna", "038": "Syria",
                                      "039": "Szwecja", "040": "Szwajcaria", "041": "Tunezja", "042": "Tajlandia", "043": "Wenezuela",
                                      "044": "Urugwaj", "045": "Peru", "046": "Jemen", "047": "Kostaryka", "048": "Kongo",
                                      "049": "Izrael", "050": "Nikaragua", "051": "Chile", "052": "Watykan", "053": "Korea Południowa",
                                      "054": "Przedstawicielstwo Komisji Wspólnot Europejskich", "055": "Irlandia", "056": "Bank Światowy",
                                      "057": "Międzynarodowy Fundusz Walutowy", "058": "Filipiny", "059": "Międzynarodowa Korporacja Finansowa",
                                      "060": "RPA", "061": "Biuro Instytucji Demokratycznych i Praw Człowieka OBWE", "062": "Cypr",
                                      "063": "Kuwejt", "064": "Organizacja Narodów Zjednoczonych", "065": "Rosja", "066": "Słowacja",
                                      "067": "Czechy", "068": "Bułgaria", "069": "Węgry", "070": "Rumunia", "071": "Wietnam",
                                      "072": "Serbia", "073": "Korea Północna", "074": "Kuba", "075": "Albania", "076": "Chiny",
                                      "077": "Mongolia", "078": "Międzynarodowa Organizacja Pracy", "079": "Organizacja Kooperacyjna ds. Kolei",
                                      "080": "Klub Dyplomatyczny", "081": "Laos", "082": "Angola", "083": "Ukraina", "084": "Europejski Bank Odbudowy i Rozwoju",
                                      "085": "Litwa", "086": "Białoruś", "087": "Łotwa", "088": "Chorwacja", "089": "Liban",
                                      "090": "Słowenia", "091": "Gwatemala", "092": "Estonia", "093": "Macedonia", "094": "Mołdawia",
                                      "095": "Izrael", "096": "Armenia", "097": "Sri Lanka", "098": "Kazachstan", "099": "Arabia Saudyjska",
                                      "100": "Gruzja", "101": "Uzbekistan", "102": "UN-HABITAT", "103": "Nowa Zelandia", "104": "Azerbejdżan",
                                      "105": "Suwerenny Wojskowy Zakon Maltański", "106": "Kambodża", "107": "Frontex", "108": "Luksemburg",
                                      "109": "Bośnia i Hercegowina", "110": "Panama", "111": "Katar", "112": "Malta",
                                      "113": "Zjednoczone Emiraty Arabskie", "114": "Czarnogóra", "115": "Senegal"}
tablice_dyplomatyczne_funkcja = {(0, 199): "Prywatny pojazd personelu dyplomatycznego ambasady",
                                    (200, 299): "Prywatny pojazd attaché wojskowego",
                                    (300, 499): "Prywatny pojazd personelu niedyplomatycznego ambasady",
                                    (500, 501): "Służbowy pojazd ambasadora",
                                    (502, 699): "Służbowy pojazd ambasady",
                                    (700, 799): "Prywatny pojazd personelu dyplomatycznego konsulatu generalnego",
                                    (800, 899): "Prywatny pojazd personelu niedyplomatycznego konsulatu generalnego",
                                    (900, 901): "Służbowy pojazd konsula generalnego",
                                    (902, 999): "Służbowy pojazd konsulatu generalnego"}

tablice_wojewodztwa = {"B": "podlaskie", "C": "kujawsko-pomorskie", "D": "dolnośląskie", "E": "łódzkie", "F": "lubuskie",
                        "G": "pomorskie", "X": "pomorskie", "K": "małopolskie", "L": "lubelskie", "N": "warmińsko-mazurskie",
                        "O": "opolskie", "P": "wielkopolskie", "R": "podkarpackie", "S": "śląskie", "T": "świętokrzyskie", "W": "mazowieckie",
                        "Z": "zachodniopomorskie", "I": "śląskie", "J": "małopolskie", "M": "wielkopolskie", "Y": "podkarpackie",
                        "V": "dolnośląskie", "A": "mazowieckie"}

polskie_tablice_rejestracyjne = {"UA": "Siły zbrojne RP:\n samochód osobowy, osobowo-terenowy\n lub specjalny na podwoziu osobowym",
                                    "UB": "Siły zbrojne RP:\n transporter opancerzony", "UC": "Siły zbrojne RP:\n samochód dostawczy",
                                    "UD": "Siły zbrojne RP:\n autobus", "UE": "Siły zbrojne RP:\n samochód ciężarowy lub ciężarowo-terenowy\n o przeznaczeniu transportowym",
                                    "UG": "Siły zbrojne RP:\n pojazd specjalny\n na podwoziu ciężarowym", "UI": "Siły zbrojne RP:\n przyczepa transportowa",
                                    "UJ": "Siły zbrojne RP:\n przyczepa specjalna", "UK": "Siły zbrojne RP:\n motocykl", "HSB": "Kontrola skarbowa\n woj. podlaskie", "HSC": "Kontrola skarbowa\n woj. kujawsko-pomorskie", "HSD": "Kontrola skarbowa\n woj. dolnośląskie",
                                    "HSE": "Kontrola skarbowa\n woj. łódzkie", "HSF": "Kontrola skarbowa\n woj. lubuskie",
                                    "HSG": "Kontrola skarbowa\n woj. pomorskie", "HSK": "Kontrola skarbowa\n woj. małopolskie",
                                    "HSL": "Kontrola skarbowa\n woj. lubelskie", "HSN": "Kontrola skarbowa\n woj. warmińsko-mazurskie",
                                    "HSO": "Kontrola skarbowa\n woj. opolskie", "HSP": "Kontrola skarbowa\n woj. wielkopolskie",
                                    "HSR": "Kontrola skarbowa\n woj. podkarpackie", "HSS": "Kontrola skarbowa\n woj. śląskie",
                                    "HST": "Kontrola skarbowa\n woj. świętokrzyskie", "HSW": "Kontrola skarbowa\n woj. mazowieckie",
                                    "HSZ": "Kontrola skarbowa\n woj. zachodniopomorskie", "HCA": "Służba celna Olsztyn",
                                    "HCB": "Służba celna Białystok", "HCC": "Służba celna Biała Podlaska",
                                    "HCD": "Służba celna Przemyśl", "HCE": "Służba celna Kraków", "HCF": "Służba celna Katowice",
                                    "HCG": "Służba celna Wrocław", "HCH": "Służba celna Rzepin", "HCJ": "Służba celna Szczecin",
                                    "HCK": "Służba celna Gdynia", "HCL": "Służba celna Warszawa", "HCM": "Służba celna Toruń",
                                    "HCN": "Służba celna Łódź", "HCO": "Służba celna Poznań", "HCP": "Służba celna Opole",
                                    "HCR": "Służba celna Kielce", "HPA": "Komenda Główna Policji", "HPB": "Policja woj. dolnośląskie",
                                    "HPC": "Policja woj. kujawsko-pomorskie", "HPD": "Policja woj. lubelskie",
                                    "HPE": "Policja woj. lubuskie", "HPF": "Policja woj. łódzkie", "HPG": "Policja woj. małopolskie",
                                    "HPH": "Policja woj. mazowieckie", "HPJ": "Policja woj. opolskie", "HPK": "Policja woj. podkarpackie", "HPL": "Szkoła Policji w Szczytnie/Pile/Słupsku/Katowicach\n lub Centrum Szkolenia Policji w Legionowie",
                                    "HPM": "Policja woj. podlaskie", "HPN": "Policja woj. pomorskie", "HPP": "Policja woj. śląskie",
                                    "HPS": "Policja woj. świętokrzyskie", "HPT": "Policja woj. warmińsko-mazurskie",
                                    "HPU": "Policja woj. wielkopolskie", "HPW": "Policja woj. zachodniopomorskie",
                                    "HPZ": "Komenda Stołeczna Policji", "HA": "Centralne Biuro Antykorupcyjne",
                                    "HB": "Służba Ochrony Państwa", "HK": "Agencja Bezpieczeństwa Wewnętrznego\n lub Agencja Wywiadu",
                                    "HW": "Straż Graniczna", "HM": "Służba Wywiadu Wojskowego\n lub Służba Kontrwywiadu Wojskowego", "BI": "Białystok", "BS": "Suwałki", "BL": "Łomża", "BAU": "powiat augustowski",
                                    "BIA": "powiat białostocki", "BBI": "powiat bielski", "BGR": "powiat grajewski", "BHA": "powiat hajnowski",
                                    "BKL": "powiat kolneński", "BMN": "powiat moniecki", "BSE": "powiat sejneński", "BSI": "powiat siemiatycki",
                                    "BSK": "powiat sokólski", "BSU": "powiat suwalski", "BWM": "powiat wysokomazowiecki", "BZA": "powiat zambrowski",
                                    "BLM": "powiat łomżyński", "CB": "Bydgoszcz", "CG": "Grudziądz", "CT": "Toruń", "CW": "Włocławek", "CAL": "powiat aleksandrowski",
                                    "CBR": "powiat brodnicki", "CBY": "powiat bydgoski", "CCH": "powiat chełmiński", "CGD": "powiat golubsko-dobrzyński",
                                    "CGR": "powiat grudziądzki", "CIN": "powiat inowrocławski", "CLI": "powiat lipnowski", "CMG": "powiat mogileński",
                                    "CNA": "powiat nakielski", "CRA": "powiat radziejowski", "CRY": "powiat rypiński", "CSE": "powiat sępoleński",
                                    "CSW": "powiat świecki", "CTR": "powiat toruński", "CTU": "powiat tucholski", "CWA": "powiat wąbrzeski",
                                    "CWL": "powiat włocławski", "CZN": "powiat żniński", "DJ": "Jelenia Góra", "VJ": "Jelenia Góra", "DL": "Legnica", "DB": "Wałbrzych", "VL": "Legnica", "VB": "Wałbrzych", "DW": "Wrocław", "DX": "Wrocław", "VW": "Wrocław", "VX": "Wrocław", "VBL": "powiat bolesławiecki",
                                    "DBL": "powiat bolesławiecki", "VBL": "powiat bolesławiecki", "DDZ": "powiat dzierżoniowski", "VDZ": "powiat dzierżoniowski",
                                    "DGR": "powiat górowski", "VGR": "powiat górowski", "DGL": "powiat głogowski", "VGL": "powiat głogowski",
                                    "DGL": "powiat głogowski", "VGL": "powiat głogowski", "DJE": "powiat jeleniogórski", "VJE": "powiat jeleniogórski",
                                    "DKA": "powiat kamiennogórski", "VKA": "powiat kamiennogórski", "DKL": "powiat kłodzki", "VKL": "powiat kłodzki",
                                    "DLE": "powiat legnicki", "VLE": "powiat legnicki", "DLB": "powiat lubański", "VLB": "powiat lubański",
                                    "DLU": "powiat lubiński", "VLU": "powiat lubiński", "DLW": "powiat lwówecki", "VLW": "powiat lwówecki",
                                    "DMI": "powiat milicki", "VMI": "powiat milicki", "DOL": "powiat oleśnicki", "VOL": "powiat oleśnicki",
                                    "DOA": "powiat oławski", "VOA": "powiat oławski", "DPL": "powiat polkowicki", "VPL": "powiat polkowicki",
                                    "DSR": "powiat średzki", "VSR": "powiat średzki", "DST": "powiat strzeliński", "VST": "powiat strzeliński",
                                    "DSW": "powiat świdnicki", "VSW": "powiat świdnicki", "DTR": "powiat trzebnicki", "VTR": "powiat trzebnicki",
                                    "DBA": "powiat wałbrzyski", "VBA": "powiat wałbrzyski", "DWL": "powiat wołowski", "VWL": "powiat wołowski",
                                    "DWR": "powiat wrocławski", "VWR": "powiat wrocławski", "DZA": "powiat ząbkowicki", "VZA": "powiat ząbkowicki",
                                    "DZG": "powiat zgorzelecki", "VZG": "powiat zgorzelecki", "DZL": "powiat złotoryjski", "VZL": "powiat złotoryjski", "ED": "Łódź",
                                    "EP": "Piotrków Trybunalski", "ES": "Skierniewice", "EL": "Łódź", "EBE": "powiat bełchatowski", "EBR": "powiat brzeziński", "EKU": "powiat kutnowski", "EOP": "powiat opoczyński", "EPA": "powiat pabianicki", "EPJ": "powiat pajęczański", "EPI": "powiat piotrkowski",
                                    "EPD": "powiat poddębicki", "ERA": "powiat radomszczański", "ERW": "powiat rawski", "ESI": "powiat sieradzki",
                                    "ESK": "powiat skierniewicki", "ETM": "powiat tomaszowski", "EWI": "powiat wieluński", "EWE": "powiat wieruszowski",
                                    "EZD": "powiat zduńskowolski", "EZG": "powiat zgierski", "ELA": "powiat łaski", "ELE": "powiat łęczycki",
                                    "ELW": "powiat łódzki wschodni", "ELC": "powiat łowicki", "FG": "Gorzów Wielkopolski", "FZ": "Zielona Góra",
                                    "FGW": "powiat gorzowski", "FKR": "powiat krośnieński", "FMI": "powiat międzyrzecki", "FNW": "powiat nowosolski",
                                    "FSD": "powiat strzelecko-drezdenecki", "FSU": "powiat sulęciński", "FSW": "powiat świebodziński",
                                    "FSL": "powiat słubicki", "FWS": "powiat wschowski", "FZG": "powiat żagański", "FZA": "powiat żarski",
                                    "FZI": "powiat zielonogórski", "GD": "Gdańsk", "XD": "Gdańsk", "GA": "Gdynia", "XA": "Gdynia",
                                    "GSP": "Sopot", "XSP": "Sopot", "GS": "Słupsk", "XS": "Słupsk", "GBY": "powiat bytowski", "XBY": "powiat bytowski",
                                    "GCH": "powiat chojnicki", "XCH": "powiat chojnicki", "GCZ": "powiat człuchowski", "XCZ": "powiat człuchowski",
                                    "GDA": "powiat gdański", "XDA": "powiat gdański", "GKA": "powiat kartuski", "GKY": "powiat kartuski", "GKZ": "powiat kartuski",
                                    "XKA": "powiat kartuski", "XKY": "powiat kartuski", "XKZ": "powiat kartuski", "GKS": "powiat kościerski", "XKS": "powiat kościerski",
                                    "GKW": "powiat kwidzyński", "XKW": "powiat kwidzyński", "GLE": "powiat lęborski", "XLE": "powiat lęborski",
                                    "GMB": "powiat malborski", "XMB": "powiat malborski", "GND": "powiat nowodworski", "XND": "powiat nowodworski",
                                    "GPU": "powiat pucki", "XPU": "powiat pucki", "GST": "powiat starogardzki", "XST": "powiat starogardzki",
                                    "GSZ": "powiat sztumski", "XSZ": "powiat sztumski", "GSL": "powiat słupski", "XSL": "powiat słupski",
                                    "GTC": "powiat tczewski", "XTC": "powiat tczewski", "GWE": "powiat wejherowski", "GWO": "powiat wejherowski",
                                    "XWE": "powiat wejherowski", "XWO": "powiat wejherowski", "KK": "Kraków", "KR": "Kraków", "JK": "Kraków", "JR": "Kraków",
                                    "KN": "Nowy Sącz", "JN": "Nowy Sącz", "KT": "Tarnów", "JT": "Tarnów", "KBC": "powiat bocheński", "JBC": "powiat bocheński",
                                    "KBA": "powiat bocheński", "JBA": "powiat bocheński", "KBR": "powiat brzeski", "JBR": "powiat brzeski",
                                    "KCH": "powiat chrzanowski", "JCH": "powiat chrzanowski", "KDA": "powiat dąbrowski", "JDA": "powiat dąbrowski",
                                    "KGR": "powiat gorlicki", "JGR": "powiat gorlicki", "KRA": "powiat krakowski", "JRA": "powiat krakowski",
                                    "KLI": "powiat limanowski", "JLI": "powiat limanowski", "KMI": "powiat miechowski", "JMI": "powiat miechowski",
                                    "KMY": "powiat myślenicki", "JMY": "powiat myślenicki", "KNS": "powiat nowosądecki", "JNS": "powiat nowosądecki",
                                    "KNT": "powiat nowotarski", "JNT": "powiat nowotarski", "KOL": "powiat olkuski", "JOL": "powiat olkuski",
                                    "KOS": "powiat oświęcimski", "JOS": "powiat oświęcimski", "KPR": "powiat proszowicki", "JPR": "powiat proszowicki",
                                    "KSU": "powiat suski", "JSU": "powiat suski", "KTA": "powiat tarnowski", "JTA": "powiat tarnowski",
                                    "KTT": "powiat tatrzański", "JTT": "powiat tatrzański", "KWA": "powiat wadowicki", "JWA": "powiat wadowicki",
                                    "KWI": "powiat wielicki", "JWI": "powiat wielicki", "LB": "Biała Podlaska", "LC": "Chełm", "LU": "Lublin", "LZ": "Zamość", "LBI": "powiat bialski", "LBL": "powiat biłgorajski", "LCH": "powiat chełmski", "LHR": "powiat hrubieszowski", "LJA": "powiat janowski", "LKR": "powiat kraśnicki",
                                    "LKS": "powiat krasnostawski", "LLB": "powiat lubartowski", "LUB": "powiat lubelski", "LOP": "powiat opolski",
                                    "LPA": "powiat parczewski", "LPU": "powiat puławski", "LRA": "powiat radzyński", "LRY": "powiat rycki",
                                    "LSW": "powiat świdnicki", "LTM": "powiat tomaszowski", "LWL": "powiat włodawski", "LZA": "powiat zamojski",
                                    "LLE": "powiat łęczyński", "LLU": "powiat łukowski", "NE": "Elbląg", "NO": "Olsztyn", "NBA": "powiat bartoszycki",
                                    "NBR": "powiat braniewski", "NDZ": "powiat działdowski", "NEB": "powiat elbląski", "NEL": "powiat ełcki",
                                    "NGI": "powiat giżycki", "NGO": "powiat gołdapski", "NIL": "powiat iławski", "NKE": "powiat kętrzyński",
                                    "NLI": "powiat lidzbarski", "NMR": "powiat mrągowski", "NNI": "powiat nidzicki", "NNM": "powiat nowomiejski",
                                    "NOE": "powiat olecki", "NOL": "powiat olsztyński", "NOS": "powiat ostródzki", "NPI": "powiat piski",
                                    "NSZ": "powiat szczycieński", "NWE": "powiat węgorzewski", "OP": "Opole", "OB": "powiat brzeski", "OGL": "powiat głubczycki",
                                    "OK": "powiat kędzierzyńsko-kozielski", "OKL": "powiat kluczborski", "OKR": "powiat krapkowicki",
                                    "ONA": "powiat namysłowski", "ONY": "powiat nyski", "OOL": "powiat oleski", "OPO": "powiat opolski",
                                    "OPR": "powiat prudnicki", "OST": "powiat strzelecki", "PK": "Kalisz", "PA": "Kalisz", "MK": "Kalisz", "MA": "Kalisz",
                                    "PN": "Konin", "PKO": "Konin", "MN": "Konin", "MKO": "Konin", "PL": "Leszno", "ML": "Leszno", "PO": "Poznań", "MO": "Poznań",
                                    "PY": "Poznań", "MY": "Poznań", "PCH": "powiat chodzieski", "MCH": "powiat chodzieski",
                                    "PCT": "powiat czarnkowsko-trzcianecki", "MCT": "powiat czarnkowsko-trzcianecki",
                                    "PGN": "powiat gnieźnieński", "MGN": "powiat gnieźnieński", "PGS": "powiat gostyński", "MGS": "powiat gostyński",
                                    "PGO": "powiat grodziski", "MGO": "powiat grodziski", "PJA": "powiat jarociński", "MJA": "powiat jarociński",
                                    "PKA": "powiat kaliski", "MKA": "powiat kaliski", "PKE": "powiat kępiński", "MKE": "powiat kępiński",
                                    "PKL": "powiat kolski", "MKL": "powiat kolski", "PKN": "powiat koniński", "MKN": "powiat koniński",
                                    "PKS": "powiat kościański", "MKS": "powiat kościański", "PKR": "powiat krotoszyński", "MKR": "powiat krotoszyński",
                                    "PLE": "powiat leszczyński", "MLE": "powiat leszczyński", "PMI": "powiat międzychodzki", "MMI": "powiat międzychodzki",
                                    "PNT": "powiat nowotomyski", "MNT": "powiat nowotomyski", "POB": "powiat obornicki", "MOB": "powiat obornicki",
                                    "POS": "powiat ostrowski", "MOS": "powiat ostrowski", "POT": "powiat ostrzeszowski", "MOT": "powiat ostrzeszowski",
                                    "PP": "powiat pilski", "MP": "powiat pilski", "PPL": "powiat pleszewski", "MPL": "powiat pleszewski",
                                    "PZ": "powiat poznański", "POZ": "powiat poznański", "MZ": "powiat poznański", "MOZ": "powiat poznański",
                                    "PRA": "powiat rawicki", "MRA": "powiat rawicki", "PSR": "powiat średzki", "MSR": "powiat średzki",
                                    "PSE": "powiat śremski", "MSE": "powiat śremski", "PSZ": "powiat szamotulski", "MSZ": "powiat szamotulski",
                                    "PSL": "powiat słupecki", "MSL": "powiat słupecki", "PTU": "powiat turecki", "MTU": "powiat turecki",
                                    "PWA": "powiat wągrowiecki", "MWA": "powiat wągrowiecki", "PWL": "powiat wolsztyński", "MWL": "powiat wolsztyński",
                                    "PWR": "powiat wrzesiński", "MWR": "powiat wrzesiński", "PZL": "powiat złotowski", "MZL": "powiat złotowski",
                                    "RK": "Krosno", "YK": "Krosno", "RP": "Przemyśl", "YP": "Przemyśl", "RZ": "Rzeszów", "YZ": "Rzeszów",
                                    "RT": "Tarnobrzeg", "YT": "Tarnobrzeg", "RBI": "powiat bieszczadzki", "YBI": "powiat bieszczadzki",
                                    "RBR": "powiat brzozowski", "YBR": "powiat brzozowski", "RDE": "powiat dębicki", "YDE": "powiat dębicki",
                                    "RJA": "powiat jarosławski", "YJA": "powiat jarosławski", "RJS": "powiat jasielski", "YJS": "powiat jasielski",
                                    "RKL": "powiat kolbuszowski", "YKL": "powiat kolbuszowski", "RKR": "powiat krośnieński", "YKR": "powiat krośnieński",
                                    "RLS": "powiat leski", "YLS": "powiat leski", "RLE": "powiat leżajski", "YLE": "powiat leżajski",
                                    "RLU": "powiat lubaczowski", "YLU": "powiat lubaczowski", "RMI": "powiat mielecki", "YMI": "powiat mielecki",
                                    "RNI": "powiat niżański", "YNI": "powiat niżański", "RPR": "powiat przemyski", "YPR": "powiat przemyski",
                                    "RPZ": "powiat przeworski", "YPZ": "powiat przeworski", "RRS": "powiat ropczycko-sędziszowski", "YRS": "powiat ropczycko-sędziszowski",
                                    "RZE": "powiat rzeszowski", "RZZ": "powiat rzeszowski", "RZR": "powiat rzeszowski", "YZE": "powiat rzeszowski", "YZZ": "powiat rzeszowski", "YZR": "powiat rzeszowski", "RSA": "powiat sanocki", "YSA": "powiat sanocki", "RST": "powiat stalowowolski", "YST": "powiat stalowowolski",
                                    "RSR": "powiat strzyżowski", "YSR": "powiat strzyżowski", "RTA": "powiat tarnobrzeski", "YTA": "powiat tarnobrzeski",
                                    "RLA": "powiat łańcucki", "YLA": "powiat łańcucki", "SB": "Bielsko-Biała", "IB": "Bielsko-Biała",
                                    "SY": "Bytom", "IY": "Bytom", "SH": "Chorzów", "IH": "Chorzów", "SC": "Częstochowa", "IC": "Częstochowa",
                                    "SD": "Dąbrowa Górnicza", "ID": "Dąbrowa Górnicza", "SG": "Gliwice", "IG": "Gliwice", "SJZ": "Jastrzębie-Zdrój", "IJZ": "Jastrzębie-Zdrój",
                                    "SJ": "Jaworzno", "IJ": "Jaworzno", "SK": "Katowice", "IK": "Katowice", "SM": "Mysłowice", "IM": "Mysłowice",
                                    "SPI": "Piekary Śląskie", "IPI": "Piekary Śląskie", "SL": "Ruda Śląska", "SRS": "Ruda Śląska", "IL": "Ruda Śląska", "IRS": "Ruda Śląska",
                                    "SR": "Rybnik", "IR": "Rybnik", "SI": "Siemianowice Śląskie", "II": "Siemianowice Śląskie", "SO": "Sosnowiec", "IO": "Sosnowiec",
                                    "SW": "Świętochłowice", "IW": "Świętochłowice", "ST": "Tychy", "IT": "Tychy", "SZ": "Zabrze", "IZ": "Zabrze", "SZO": "Żory", "IZO": "Żory",
                                    "SBE": "powiat będziński", "SE": "powiat będziński", "SBN": "powiat będziński", "IBE": "powiat będziński", "IE": "powiat będziński", "IBN": "powiat będziński", "SBI": "powiat bielski", "IBI": "powiat bielski", "SBL": "powiat bieruńsko-lędziński", "IBL": "powiat bieruńsko-lędziński", "SCI": "powiat cieszyński", "SCN": "powiat cieszyński", "ICI": "powiat cieszyński", "ICN": "powiat cieszyński",
                                    "SCZ": "powiat częstochowski", "ICZ": "powiat częstochowski", "SGL": "powiat gliwicki", "IGL": "powiat gliwicki",
                                    "SKL": "powiat kłobucki", "IKL": "powiat kłobucki", "SLU": "powiat lubliniecki", "ILU": "powiat lubliniecki",
                                    "SMI": "powiat mikołowski", "IMI": "powiat mikołowski", "SMY": "powiat myszkowski", "IMY": "powiat myszkowski",
                                    "SPS": "powiat pszczyński", "IPS": "powiat pszczyński", "SRC": "powiat raciborski", "IRC": "powiat raciborski",
                                    "SRB": "powiat rybnicki", "IRB": "powiat rybnicki", "STA": "powiat tarnogórski", "ITA": "powiat tarnogórski",
                                    "IWD": "powiat wodzisławski", "IWZ": "powiat wodzisławski", "SWD": "powiat wodzisławski", "SWZ": "powiat wodzisławski",
                                    "SZA": "powiat zawierciański", "IZA": "powiat zawierciański", "SZY": "powiat żywiecki", "IZY": "powiat żywiecki",
                                    "TK": "Kielce", "TBU": "powiat buski", "TJE": "powiat jędrzejowski", "TKA": "powiat kazimierski", "TKI": "powiat kielecki",
                                    "TKN": "powiat konecki", "TOP": "powiat opatowski", "TOS": "powiat ostrowiecki", "TPI": "powiat pińczowski",
                                    "TSA": "powiat sandomierski", "TSK": "powiat skarżyski", "TST": "powiat starachowicki", "TSZ": "powiat staszowski",
                                    "TLW": "powiat włoszczowski", "WO": "Ostrołęka", "AO": "Ostrołęka", "WP": "Płock", "AP": "Płock", "WR": "Radom", "AR": "Radom",
                                    "WS": "Siedlce", "AS": "Siedlce", "WB": "Warszawa Bemowo", "AB": "Warszawa Bemowo",
                                    "WA": "Warszawa Białołęka", "AA": "Warszawa Białołęka", "WD": "Warszawa Bielany", "AD": "Warszawa Bielany",
                                    "WE": "Warszawa Mokotów", "AE": "Warszawa Mokotów", "WU": "Warszawa Ochota", "AU": "Warszawa Ochota",
                                    "WH": "Warszawa Praga Północ", "AH": "Warszawa Praga Północ", "WF": "Warszawa Praga Południe", "AF": "Warszawa Praga Południe",
                                    "WI": "Warszawa Śródmieście", "AI": "Warszawa Śródmieście", "WJ": "Warszawa Targówek", "AJ": "Warszawa Targówek",
                                    "WK": "Warszawa Ursus", "AK": "Warszawa Ursus", "WN": "Warszawa Ursynów", "AN": "Warszawa Ursynów",
                                    "WT": "Warszawa Wawer", "AT": "Warszawa Wawer", "WBR": "powiat białobrzeski", "ABR": "powiat białobrzeski",
                                    "WCI": "powiat ciechanowski", "ACI": "powiat ciechanowski", "WG": "powiat garwoliński", "AG": "powiat garwoliński",
                                    "WGS": "powiat gostyniński", "AGS": "powiat gostyniński", "WGM": "powiat grodziski", "AGM": "powiat grodziski",
                                    "WGR": "powiat grójecki", "AGR": "powiat grójecki", "WKZ": "powiat kozienicki", "AKZ": "powiat kozienicki",
                                    "WL": "powiat legionowski", "AL": "powiat legionowski", "WLI": "powiat lipski", "ALI": "powiat lipski",
                                    "WMA": "powiat makowski", "AMA": "powiat makowski", "WM": "powiat miński", "AM": "powiat miński",
                                    "WML": "powiat mławski", "AML": "powiat mławski", "WND": "powiat nowodworski", "AND": "powiat nowodworski",
                                    "WOR": "powiat ostrowski", "AOR": "powiat ostrowski", "WOS": "powiat ostrołęcki", "AOS": "powiat ostrołęcki",
                                    "WOT": "powiat otwocki", "AOT": "powiat otwocki", "WPI": "powiat piaseczyński", "WPA": "powiat piaseczyński", "WPW": "powiat piaseczyński", "WPX": "powiat piaseczyński", "API": "powiat piaseczyński", "APA": "powiat piaseczyński", "APW": "powiat piaseczyński", "APX": "powiat piaseczyński", "WPS": "powiat pruszkowski", "WPR": "powiat pruszkowski", "WPP": "powiat pruszkowski",
                                    "APS": "powiat pruszkowski", "APR": "powiat pruszkowski", "APP": "powiat pruszkowski",
                                    "WPZ": "powiat przasnyski", "APZ": "powiat przasnyski", "WPY": "powiat przysuski", "APY": "powiat przysuski",
                                    "WPU": "powiat pułtuski", "APU": "powiat pułtuski", "WPL": "powiat płocki", "APL": "powiat płocki",
                                    "WPN": "powiat płoński", "APN": "powiat płoński", "WRA": "powiat radomski", "ARA": "powiat radomski",
                                    "WSI": "powiat siedlecki", "ASI": "powiat siedlecki", "WSE": "powiat sierpecki", "ASE": "powiat sierpecki",
                                    "WSC": "powiat sochaczewski", "ASC": "powiat sochaczewski", "WSK": "powiat sokołowski", "ASK": "powiat sokołowski",
                                    "WSZ": "powiat szydłowiecki", "ASZ": "powiat szydłowiecki", "WZ": "powiat warszawski zachodni", "AZ": "powiat warszawski zachodni",
                                    "WWE": "powiat węgrowski", "AWE": "powiat węgrowski", "WWL": "powiat wołomiński", "AWL": "powiat wołomiński",
                                    "WV": "powiat wołomiński", "AV": "powiat wołomiński", "WWY": "powiat wyszkowski", "AWY": "powiat wyszkowski",
                                    "WZU": "powiat żuromiński", "AZU": "powiat żuromiński", "WZW": "powiat zwoleński", "AZW": "powiat zwoleński",
                                    "WZY": "powiat żyrardowski", "AZY": "powiat żyrardowski", "WLS": "powiat łosicki", "ALS": "powiat łosicki",
                                    "ZK": "Koszalin", "ZSW": "Świnoujście", "ZS": "Szczecin", "ZZ": "Szczecin", "ZBI": "powiat białogardzki",
                                    "ZCH": "powiat choszczeński", "ZDR": "powiat drawski", "ZGL": "powiat goleniowski", "ZGY": "powiat gryficki",
                                    "ZGR": "powiat gryfiński", "ZKA": "powiat kamieński", "ZKO": "powiat koszaliński", "ZKL": "powiat kołobrzeski",
                                    "ZMY": "powiat myśliborski", "ZPL": "powiat policki", "ZPY": "powiat pyrzycki", "ZST": "powiat stargardzki",
                                    "ZSD": "powiat świdwiński", "ZSZ": "powiat szczecinecki", "ZSL": "powiat sławieński", "ZWA": "powiat wałecki",
                                    "ZLO": "powiat łobeski"}
wojsko = {"UAxxxxx": "samochód osobowy", "UBxxxxx": "Transporter opancerzony", "UCxxxxx": "Samochód dostawczy",
          "UDxxxxx": "Autobus", "UExxxxx": "Samochód ciężarowy", "UGxxxxx": "Pojazd specjalny na podwoziu ciężarowym", "UIxxxxx": "Przyczepa transportowa",
          "UJxxxxx": "Przyczepa specjalna", "UKxxxxx": "Motocykl"}
kontrola_skarbowa = {"HSBxxxxx": "Woj. podlaskie", "HSCxxxxx": "Woj. kujawsko-pomorskie", "HSDxxxxx": "Woj. dolnośląskie",
                     "HSExxxxx": "Woj. łódzkie", "HSFxxxxx": "Woj. lubuskie","HSGxxxxx": "Woj. pomorskie", "HSKxxxxx": "Woj. małopolskie",
                     "HSLxxxxx": "Woj. lubelskie", "HSNxxxxx": "Woj. warmińsko-mazurskie", "HSOxxxxx": "Woj. opolskie", "HSPxxxxx": "Woj. wielkopolskie",
                     "HSRxxxxx": "Woj. podkarpackie", "HSSxxxxx": "Woj. śląskie", "HSTxxxxx": "Woj. świętokrzyskie", "HSWxxxxx": "Woj. mazowieckie", "HSZxxxxx": "Woj. zachodniopomorskie"}
sluzba_celna = {"HCAxxxxx": "Olsztyn", "HCBxxxxx": "Białystok", "HCCxxxxx": "Biała Podlaska", "HCGxxxxx": "Wrocław", "HCHxxxxx": "Rzepin", "HCJxxxxx": "Szczecin", "HCKxxxxx": "Gdynia", "HCLxxxxx": "Warszawa", "HCMxxxxx": "Toruń",
                "HCNxxxxx": "Łódź", "HCOxxxxx": "Poznań", "HCPxxxxx": "Opole", "HCRxxxxx": "Kielce"}
policja = {"HPAxxxxx": "Komenda Główna Policji", "HPBxxxxx": "Woj. dolnośląskie", "HPCxxxxx": "Woj. kujawsko-pomorskie", "HPDxxxxx": "Woj. lubelskie", "HPExxxxx": "Woj. lubuskie", "HPFxxxxx": "Woj. łódzkie", "HPGxxxxx": "Woj. małopolskie",
           "HPHxxxxx": "Woj. mazowieckie", "HPJxxxxx": "Woj. opolskie", "HPKxxxxx": "Woj. podkarpackie", "HPLxxxxx": "Szkoła Policji",
           "HPMxxxxx": "Woj. podlaskie", "HPNxxxxx": "Woj. pomorskie", "HPPxxxxx": "Woj. śląskie", "HPSxxxxx": "Woj. świętokrzyskie", "HPTxxxxx": "Woj. warmińsko-mazurskie",
           "HPUxxxxx": "Woj. wielkopolskie", "HPWxxxxx": "Woj. zachodniopomorskie", "HPZxxxxx": "Komenda Stołeczna Policji"}
inne_sluzby = {"HAxxxxx": "Centralne Biuro Antykorupcyjne", "HBxxxxx": "Służba Ochrony Państwa", "HKxxxxx": "ABW lub AW", "HWxxxxx": "Straż Graniczna", "HMxxxxx": "SWW lub SKW"}

class MenuApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("B130N")
        self.resizable(False, False)
        self.configure(bg='lightblue')

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

        self.button6 = tk.Button(
            self, text="TRANSLITERACJA", command=self.open_transliteracja, width=15, height=5)
        self.button6.grid(row=0, column=1, padx=2, pady=2)

        self.button7 = tk.Button(self, text="KODY QR",
                                 command=self.open_kodyqr, width=15, height=5)
        self.button7.grid(row=2, column=0, padx=2, pady=2)

        self.button8 = tk.Button(
            self, text="POGODA IMGW", command=self.open_pogoda, width=15, height=5)
        self.button8.grid(row=1, column=1, padx=2, pady=2)

        self.button9 = tk.Button(
            self, text="TABLICE\n REJESTRACYJNE", command=self.open_tablice, width=15, height=5)
        self.button9.grid(row=2, column=2, padx=2, pady=2)
        
        self.button10 = tk.Button(
            self, text="ALKOMAT", command=self.open_alkomat, width=15, height=5)
        self.button10.grid(row=3, column=0, padx=2, pady=2)
        
        self.button11 = tk.Button(
            self, text="KONWERTER\n TEMPERATUR", command=self.open_temperatury, width=15, height=5)
        self.button11.grid(row=3, column=1, padx=2, pady=2)
        
        self.button12 = tk.Button(
            self, text="CZYTNIK RSS", command=self.open_czytnik, width=15, height=5)
        self.button12.grid(row=3, column=2, padx=2, pady=2)

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

    def open_alkomat(self):
        self.hide_menu()
        if self.current_app:
            self.current_app.destroy()
        app10 = Alkomat(self)
        app10.grid()
        self.current_app = app10
        
    def open_temperatury(self):
        self.hide_menu()
        if self.current_app:
            self.current_app.destroy()
        app11 = Temperatury(self)
        app11.grid()
        self.current_app = app11

    def open_czytnik(self):
        self.hide_menu()
        if self.current_app:
            self.current_app.destroy()
        app12 = Czytnik(self)
        app12.grid()
        self.current_app = app12

    def hide_menu(self):
        self.withdraw()

    def show_menu(self):
        self.deiconify()

class Alkomat(tk.Toplevel):
    def __init__(self, menu_app):
        super().__init__()
        self.menu_app = menu_app
        self.title("ALKOMAT")
        self.protocol("WM_DELETE_WINDOW", self.on_close_window)
        self.current_page = None
        self.resizable(False, False)
        self.strona_pierwsza()
        self.show_page(self.page1)

    def strona_pierwsza(self):
        self.page1 = tk.Frame(self)
        frame_input = ttk.Frame(self.page1, padding="10")
        frame_input.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        # Pole wejściowe dla masy ciała
        ttk.Label(frame_input, text="Masa ciała (kg):").grid(row=0, column=0, sticky="W")
        self.entry_weight = ttk.Entry(frame_input, width=20)
        self.entry_weight.grid(row=0, column=1, padx=5, pady=5)
        self.entry_weight.insert(0, "95")

        # Pole wejściowe dla ilości wypitego alkoholu (piwo)
        ttk.Label(frame_input, text="Piwo 5% (ml):").grid(row=1, column=0, sticky="W")
        self.entry_beer = ttk.Entry(frame_input, width=20)
        self.entry_beer.grid(row=1, column=1, padx=5, pady=5)
        self.entry_beer.insert(0, "0")

        # Pole wejściowe dla ilości wypitego alkoholu (wino)
        ttk.Label(frame_input, text="Wino 12% (ml):").grid(row=2, column=0, sticky="W")
        self.entry_wine = ttk.Entry(frame_input, width=20)
        self.entry_wine.grid(row=2, column=1, padx=5, pady=5)
        self.entry_wine.insert(0, "0")

        # Pole wejściowe dla ilości wypitego alkoholu (wódka)
        ttk.Label(frame_input, text="Wódka 40% (ml):").grid(row=3, column=0, sticky="W")
        self.entry_vodka = ttk.Entry(frame_input, width=20)
        self.entry_vodka.grid(row=3, column=1, padx=5, pady=5)
        self.entry_vodka.insert(0, "0")

        # Pole wyboru płci
        ttk.Label(frame_input, text="Płeć:").grid(row=4, column=0, sticky="W")
        self.gender_var = tk.StringVar()
        self.radio_male = ttk.Radiobutton(frame_input, text="M", variable=self.gender_var, value="male")
        self.radio_female = ttk.Radiobutton(frame_input, text="K", variable=self.gender_var, value="female")
        self.radio_male.grid(row=4, column=1, padx=5, pady=5, sticky="W")
        self.radio_female.grid(row=4, column=1, padx=5, pady=5, sticky="E")

        # Pole wejściowe dla daty i godziny startu spożywania alkoholu
        ttk.Label(frame_input, text="Start spożywania (HH:MM):").grid(row=5, column=0, sticky="W")
        self.entry_start_time = ttk.Entry(frame_input, width=20)
        self.entry_start_time.grid(row=5, column=1, padx=5, pady=5)
        self.entry_start_time.insert(0, datetime.now().strftime("%H:%M"))

        # Pole wejściowe dla daty i godziny końca spożywania alkoholu
        ttk.Label(frame_input, text="Koniec spożywania (HH:MM):").grid(row=6, column=0, sticky="W")
        self.entry_end_time = ttk.Entry(frame_input, width=20)
        self.entry_end_time.grid(row=6, column=1, padx=5, pady=5)
        self.entry_end_time.insert(0, datetime.now().strftime("%H:%M"))

        # Przycisk do obliczania promili
        button_calculate = ttk.Button(self.page1, text="OBLICZ", command=self.calculate_bac)
        button_calculate.grid(row=7, column=1, pady=10)
        
        self.back_button = ttk.Button(self.page1, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=7, column=0, pady=10)

    def calculate_bac(self):
        try:
            weight = float(self.entry_weight.get())
            beer_volume = float(self.entry_beer.get())
            wine_volume = float(self.entry_wine.get())
            vodka_volume = float(self.entry_vodka.get())
            gender = self.gender_var.get()
            start_time = datetime.strptime(self.entry_start_time.get(), "%H:%M")
            end_time = datetime.strptime(self.entry_end_time.get(), "%H:%M")

            beer = beer_volume * 0.05 * 0.8
            wine = wine_volume * 0.12 * 0.8
            vodka = vodka_volume * 0.40 * 0.8
            total_grams = beer + wine + vodka

            if gender == "male":
                k = 0.7
            else:
                k = 0.6

            sobering_process = []
            current_time = start_time
            alcohol_in_body = 0

            # Obliczenie ilości alkoholu w ciele co 15 minut
            duration_minutes = (end_time - start_time).total_seconds() / 60
            getting_grams = total_grams / (duration_minutes / 15)

            while current_time <= end_time or alcohol_in_body > 0:
                if total_grams > 0:
                    alcohol_in_body += getting_grams
                    total_grams -= getting_grams
                alcohol_in_body -= 2.25
                alcohol_in_body = max(alcohol_in_body, 0)
                bac = alcohol_in_body / (k * weight)
                sobering_process.append(f"{current_time:%H:%M}             {alcohol_in_body:.2f} g             {bac:.2f} ‰")
                current_time += timedelta(minutes=15)

            self.show_results(sobering_process)
            self.clear_entries()

        except ValueError:
            messagebox.showerror("Błąd", "Proszę wprowadzić prawidłowe wartości liczbowe.")
        except Exception as e:
            messagebox.showerror("Błąd", str(e))

    def show_results(self, results):
        result_window = tk.Toplevel(self.page1)
        result_window.title("Wynik Obliczeń")
        result_text = tk.Text(result_window, wrap="word", width=60, height=20)
        result_text.pack(padx=10, pady=10)
        result_text.insert(tk.END, "Godzina        Ilość alkoholu (g)   Promile (‰)\n")
        result_text.insert(tk.END, "----------------------------------------------\n")
        result_text.insert(tk.END, "\n".join(results))
        result_text.config(state=tk.DISABLED)

    def clear_entries(self):
        self.entry_weight.delete(0, tk.END)
        self.entry_beer.delete(0, tk.END)
        self.entry_wine.delete(0, tk.END)
        self.entry_vodka.delete(0, tk.END)
        self.entry_start_time.delete(0, tk.END)
        self.entry_end_time.delete(0, tk.END)
        self.entry_weight.insert(0, "95")
        self.entry_beer.insert(0, "0")
        self.entry_wine.insert(0, "0")
        self.entry_vodka.insert(0, "0")
        self.entry_start_time.insert(0, "10:00")
        self.entry_end_time.insert(0, "12:00")

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
        
class Temperatury(tk.Toplevel):  
    def __init__(self, menu_app):
        super().__init__()
        self.menu_app = menu_app
        self.title("KONWERTER TEMPERATUR")
        self.protocol("WM_DELETE_WINDOW", self.on_close_window)
        self.current_page = None
        self.resizable(False, False)
        self.strona_pierwsza()
        self.show_page(self.page1)
    
    def strona_pierwsza(self):
        self.page1 = tk.Frame(self)
        frame_input = ttk.Frame(self.page1, padding="10")
        frame_input.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        # Pole wejściowe dla temperatury w stopniach Celsjusza
        ttk.Label(frame_input, text="Celsius:").grid(row=0, column=0, sticky="W")
        self.entry_celsius = ttk.Entry(frame_input, width=20)
        self.entry_celsius.grid(row=0, column=1, padx=5, pady=5, columnspan=2)
        self.entry_celsius.bind("<FocusOut>", self.convert_from_celsius)

        # Pole wejściowe dla temperatury w stopniach Fahrenheita
        ttk.Label(frame_input, text="Fahrenheit:").grid(row=1, column=0, sticky="W")
        self.entry_fahrenheit = ttk.Entry(frame_input, width=20)
        self.entry_fahrenheit.grid(row=1, column=1, padx=5, pady=5, columnspan=2)
        self.entry_fahrenheit.bind("<FocusOut>", self.convert_from_fahrenheit)

        # Pole wejściowe dla temperatury w Kelvinach
        ttk.Label(frame_input, text="Kelvin:").grid(row=2, column=0, sticky="W")
        self.entry_kelvin = ttk.Entry(frame_input, width=20)
        self.entry_kelvin.grid(row=2, column=1, padx=5, pady=5, columnspan=2)
        self.entry_kelvin.bind("<FocusOut>", self.convert_from_kelvin)

        # Przycisk do konwersji
        button_convert = ttk.Button(self.page1, text="KONWERTUJ", command=lambda: [
            self.convert_from_celsius(),
            self.convert_from_fahrenheit(),
            self.convert_from_kelvin()
        ])
        button_convert.grid(row=3, column=0, pady=10)
        
        self.back_button = ttk.Button(
        self.page1, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=3, column=1, pady=10)
    
    def celsius_to_fahrenheit(self, c):
        return c * 9/5 + 32

    def celsius_to_kelvin(self, c):
        return c + 273.15

    def fahrenheit_to_celsius(self, f):
        return (f - 32) * 5/9

    def fahrenheit_to_kelvin(self, f):
        return (f - 32) * 5/9 + 273.15

    def kelvin_to_celsius(self, k):
        return k - 273.15

    def kelvin_to_fahrenheit(self, k):
        return (k - 273.15) * 9/5 + 32

    def convert_from_celsius(self, event=None):
        try:
            celsius = float(self.entry_celsius.get())
            self.entry_fahrenheit.delete(0, tk.END)
            self.entry_fahrenheit.insert(0, f"{self.celsius_to_fahrenheit(celsius):.2f}")
            self.entry_kelvin.delete(0, tk.END)
            self.entry_kelvin.insert(0, f"{self.celsius_to_kelvin(celsius):.2f}")
        except ValueError:
            if self.entry_celsius.get() != '':
                messagebox.showerror("Błąd", "Proszę wprowadzić prawidłową wartość liczbową.")

    def convert_from_fahrenheit(self, event=None):
        try:
            fahrenheit = float(self.entry_fahrenheit.get())
            self.entry_celsius.delete(0, tk.END)
            self.entry_celsius.insert(0, f"{self.fahrenheit_to_celsius(fahrenheit):.2f}")
            self.entry_kelvin.delete(0, tk.END)
            self.entry_kelvin.insert(0, f"{self.fahrenheit_to_kelvin(fahrenheit):.2f}")
        except ValueError:
            if self.entry_fahrenheit.get() != '':
                messagebox.showerror("Błąd", "Proszę wprowadzić prawidłową wartość liczbową.")

    def convert_from_kelvin(self, event=None):
        try:
            kelvin = float(self.entry_kelvin.get())
            self.entry_celsius.delete(0, tk.END)
            self.entry_celsius.insert(0, f"{self.kelvin_to_celsius(kelvin):.2f}")
            self.entry_fahrenheit.delete(0, tk.END)
            self.entry_fahrenheit.insert(0, f"{self.kelvin_to_fahrenheit(kelvin):.2f}")
        except ValueError:
            if self.entry_kelvin.get() != '':
                messagebox.showerror("Błąd", "Proszę wprowadzić prawidłową wartość liczbową.")
    
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

class Czytnik(tk.Toplevel):
    def __init__(self, menu_app):
        super().__init__()
        self.menu_app = menu_app
        self.title("CZYTNIK RSS")
        self.protocol("WM_DELETE_WINDOW", self.on_close_window)
        self.resizable(False, False)
        self.geometry("750x600")
        self.create_widgets()
        self.odswiez_rss()
    
    def create_widgets(self):
        # Tworzymy główny Frame
        self.page1 = tk.Frame(self)
        self.page1.pack(fill=tk.BOTH, expand=True)  # Wypełnia całą przestrzeń w rodzicu

        # Tworzymy Frame dla wiadomości
        frame_wiadomosci = tk.Frame(self.page1)
        frame_wiadomosci.pack(fill=tk.BOTH, expand=True)  # Wypełnia całą przestrzeń w rodzicu

        # Dodanie Scrollbar
        self.scrollbar = ttk.Scrollbar(frame_wiadomosci, orient="vertical")
        self.scrollbar.pack(side="right", fill="y")

        # Dodanie Canvas
        self.canvas = tk.Canvas(frame_wiadomosci, yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side="left", fill=tk.BOTH, expand=True)  # Rozciąga się na całą przestrzeń Frame
        self.scrollbar.config(command=self.canvas.yview)

        # Dodanie Frame do Canvas
        self.frame_wiadomosci_window = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame_wiadomosci_window, anchor="nw")

        # Bind do aktualizacji scrollregion
        self.frame_wiadomosci_window.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)
        self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

        # Dodanie Przycisku
        self.back_button = ttk.Button(
            self.page1, text="POWRÓT DO MENU", command=self.back_to_menu, compound="right")
        self.back_button.pack(pady=10, side=tk.BOTTOM)

    def on_canvas_configure(self, event):
        # Ustalamy szerokość frame_wiadomosci_window na szerokość Canvas
        canvas_width = event.width
        self.canvas.itemconfig(self.canvas.create_window((0, 0), window=self.frame_wiadomosci_window, anchor="nw"), width=canvas_width)

    def on_frame_configure(self, event):
        # Ustalamy scrollregion Canvas na zawartość frame_wiadomosci_window
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def odswiez_rss(self):
        rss_url = 'https://www.polsatnews.pl/rss/wszystkie.xml'
        try:
            feed = feedparser.parse(rss_url)
        except Exception as e:
            feed = None
            print(f"Błąd pobierania RSS: {e}")

        for widget in self.frame_wiadomosci_window.winfo_children():
            widget.destroy()

        if feed and feed.entries:
            for entry in feed.entries:
                tytul = entry.title
                opis = entry.summary

                label_tytul = tk.Label(self.frame_wiadomosci_window, text=tytul, font=("Arial", 12, "bold"))
                label_tytul.pack(anchor='w', padx=10, pady=5)

                label_opis = tk.Label(self.frame_wiadomosci_window, text=opis, wraplength=600, justify='left')
                label_opis.pack(anchor='w', padx=10, pady=5)

                separator = ttk.Separator(self.frame_wiadomosci_window, orient='horizontal')
                separator.pack(fill='x', pady=5)
        else:
            label_blad = tk.Label(self.frame_wiadomosci_window, text="Nie udało się pobrać danych RSS. Sprawdź URL i spróbuj ponownie.", fg="red")
            label_blad.pack(anchor='w', padx=10, pady=5)

        # Ustawiamy automatyczne odświeżanie co minutę (60000 ms)
        self.after(60000, self.odswiez_rss)

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

class Pogoda(tk.Toplevel):
    def __init__(self, menu_app):
        super().__init__()
        self.menu_app = menu_app
        self.title("POGODA IMGW")
        self.protocol("WM_DELETE_WINDOW", self.on_close_window)
        self.current_page = None
        self.resizable(False, False)
        self.geometry("270x230")
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

        self.page1 = ttk.Frame(self)
        self.top_frame = ttk.Frame(self.page1)
        self.top_frame.grid(row=0, column=0, sticky="nsew", padx=10,  pady=10)

        self.label_start = ttk.Label(
            self.top_frame, text="Warunki atmosferyczne\n dla wybranej stacji pomiarowej IMGW")
        self.label_start.grid(row=1, column=0, padx=5,
                              pady=5, sticky=N, columnspan=3)

        self.option_var = StringVar(self.top_frame)
        self.max_length = max(len(option) for option in self.opcje_miast)

        self.choice_frame = ttk.Frame(self.page1)
        self.choice_frame.grid(row=2, column=0, sticky=NS,
                               padx=10, pady=10, columnspan=3)

        scrollbar = ttk.Scrollbar(self.choice_frame)
        scrollbar.grid(row=0, column=1, sticky=NS)

        self.listbox = Listbox(
            self.choice_frame, selectmode=SINGLE, yscrollcommand=scrollbar.set)
        self.listbox.grid(row=0, column=0, sticky=NS)
        self.listbox.config(height=5)
        self.listbox.bind("<ButtonRelease-1>", self.on_listbox_click)

        for option in self.opcje_miast:
            self.listbox.insert(END, option)

        scrollbar.config(command=self.listbox.yview)

        self.button_frame = ttk.Frame(self.page1)
        self.button_frame.grid(row=3, column=0, sticky=NS,
                               padx=10, pady=10, columnspan=3)

        self.button = ttk.Button(
            self.button_frame, text='POKAŻ', command=self.pokaz_pogode)
        self.button.grid(row=0, column=0, sticky=NS, padx=5, pady=5)

        self.back_button = ttk.Button(
            self.button_frame, text="POWRÓT DO MENU", command=self.back_to_menu, compound="right")
        self.back_button.grid(row=0, column=1, sticky=NS, padx=5, pady=5)

    def on_listbox_click(self, event):
        selected_index = self.listbox.curselection()
        if selected_index:
            selected_option = self.opcje_miast[selected_index[0]]
            self.option_var.set(selected_option)

    def pokaz_pogode(self):
        if self.option_var.get() == '':
            info = "Nie wybrałeś stacji!"
            messagebox.showinfo("Wystąpił problem", info)
        else:
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
                        z godz. {godzina_pomiaru}:00 
                        ze stacji {stacja}
                        
                        - Temperatura powietrza {temperatura} ℃
                        - Wiatr o prędkości {predkosc_wiatru} m/s 
                          ({y} {x})
                        - Wilgotność powietrza: {wilgotnosc_wzgledna}%
                        - Suma opadów: {suma_opadu} mm
                        - Ciśnienie atmosferyczne: {cisnienie} hPa
                        """)
                messagebox.showinfo(f"Pomiar IMGW dla stacji {stacja}", info)
            else:
                info = (f"Wystąpił problem z połączeniem z Internetem!")
                messagebox.showinfo("Wystąpił problem", info)

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
        self.page1 = ttk.Frame(self)
        self.data_label = Label(
            self.page1, text="Wprowadź dane do wygenerowania kodu QR:")
        self.data_label.grid(row=0, column=0, columnspan=2)

        self.data_entry = ttk.Entry(self.page1, width=40)
        self.data_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.box_size_label = ttk.Label(
            self.page1, text="Wybierz rozmiar kwadratu (1-10):")
        self.box_size_label.grid(row=2, column=0, sticky=EW)

        self.box_size_var = StringVar()
        self.box_size_var.set("5")
        self.box_size_option_menu = ttk.OptionMenu(
            self.page1, self.box_size_var, *map(str, range(1, 11)))
        self.box_size_option_menu.grid(row=2, column=1)

        self.border_label = Label(
            self.page1, text="Wybierz grubość ramki (0-10):")
        self.border_label.grid(row=3, column=0, sticky=EW)

        self.border_var = StringVar()
        self.border_var.set("2")
        self.border_option_menu = ttk.OptionMenu(
            self.page1, self.border_var, *map(str, range(11)))
        self.border_option_menu.grid(row=3, column=1)

        self.generate_button = ttk.Button(
            self.page1, text="GENERUJ QR", command=self.generate_qr)
        self.generate_button.grid(row=4, column=0, sticky=EW, padx=5, pady=5)

        self.back_button = ttk.Button(
            self.page1, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=4, column=1, sticky=EW, padx=5, pady=5)

        self.result_label = ttk.Label(self.page1)
        self.result_label.grid(row=5, column=0, columnspan=2)

    def generate_unique_filename(self, folder, base_filename):
        unique_filename = base_filename
        counter = 1
        while os.path.exists(os.path.join(folder, unique_filename)):
            unique_filename = f"qr_code_{counter}.jpg"
            counter += 1
        return os.path.join(folder, unique_filename)

    def qr_generate(self, data, box_size, border):
        folder_path = filedialog.askdirectory()
        filename = "qr_code.jpg"
        save_path = os.path.join(folder_path, filename)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        if os.path.exists(save_path):
            save_path = self.generate_unique_filename(
                folder_path, "qr_code.jpg")

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

    def generate_qr(self):
        data = self.data_entry.get()
        box_size = int(self.box_size_var.get())
        border = int(self.border_var.get())

        if data:
            if box_size >= 1 and box_size <= 10:
                if border >= 0 and border <= 10:
                    self.qr_generate(data, box_size, border)
                else:
                    self.result_label.config(
                        text="Wprowadź poprawny border (od 0 do 10).")
            else:
                self.result_label.config(
                    text="Wprowadź poprawny box size (od 1 do 10).")
        else:
            self.result_label.config(
                text="Wprowadź dane do wygenerowania kodu QR.")

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
        self.page1 = ttk.Frame(self)

        self.label = ttk.Label(
            self.page1, text="Wprowadź numer tablicy rejestracyjnej")
        self.label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        self.entry = ttk.Entry(self.page1)
        self.entry.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        self.przyciski = ttk.Frame(self.page1)
        self.przyciski.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

        self.check_button = ttk.Button(
            self.przyciski, text="SPRAWDŹ", command=self.check_tablica)
        self.check_button.grid(row=0, column=0, padx=5, pady=5)

        self.back_to_menu_button = ttk.Button(
            self.przyciski, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_to_menu_button.grid(row=0, column=1, padx=5, pady=5)
        
        separator1 = ttk.Separator(self.page1)
        separator1.grid(row=3, column=0, columnspan=3, sticky='ew', padx=10, pady=10)       
         
        self.result_label = ttk.Label(self.page1, text="")
        self.result_label.grid(row=4, column=0, columnspan=3, padx=5, pady=5)
        
        separator2 = ttk.Separator(self.page1)
        separator2.grid(row=5, column=0, columnspan=3, sticky='ew', padx=10, pady=10)  
        
        self.dyplomaci_button = ttk.Button(
            self.page1, text="Tablice dyplomatyczne", command=self.dyplomaci, width=21)
        self.dyplomaci_button.grid(row=6, column=0, padx=5, pady=5)

        self.wojsko_button = ttk.Button(
            self.page1, text="Siły zbrojne RP", command=self.wojsko, width=21)
        self.wojsko_button.grid(row=6, column=1, padx=5, pady=5)
        
        self.skarbowka_button = ttk.Button(
            self.page1, text="Kontrola Skarbowa", command=self.kontrola_skarbowa, width=21)
        self.skarbowka_button.grid(row=6, column=2, padx=5, pady=5)

        self.celnicy_button = ttk.Button(
            self.page1, text="Służba Celna", command=self.sluzba_celna, width=21)
        self.celnicy_button.grid(row=7, column=0, padx=5, pady=5)

        self.policja_button = ttk.Button(
            self.page1, text="Policja", command=self.policja, width=21)
        self.policja_button.grid(row=7, column=1, padx=5, pady=5)
        
        self.sluzby_button = ttk.Button(
            self.page1, text="Inne Służby", command=self.inne_sluzby, width=21)
        self.sluzby_button.grid(row=7, column=2, padx=5, pady=5)

    def check_tablica(self):
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

            self.result_label.config(
                text=f"Tablica dyplomatyczna:\nKraj: {kraj}\n{stanowisko}")

        elif numer_tablicy.startswith("WX") or numer_tablicy.startswith("AX"):
            if numer_tablicy.endswith("YV") or numer_tablicy.endswith("YZ") or numer_tablicy[-2] == "Y":
                self.result_label.config(
                    text=f"Przynależność: Warszawa Wesoła")
            else:
                self.result_label.config(
                    text=f"Przynależność: Warszawa Żoliborz")
        elif numer_tablicy.startswith("WY") or numer_tablicy.startswith("AY"):
            if numer_tablicy[-1] == "Y":
                self.result_label.config(
                    text=f"Samochód służbowy warszawskiego urzędu miasta\n lub pojazd cudzoziemca zameldowanego w stolicy.")
                if numer_tablicy[-2:] == "YY":
                    self.result_label.config(text=f"Przynależność: Sulejówek")
            else:
                self.result_label.config(text=f"Przynależność: Warszawa Wola")

        elif numer_tablicy[:1].isalpha() and numer_tablicy[1].isdigit():
            znaki = numer_tablicy[:1]
            if znaki in tablice_wojewodztwa:
                self.result_label.config(
                    text=f"Województwo {tablice_wojewodztwa[znaki]},\n tablica indywidualna")
            else:
                self.result_label.config(
                    text="Brak informacji dla tego rodzaju tablicy rejestracyjnej.")

        elif numer_tablicy[:3].isalpha():
            znaki = numer_tablicy[:3]
            wojewodztwo = numer_tablicy[:1]
            if znaki in polskie_tablice_rejestracyjne:
                if wojewodztwo in tablice_wojewodztwa:
                    self.result_label.config(
                        text=f"Przynależność: {polskie_tablice_rejestracyjne[znaki]},\n województwo {tablice_wojewodztwa[wojewodztwo]}")
                else:
                    self.result_label.config(
                        text=f"Przynależność: {polskie_tablice_rejestracyjne[znaki]}")
            else:
                self.result_label.config(
                    text="Brak informacji dla tego rodzaju tablicy rejestracyjnej.")

        elif numer_tablicy.startswith("WW") or numer_tablicy.startswith("AW") and numer_tablicy[1].isdigit():
            rembertow = ["A", "C", "E", "X", "Y"]
            wilanow = ["F", "G", "H", "J", "W"]
            wlochy = ["K", "L", "M", "N", "V"]
            if numer_tablicy[-1] in rembertow:
                self.result_label.config(
                    text=f"Przynależność: Warszawa Rembertów")
            elif numer_tablicy[-1] in wilanow:
                self.result_label.config(
                    text=f"Przynależność: Warszawa Wilanów")
            elif numer_tablicy[-1] in wlochy:
                self.result_label.config(
                    text=f"Przynależność: Warszawa Włochy")

        elif numer_tablicy[:2].isalpha():
            znaki = numer_tablicy[:2]
            wojewodztwo = numer_tablicy[:1]
            if znaki in polskie_tablice_rejestracyjne:
                if wojewodztwo in tablice_wojewodztwa:
                    self.result_label.config(
                        text=f"Przynależność: {polskie_tablice_rejestracyjne[znaki]},\n województwo {tablice_wojewodztwa[wojewodztwo]}")
                else:
                    self.result_label.config(
                        text=f"Przynależność: {polskie_tablice_rejestracyjne[znaki]}")
            else:
                self.result_label.config(
                    text="Brak informacji dla tego rodzaju tablicy rejestracyjnej.")
        else:
            self.result_label.config(text="Nieznany format numeru tablicy.")

    def dyplomaci(self):
        self.window = Toplevel()
        self.window.title("TABLICE DYPLOMATYCZNE")
        self.window.resizable(True, True)

        self.frame = ttk.Frame(self.window, padding=5)
        self.frame.pack(fill="both", expand=True)

        self.table = ttk.Treeview(self.frame, columns=(
            "Kraj", "Numer"), show="headings")
        self.table.heading("Kraj", text="Kraj")
        self.table.heading("Numer", text="Numer")

        self.table.column("Kraj", width=180)
        self.table.column("Numer", width=50)

        for numer, kraj in tablice_dyplomatyczne_kraj.items():
            self.table.insert("", "end", values=(kraj, numer))

        self.scroll = ttk.Scrollbar(
            self.frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=self.scroll.set)
        self.scroll.pack(side="right", fill="y")
        self.table.pack(fill="both", expand=True)
        
    def wojsko(self):
        self.window = Toplevel()
        self.window.title("SIŁY ZBROJNE RP")
        self.window.resizable(True, True)

        self.frame = ttk.Frame(self.window, padding=5)
        self.frame.pack(fill="both", expand=True)

        self.table = ttk.Treeview(self.frame, columns=(
            "Przeznaczenie sprzętu", "Numer"), show="headings")
        self.table.heading("Przeznaczenie sprzętu", text="Przeznaczenie sprzętu")
        self.table.heading("Numer", text="Numer")

        self.table.column("Przeznaczenie sprzętu", width=180)
        self.table.column("Numer", width=80)

        for numer, kraj in wojsko.items():
            self.table.insert("", "end", values=(kraj, numer))

        self.scroll = ttk.Scrollbar(
            self.frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=self.scroll.set)
        self.scroll.pack(side="right", fill="y")
        self.table.pack(fill="both", expand=True)

    def kontrola_skarbowa(self):
        self.window = Toplevel()
        self.window.title("KONTROLA SKARBOWA")
        self.window.resizable(True, True)

        self.frame = ttk.Frame(self.window, padding=5)
        self.frame.pack(fill="both", expand=True)

        self.table = ttk.Treeview(self.frame, columns=(
            "Przynależność", "Numer"), show="headings")
        self.table.heading("Przynależność", text="Przynależność")
        self.table.heading("Numer", text="Numer")

        self.table.column("Przynależność", width=180)
        self.table.column("Numer", width=80)

        for numer, kraj in kontrola_skarbowa.items():
            self.table.insert("", "end", values=(kraj, numer))

        self.scroll = ttk.Scrollbar(
            self.frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=self.scroll.set)
        self.scroll.pack(side="right", fill="y")
        self.table.pack(fill="both", expand=True)

    def sluzba_celna(self):
        self.window = Toplevel()
        self.window.title("SŁUŻBA CELNA")
        self.window.resizable(True, True)

        self.frame = ttk.Frame(self.window, padding=5)
        self.frame.pack(fill="both", expand=True)

        self.table = ttk.Treeview(self.frame, columns=(
            "Przynależność", "Numer"), show="headings")
        self.table.heading("Przynależność", text="Przynależność")
        self.table.heading("Numer", text="Numer")

        self.table.column("Przynależność", width=180)
        self.table.column("Numer", width=80)

        for numer, kraj in sluzba_celna.items():
            self.table.insert("", "end", values=(kraj, numer))

        self.scroll = ttk.Scrollbar(
            self.frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=self.scroll.set)
        self.scroll.pack(side="right", fill="y")
        self.table.pack(fill="both", expand=True)

    def policja(self):
        self.window = Toplevel()
        self.window.title("POLICJA")
        self.window.resizable(True, True)

        self.frame = ttk.Frame(self.window, padding=5)
        self.frame.pack(fill="both", expand=True)

        self.table = ttk.Treeview(self.frame, columns=(
            "Przynależność", "Numer"), show="headings")
        self.table.heading("Przynależność", text="Przynależność")
        self.table.heading("Numer", text="Numer")

        self.table.column("Przynależność", width=180)
        self.table.column("Numer", width=80)

        for numer, kraj in policja.items():
            self.table.insert("", "end", values=(kraj, numer))

        self.scroll = ttk.Scrollbar(
            self.frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=self.scroll.set)
        self.scroll.pack(side="right", fill="y")
        self.table.pack(fill="both", expand=True)
        
    def inne_sluzby(self):
        self.window = Toplevel()
        self.window.title("INNE SŁUŻBY")
        self.window.resizable(True, True)

        self.frame = ttk.Frame(self.window, padding=5)
        self.frame.pack(fill="both", expand=True)

        self.table = ttk.Treeview(self.frame, columns=(
            "Przynależność", "Numer"), show="headings")
        self.table.heading("Przynależność", text="Przynależność")
        self.table.heading("Numer", text="Numer")

        self.table.column("Przynależność", width=180)
        self.table.column("Numer", width=80)

        for numer, kraj in inne_sluzby.items():
            self.table.insert("", "end", values=(kraj, numer))

        self.scroll = ttk.Scrollbar(
            self.frame, orient="vertical", command=self.table.yview)
        self.table.configure(yscroll=self.scroll.set)
        self.scroll.pack(side="right", fill="y")
        self.table.pack(fill="both", expand=True)

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
        self.strona_piata()

        self.show_page(self.page1)

    def strona_pierwsza(self):
        self.page1 = ttk.Frame(self)
        label_start = ttk.Label(
            self.page1, text="Wybierz datę i godzinę rozpoczęcia delegacji", anchor='center')
        label_start.grid(row=0, column=0, sticky="EW",
                         padx=5, pady=5, columnspan=8)

        label_godzina_startu = ttk.Label(self.page1, text="GODZINA")
        label_godzina_startu.grid(row=1, column=3, padx=5, pady=5, sticky=S)
        label_minuta_startu = ttk.Label(self.page1, text="MINUTA")
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

        button_container = ttk.Frame(self.page1)
        button_container.grid(row=4, column=0, padx=5, pady=5, columnspan=8)

        self.back_button = ttk.Button(
            button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=0, padx=5, pady=5)

        self.button_next_page2 = ttk.Button(
            button_container, text="DALEJ", command=self.next_page1)
        self.button_next_page2.grid(row=0, column=1, padx=5, pady=5)

    def strona_druga(self):
        self.page2 = ttk.Frame(self)
        label_start = ttk.Label(
            self.page2, text="Wybierz datę i godzinę zakończenia delegacji", anchor='center')
        label_start.grid(row=0, column=0, sticky="EW",
                         padx=5, pady=5, columnspan=8)

        self.cal_koniec = Calendar(self.page2, selectmode='day',
                                   date_pattern='dd/mm/yyyy', locale='pl_PL')
        self.date = self.cal_koniec.datetime.today()
        self.cal_koniec.grid(row=1, column=0, padx=5, pady=5,
                             sticky="N", rowspan=3, columnspan=3)

        self.label_godzina_konca = ttk.Label(self.page2, text="GODZINA")
        self.label_godzina_konca.grid(
            row=1, column=3, padx=5, pady=5, sticky=S)
        label_minuta_konca = ttk.Label(self.page2, text="MINUTA")
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

        button_container = ttk.Frame(self.page2)
        button_container.grid(row=4, column=0, padx=5, pady=5, columnspan=8)

        self.button_back_page2 = ttk.Button(
            button_container, text="WSTECZ", command=self.back_page2)
        self.button_back_page2.grid(row=0, column=0, padx=5, pady=5)

        self.back_button = ttk.Button(
            button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=1, padx=5, pady=5)

        self.button_next_page2 = ttk.Button(
            button_container, text="DALEJ", command=self.next_page2)
        self.button_next_page2.grid(
            row=0, column=2, columnspan=2, padx=5, pady=5)

    def strona_trzecia(self):
        self.page3 = ttk.Frame(self)
        self.label_posilki = ttk.Label(
            self.page3, text="Wskaż posiłki zapewnione podczas delegacji", anchor='center')
        self.label_posilki.grid(
            row=0, column=0, sticky="EW", padx=5, pady=5, columnspan=8)

        self.var1dk = tk.IntVar()
        self.check_sniadaniedk = ttk.Checkbutton(self.page3, text="ŚNIADANIE", onvalue=1,
                                                offvalue=0, command=self.checking_sniadaniedk, variable=self.var1dk)
        self.check_sniadaniedk.grid(
            row=1, column=0, padx=50, pady=5, sticky="W", columnspan=2)
        self.label_sniadanie = ttk.Label(self.page3, text="w ilości")
        self.label_sniadanie.grid(row=1, column=2, sticky="E", padx=5, pady=5)
        self.ilosc_sniadaniedk = ttk.Entry(self.page3, width=5, state=DISABLED)
        self.ilosc_sniadaniedk.grid(
            row=1, column=3, sticky="W", padx=5, pady=5)

        self.var2dk = IntVar()
        self.check_obiaddk = ttk.Checkbutton(self.page3, text="OBIAD", onvalue=1,
                                         offvalue=0, command=self.checking_obiaddk, variable=self.var2dk)
        self.check_obiaddk.grid(row=2, column=0, padx=50,
                                pady=5, sticky=W, columnspan=2)
        self.label_obiad = ttk.Label(self.page3, text="w ilości")
        self.label_obiad.grid(row=2, column=2, sticky=E, padx=5, pady=5)
        self.ilosc_obiaddk = ttk.Entry(self.page3, width=5, state=DISABLED)
        self.ilosc_obiaddk.grid(row=2, column=3, sticky=W, padx=5, pady=5)

        self.var3dk = IntVar()
        self.check_kolacjadk = ttk.Checkbutton(self.page3, text="KOLACJA", onvalue=1,
                                           offvalue=0, command=self.checking_kolacjadk, variable=self.var3dk)
        self.check_kolacjadk.grid(
            row=3, column=0, padx=50, pady=5, sticky=W, columnspan=2)
        self.label_kolacja = ttk.Label(self.page3, text="w ilości")
        self.label_kolacja.grid(row=3, column=2, sticky=E, padx=5, pady=5)
        self.ilosc_kolacjadk = ttk.Entry(self.page3, width=5, state=DISABLED)
        self.ilosc_kolacjadk.grid(row=3, column=3, sticky=W, padx=5, pady=5)
        
        self.button_container = ttk.Frame(self.page3)
        self.button_container.grid(
            row=4, column=0, padx=5, pady=5, columnspan=8)

        self.button_back_page2 = ttk.Button(
            self.button_container, text="WSTECZ", command=self.back_page3)
        self.button_back_page2.grid(row=0, column=0, sticky=E, padx=5, pady=5)

        self.back_button = ttk.Button(
            self.button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=1, padx=5, pady=5)

        self.button_next_page2 = ttk.Button(
            self.button_container, text="DALEJ", command=self.next_page3)
        self.button_next_page2.grid(row=0, column=2, sticky=W, padx=5, pady=5)

    def strona_czwarta(self):
        self.page4= ttk.Frame(self)

        self.label_dodatki = ttk.Label(
            self.page4, text="Wskaż przysługujące ci ryczałty", anchor='center')
        self.label_dodatki.grid(
            row=0, column=0, sticky=EW, padx=5, pady=5, columnspan=8)

        self.nocleg_var1 = tk.BooleanVar()
        self.auto_var2 = tk.BooleanVar()
        self.komunikacja_var3 = tk.BooleanVar()

        self.checkframe = ttk.Frame(self.page4)
        self.checkframe.grid(row=1, column=0, columnspan=8)

        self.check_nocleg = ttk.Checkbutton(
            self.checkframe, text="NOCLEG", variable=self.nocleg_var1, command=self.rycz_nocleg)
        self.check_auto = ttk.Checkbutton(
            self.checkframe, text="PRYWATNE AUTO", variable=self.auto_var2, command=self.rycz_auto)
        self.check_komunikacja = ttk.Checkbutton(
            self.checkframe, text="KOMUNIKACJA MIEJSCOWA", variable=self.komunikacja_var3, command=self.rycz_komunikacja)
        self.check_nocleg.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.check_auto.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.check_komunikacja.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        
        self.button_container = ttk.Frame(self.page4)
        self.button_container.grid(row=2, column=0, padx=5, pady=5, columnspan=8)

        self.button_back_page2 = ttk.Button(
            self.button_container, text="WSTECZ", command=self.back_page4)
        self.button_back_page2.grid(row=0, column=0, sticky=E, padx=5, pady=5)

        self.back_button = ttk.Button(
            self.button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=1, padx=5, pady=5)

        self.button_next_page2 = ttk.Button(
            self.button_container, text="DALEJ", command=self.next_page4)
        self.button_next_page2.grid(row=0, column=2, sticky=W, padx=5, pady=5)

    def strona_piata(self):
        self.page5 = ttk.Frame(self)

        button_container = ttk.Frame(self.page5)
        button_container.grid(row=1, column=0, padx=5, pady=5, columnspan=8)

        self.label_wynik = ttk.Label(self.page5)
        self.label_wynik.grid(row=0, column=0, padx=5,
                              pady=5, columnspan=8, sticky=W)

        self.button_back_page2 = ttk.Button(
            button_container, text="WSTECZ", command=self.back_page5)
        self.button_back_page2.grid(row=0, column=0, sticky=E, padx=5, pady=5)

        self.back_button = ttk.Button(
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
        if self.auto_var2.get() == 1:
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
                if option_var.get() != 0.0:
                    try:
                        self.kilometry = float(entry.get())
                        self.stawka = option_var.get()
                        self.ryczalt_auto = self.kilometry * self.stawka
                        self.top.destroy()
                    except ValueError:
                        messagebox.showerror(
                            "Wystąpił błąd", "Aby przejść dalej musisz wprowadzić kilometry.")
                else:
                    messagebox.showerror(
                        "Wystąpił błąd", "Aby przejść dalej musisz wybrać środek transportu.")

            submit_button = tk.Button(
                self.top, text="POTWIERDŹ", command=submit)
            submit_button.pack(padx=10, pady=10)
        else:
            pass

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
            liczba_sniadań = int(self.ilosc_sniadaniedk.get())
        except ValueError:
            sniadanie = 0
            liczba_sniadań = 0

        try:
            obiad = int(self.ilosc_obiaddk.get()) * 22.50
            liczba_obiadow = int(self.ilosc_obiaddk.get())
        except ValueError:
            obiad = 0
            liczba_obiadow = 0

        try:
            kolacja = int(self.ilosc_kolacjadk.get()) * 11.25
            liczba_kolacji = int(self.ilosc_kolacjadk.get())
        except ValueError:
            kolacja = 0
            liczba_kolacji = 0

        if self.nocleg_var1.get():
            self.ryczalt_nocleg
            ryc_noc_info = (
                f"Za ryczałt za nocleg należy doliczyć {round(self.ryczalt_nocleg,2)} PLN.")
        else:
            self.ryczalt_nocleg = 0
            ryc_noc_info = ("Ryczałt za nocleg nie przysługuje.")

        if self.auto_var2.get():
            self.ryczalt_auto
            ryc_auto_info = (
                f"Za ryczałt za pozdróż prywatnym środkiem transportu\n należy doliczyć {round(self.ryczalt_auto,2)} PLN.")
        else:
            self.ryczalt_auto = 0
            ryc_auto_info = ("Ryczałt za pozdróż prywatnym środkiem transportu nie przysługuje.")

        if self.komunikacja_var3.get():
            self.ryczalt_komunikacja
            ryc_kom_info = (
                f"Za ryczałt za dojazd środkami komunikacji miejscowej\n należy doliczyć {round(self.ryczalt_komunikacja,2)} PLN.")
        else:
            self.ryczalt_komunikacja = 0
            ryc_kom_info = ("Ryczałt za dojazd środkami komunikacji miejscowej nie przysługuje.")

        zarcie = sniadanie + obiad + kolacja
        dieta = nalezna_dieta_dzien + nalezna_dieta_godz
        dieta_bez_posilkow = dieta - zarcie

        if zarcie != 0:
            zarcie_info = (
                f"""Za zapewnione posiłki należy odjąć {round(zarcie,2)} PLN.
                - {liczba_sniadań} razy śniadanie = {round(sniadanie,2)} PLN
                - {liczba_obiadow} razy obiad = {round(obiad,2)} PLN
                - {liczba_kolacji} razy kolacja = {round(kolacja,2)} PLN
                Po odjęciu posiłków dieta wynosi {round(dieta_bez_posilkow,2)} PLN.""")
        else:
            zarcie_info = ("Nie zapewniono posiłków podczas delegacji.")

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

        dodatki = self.komunikacja_var3.get() + self.auto_var2.get() + \
            self.nocleg_var1.get()

        if dodatki != 0:
            result = (f"""
                Start delegacji: {data_startu}
                Koniec delegacji: {data_konca}\n
                Delegacja trwała {int(liczba_dni)} {wersja_dzien}, {int(liczba_godzin)} {wersja_godzin} i {int(liczba_minut)} {wersja_minut}.
                Przysługuje za to {round(dieta,2)} PLN.
                ({round(nalezna_dieta_dzien,2)} PLN za pełne dni + {round(nalezna_dieta_godz,2)} PLN reszta)\n
                {zarcie_info}\n
                {ryc_noc_info}
                {ryc_kom_info}
                {ryc_auto_info}\n
                Finalnie należy się {round(nalezna_dieta,2)} PLN.
                """)
        else:
            result = (f"""
                Start delegacji: {data_startu}
                Koniec delegacji: {data_konca}\n
                Delegacja trwała {int(liczba_dni)} {wersja_dzien}, {int(liczba_godzin)} {wersja_godzin} i {int(liczba_minut)} {wersja_minut} ({round(nalezna_dieta_dzien,2)} PLN + {round(nalezna_dieta_godz,2)} PLN).\n
                {zarcie_info}\n
                Finalnie należy się {round(nalezna_dieta,2)} PLN.
                """)

        self.label_wynik.config(text=result)

    def show_page(self, page):
        if self.current_page:
            self.current_page.grid_forget()
        page.grid(row=0, column=0, sticky="nsew")
        self.current_page = page

    def next_page1(self):
        try:
            godziny_startu = int(self.wybor_godziny_startu.get())
            minuty_startu = int(self.wybor_minuty_startu.get())

            if not (godziny_startu <= 23) or not (minuty_startu <= 59):
                messagebox.showerror(
                    "Błąd", "Wprowadzono nieprawidłową wartość godzin lub minut")
            else:
                self.show_page(self.page2)
        except ValueError:
            messagebox.showerror(
                "Błąd", "Wprowadzono nieprawidłowe wartości. Proszę wprowadzić liczby.")

    def back_page2(self):
        self.show_page(self.page1)

    def next_page2(self):
        try:
            godziny_konca = int(self.wybor_godziny_konca.get())
            minuty_konca = int(self.wybor_minuty_konca.get())

            if not (godziny_konca <= 23) or not (minuty_konca <= 59):
                messagebox.showerror(
                    "Błąd", "Wprowadzono nieprawidłową wartość godzin lub minut")
            else:
                self.show_page(self.page3)
        except ValueError:
            messagebox.showerror(
                "Błąd", "Wprowadzono nieprawidłowe wartości. Proszę wprowadzić liczby.")

    def next_page3(self):
        if (self.ilosc_sniadaniedk.get().isdigit() or self.ilosc_sniadaniedk.get() == "") and (self.ilosc_obiaddk.get().isdigit() or self.ilosc_obiaddk.get() == "") and (self.ilosc_kolacjadk.get().isdigit() or self.ilosc_kolacjadk.get() == ""):
            self.show_page(self.page4)
        else:
            messagebox.showerror(
                "Błąd", "Wprowadzono nieprawidłowe wartości. Proszę wprowadzić liczby.")

    def next_page4(self):
        self.licz_diete()
        self.show_page(self.page5)

    def back_page4(self):
        self.show_page(self.page3)

    def back_page5(self):
        self.show_page(self.page4)

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
        self.strona_piata()
        self.strona_szosta()

        self.show_page(self.page1)

    def on_close_window(self):
        self.back_to_menu()

    def back_to_menu(self):
        self.menu_app.show_menu()
        self.destroy()

    def strona_pierwsza(self):
        self.page1 = ttk.Frame(self)

        kraj_container = ttk.Frame(self.page1)
        kraj_container.grid(row=0, column=0, padx=5, pady=5, columnspan=5)

        label_wybierz_kraj = ttk.Label(
            kraj_container, text="Wskaż kraj docelowy delegacji: ", anchor='center')
        label_wybierz_kraj.grid(row=0, column=0, padx=5,
                                pady=5, sticky=E, columnspan=3)

        scrollbar = ttk.Scrollbar(kraj_container)
        scrollbar.grid(row=0, column=5, sticky=NS)

        self.wybor_kraju = Listbox(kraj_container, yscrollcommand=scrollbar.set,
                                   height=5, width=15, selectmode=SINGLE)
        for key in diet_zagranica:
            self.wybor_kraju.insert(END, str(key))

        self.wybor_kraju.grid(row=0, column=3, sticky=E, columnspan=2)
        scrollbar.config(command=self.wybor_kraju.yview)

        zlabel_start = ttk.Label(
            self.page1, text="Wybierz datę i godzinę opuszczenia Polski", anchor='center')
        zlabel_start.grid(row=1, column=0, sticky=EW,
                          padx=5, pady=5, columnspan=5)

        zlabel_godzina_startu = ttk.Label(self.page1, text="GODZINA")
        zlabel_godzina_startu.grid(row=2, column=3, padx=5, pady=5, sticky=S)
        zlabel_minuta_startu = ttk.Label(self.page1, text="MINUTA")
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

        button_container = ttk.Frame(self.page1)
        button_container.grid(row=5, column=0, padx=5, pady=5, columnspan=5)

        self.back_button = ttk.Button(
            button_container, text="STAWKI DIET ZAGRANICZNYCH", command=self.stawki_diet_zagra)
        self.back_button.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.back_button = ttk.Button(
            button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=1, column=0, sticky=E, padx=5, pady=5)

        self.button_next_page2 = ttk.Button(
            button_container, text="DALEJ", command=self.next_page1)
        self.button_next_page2.grid(row=1, column=1, sticky=W, padx=5, pady=5)

    def strona_druga(self):
        self.page2 = ttk.Frame(self)
        zlabel_start = ttk.Label(
            self.page2, text="Wybierz datę i godzinę powrotu do Polski", anchor='center')
        zlabel_start.grid(row=0, column=0, sticky=EW,
                          padx=5, pady=5, columnspan=8)

        self.zcal_koniec = Calendar(self.page2, selectmode='day',
                                    date_pattern='dd/mm/yyyy', locale='pl_PL')
        self.date = self.zcal_koniec.datetime.today()
        self.zcal_koniec.grid(row=1, column=0, padx=5, pady=5,
                              sticky=N, rowspan=3, columnspan=3)

        zlabel_godzina_konca = ttk.Label(self.page2, text="GODZINA")
        zlabel_godzina_konca.grid(row=1, column=3, padx=5, pady=5, sticky=S)
        zlabel_minuta_konca = ttk.Label(self.page2, text="MINUTA")
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

        button_container = ttk.Frame(self.page2)
        button_container.grid(row=4, column=0, padx=5, pady=5, columnspan=8)

        self.button_back_page2 = ttk.Button(
            button_container, text="WSTECZ", command=self.back_page2)
        self.button_back_page2.grid(row=0, column=0, padx=5, pady=5)

        self.back_button = ttk.Button(
            button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=1, padx=5, pady=5)

        self.button_next_page2 = ttk.Button(
            button_container, text="DALEJ", command=self.next_page2)
        self.button_next_page2.grid(
            row=0, column=2, columnspan=2, padx=5, pady=5)

    def strona_trzecia(self):
        self.page3 = ttk.Frame(self)
        self.zlabel_posilki = ttk.Label(
            self.page3, text="Wskaż posiłki zapewnione podczas delegacji zagranicznej", anchor='center')
        self.zlabel_posilki.grid(
            row=0, column=0, sticky=EW, padx=5, pady=5, columnspan=8)

        self.zvar1 = IntVar()
        self.zcheck_sniadanie = ttk.Checkbutton(self.page3, text="ŚNIADANIE", onvalue=1,
                                            offvalue=0, command=self.zchecking_sniadanie, variable=self.zvar1)
        self.zcheck_sniadanie.grid(row=1, column=0, padx=50,
                                   pady=5, sticky=W, columnspan=2)
        self.zlabel_sniadanie = ttk.Label(self.page3, text="w ilości")
        self.zlabel_sniadanie.grid(row=1, column=2, sticky=E, padx=5, pady=5)
        self.zilosc_sniadanie = ttk.Entry(self.page3, width=5, state=DISABLED)
        self.zilosc_sniadanie.grid(row=1, column=3, sticky=W, padx=5, pady=5)

        self.zvar2 = IntVar()
        self.zcheck_obiad = ttk.Checkbutton(self.page3, text="OBIAD", onvalue=1,
                                        offvalue=0, command=self.zchecking_obiad, variable=self.zvar2)
        self.zcheck_obiad.grid(row=2, column=0, padx=50,
                               pady=5, sticky=W, columnspan=2)
        self.zlabel_obiad = ttk.Label(self.page3, text="w ilości")
        self.zlabel_obiad.grid(row=2, column=2, sticky=E, padx=5, pady=5)
        self.zilosc_obiad = ttk.Entry(self.page3, width=5, state=DISABLED)
        self.zilosc_obiad.grid(row=2, column=3, sticky=W, padx=5, pady=5)

        self.zvar3 = IntVar()
        self.zcheck_kolacja = ttk.Checkbutton(self.page3, text="KOLACJA", onvalue=1,
                                          offvalue=0, command=self.zchecking_kolacja, variable=self.zvar3)
        self.zcheck_kolacja.grid(
            row=3, column=0, padx=50, pady=5, sticky=W, columnspan=2)
        self.zlabel_kolacja = ttk.Label(self.page3, text="w ilości")
        self.zlabel_kolacja.grid(row=3, column=2, sticky=E, padx=5, pady=5)
        self.zilosc_kolacja = ttk.Entry(self.page3, width=5, state=DISABLED)
        self.zilosc_kolacja.grid(row=3, column=3, sticky=W, padx=5, pady=5)

        self.button_container = ttk.Frame(self.page3)
        self.button_container.grid(
            row=8, column=0, padx=5, pady=5, columnspan=8)

        self.button_back_page2 = ttk.Button(
            self.button_container, text="WSTECZ", command=self.back_page3)
        self.button_back_page2.grid(row=0, column=0, sticky=E, padx=5, pady=5)

        self.back_button = ttk.Button(
            self.button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=1, padx=5, pady=5)

        self.button_next_page2 = ttk.Button(
            self.button_container, text="DALEJ", command=self.next_page3)
        self.button_next_page2.grid(row=0, column=2, sticky=W, padx=5, pady=5)

    def strona_czwarta(self):
        self.page4 = ttk.Frame(self)
        self.label_dodatki = ttk.Label(
            self.page4, text="Wskaż przysługujące ci ryczałty", anchor='center')
        self.label_dodatki.grid(
            row=0, column=0, sticky=EW, padx=5, pady=5, columnspan=8)

        self.nocleg_var1 = tk.BooleanVar()
        self.auto_var2 = tk.BooleanVar()
        self.komunikacja_var3 = tk.BooleanVar()
        self.dojazd_do_var4 = tk.BooleanVar()
        self.dojazd_z_var5 = tk.BooleanVar()

        self.checkframe = ttk.Frame(self.page4)
        self.checkframe.grid(row=1, column=0, columnspan=8)

        self.check_nocleg = ttk.Checkbutton(
            self.checkframe, text="NOCLEG", variable=self.nocleg_var1, command=self.rycz_nocleg)
        self.check_auto = ttk.Checkbutton(
            self.checkframe, text="PRYWATNE AUTO", variable=self.auto_var2, command=self.rycz_auto)
        self.check_komunikacja = ttk.Checkbutton(
            self.checkframe, text="KOMUNIKACJA MIEJSCOWA", variable=self.komunikacja_var3, command=self.rycz_komunikacja)
        self.check_dojazd_do = ttk.Checkbutton(
            self.checkframe, text="DOJAZD DO LOTNISKA", variable=self.dojazd_do_var4, command=self.rycz_dojazd_do)
        self.check_dojazd_z = ttk.Checkbutton(
            self.checkframe, text="DOJAZD Z LOTNISKA", variable=self.dojazd_z_var5, command=self.rycz_dojazd_z)
        self.check_nocleg.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.check_auto.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        self.check_komunikacja.grid(row=2, column=0, padx=5, pady=5, sticky=W)
        self.check_dojazd_do.grid(row=3, column=0, padx=5, pady=5, sticky=W)
        self.check_dojazd_z.grid(row=4, column=0, padx=5, pady=5, sticky=W)
        
        self.button_container = ttk.Frame(self.page4)
        self.button_container.grid(row=2, column=0, padx=5, pady=5, columnspan=8)
        
        self.button_back_page2 = ttk.Button(
            self.button_container, text="WSTECZ", command=self.back_page4)
        self.button_back_page2.grid(row=0, column=0, sticky=E, padx=5, pady=5)

        self.back_button = ttk.Button(
            self.button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=1, padx=5, pady=5)

        self.button_next_page2 = ttk.Button(
            self.button_container, text="DALEJ", command=self.next_page4)
        self.button_next_page2.grid(row=0, column=2, sticky=W, padx=5, pady=5)
        
    def strona_piata(self):
        self.page5 = ttk.Frame(self)

        self.label_naleznosc = ttk.Label(
            self.page5, text="Wskaż wysokość przysługującej Ci należności", anchor='center')
        self.label_naleznosc.grid(row=0, column=0, sticky=EW, padx=5, pady=5, columnspan=3)
        
        self.wybor_naleznosc = tk.StringVar()
        self.wybor_naleznosc.set("0")

        option1 = ttk.Radiobutton(self.page5, text="0%", variable=self.wybor_naleznosc, value="0")
        option1.grid(row=1, column=1, padx=5, pady=5, sticky=EW)

        option2 = ttk.Radiobutton(self.page5, text="25%", variable=self.wybor_naleznosc, value="0.25")
        option2.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")

        option3 = ttk.Radiobutton(self.page5, text="50%", variable=self.wybor_naleznosc, value="0.5")
        option3.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

        option4 = ttk.Radiobutton(self.page5, text="75%", variable=self.wybor_naleznosc, value="0.75")
        option4.grid(row=4, column=1, padx=5, pady=5, sticky="nsew")
        
        option5 = ttk.Radiobutton(self.page5, text="100%", variable=self.wybor_naleznosc, value="1")
        option5.grid(row=5, column=1, padx=5, pady=5, sticky="nsew")
        
        self.button_container = ttk.Frame(self.page5)
        self.button_container.grid(row=6, column=0, padx=5, pady=5, columnspan=3)
        
        self.button_back_page2 = ttk.Button(
            self.button_container, text="WSTECZ", command=self.back_page5)
        self.button_back_page2.grid(row=0, column=0, sticky=E, padx=5, pady=5)

        self.back_button = ttk.Button(
            self.button_container, text="POWRÓT DO MENU", command=self.back_to_menu)
        self.back_button.grid(row=0, column=1, padx=5, pady=5)

        self.button_next_page2 = ttk.Button(
            self.button_container, text="DALEJ", command=self.next_page5)
        self.button_next_page2.grid(row=0, column=2, sticky=W, padx=5, pady=5)

    def strona_szosta(self):
        self.page6 = ttk.Frame(self)

        self.zlabel_wynik = ttk.Label(self.page6)
        self.zlabel_wynik.grid(row=0, column=0, padx=5, pady=5, columnspan=8)

        button_container = ttk.Frame(self.page6)
        button_container.grid(row=1, column=0, padx=5, pady=5, columnspan=8)

        self.button_back_page2 = ttk.Button(
            button_container, text="WSTECZ", command=self.back_page6)
        self.button_back_page2.grid(row=0, column=0, sticky=E, padx=5, pady=5)

        self.back_button = ttk.Button(
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
        if self.auto_var2.get() == 1:
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
                if option_var.get() != 0.0:
                    try:
                        self.kilometry = float(entry.get())
                        self.stawka = option_var.get()
                        self.ryczalt_auto = self.kilometry * self.stawka
                        self.top.destroy()
                    except ValueError:
                        messagebox.showerror(
                            "Wystąpił błąd", "Aby przejść dalej musisz wprowadzić kilometry.")
                else:
                    messagebox.showerror(
                        "Wystąpił błąd", "Aby przejść dalej musisz wybrać środek transportu.")

            submit_button = tk.Button(
                self.top, text="POTWIERDŹ", command=submit)
            submit_button.pack(padx=10, pady=10)
        else:
            pass

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
            wysokosc_stawki = "0"
        if 0 < liczba_godzin < 8:
            nalezna_dieta_godz = dieta/3
            wysokosc_stawki = "1/3"
        if 8 <= liczba_godzin < 12:
            nalezna_dieta_godz = dieta * 0.5
            wysokosc_stawki = "1/2"
        if liczba_godzin >= 12:
            nalezna_dieta_godz = dieta
            wysokosc_stawki = "0"

        try:
            sniadanie = int(self.zilosc_sniadanie.get()) * (dieta * 0.15)
            liczba_sniadan = int(self.zilosc_sniadanie.get())
        except ValueError:
            sniadanie = 0
            liczba_sniadan = 0

        try:
            obiad = int(self.zilosc_obiad.get()) * (dieta * 0.3)
            liczba_obiadow = int(self.zilosc_obiad.get())
        except ValueError:
            obiad = 0
            liczba_obiadow = 0

        try:
            kolacja = int(self.zilosc_kolacja.get()) * (dieta * 0.3)
            liczba_kolacji = int(self.zilosc_kolacja.get())
        except ValueError:
            kolacja = 0
            liczba_kolacji = 0

        if self.nocleg_var1.get():
            self.ryczalt_nocleg
            ryc_noc_info = (
                f"Za ryczałt za nocleg należy doliczyć {round(self.ryczalt_nocleg,2)} {omega}.")
        else:
            self.ryczalt_nocleg = 0
            ryc_noc_info = ("Ryczałt za nocleg nie przysługuje.")

        if self.auto_var2.get():
            self.ryczalt_auto
            ryc_auto_info = (
                f"Za ryczałt za pozdróż prywatnym środkiem transportu\n należy doliczyć {round(self.ryczalt_auto,2)} {omega}.")
        else:
            self.ryczalt_auto = 0
            ryc_auto_info = ("Ryczałt za pozdróż prywatnym środkiem transportu nie przysługuje.")

        if self.komunikacja_var3.get():
            self.ryczalt_komunikacja
            ryc_kom_info = (
                f"Za ryczałt za dojazd środkami komunikacji miejscowej\n należy doliczyć {round(self.ryczalt_komunikacja,2)} {omega}.")
        else:
            self.ryczalt_komunikacja = 0
            ryc_kom_info = ("Ryczałt za dojazd środkami komunikacji miejscowej nie przysługuje.")

        if self.dojazd_do_var4.get():
            self.ryczalt_dojazd_do
            ryc_dojazd_do = (
                f"Za ryczałt za dojazd do lotniska należy doliczyć {round(self.ryczalt_dojazd_do,2)} {omega}.")
        else:
            self.ryczalt_dojazd_do = 0
            ryc_dojazd_do = ("Ryczałt za dojazd do lotniska nie przysługuje.")

        if self.dojazd_z_var5.get():
            self.ryczalt_dojazd_z
            ryc_dojazd_z = (
                f"Za ryczałt za dojazd z lotniska należy doliczyć {round(self.ryczalt_dojazd_z,2)} {omega}.")
        else:
            self.ryczalt_dojazd_z = 0
            ryc_dojazd_z = ("Ryczałt za dojazd z lotniska nie przysługuje.")

        zarcie = sniadanie + obiad + kolacja
        diet = nalezna_dieta_dzien + nalezna_dieta_godz
        dieta_bez_posilkow = diet - zarcie
        
        if zarcie != 0:
            zarcie_info = (
                f"""Za zapewnione posiłki należy odjąć {round(zarcie,2)} {omega}.
                - {liczba_sniadan} razy śniadanie = {round(sniadanie,2)} {omega}
                - {liczba_obiadow} razy obiad = {round(obiad,2)} {omega}
                - {liczba_kolacji} razy kolacja = {round(kolacja,2)} {omega}
                Po odjęciu posiłków dieta wynosi {round(dieta_bez_posilkow,2)} {omega}.""")
        else:
            zarcie_info = ("Nie zapewniono posiłków podczas delegacji.")

        nalezna_dieta = nalezna_dieta_dzien + \
            nalezna_dieta_godz - sniadanie - obiad - kolacja + \
            self.ryczalt_nocleg + self.ryczalt_komunikacja + \
            self.ryczalt_auto + self.ryczalt_dojazd_z + self.ryczalt_dojazd_do

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

        dodatki = self.dojazd_z_var5.get() + self.dojazd_do_var4.get() + \
            self.komunikacja_var3.get() + self.auto_var2.get() + self.nocleg_var1.get()

        naleznosc = (nalezna_dieta_dzien + nalezna_dieta_godz)*(float(self.wybor_naleznosc.get()))

        if dodatki != 0:
            result = (f"""
                Start delegacji: {data_startu}
                Koniec delegacji: {data_konca}\n
                Delegacja {gamma} trwała {int(liczba_dni)} {wersja_dzien}, {int(liczba_godzin)} {wersja_godzin} i {int(liczba_minut)} {wersja_minut}
                Przysługuje za to {round(diet,2)} {omega}.
                ({round(nalezna_dieta_dzien,2)} {omega} za pełne dni + {round(nalezna_dieta_godz,2)} {omega} reszta)\n
                {zarcie_info}\n
                {ryc_noc_info}
                {ryc_kom_info}
                {ryc_auto_info}
                {ryc_dojazd_do}
                {ryc_dojazd_z}\n
                Finalnie należy się {round(nalezna_dieta,2)} {omega}.\n
                ***N A L E Ż N O Ś Ć***\n
                Przysługuje Ci {round(naleznosc,2)} {omega} należności.
                - diety w pełnej wysokości stawki [{liczba_dni} x {dieta} {omega} = {round(nalezna_dieta_dzien,2)} {omega}]
                - diety w wysokości {wysokosc_stawki} stawki [{wysokosc_stawki} x {dieta} {omega} = {round(nalezna_dieta_godz,2)} {omega}]
                - razem [{round(diet,2)} x {(self.wybor_naleznosc.get())} = {round(naleznosc,2)} {omega}]
                """)
        else:
            result = (f"""
                Start delegacji: {data_startu}
                Koniec delegacji: {data_konca}\n
                Delegacja {gamma} trwała {int(liczba_dni)} {wersja_dzien}, {int(liczba_godzin)} {wersja_godzin} i {int(liczba_minut)} {wersja_minut}
                Przysługuje za to {round(diet,2)} {omega}.
                ({round(nalezna_dieta_dzien,2)} {omega} za pełne dni + {round(nalezna_dieta_godz,2)} {omega} reszta)\n
                {zarcie_info}\n
                Finalnie należy się {round(nalezna_dieta,2)} {omega}.\n
                ***N A L E Ż N O Ś Ć***\n
                Przysługuje Ci {round(naleznosc,2)} {omega} należności.
                - diety w pełnej wysokości stawki [{liczba_dni} x {dieta} {omega} = {round(nalezna_dieta_dzien,2)} {omega}]
                - diety w wysokości {wysokosc_stawki} stawki [{wysokosc_stawki} x {dieta} {omega} = {round(nalezna_dieta_godz,2)} {omega}]
                - razem [{round(diet,2)} x {(self.wybor_naleznosc.get())} = {round(naleznosc,2)} {omega}]
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
        try:
            godziny_startu = int(self.zwybor_godziny_startu.get())
            minuty_startu = int(self.zwybor_minuty_startu.get())

            if not (godziny_startu <= 23) or not (minuty_startu <= 59):
                messagebox.showerror(
                    "Błąd", "Wprowadzono nieprawidłową wartość godzin lub minut")
            else:
                self.show_page(self.page2)
        except ValueError:
            messagebox.showerror(
                "Błąd", "Wprowadzono nieprawidłowe wartości. Proszę wprowadzić liczby.")

    def back_page2(self):
        self.show_page(self.page1)

    def next_page2(self):
        try:
            godziny_konca = int(self.zwybor_godziny_konca.get())
            minuty_konca = int(self.zwybor_minuty_konca.get())

            if not (godziny_konca <= 23) or not (minuty_konca <= 59):
                messagebox.showerror(
                    "Błąd", "Wprowadzono nieprawidłową wartość godzin lub minut")
            else:
                self.show_page(self.page3)
        except ValueError:
            messagebox.showerror(
                "Błąd", "Wprowadzono nieprawidłowe wartości. Proszę wprowadzić liczby.")

    def next_page3(self):
        if (self.zilosc_sniadanie.get().isdigit() or self.zilosc_sniadanie.get() == "") and (self.zilosc_obiad.get().isdigit() or self.zilosc_obiad.get() == "") and (self.zilosc_kolacja.get().isdigit() or self.zilosc_kolacja.get() == ""):
            self.show_page(self.page4)
        else:
            messagebox.showerror(
                "Błąd", "Wprowadzono nieprawidłowe wartości. Proszę wprowadzić liczby.")

    def next_page4(self):
        self.show_page(self.page5)

    def back_page4(self):
        self.show_page(self.page3)
        
    def next_page5(self):
        self.licz_diete_zagra()
        self.show_page(self.page6)

    def back_page5(self):
        self.show_page(self.page4)
    
    def back_page6(self):
        self.show_page(self.page5)

    def back_page3(self):
        self.show_page(self.page2)

    def on_close_window(self):
        self.back_to_menu()

    def back_to_menu(self):
        self.menu_app.show_menu()
        self.destroy()


class PESEL(tk.Toplevel):
    data = ''
    women_names = ["ANNA", "KATARZYNA", "MARIA", "MAŁGORZATA", "AGNIESZKA", "BARBARA", "EWA", "MAGDALENA", "JOANNA",
                   "ALEKSANDRA", "MONIKA", "ZOFIA", "NATALIA", "JULIA", "KAROLINA", "MARTA", "BEATA", "DOROTA", "ALICJA", 
                   "JOLANTA", "IWONA", "PAULINA", "ZUZANNA", "JUSTYNA", "HANNA", "WIKTORIA",
                   "RENATA", "URSZULA", "AGATA", "SYLWIA", "PATRYCJA", "IZABELA", "EMILIA", "OLIWIA", "ANETA", "WERONIKA",
                   "EWELINA", "MARTYNA", "KLAUDIA", "GABRIELA", "MARZENA", "LENA", "DOMINIKA", "MARIANNA", "AMELIA", "KINGA",
                   "EDYTA", "KAMILA", "ALINA", "WANDA", "DARIA", "MARIOLA", "MILENA", "WIOLETTA",
                   "LAURA", "OLGA", "KAZIMIERA", "ILONA", "MICHALINA", "SANDRA", "GENOWEFA",
                   "MARLENA", "SABINA", "NINA", "ANITA", "IGA", "POLA", "MARCELINA", "ANIELA", "KARINA", "ADRIANNA", "DIANA", "ROKSANA",
                   "DAGMARA", "MALWINA", "ELIZA", "KLARA", "RÓŻA", "KAJA", "LEOKADIA", "BLANKA", "ANASTAZJA", "BRONISŁAWA",
                   "JULITA", "DANIELA", "MAGDA", "MATYLDA", "ADRIANA", "LUIZA", "JUDYTA"]
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
    men_names = ["PIOTR", "KRZYSZTOF", "TOMASZ", "PAWEŁ", "MICHAŁ", "JAN", "MARCIN", "JAKUB", "ADAM", "ŁUKASZ", "MAREK", "GRZEGORZ",
                 "MATEUSZ", "WOJCIECH", "MARIUSZ", "DARIUSZ", "MACIEJ", "RAFAŁ", "ROBERT", "KAMIL", "DAWID",
                 "SZYMON", "JACEK", "KACPER", "JÓZEF", "RYSZARD", "BARTOSZ", "ARTUR", "JAROSŁAW", "SEBASTIAN",
                 "DAMIAN", "PATRYK", "ROMAN", "DANIEL", "FILIP", "PRZEMYSŁAW", "KAROL", "ALEKSANDER", "ADRIAN",
                 "ARKADIUSZ", "DOMINIK", "MIKOŁAJ", "BARTŁOMIEJ", "WIKTOR", "KRYSTIAN",
                 "RADOSŁAW", "KONRAD", "IGOR", "HUBERT", "EDWARD", "OSKAR", "MARCEL", "MAKSYMILIAN", "MIŁOSZ", "BOGUSŁAW", "IRENEUSZ", "NIKODEM", "STEFAN", "LEON", "OLIWIER", "SYLWESTER",
                 "CEZARY", "ZENON", "GABRIEL", "IGNACY", "JULIAN", "NORBERT", "TYMON", "BŁAŻEJ", "ERYK", "EMIL", "KSAWERY", "BORYS", "OLAF", "KAJETAN", "KUBA","ALBERT"]
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
    cities = ["WARSZAWA", "KRAKÓW", "SZCZECIN", "ŁÓDŹ", "WROCŁAW", "ZIELONA GÓRA", "GDAŃSK", "GDYNIA", "POZNAŃ",
              "KATOWICE", "BIAŁYSTOK", "KIELCE", "BYDGOSZCZ", "TORUŃ", "CZĘSTOCHOWA", "LUBLIN", "RZESZÓW",
              "RADOM", "GORZÓW WIELKOPOLSKI", "KOSZALIN", "ELBLĄG", "OLSZTYN", "ŁOMŻA", "SIEDLCE", "KALISZ",
              "PIOTRKÓW TRYBUNALSKI", "NOWY SĄCZ", "OPOLE", "LUBIN", "LEGNICA", "PIŁA", "PŁOCK", "GOLENIÓW", "HRUBIESZÓW",
              "LIPSKO", "MALBORK", "KARTUZY", "SKARŻYSKO-KAMIENNA", "ZAWIERCIE", "BOLESŁAWIEC", "MIĘDZYCHÓD", "OSTRZESZÓW",
              "BRZEZINY", "RADZIEJÓW", "JAROSŁAW", "PRZEMYŚL", "PUŁAWY", "CHRZANÓW", "STARACHOWICE", "ŚWIĘTOCHŁOWICE"]
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
        self.resizable(False, False)
        self.geometry("330x350")
        self.strona_pierwsza()

        self.show_page(self.page1)

    def strona_pierwsza(self):
        self.page1 = ttk.Frame(self)

        self.tabGeneral = ttk.Notebook(self.page1)
        self.tabGeneral.grid()

        # Zakładka numer 1 GENEROWANIE PESEL

        self.tab1_gen = ttk.Frame(self.tabGeneral)
        self.tabGeneral.add(self.tab1_gen, text='Wygeneruj PESEL')

        L1 = ttk.Label(self.tab1_gen, text="Wskaż datę urodzenia", anchor='center')
        L1.grid(row=0, column=0, padx=5, pady=5, columnspan=3)

        self.kalendarz = Calendar(
            self.tab1_gen, selectmode='day', date_pattern='dd/mm/yyyy', locale='pl_PL')
        date = self.kalendarz.datetime.today()
        self.kalendarz.grid(row=1, column=0, columnspan=3)

        self.plec_frame = ttk.Frame(self.tab1_gen)
        self.plec_frame.grid(row=2, column=0, padx=5, pady=5, columnspan=3)

        L2 = ttk.Label(self.plec_frame, text="Wybierz płeć:")
        L2.grid(row=0, column=0, padx=5, pady=5)

        self.man = IntVar()
        self.check_man = ttk.Checkbutton(self.plec_frame,
                                     text="MĘŻCZYZNA",
                                     variable=self.man,
                                     command=self.checkbutton_man_selected)
        self.check_man.grid(row=0, column=1, padx=5, pady=5)

        self.woman = IntVar()
        self.check_woman = ttk.Checkbutton(self.plec_frame,
                                       text="KOBIETA",
                                       variable=self.woman,
                                       command=self.checkbutton_woman_selected)
        self.check_woman.grid(row=0, column=2, padx=5, pady=5)

        self.przyciski_frame = ttk.Frame(self.tab1_gen)
        self.przyciski_frame.grid(
            row=3, column=0, padx=5, pady=5, columnspan=3)

        self.back_button0 = ttk.Button(self.przyciski_frame,
                                   text="POWRÓT DO MENU",
                                   command=self.back_to_menu,
                                   state=ACTIVE,
                                   compound=LEFT)
        self.back_button0.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.gen_button = ttk.Button(self.przyciski_frame,
                                 text="GENERUJ",
                                 command=self.generate_pesel,
                                 state=ACTIVE)
        self.gen_button.grid(row=0, column=1, sticky=E, padx=5, pady=5)

        self.copy_button0 = ttk.Button(self.przyciski_frame,
                                   text="KOPIUJ",
                                   command=self.copy_result,
                                   state=DISABLED)
        self.copy_button0.grid(row=0, column=2, sticky=W, padx=5, pady=5)

        self.L4 = ttk.Label(self.tab1_gen)
        self.L4.grid(row=4, column=0, padx=5, pady=5, columnspan=3)

        self.L4a = ttk.Label(self.tab1_gen)
        self.L4a.grid(row=5, column=0, padx=5, pady=5, columnspan=3)

        # Zakładka numer 2 SPRAWDZANIE PESEL

        self.tab2_check = ttk.Frame(self.tabGeneral)
        self.tabGeneral.add(self.tab2_check, text='Sprawdź PESEL')

        self.Lab1 = ttk.Label(self.tab2_check, text="Wprowadź PESEL", anchor='center')
        self.Lab1.grid(row=0, column=0, padx=100, pady=5, sticky=N)

        self.Enter1 = ttk.Entry(self.tab2_check, width=15)
        self.Enter1.grid(row=1, column=0, padx=100, pady=5)

        self.przycisk_frame = ttk.Frame(self.tab2_check)
        self.przycisk_frame.grid(row=2, column=0, padx=5, pady=5)

        self.back_button1 = ttk.Button(self.przycisk_frame,
                                   text="POWRÓT DO MENU",
                                   command=self.back_to_menu,
                                   state=ACTIVE,
                                   compound=LEFT)
        self.back_button1.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.check_button = ttk.Button(self.przycisk_frame,
                                   text="SPRAWDŹ",
                                   command=self.check_pesel,
                                   state=ACTIVE)
        self.check_button.grid(row=0, column=1, padx=5, pady=5)

        self.Lab4 = ttk.Label(self.tab2_check)
        self.Lab4.grid(row=3, column=0, padx=5, pady=5)

        # Zakładka numer 3 TWORZENIE TOZSAMOSCI

        self.tab3_check = ttk.Frame(self.tabGeneral)
        self.tabGeneral.add(self.tab3_check, text='Stwórz tożsamość')

        self.Ldsd2 = ttk.Label(self.tab3_check, text="Wybierz płeć:")
        self.Ldsd2.grid(row=0, column=0, padx=5, pady=5)

        self.man_opt = IntVar()
        self.option_man = ttk.Checkbutton(self.tab3_check,
                                      text="Mężczyzna",
                                      variable=self.man_opt,
                                      command=self.checkbutton_man_opt_selected)
        self.option_man.grid(row=0, column=1, padx=5, pady=5)

        self.woman_opt = IntVar()
        self.option_woman = ttk.Checkbutton(self.tab3_check,
                                        text="Kobieta",
                                        variable=self.woman_opt,
                                        command=self.checkbutton_woman_opt_selected)
        self.option_woman.grid(row=0, column=2, padx=5, pady=5)

        self.L7 = ttk.Label(self.tab3_check, text="Podaj wiek w latach:")
        self.L7.grid(row=1, column=0, padx=5, pady=5)

        self.EE = ttk.Entry(self.tab3_check, width=15)
        self.EE.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky=W)

        self.przycis_frame = ttk.Frame(self.tab3_check)
        self.przycis_frame.grid(row=2, column=0, padx=5, pady=5, columnspan=3)

        self.back_button1 = ttk.Button(self.przycis_frame,
                                   text="POWRÓT DO MENU",
                                   command=self.back_to_menu,
                                   state=ACTIVE,
                                   compound=LEFT)
        self.back_button1.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        self.makenew_button = ttk.Button(self.przycis_frame,
                                     text="STWÓRZ",
                                     command=self.generate_identity,
                                     state=ACTIVE,
                                     compound=LEFT)
        self.makenew_button.grid(row=0, column=1, padx=5, pady=5, sticky=E)

        self.copy_button01 = ttk.Button(self.przycis_frame,
                                    text="KOPIUJ",
                                    command=self.copy_result2,
                                    state=DISABLED,
                                    compound=RIGHT)
        self.copy_button01.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        
        self.save_button = ttk.Button(self.przycis_frame,
                                    text="ZAPISZ",
                                    command=self.save_to_file,
                                    state=DISABLED,
                                    compound=RIGHT)
        self.save_button.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        self.wynik_frame = ttk.Frame(self.tab3_check)
        self.wynik_frame.grid(row=4, column=0, padx=5,
                              pady=5, columnspan=3, sticky=W)

        self.Lab6 = ttk.Label(self.wynik_frame)
        self.Lab6.grid(row=0, column=0, padx=5, pady=5, sticky=W)

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
        info = "Wygenerowany PESEL skopiowano do pamięci podręcznej."
        messagebox.showinfo("Sukces!", info)

    def copy_result2(self):
        self.page1.clipboard_clear()
        self.page1.clipboard_append(self.generated_identity)
        info = "Wygenerowany tekst skopiowano do pamięci podręcznej."
        messagebox.showinfo("Sukces!", info)

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
            control_sum = position_1 + (position_2 * 3) + (position_3 * 7) + (position_4 * 9) + position_5 + (
                position_6 * 3) + (position_7 * 7) + (position_8 * 9) + (position_10 * 3)
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
            control_sum = position_1 + (position_2 * 3) + (position_3 * 7) + (position_4 * 9) + position_5 + (
                position_6 * 3) + (position_7 * 7) + (position_8 * 9) + (position_10 * 3)
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

    def id_number(self):
        wartosci_liter = {
            "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "G": 16, "H": 17, "I": 18,
            "J": 19, "K": 20, "L": 21, "M": 22, "N": 23, "O": 24, "P": 25, "Q": 26, "R": 27,
            "S": 28, "T": 29, "U": 30, "V": 31, "W": 32, "X": 33, "Y": 34, "Z": 35
        }

        while True:
            seria = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=3))
            numer = "".join(random.choices("0123456789", k=6))
            self.numer_dowodu = seria + numer
            
            suma_seria = (int(wartosci_liter.get(seria[0]))*7) + (int(wartosci_liter.get(seria[1])*3)) + (int(wartosci_liter.get(seria[2])))
            suma_numer = (int(numer[0])*9)+(int(numer[1])*7)+(int(numer[2])*3)+(int(numer[3]))+(int(numer[4])*7)+(int(numer[5])*3)
            suma = int(suma_seria) + int(suma_numer)
               
            if suma % 10 == 0:
                return self.numer_dowodu
            
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
                control_sum = position_1 + (position_2 * 3) + (position_3 * 7) + (position_4 * 9) + position_5 + (
                    position_6 * 3) + (position_7 * 7) + (position_8 * 9) + (position_10 * 3)
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
                self.id_number()
                self.generated_identity = (
                    "Wygenerowana tożsamość:\n"
                    f"{self.name} {self.last_name}\n"
                    f"{self.date_of_birth} {random.choice(self.cities)}\n"
                    f"PESEL: {self.generated_pesel}\n"
                    f"Numer dowodu osobistego: {self.numer_dowodu}\n"
                    f"Znak zodiaku: {self.sign}\n"
                    f"Numer telefonu: {self.numer_telefonu}\n"
                    f"Adres mailowy: {self.adres_email}\n"
                )
                self.Lab6.config(text=self.generated_identity, anchor='w')
                self.copy_button01.config(state=ACTIVE)
                self.save_button.config(state=ACTIVE)
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
                control_sum = position_1 + (position_2 * 3) + (position_3 * 7) + (position_4 * 9) + position_5 + (
                    position_6 * 3) + (position_7 * 7) + (position_8 * 9) + (position_10 * 3)
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
                self.id_number()
                self.generated_identity = (
                    "Wygenerowana tożsamość:\n"
                    f"{self.name} {self.last_name}\n"
                    f"{self.date_of_birth} {random.choice(self.cities)}\n"
                    f"PESEL: {self.generated_pesel}\n"
                    f"Numer dowodu osobistego: {self.numer_dowodu}\n"
                    f"Znak zodiaku: {self.sign}\n"
                    f"Numer telefonu: {self.numer_telefonu}\n"
                    f"Adres mailowy: {self.adres_email}\n"
                )
                self.Lab6.config(text=self.generated_identity)
                self.copy_button01.config(state=ACTIVE)
                self.save_button.config(state=ACTIVE)
                break
            
    def get_unique_file_name(self, folder_path, file_name):
        base, extension = os.path.splitext(file_name)
        counter = 1
        while os.path.exists(os.path.join(folder_path, file_name)):
            file_name = f"{base}_{counter}{extension}"
            counter += 1
        return file_name

    def save_to_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Pliki tekstowe", "*.txt")])
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(str(self.generated_identity))
                messagebox.showinfo('Śliwka Coding Center ©', 'Wygenerowana tożsamość została zapisana do pliku')
            except Exception as e:
                messagebox.showerror('Śliwka Coding Center ©', 'Wystąpił błąd podczas zapisywania pliku')
                print("Wystąpił błąd podczas zapisywania pliku:", e)
        else:
            messagebox.showinfo('Śliwka Coding Center ©', 'Anulowano zapis do pliku.')

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
        self.page1 = ttk.Frame(self)

        self.label_start = ttk.Label(self.page1, text="Wskaż kwotę do przeliczenia", anchor='center')
        self.label_start.grid(row=0, column=0, padx=5, pady=5, sticky="ns", columnspan=2)

        self.kwota = ttk.Entry(self.page1)
        self.kwota.grid(row=1, column=0, padx=5, pady=5, sticky="ns", columnspan=2)

        self.options = ["polski złoty [PLN]", "dolar amerykański [USD]", "dolar australijski [AUD]", "dolar kanadyjski [CAD]", "euro [EUR]",
           "forint [HUF]", "frank szwajcarski [CHF]", "funt szterling [GBP]", "hrywna [UAH]", "jen [JPY]",
           "korona czeska [CZK]", "korona duńska [DKK]", "korona islandzka [ISK]", "korona norweska [NOK]",
           "korona szwedzka [SEK]", "lej rumuński [RON]", "lira turecka [TRY]", "szekel [ILS]",
           "dirham ZEA [AED]", "rubel białoruski [BYN]", "rubel rosyjski [RUB]", "bat tajski [THB]", "dolar nowozelandzki [NZD]",
           "dolar singapurski [SGD]", "lew bułgarski [BGN]", "real brazylijski [BRL]", "rupia indonezyjska [IDR]",
           "rupia indyjska [INR]","won koreański [KRW]","juan renminbi [CNY]","dong wietnamski [VND]","nowy dolar tajwański [TWD]"]
        
        self.option_var1 = tk.StringVar(self)
        self.option_var2 = tk.StringVar(self)
        
        self.max_length = max(len(option) for option in self.options)
        
        self.option_menu1 = ttk.OptionMenu(self.page1, self.option_var1, *self.options)
        self.option_menu1.grid(row=2, column=0)
        self.option_menu1.config(width=self.max_length + 2)
        self.option_var1.set("Wybierz pierwszą walutę")

        self.option_menu2 = ttk.OptionMenu(self.page1, self.option_var2, *self.options)
        self.option_menu2.grid(row=2, column=1)
        self.option_menu2.config(width=self.max_length + 2)
        self.option_var2.set("Wybierz drugą walutę")

        self.button_table = ttk.Button(self.page1, text='KURS WALUT', command=self.tabela)
        self.button_table.grid(row=3, column=0, padx=5, pady=5, sticky="e")

        self.button_convert = ttk.Button(self.page1, text='PRZELICZ', command=self.konwertuj)
        self.button_convert.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        self.label1 = ttk.Label(self.page1)
        self.label1.grid(row=4, column=0, padx=5, pady=5, columnspan=2, sticky="ns")

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
        if skrot == "PLN":
            return 1.00
        else:
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
        
    def konwertuj(self):
        try:
            waluta1 = str(self.option_var1.get())
            skrot1 = waluta1.split("[")[1].split("]")[0]
            waluta2 = str(self.option_var2.get())
            skrot2 = waluta2.split("[")[1].split("]")[0]
            ilosc = float(self.kwota.get())

            kurs1 = self.kurs_walut(skrot1)
            kurs2 = self.kurs_walut(skrot2)

            if isinstance(kurs1, float) and isinstance(kurs2, float):
                calc = ilosc * kurs1 / kurs2

                info = (
                    f"{ilosc} {skrot1} jest warte {round(calc,2)} {skrot2}")
                self.label1.config(text=info)
            else:
                self.label1.config(text="Nie można przeliczyć - błąd pobierania kursów walut!")
        except ValueError:
            info = (f"Wskaż kwotę do przeliczenia!")
            self.label1.config(text=info)
        except IndexError:
            info = (f"Wskaż waluty!")
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
        self.page1 = ttk.Frame(self)
        self.label1 = ttk.Label(self.page1,
                            text="Z jakich znaków ma składać się hasło?", anchor='center')
        self.label1.grid(row=0, column=0, columnspan=2)

        self.check_numbers = IntVar()
        self.check_button_numbers = ttk.Checkbutton(self.page1,
                                                text="Liczby",
                                                variable=self.check_numbers)
        self.check_button_numbers.grid(row=1, column=0, columnspan=2)

        self.check_letters = IntVar()
        self.check_button_letters = ttk.Checkbutton(self.page1,
                                                text="Litery",
                                                variable=self.check_letters)
        self.check_button_letters.grid(row=2, column=0, columnspan=2)

        self.check_special_characters = IntVar()
        self.check_button_special = ttk.Checkbutton(self.page1,
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

        self.gen_button = ttk.Button(self.page1,
                                 text="GENERUJ",
                                 command=self.click,
                                 state=ACTIVE,
                                 compound="left")
        self.gen_button.grid(row=5, column=0)

        self.back_button = ttk.Button(
            self.page1, text="POWRÓT DO MENU", command=self.back_to_menu, compound="right")
        self.back_button.grid(row=5, column=1)

        self.label2 = ttk.Label(self.page1)
        self.label2.grid(row=6, column=0, columnspan=2)

        self.label3 = ttk.Label(self.page1)
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

        self.password = ""  # Resetowanie hasła
        self.generate_password(charset)
        self.create_result(self.password)
        self.check_passwd_power()

    def create_result(self, password):
        self.page1.clipboard_clear()
        self.page1.clipboard_append(password)

    def generate_password(self, charset):
        self.password = ""  # Resetowanie hasła
        for _ in range(self.pass_len.get()):
            self.password += ''.join(secrets.choice(charset))

    def check_password_strength(self):
        dlugosc_hasla = len(self.password)
        znaki = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+{}[]|;:,.<>?/~`"
        liczba_znakow = len(znaki)
        liczba_kombinacji_slownikowy = liczba_znakow ** dlugosc_hasla
        liczba_kombinacji_brute_force = math.factorial(dlugosc_hasla) * (liczba_znakow ** dlugosc_hasla)
        moc_komputera = psutil.cpu_count() * psutil.cpu_freq().max
        szybkosc_ataku = moc_komputera * 1000000
        czas_zlamania_slownik = liczba_kombinacji_slownikowy / szybkosc_ataku
        czas_zlamania_brute = liczba_kombinacji_brute_force / szybkosc_ataku

        jednostki_czasu = [("lat", 60 * 60 * 24 * 365), ("dni", 60 * 60 * 24), ("godzin", 60 * 60), ("minut", 60), ("sekundy", 1)]

        for jednostka, wartosc_w_sekundach in jednostki_czasu:
            if czas_zlamania_brute >= wartosc_w_sekundach:
                czas_brute_jednostka = czas_zlamania_brute / wartosc_w_sekundach
                czas_zlamania_brute %= wartosc_w_sekundach
                czas_zlamania_brute = int(czas_zlamania_brute)
                break

        for jednostka, wartosc_w_sekundach in jednostki_czasu:
            if czas_zlamania_slownik >= wartosc_w_sekundach:
                czas_slownik_jednostka = czas_zlamania_slownik / wartosc_w_sekundach
                czas_zlamania_slownik %= wartosc_w_sekundach
                czas_zlamania_slownik = int(czas_zlamania_slownik)
                break

        self.power = (f"""Hasło można złamać:
            metodą brute force w czasie {math.floor(czas_brute_jednostka)} {jednostka}
            metodą słownikową w czasie {math.floor(czas_slownik_jednostka)} {jednostka}""")
        return self.power

    def check_passwd_power(self):
        self.check_password_strength()
        self.msgbox = (f"""
            Wygenerowane hasło to:\n
            {str(self.password)}\n
            {self.power}\n
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
        self.all_chars_rus = {"Й": "Y", "Ц": "TS", "У": "U", "К": "K", "Е": "E", "Н": "N", "Г": "G", "Ш": "SH", "Ё": "E",
                              "Щ": "SHCH", "З": "Z", "Х": "H", "Ъ": "", "Ф": "F", "Ы": "Y", "В": "V", "А": "A",
                              "П": "P", "Р": "R", "О": "O", "Л": "L", "Д": "D", "Ж": "ZH", "Э": "E", "Я": "YA",
                              "Ч": "CH", "С": "S", "М": "M", "И": "I", "Т": "T", "Ь": "", "Б": "B", "Ю": "YU",
                              "й": "y",  "ц": "ts",  "у": "u",  "к": "k",  "е": "e",  "н": "n",  "г": "g",
                              "ш": "sh",  "щ": "shch",  "з": "z",  "х": "h",  "ъ": "",  "ф": "f",  "ы": "y",
                              "в": "v",  "а": "a",  "п": "p", "р": "r",  "о": "o",  "л": "l",  "д": "d", "ё": "e",
                              "ж": "zh",  "э": "e",  "я": "ya",  "ч": "ch",  "с": "s",  "м": "m",  "и": "i",
                              "т": "t",  "ь": "",  "б": "b",  "ю": "yu", " ": " "}
        self.all_chars_ukr = {"А": "A", "Б": "B", "В": "V", "Г": "H", "Ґ": "G", "Д": "D", "Е": "E", "Є": "Ye",
                              "Ж": "Zh", "З": "Z", "И": "Y", "І": "I", "Ї": "Yi", "Й": "Y", "К": "K", "Л": "L",
                              "М": "M", "Н": "N", "О": "O", "П": "P", "Р": "R", "С": "S", "Т": "T", "У": "U",
                              "Ф": "F", "Х": "Kh", "Ц": "Ts", "Ч": "Ch", "Ш": "Sh", "Щ": "Shch", "Ь": "",
                              "Ю": "Yu", "Я": "Ya",
                              "а": "a", "б": "b", "в": "v", "г": "h", "ґ": "g", "д": "d", "е": "e", "є": "ie",
                              "ж": "zh", "з": "z", "и": "y", "і": "i", "ї": "i", "й": "i", "к": "k", "л": "l",
                              "м": "m", "н": "n", "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u",
                              "ф": "f", "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh", "щ": "shch", "ь": "",
                              "ю": "iu", "я": "ia", " ": " "}
        self.all_chars_bel = {"А": "A", "Б": "B", "В": "V", "Г": "H", "Ґ": "G", "Д": "D", "Е": "E", "Ё": "Yo",
                              "Ж": "Zh", "З": "Z", "І": "I", "Й": "Y", "К": "K", "Л": "L", "М": "M", "Н": "N",
                              "О": "O", "П": "P", "Р": "R", "С": "S", "Т": "T", "У": "U", "Ў": "Ŭ", "Ф": "F",
                              "Х": "Kh", "Ц": "Ts", "Ч": "Ch", "Ш": "Sh", "Ы": "Y", "Ь": "'", "Э": "E", "Ю": "Yu",
                              "Я": "Ya",
                              "а": "a", "б": "b", "в": "v", "г": "h", "ґ": "g", "д": "d", "е": "e", "ё": "yo",
                              "ж": "zh", "з": "z", "і": "i", "й": "y", "к": "k", "л": "l", "м": "m", "н": "n",
                              "о": "o", "п": "p", "р": "r", "с": "s", "т": "t", "у": "u", "ў": "ŭ", "ф": "f",
                              "х": "kh", "ц": "ts", "ч": "ch", "ш": "sh", "ы": "y", "ь": "'", "э": "e", "ю": "yu",
                              "я": "ya", " ": " "}
        self.all_chars_china = {"吖":"ā", "阿":"ā","啊":"ā", "锕":"ā", "腌":"ā","啊":"á","啊":"ǎ","啊":"à","啊":"a","哎":"āi", "哀":"āi", "埃":"āi", "挨":"āi", "唉":"āi", "锿":"āi",
        "挨":"ái", "皑":"ái", "癌":"ái","毐":"ǎi", "欸":"ǎi", "嗳":"ǎi", "矮":"ǎi", "蔼":"ǎi", "霭":"ǎi",
        "艾":"ài", "砹":"ài", "唉":"ài", "爱":"ài", "隘":"ài", "碍":"ài", "嗳":"ài", "嗌":"ài", "嫒":"ài", "瑷":"ài", "叆":"ài", "暧":"ài","安":"ān", "垵":"ān", "桉":"ān", "氨":"ān", "庵":"ān", "谙":"ān", "鹌":"ān", "𩽾":"ān", "鞍":"ān", "盦":"ān",
        "俺":"ǎn", "埯":"ǎn", "唵":"ǎn", "铵":"ǎn","犴":"àn", "岸":"àn", "按":"àn", "胺":"àn", "案":"àn", "暗":"àn", "黯":"àn","肮":"āng","卬":"áng", "昂":"áng","盎":"àng","凹":"āo", "熬":"āo",
        "敖":"áo", "嶅":"áo", "遨":"áo", "嗷":"áo", "廒":"áo", "璈":"áo", "獒":"áo", "熬":"áo", "聱":"áo", "螯":"áo", "翱":"áo", "鳌":"áo", "鏖":"áo",
        "袄":"ǎo", "媪":"ǎo","岙":"ào", "坳":"ào", "拗":"ào", "奡":"ào", "傲":"ào", "奥":"ào", "骜":"ào", "隩":"ào", "薁":"ào", "澳":"ào", "懊":"ào", "鏊":"ào",
        "八":"bā", "巴":"bā", "扒":"bā", "叭":"bā", "朳":"bā", "芭":"bā", "吧":"bā", "岜":"bā", "疤":"bā", "捌":"bā", "蚆":"bā", "笆":"bā", "羓":"bā", "粑":"bā", "鲃":"bā",
        "拔":"bá", "妭":"bá", "胈":"bá", "菝":"bá", "跋":"bá", "魃":"bá","把":"bǎ", "钯":"bǎ", "靶":"bǎ",
        "坝":"bà", "把":"bà", "爸":"bà", "耙":"bà", "罢":"bà", "鲅":"bà", "霸":"bà", "灞":"bà","吧":"ba", "罢":"ba",
        "掰":"bāi","白":"bái", "拜":"bái","百":"bǎi", "伯":"bǎi", "佰":"bǎi", "柏":"bǎi", "捭":"bǎi", "摆":"bǎi","败":"bài", "拜":"bài", "稗":"bài",
        "扳":"bān", "攽":"bān", "班":"bān", "般":"bān", "颁":"bān", "斑":"bān", "搬":"bān", "瘢":"bān", "癍":"bān", "𨭉":"bān",
        "阪":"bǎn", "坂":"bǎn", "板":"bǎn", "昄":"bǎn", "版":"bǎn", "钣":"bǎn","办":"bàn", "半":"bàn", "扮":"bàn", "伴":"bàn", "拌":"bàn", "绊":"bàn", "柈":"bàn", "湴":"bàn", "靽":"bàn", "瓣":"bàn",
        "邦":"bāng", "帮":"bāng", "𠳐":"bāng", "梆":"bāng", "浜":"bāng","绑":"bǎng", "榜":"bǎng", "膀":"bǎng",
        "玤":"bàng", "蚌":"bàng", "棒":"bàng", "傍":"bàng", "谤":"bàng", "塝":"bàng", "搒":"bàng", "蒡":"bàng", "磅":"bàng", "镑":"bàng",
        "包":"bāo", "苞":"bāo", "孢":"bāo", "枹":"bāo", "胞":"bāo", "炮":"bāo", "剥":"bāo", "龅":"bāo", "煲":"bāo", "褒":"bāo",
        "雹":"báo", "薄":"báo","饱":"bǎo", "宝":"bǎo", "保":"bǎo", "鸨":"bǎo", "葆":"bǎo", "堡":"bǎo", "褓":"bǎo",
        "报":"bào", "刨":"bào", "抱":"bào", "趵":"bào", "豹":"bào", "鲍":"bào", "暴":"bào", "瀑":"bào", "曝":"bào", "爆":"bào",
        "杯":"bēi", "卑":"bēi", "背":"bēi", "椑":"bēi", "悲":"bēi", "碑":"bēi", "鹎":"bēi","北":"běi",
        "贝":"bèi", "孛":"bèi", "邶":"bèi", "狈":"bèi", "𬇙":"bèi", "备":"bèi", "背":"bèi", "钡":"bèi", "倍":"bèi", "悖":"bèi", "被":"bèi", "琲":"bèi", "棓":"bèi", "辈":"bèi", "惫":"bèi", "焙":"bèi", "蓓":"bèi", "碚":"bèi", "鞁":"bèi", "褙":"bèi", "糒":"bèi", "鞴":"bèi", "鐾":"bèi",
        "呗":"bei", "臂":"bei","奔":"bēn", "贲":"bēn", "栟":"bēn", "犇":"bēn", "锛":"bēn","本":"běn", "苯":"běn", "畚":"běn","坌":"bèn", "奔":"bèn", "倴":"bèn", "笨":"bèn",
        "祊":"bēng", "崩":"bēng", "绷":"bēng", "嘣":"bēng","甭":"béng","绷":"běng", "琫":"běng",
        "泵":"bèng", "迸":"bèng", "蚌":"bèng", "绷":"bèng", "甏":"bèng", "镚":"bèng", "蹦":"bèng","逼":"bī", "鲾":"bī","荸":"bí", "鼻":"bí",
        "匕":"bǐ", "比":"bǐ", "芘":"bǐ", "吡":"bǐ", "沘":"bǐ", "妣":"bǐ", "彼":"bǐ", "秕":"bǐ", "笔":"bǐ", "俾":"bǐ", "舭":"bǐ", "鄙":"bǐ",
        "币":"bì", "必":"bì", "毕":"bì", "闭":"bì", "坒":"bì", "佖":"bì", "庇":"bì", "邲":"bì", "诐":"bì", "苾":"bì", "畀":"bì", "咇":"bì", "泌":"bì", "珌":"bì", "荜":"bì", "毖":"bì", "哔":"bì", "陛":"bì", "毙":"bì", "铋":"bì", "秘":"bì", "狴":"bì", "萆":"bì", "庳":"bì", "敝":"bì", "婢":"bì", "皕":"bì", "赑":"bì", "筚":"bì", "愎":"bì", "弼":"bì", "蓖":"bì", "跸":"bì", "痹":"bì", "滗":"bì", "裨":"bì", "辟":"bì", "碧":"bì", "蔽":"bì", "馝":"bì", "箅":"bì", "弊":"bì", "薜":"bì", "觱":"bì", "篦":"bì", "壁":"bì", "避":"bì", "嬖":"bì", "髀":"bì", "濞":"bì", "臂":"bì", "璧":"bì", "襞":"bì",
        "边":"biān", "砭":"biān", "笾":"biān", "萹":"biān", "编":"biān", "煸":"biān", "蝙":"biān", "鳊":"biān", "鞭":"biān",
        "贬":"biǎn", "扁":"biǎn", "匾":"biǎn", "碥":"biǎn", "褊":"biǎn","卞":"biàn", "弁":"biàn", "抃":"biàn", "苄":"biàn", "汴":"biàn", "忭":"biàn", "𨚕":"biàn", "变":"biàn", "昪":"biàn", "便":"biàn", "遍":"biàn", "辨":"biàn", "辩":"biàn", "辫":"biàn",
        "杓":"biāo", "标":"biāo", "飑":"biāo", "骉":"biāo", "彪":"biāo", "幖":"biāo", "骠":"biāo", "膘":"biāo", "熛":"biāo", "飙":"biāo", "镖":"biāo", "瘭":"biāo", "儦":"biāo", "藨":"biāo", "瀌":"biāo", "镳":"biāo",
        "表":"biǎo", "婊":"biǎo", "脿":"biǎo", "裱":"biǎo","俵":"biào", "摽":"biào", "鳔":"biào","瘪":"biē", "憋":"biē", "鳖":"biē",
        "癿":"bié", "别":"bié", "蹩":"bié","瘪":"biě","别":"biè","邠":"bīn", "玢":"bīn", "宾":"bīn", "彬":"bīn", "傧":"bīn", "斌":"bīn", "滨":"bīn", "缤":"bīn", "槟":"bīn", "镔":"bīn", "濒":"bīn", "豳":"bīn",
        "摈":"bìn", "殡":"bìn", "膑":"bìn", "髌":"bìn", "鬓":"bìn","冰":"bīng", "并":"bīng", "兵":"bīng", "槟":"bīng","丙":"bǐng", "邴":"bǐng", "秉":"bǐng", "柄":"bǐng", "昺":"bǐng", "饼":"bǐng", "炳":"bǐng", "屏":"bǐng", "蛃":"bǐng", "禀":"bǐng",
        "并":"bìng", "病":"bìng", "摒":"bìng","拨":"bō", "波":"bō", "玻":"bō", "砵":"bō", "哱":"bō", "钵":"bō", "饽":"bō", "剥":"bō", "菠":"bō", "𬭛":"bō", "播":"bō", "蕃":"bō", "嶓":"bō",
        "伯":"bó", "驳":"bó", "帛":"bó", "泊":"bó", "柏":"bó", "勃":"bó", "钹":"bó", "铂":"bó", "亳":"bó", "浡":"bó", "袯":"bó", "桲":"bó", "舶":"bó", "脖":"bó", "艴":"bó", "博":"bó", "鹁":"bó", "渤":"bó", "搏":"bó", "鲌":"bó", "僰":"bó", "箔":"bó", "膊":"bó", "踣":"bó", "镈":"bó", "薄":"bó", "馞":"bó", "欂":"bó", "礴":"bó",
        "跛":"bǒ", "簸":"bǒ","薄":"bò", "檗":"bò", "擘":"bò", "簸":"bò","卜":"bo", "啵":"bo","逋":"bū", "晡":"bū","醭":"bú",
        "卜":"bǔ", "卟":"bǔ", "补":"bǔ", "捕":"bǔ", "哺":"bǔ", "𬷕":"bǔ", "堡":"bǔ",
        "不":"bù", "布":"bù", "步":"bù", "怖":"bù", "钚":"bù", "埔":"bù", "埗":"bù", "部":"bù", "埠":"bù", "瓿":"bù", "蔀":"bù", "簿":"bù",
        "擦":"cā", "嚓":"cā","偲":"cāi", "猜":"cāi","才":"cái", "材":"cái", "财":"cái", "裁":"cái","采":"cǎi", "彩":"cǎi", "睬":"cǎi", "踩":"cǎi","采":"cài", "菜":"cài", "蔡":"cài",
        "参":"cān", "骖":"cān", "餐":"cān","残":"cán", "蚕":"cán", "惭":"cán","惨":"cǎn", "䅟":"cǎn", "黪":"cǎn",
        "灿":"càn", "粲":"càn", "璨":"càn","仓":"cāng", "伧":"cāng", "苍":"cāng", "沧":"cāng", "鸧":"cāng", "舱":"cāng","藏":"cáng","操":"cāo", "糙":"cāo",
        "曹":"cáo", "嘈":"cáo", "漕":"cáo", "槽":"cáo", "𥕢":"cáo", "螬":"cáo", "艚":"cáo","草":"cǎo","册":"cè", "厕":"cè", "侧":"cè", "测":"cè", "恻":"cè", "策":"cè","参":"cēn","岑":"cén", "涔":"cén",
        "噌":"cēng","层":"céng", "曾":"céng", "嶒":"céng","蹭":"cèng","叉":"chā", "杈":"chā", "差":"chā", "插":"chā", "喳":"chā", "馇":"chā", "碴":"chā", "锸":"chā", "嚓":"chā",
        "叉":"chá", "垞":"chá", "茬":"chá", "茶":"chá", "查":"chá", "搽":"chá", "嵖":"chá", "猹":"chá", "槎":"chá", "碴":"chá", "察":"chá", "𥻗":"chá", "檫":"chá",
        "叉":"chǎ", "衩":"chǎ", "蹅":"chǎ", "镲":"chǎ","叉":"chà", "汊":"chà", "杈":"chà", "岔":"chà", "侘":"chà", "刹":"chà", "衩":"chà", "诧":"chà", "差":"chà", "姹":"chà",
        "拆":"chāi", "钗":"chāi", "差":"chāi","侪":"chái", "柴":"chái", "豺":"chái","茝":"chǎi","虿":"chài", "瘥":"chài",
        "辿":"chān", "觇":"chān", "梴":"chān", "掺":"chān", "搀":"chān", "襜":"chān",
        "单":"chán", "谗":"chán", "婵":"chán", "馋":"chán", "禅":"chán", "孱":"chán", "缠":"chán", "蝉":"chán", "廛":"chán", "潺":"chán", "澶":"chán", "镡":"chán", "瀍":"chán", "蟾":"chán", "儳":"chán", "巉":"chán", "躔":"chán", "镵":"chán",
        "产":"chǎn", "旵":"chǎn", "浐":"chǎn", "谄":"chǎn", "啴":"chǎn", "铲":"chǎn", "阐":"chǎn", "蒇":"chǎn", "𬊤":"chǎn", "骣":"chǎn", "冁":"chǎn",
        "忏":"chàn", "刬":"chàn", "颤":"chàn", "羼":"chàn", "韂":"chàn","伥":"chāng", "昌":"chāng", "菖":"chāng", "猖":"chāng", "阊":"chāng", "娼":"chāng", "鲳":"chāng",
        "长":"cháng", "场":"cháng", "苌":"cháng", "肠":"cháng", "尝":"cháng", "常":"cháng", "偿":"cháng", "徜":"cháng", "嫦":"cháng", "鲿":"cháng",
        "厂":"chǎng", "场":"chǎng", "𬬮":"chǎng", "昶":"chǎng", "惝":"chǎng", "敞":"chǎng", "氅":"chǎng",
        "怅":"chàng", "畅":"chàng", "倡":"chàng", "鬯":"chàng", "唱":"chàng","抄":"chāo", "吵":"chāo", "怊":"chāo", "弨":"chāo", "钞":"chāo", "绰":"chāo", "超":"chāo", "焯":"chāo",
        "晁":"cháo", "巢":"cháo", "朝":"cháo", "嘲":"cháo", "潮":"cháo","吵":"chǎo", "炒":"chǎo","耖":"chào",
        "车":"chē", "砗":"chē","尺":"chě", "扯":"chě","彻":"chè", "坼":"chè", "掣":"chè", "撤":"chè", "澈":"chè", "㬚":"chè",
        "抻":"chēn", "郴":"chēn", "𬘭":"chēn", "琛":"chēn", "棽":"chēn", "嗔":"chēn", "瞋":"chēn",
        "臣":"chén", "尘":"chén", "辰":"chén", "沉":"chén", "忱":"chén", "陈":"chén", "宸":"chén", "梣":"chén", "晨":"chén", "谌":"chén", "煁":"chén",
        "碜":"chěn","衬":"chèn", "疢":"chèn", "龀":"chèn", "称":"chèn", "趁":"chèn", "榇":"chèn", "谶":"chèn",
        "柽":"chēng", "琤":"chēng", "称":"chēng", "蛏":"chēng", "铛":"chēng", "偁":"chēng", "赪":"chēng", "撑":"chēng", "瞠":"chēng",
        "成":"chéng", "丞":"chéng", "呈":"chéng", "枨":"chéng", "诚":"chéng", "承":"chéng", "城":"chéng", "宬":"chéng", "珹":"chéng", "埕":"chéng", "晟":"chéng", "乘":"chéng", "珵":"chéng", "盛":"chéng", "铖":"chéng", "程":"chéng", "惩":"chéng", "裎":"chéng", "塍":"chéng", "酲":"chéng", "澂":"chéng", "澄":"chéng", "憕":"chéng", "橙":"chéng",
        "逞":"chěng", "骋":"chěng", "庱":"chěng", "裎":"chěng","秤":"chèng", "牚":"chèng",
        "吃":"chī", "哧":"chī", "鸱":"chī", "蚩":"chī", "𫄨":"chī", "眵":"chī", "笞":"chī", "瓻":"chī", "摛":"chī", "嗤":"chī", "痴":"chī", "媸":"chī", "螭":"chī", "魑":"chī",
        "池":"chí", "弛":"chí", "驰":"chí", "迟":"chí", "茌":"chí", "持":"chí", "匙":"chí", "漦":"chí", "墀":"chí", "踟":"chí", "篪":"chí",
        "尺":"chǐ", "齿":"chǐ", "侈":"chǐ", "胣":"chǐ", "耻":"chǐ", "豉":"chǐ", "褫":"chǐ",
        "彳":"chì", "叱":"chì", "斥":"chì", "赤":"chì", "饬":"chì", "炽":"chì", "翅":"chì", "敕":"chì", "痓":"chì", "啻":"chì", "傺":"chì", "瘛":"chì",
        "冲":"chōng", "充":"chōng", "忡":"chōng", "茺":"chōng", "㳘":"chōng", "珫":"chōng", "涌":"chōng", "翀":"chōng", "舂":"chōng", "摏":"chōng", "憧":"chōng", "艟":"chōng",
        "虫":"chóng", "种":"chóng", "重":"chóng", "崇":"chóng", "漴":"chóng","宠":"chǒng","冲":"chòng", "铳":"chòng","抽":"chōu", "瘳":"chōu", "犨":"chōu",
        "仇":"chóu", "俦":"chóu", "帱":"chóu", "惆":"chóu", "绸":"chóu", "椆":"chóu", "畴":"chóu", "酬":"chóu", "稠":"chóu", "愁":"chóu", "筹":"chóu", "踌":"chóu", "雠":"chóu",
        "丑":"chǒu", "杻":"chǒu", "侴":"chǒu", "瞅":"chǒu","臭":"chòu","出":"chū", "初":"chū", "䢺":"chū", "䝙":"chū", "摴":"chū", "樗":"chū",
        "刍":"chú", "除":"chú", "厨":"chú", "锄":"chú", "滁":"chú", "蜍":"chú", "雏":"chú", "橱":"chú", "躇":"chú", "蹰":"chú",
        "处":"chǔ", "杵":"chǔ", "础":"chǔ", "楮":"chǔ", "储":"chǔ", "楚":"chǔ", "褚":"chǔ", "濋":"chǔ", "𬺓":"chǔ",
        "亍":"chù", "处":"chù", "怵":"chù", "绌":"chù", "俶":"chù", "畜":"chù", "琡":"chù", "搐":"chù", "触":"chù", "憷":"chù", "黜":"chù", "斶":"chù", "矗":"chù",
        "揣":"chuāi", "搋":"chuāi","揣":"chuǎi","啜":"chuài", "揣":"chuài", "踹":"chuài","川":"chuān", "氚":"chuān", "穿":"chuān","传":"chuán", "船":"chuán", "遄":"chuán", "椽":"chuán",
        "舛":"chuǎn", "喘":"chuǎn","串":"chuàn", "钏":"chuàn","创":"chuāng", "疮":"chuāng", "窗":"chuāng",
        "床":"chuáng", "噇":"chuáng", "幢":"chuáng","闯":"chuǎng","创":"chuàng", "怆":"chuàng","吹":"chuī", "炊":"chuī",
        "垂":"chuí", "倕":"chuí", "陲":"chuí", "捶":"chuí", "棰":"chuí", "圌":"chuí", "槌":"chuí", "锤":"chuí",
        "春":"chūn", "堾":"chūn", "瑃":"chūn", "椿":"chūn", "蝽":"chūn", "䲠":"chūn",
        "纯":"chún", "莼":"chún", "唇":"chún", "淳":"chún", "𬭚":"chún", "鹑":"chún", "醇":"chún","蠢":"chǔn","逴":"chuō", "踔":"chuō", "戳":"chuō",
        "啜":"chuò", "惙":"chuò", "绰":"chuò", "辍":"chuò", "龊":"chuò","刺":"cī", "呲":"cī", "差":"cī", "疵":"cī", "跐":"cī",
        "词":"cí", "茈":"cí", "茨":"cí", "兹":"cí", "祠":"cí", "瓷":"cí", "辞":"cí", "慈":"cí", "磁":"cí", "雌":"cí", "鹚":"cí", "糍":"cí",
        "此":"cǐ", "泚":"cǐ", "玼":"cǐ", "𫚖":"cǐ","次":"cì", "伺":"cì", "刺":"cì", "佽":"cì", "莿":"cì", "赐":"cì",
        "匆":"cōng", "苁":"cōng", "囱":"cōng", "枞":"cōng", "葱":"cōng", "骢":"cōng", "璁":"cōng", "聪":"cōng", "熜":"cōng",
        "从":"cóng", "丛":"cóng", "淙":"cóng", "悰":"cóng", "琮":"cóng","凑":"còu", "辏":"còu", "腠":"còu","粗":"cū","徂":"cú", "殂":"cú",
        "卒":"cù", "促":"cù", "猝":"cù", "蔟":"cù", "醋":"cù", "簇":"cù", "蹙":"cù", "蹴":"cù",
        "汆":"cuān", "撺":"cuān", "镩":"cuān", "蹿":"cuān","攒":"cuán","窜":"cuàn", "篡":"cuàn", "爨":"cuàn",
        "崔":"cuī", "催":"cuī", "缞":"cuī", "摧":"cuī", "榱":"cuī","漼":"cuǐ", "璀":"cuǐ",
        "脆":"cuì", "萃":"cuì", "啐":"cuì", "淬":"cuì", "悴":"cuì", "毳":"cuì", "瘁":"cuì", "粹":"cuì", "翠":"cuì",
        "邨":"cūn", "村":"cūn", "皴":"cūn","存":"cún","忖":"cǔn","寸":"cùn","搓":"cuō", "瑳":"cuō", "磋":"cuō", "撮":"cuō", "蹉":"cuō",
        "嵯":"cuó", "矬":"cuó", "痤":"cuó", "鹾":"cuó","脞":"cuǒ","挫":"cuò", "莝":"cuò", "厝":"cuò", "措":"cuò", "棤":"cuò", "锉":"cuò", "错":"cuò",
        "耷":"dā", "哒":"dā", "搭":"dā", "嗒":"dā", "答":"dā", "𨱏":"dā", "褡":"dā",
        "打":"dá", "达":"dá", "沓":"dá", "怛":"dá", "妲":"dá", "荙":"dá", "炟":"dá", "鿎":"dá", "𫟼":"dá", "笪":"dá", "答":"dá", "溚":"dá", "靼":"dá", "瘩":"dá", "鞑":"dá",
        "打":"dǎ","大":"dà","垯":"da", "跶":"da", "瘩":"da","呆":"dāi", "呔":"dāi", "待":"dāi","歹":"dǎi", "逮":"dǎi", "傣":"dǎi",
        "大":"dài", "代":"dài", "轪":"dài", "垈":"dài", "岱":"dài", "迨":"dài", "骀":"dài", "绐":"dài", "玳":"dài", "带":"dài", "殆":"dài", "贷":"dài", "待":"dài", "怠":"dài", "埭":"dài", "袋":"dài", "逮":"dài", "叇":"dài", "戴":"dài", "黛":"dài",
        "丹":"dān", "担":"dān", "单":"dān", "眈":"dān", "耽":"dān", "郸":"dān", "聃":"dān", "殚":"dān", "瘅":"dān", "箪":"dān", "儋":"dān",
        "𬘘":"dǎn", "胆":"dǎn", "疸":"dǎn", "掸":"dǎn", "赕":"dǎn", "亶":"dǎn",
        "石":"dàn", "旦":"dàn", "但":"dàn", "担":"dàn", "诞":"dàn", "𫢸":"dàn", "疍":"dàn", "萏":"dàn", "啖":"dàn", "淡":"dàn", "惮":"dàn", "弹":"dàn", "蛋":"dàn", "氮":"dàn", "瘅":"dàn", "澹":"dàn", "憺":"dàn", "膻":"dàn",
        "当":"dāng", "珰":"dāng", "铛":"dāng", "裆":"dāng", "筜":"dāng","挡":"dǎng", "党":"dǎng", "谠":"dǎng", "𣗋":"dǎng",
        "当":"dàng", "凼":"dàng", "砀":"dàng", "宕":"dàng", "垱":"dàng", "挡":"dàng", "荡":"dàng", "档":"dàng", "菪":"dàng", "𬍡":"dàng",
        "刀":"dāo", "叨":"dāo", "忉":"dāo", "氘":"dāo", "舠":"dāo", "鱽":"dāo","叨":"dáo", "捯":"dáo",
        "导":"dǎo", "岛":"dǎo", "捣":"dǎo", "倒":"dǎo", "祷":"dǎo", "蹈":"dǎo","到":"dào", "帱":"dào", "倒":"dào", "盗":"dào", "悼":"dào", "道":"dào", "稻":"dào", "纛":"dào",
        "嘚":"dē","得":"dé", "锝":"dé", "德":"dé","地":"de", "的":"de", "得":"de",
        "嘚":"dēi","得":"děi","扽":"dèn","灯":"dēng", "登":"dēng", "噔":"dēng", "璒":"dēng", "蹬":"dēng","等":"děng", "戥":"děng",
        "邓":"dèng", "凳":"dèng", "嶝":"dèng", "澄":"dèng", "磴":"dèng", "瞪":"dèng", "镫":"dèng",
        "氐":"dī", "低":"dī", "的":"dī", "羝":"dī", "堤":"dī", "提":"dī", "䃅":"dī", "滴":"dī", "镝":"dī", "鞮":"dī",
        "狄":"dí", "迪":"dí", "的":"dí", "籴":"dí", "荻":"dí", "敌":"dí", "涤":"dí", "𬱖":"dí", "笛":"dí", "觌":"dí", "髢":"dí", "嘀":"dí", "嫡":"dí", "翟":"dí", "蹢":"dí",
        "氐":"dǐ", "邸":"dǐ", "诋":"dǐ", "坻":"dǐ", "抵":"dǐ", "茋":"dǐ", "底":"dǐ", "柢":"dǐ", "砥":"dǐ", "骶":"dǐ",
        "地":"dì", "玓":"dì", "杕":"dì", "弟":"dì", "的":"dì", "帝":"dì", "递":"dì", "娣":"dì", "菂":"dì", "第":"dì", "谛":"dì", "蒂":"dì", "棣":"dì", "睇":"dì", "媂":"dì", "缔":"dì", "𤧛":"dì", "禘":"dì", "碲":"dì", "䗖":"dì", "踶":"dì",
        "嗲":"diǎ","掂":"diān", "滇":"diān", "颠":"diān", "巅":"diān", "癫":"diān","典":"diǎn", "点":"diǎn", "碘":"diǎn", "踮":"diǎn",
        "电":"diàn", "佃":"diàn", "甸":"diàn", "阽":"diàn", "坫":"diàn", "店":"diàn", "玷":"diàn", "垫":"diàn", "扂":"diàn", "钿":"diàn", "淀":"diàn", "惦":"diàn", "琔":"diàn", "奠":"diàn", "殿":"diàn", "靛":"diàn", "簟":"diàn", "癜":"diàn",
        "刁":"diāo", "叼":"diāo", "汈":"diāo", "凋":"diāo", "貂":"diāo", "碉":"diāo", "雕":"diāo", "鲷":"diāo",
        "吊":"diào", "钓":"diào", "窎":"diào", "调":"diào", "掉":"diào", "铞":"diào", "铫":"diào",
        "爹":"diē", "跌":"diē","迭":"dié", "垤":"dié", "昳":"dié", "绖":"dié", "瓞":"dié", "谍":"dié", "堞":"dié", "耋":"dié", "喋":"dié", "𫶇":"dié", "楪":"dié", "牒":"dié", "叠":"dié", "碟":"dié", "蝶":"dié", "蹀":"dié", "鲽":"dié",
        "丁":"dīng", "仃":"dīng", "叮":"dīng", "玎":"dīng", "盯":"dīng", "町":"dīng", "钉":"dīng", "疔":"dīng", "耵":"dīng", "酊":"dīng",
        "顶":"dǐng", "酊":"dǐng", "鼎":"dǐng","订":"dìng", "钉":"dìng", "定":"dìng", "萣":"dìng", "啶":"dìng", "腚":"dìng", "碇":"dìng", "锭":"dìng",
        "丢":"diū", "铥":"diū","东":"dōng", "冬":"dōng", "咚":"dōng", "岽":"dōng", "氡":"dōng", "鸫":"dōng", "𬟽":"dōng",
        "董":"dǒng", "懂":"dǒng","动":"dòng", "冻":"dòng", "侗":"dòng", "垌":"dòng", "栋":"dòng", "峒":"dòng", "胨":"dòng", "洞":"dòng", "恫":"dòng", "胴":"dòng", "硐":"dòng",
        "都":"dōu", "兜":"dōu", "蔸":"dōu", "篼":"dōu","斗":"dǒu", "抖":"dǒu", "钭":"dǒu", "陡":"dǒu", "蚪":"dǒu",
        "斗":"dòu", "豆":"dòu", "逗":"dòu", "读":"dòu", "痘":"dòu", "窦":"dòu",
        "厾":"dū", "都":"dū", "阇":"dū", "督":"dū", "嘟":"dū","毒":"dú", "独":"dú", "读":"dú", "渎":"dú", "椟":"dú", "犊":"dú", "牍":"dú", "黩":"dú", "髑":"dú",
        "肚":"dǔ", "笃":"dǔ", "堵":"dǔ", "赌":"dǔ", "睹":"dǔ","芏":"dù", "杜":"dù", "肚":"dù", "妒":"dù", "度":"dù", "𬭊":"dù", "渡":"dù", "镀":"dù", "蠹":"dù",
        "耑":"duān", "端":"duān","短":"duǎn","段":"duàn", "断":"duàn", "塅":"duàn", "缎":"duàn", "瑖":"duàn", "椴":"duàn", "煅":"duàn", "锻":"duàn", "簖":"duàn",
        "堆":"duī","队":"duì", "对":"duì", "兑":"duì", "祋":"duì", "怼":"duì", "碓":"duì",
        "吨":"dūn", "惇":"dūn", "敦":"dūn", "墩":"dūn", "礅":"dūn", "镦":"dūn", "蹾":"dūn", "蹲":"dūn",
        "盹":"dǔn", "趸":"dǔn","囤":"dùn", "沌":"dùn", "炖":"dùn", "砘":"dùn", "钝":"dùn", "盾":"dùn", "顿":"dùn", "遁":"dùn",
        "多":"duō", "咄":"duō", "哆":"duō", "剟":"duō", "㙍":"duō", "掇":"duō", "裰":"duō",
        "夺":"duó", "度":"duó", "铎":"duó", "踱":"duó","朵":"duǒ", "垛":"duǒ", "哚":"duǒ", "埵":"duǒ", "躲":"duǒ", "亸":"duǒ",
        "驮":"duò", "剁":"duò", "饳":"duò", "垛":"duò", "舵":"duò", "堕":"duò", "惰":"duò", "跺":"duò",
        "阿":"ē", "屙":"ē", "婀":"ē","讹":"é", "俄":"é", "莪":"é", "哦":"é", "峨":"é", "涐":"é", "娥":"é", "锇":"é", "鹅":"é", "蛾":"é", "额":"é",
        "恶":"ě","厄":"è", "扼":"è", "苊":"è", "呃":"è", "轭":"è", "垩":"è", "姶":"è", "恶":"è", "饿":"è", "鄂":"è", "谔":"è", "堨":"è", "萼":"è", "遏":"è", "崿":"è", "愕":"è", "𫫇":"è", "腭":"è", "𥔲":"è", "鹗":"è", "锷":"è", "颚":"è", "噩":"è", "鳄":"è",
        "呃":"e","欸":"ê̄","欸":"ế","欸":"ê̌","欸":"ề","恩":"ēn", "蒽":"ēn","摁":"èn","儿":"ér", "而":"ér", "陑":"ér", "耏":"ér", "鸸":"ér", "鲕":"ér",
        "尔":"ěr", "耳":"ěr", "迩":"ěr", "饵":"ěr", "洱":"ěr", "珥":"ěr", "铒":"ěr",
        "二":"èr", "贰":"èr", "咡":"èr","发":"fā","乏":"fá", "伐":"fá", "罚":"fá", "垡":"fá", "阀":"fá", "筏":"fá","法":"fǎ", "砝":"fǎ","发":"fà", "珐":"fà",
        "帆":"fān", "番":"fān", "幡":"fān", "藩":"fān", "翻":"fān","凡":"fán", "氾":"fán", "矾":"fán", "钒":"fán", "烦":"fán", "墦":"fán", "樊":"fán", "璠":"fán", "燔":"fán", "𫔍":"fán", "繁":"fán", "𬸪":"fán", "蹯":"fán", "蘩":"fán",
        "反":"fǎn", "返":"fǎn","犯":"fàn", "饭":"fàn", "泛":"fàn", "范":"fàn", "贩":"fàn", "畈":"fàn", "梵":"fàn",
        "方":"fāng", "邡":"fāng", "坊":"fāng", "芳":"fāng", "枋":"fāng", "牥":"fāng", "钫":"fāng", "蚄":"fāng",
        "防":"fáng", "坊":"fáng", "妨":"fáng", "肪":"fáng", "房":"fáng", "鲂":"fáng","仿":"fǎng", "访":"fǎng", "纺":"fǎng", "昉":"fǎng", "舫":"fǎng","放":"fàng",
        "飞":"fēi", "妃":"fēi", "非":"fēi", "菲":"fēi", "啡":"fēi", "𬴂":"fēi", "绯":"fēi", "扉":"fēi", "蜚":"fēi", "霏":"fēi", "鲱":"fēi",
        "肥":"féi", "淝":"féi", "腓":"féi","朏":"fěi", "匪":"fěi", "诽":"fěi", "菲":"fěi", "悱":"fěi", "棐":"fěi", "斐":"fěi", "榧":"fěi", "蜚":"fěi", "翡":"fěi", "篚":"fěi",
        "芾":"fèi", "吠":"fèi", "肺":"fèi", "狒":"fèi", "废":"fèi", "沸":"fèi", "费":"fèi", "剕":"fèi", "痱":"fèi", "镄":"fèi",
        "分":"fēn", "芬":"fēn", "吩":"fēn", "纷":"fēn", "玢":"fēn", "氛":"fēn", "翂":"fēn", "棻":"fēn", "酚":"fēn",
        "坟":"fén", "汾":"fén", "棼":"fén", "焚":"fén", "𣸣":"fén", "豮":"fén", "鼢":"fén","粉":"fěn",
        "分":"fèn", "份":"fèn", "坋":"fèn", "奋":"fèn", "忿":"fèn", "偾":"fèn", "粪":"fèn", "愤":"fèn", "鲼":"fèn", "瀵":"fèn",
        "丰":"fēng", "风":"fēng", "沣":"fēng", "沨":"fēng", "枫":"fēng", "封":"fēng", "砜":"fēng", "疯":"fēng", "峰":"fēng", "烽":"fēng", "葑":"fēng", "崶":"fēng", "锋":"fēng", "蜂":"fēng", "酆":"fēng",
        "冯":"féng", "逢":"féng", "浲":"féng", "缝":"féng","讽":"fěng", "唪":"fěng","凤":"fèng", "奉":"fèng", "俸":"fèng", "赗":"fèng", "缝":"fèng","佛":"fó","缶":"fǒu", "否":"fǒu",
        "夫":"fū", "呋":"fū", "玞":"fū", "肤":"fū", "砆":"fū", "𫓧":"fū", "麸":"fū", "趺":"fū", "跗":"fū", "稃":"fū", "鄜":"fū", "孵":"fū", "敷":"fū",
        "弗":"fú", "伏":"fú", "凫":"fú", "扶":"fú", "芙":"fú", "芾":"fú", "芣":"fú", "佛":"fú", "孚":"fú", "拂":"fú", "苻":"fú", "茀":"fú", "服":"fú", "怫":"fú", "宓":"fú", "绂":"fú", "绋":"fú", "韨":"fú", "茯":"fú", "罘":"fú", "氟":"fú", "俘":"fú", "郛":"fú", "洑":"fú", "祓":"fú", "垺":"fú", "莩":"fú", "蚨":"fú", "浮":"fú", "琈":"fú", "菔":"fú", "桴":"fú", "符":"fú", "匐":"fú", "涪":"fú", "袱":"fú", "幅":"fú", "辐":"fú", "蜉":"fú", "福":"fú", "榑":"fú", "蝠":"fú", "幞":"fú", "黻":"fú",
        "抚":"fǔ", "甫":"fǔ", "㕮":"fǔ", "拊":"fǔ", "斧":"fǔ", "府":"fǔ", "俯":"fǔ", "釜":"fǔ", "辅":"fǔ", "脯":"fǔ", "𫖯":"fǔ", "腑":"fǔ", "滏":"fǔ", "腐":"fǔ", "簠":"fǔ", "黼":"fǔ",
        "父":"fù", "讣":"fù", "付":"fù", "负":"fù", "妇":"fù", "㳇":"fù", "附":"fù", "咐":"fù", "阜":"fù", "服":"fù", "驸":"fù", "赴":"fù", "复":"fù", "副":"fù", "赋":"fù", "傅":"fù", "富":"fù", "腹":"fù", "鲋":"fù", "缚":"fù", "赙":"fù", "蝮":"fù", "覆":"fù", "馥":"fù",
        "夹":"gā", "旮":"gā", "伽":"gā", "咖":"gā", "戛":"gā", "嘎":"gā","钆":"gá", "尜":"gá", "嘎":"gá", "噶":"gá",
        "尕":"gǎ", "嘎":"gǎ","尬":"gà","该":"gāi", "陔":"gāi", "垓":"gāi", "荄":"gāi", "晐":"gāi", "赅":"gāi","改":"gǎi",
        "丐":"gài", "芥":"gài", "𬮿":"gài", "钙":"gài", "盖":"gài", "溉":"gài", "概":"gài", "戤":"gài",
        "干":"gān", "甘":"gān", "玕":"gān", "杆":"gān", "肝":"gān", "坩":"gān", "苷":"gān", "矸":"gān", "泔":"gān", "柑":"gān", "虷":"gān", "竿":"gān", "酐":"gān", "疳":"gān", "尴":"gān",
        "杆":"gǎn", "秆":"gǎn", "赶":"gǎn", "敢":"gǎn", "感":"gǎn", "澉":"gǎn", "橄":"gǎn", "擀":"gǎn", "鳡":"gǎn",
        "干":"gàn", "旰":"gàn", "绀":"gàn", "淦":"gàn", "㽏":"gàn", "赣":"gàn",
        "冈":"gāng", "冮":"gāng", "扛":"gāng", "刚":"gāng", "岗":"gāng", "肛":"gāng", "纲":"gāng", "㭎":"gāng", "矼":"gāng", "钢":"gāng", "缸":"gāng", "罡":"gāng", "堽":"gāng",
        "岗":"gǎng", "港":"gǎng","杠":"gàng", "鿍":"gàng", "钢":"gàng", "筻":"gàng", "戆":"gàng",
        "皋":"gāo", "高":"gāo", "羔":"gāo", "槔":"gāo", "睾":"gāo", "膏":"gāo", "篙":"gāo", "糕":"gāo",
        "杲":"gǎo", "搞":"gǎo", "缟":"gǎo", "槁":"gǎo", "镐":"gǎo", "稿":"gǎo", "藁":"gǎo","告":"gào", "郜":"gào", "诰":"gào", "锆":"gào", "筶":"gào", "膏":"gào",
        "戈":"gē", "仡":"gē", "圪":"gē", "疙":"gē", "咯":"gē", "饹":"gē", "哥":"gē", "胳":"gē", "鸽":"gē", "袼":"gē", "搁":"gē", "割":"gē", "歌":"gē",
        "革":"gé", "阁":"gé", "格":"gé", "鬲":"gé", "胳":"gé", "搁":"gé", "葛":"gé", "蛤":"gé", "隔":"gé", "塥":"gé", "嗝":"gé", "滆":"gé", "膈":"gé", "骼":"gé", "镉":"gé",
        "个":"gě", "合":"gě", "哿":"gě", "舸":"gě", "盖":"gě", "葛":"gě",
        "个":"gè", "各":"gè", "虼":"gè", "硌":"gè", "铬":"gè","给":"gěi","根":"gēn", "跟":"gēn","哏":"gén","艮":"gěn",
        "亘":"gèn", "艮":"gèn", "茛":"gèn","更":"gēng", "庚":"gēng", "耕":"gēng", "浭":"gēng", "赓":"gēng", "鹒":"gēng", "羹":"gēng",
        "埂":"gěng", "耿":"gěng", "哽":"gěng", "绠":"gěng", "梗":"gěng", "颈":"gěng", "𬒔":"gěng", "鲠":"gěng",
        "更":"gèng", "暅":"gèng","工":"gōng", "弓":"gōng", "公":"gōng", "功":"gōng", "攻":"gōng", "䢼":"gōng", "供":"gōng", "肱":"gōng", "宫":"gōng", "恭":"gōng", "蚣":"gōng", "躬":"gōng", "龚":"gōng", "觥":"gōng",
        "巩":"gǒng", "汞":"gǒng", "拱":"gǒng", "珙":"gǒng", "硔":"gǒng",
        "共":"gòng", "贡":"gòng", "供":"gòng","勾":"gōu", "句":"gōu", "佝":"gōu", "沟":"gōu", "枸":"gōu", "钩":"gōu", "缑":"gōu", "篝":"gōu", "鞲":"gōu",
        "苟":"gǒu", "岣":"gǒu", "狗":"gǒu", "耇":"gǒu", "枸":"gǒu", "笱":"gǒu",
        "勾":"gòu", "构":"gòu", "购":"gòu", "诟":"gòu", "垢":"gòu", "姤":"gòu", "够":"gòu", "遘":"gòu", "彀":"gòu", "雊":"gòu", "媾":"gòu", "觏":"gòu",
        "估":"gū", "咕":"gū", "呱":"gū", "沽":"gū", "孤":"gū", "姑":"gū", "轱":"gū", "骨":"gū", "鸪":"gū", "菰":"gū", "菇":"gū", "蛄":"gū", "蓇":"gū", "辜":"gū", "酤":"gū", "觚":"gū", "箍":"gū",
        "古":"gǔ", "谷":"gǔ", "汩":"gǔ", "诂":"gǔ", "股":"gǔ", "骨":"gǔ", "牯":"gǔ", "𦙶":"gǔ", "贾":"gǔ", "罟":"gǔ", "钴":"gǔ", "羖":"gǔ", "蛄":"gǔ", "蛊":"gǔ", "鹄":"gǔ", "馉":"gǔ", "鼓":"gǔ", "毂":"gǔ", "榖":"gǔ", "嘏":"gǔ", "鹘":"gǔ", "臌":"gǔ", "瞽":"gǔ", "瀔":"gǔ",
        "估":"gù", "固":"gù", "故":"gù", "顾":"gù", "堌":"gù", "梏":"gù", "崮":"gù", "牿":"gù", "雇":"gù", "锢":"gù", "痼":"gù", "鲴":"gù",
        "瓜":"guā", "呱":"guā", "刮":"guā", "胍":"guā", "栝":"guā", "鸹":"guā","剐":"guǎ", "寡":"guǎ",
        "卦":"guà", "坬":"guà", "诖":"guà", "挂":"guà", "褂":"guà","乖":"guāi", "掴":"guāi","拐":"guǎi","夬":"guài", "怪":"guài",
        "关":"guān", "观":"guān", "纶":"guān", "官":"guān", "冠":"guān", "倌":"guān", "蒄":"guān", "棺":"guān", "鳏":"guān",
        "莞":"guǎn", "馆":"guǎn", "琯":"guǎn", "筦":"guǎn", "管":"guǎn", "鳤":"guǎn",
        "毌":"guàn", "观":"guàn", "贯":"guàn", "冠":"guàn", "掼":"guàn", "涫":"guàn", "惯":"guàn", "祼":"guàn", "盥":"guàn", "灌":"guàn", "瓘":"guàn", "爟":"guàn", "鹳":"guàn", "罐":"guàn",
        "光":"guāng", "垙":"guāng", "咣":"guāng", "洸":"guāng", "珖":"guāng", "桄":"guāng", "𨐈":"guāng", "胱":"guāng",
        "广":"guǎng", "犷":"guǎng","桄":"guàng", "逛":"guàng","归":"guī", "圭":"guī", "龟":"guī", "妫":"guī", "规":"guī", "邽":"guī", "皈":"guī", "闺":"guī", "珪":"guī", "硅":"guī", "瑰":"guī", "鲑":"guī", "鬶":"guī",
        "宄":"guǐ", "轨":"guǐ", "庋":"guǐ", "匦":"guǐ", "诡":"guǐ", "鬼":"guǐ", "姽":"guǐ", "癸":"guǐ", "晷":"guǐ", "簋":"guǐ",
        "柜":"guì", "炅":"guì", "刿":"guì", "刽":"guì", "贵":"guì", "桂":"guì", "桧":"guì", "筀":"guì", "跪":"guì", "鳜":"guì",
        "衮":"gǔn", "绲":"gǔn", "辊":"gǔn", "滚":"gǔn", "磙":"gǔn", "鲧":"gǔn","棍":"gùn",
        "过":"guō", "呙":"guō", "埚":"guō", "郭":"guō", "涡":"guō", "崞":"guō", "聒":"guō", "锅":"guō", "蝈":"guō",
        "国":"guó", "帼":"guó", "𬇹":"guó", "腘":"guó", "虢":"guó", "馘":"guó",
        "果":"guǒ", "馃":"guǒ", "椁":"guǒ", "蜾":"guǒ", "裹":"guǒ", "粿":"guǒ","过":"guò","哈":"hā", "铪":"hā","蛤":"há",
        "哈":"hǎ","哈":"hà","咍":"hāi", "咳":"hāi", "嗨":"hāi","还":"hái", "孩":"hái", "骸":"hái","胲":"hǎi", "海":"hǎi", "醢":"hǎi",
        "亥":"hài", "骇":"hài", "氦":"hài", "害":"hài", "嗐":"hài","犴":"hān", "顸":"hān", "蚶":"hān", "酣":"hān", "憨":"hān", "鼾":"hān",
        "邗":"hán", "汗":"hán", "邯":"hán", "含":"hán", "函":"hán", "虷":"hán", "浛":"hán", "琀":"hán", "晗":"hán", "崡":"hán", "焓":"hán", "涵":"hán", "韩":"hán", "嵅":"hán", "寒":"hán",
        "罕":"hǎn", "喊":"hǎn", "蔊":"hǎn", "㘎":"hǎn","汉":"hàn", "扞":"hàn", "汗":"hàn", "旱":"hàn", "垾":"hàn", "捍":"hàn", "悍":"hàn", "菡":"hàn", "焊":"hàn", "颔":"hàn", "撖":"hàn", "蔊":"hàn", "暵":"hàn", "撼":"hàn", "翰":"hàn", "憾":"hàn", "瀚":"hàn",
        "夯":"hāng","行":"háng", "吭":"háng", "杭":"háng", "绗":"háng", "航":"háng", "颃":"háng",
        "沆":"hàng", "巷":"hàng","蒿":"hāo", "薅":"hāo", "嚆":"hāo","号":"háo", "蚝":"háo", "毫":"háo", "嗥":"háo", "貉":"háo", "豪":"háo", "壕":"háo", "嚎":"háo", "濠":"háo",
        "好":"hǎo", "郝":"hǎo","号":"hào", "好":"hào", "昊":"hào", "耗":"hào", "浩":"hào", "淏":"hào", "皓":"hào", "鄗":"hào", "皞":"hào", "颢":"hào", "灏":"hào",
        "诃":"hē", "呵":"hē", "喝":"hē", "嗬":"hē","禾":"hé", "合":"hé", "纥":"hé", "何":"hé", "和":"hé", "郃":"hé", "劾":"hé", "河":"hé", "曷":"hé", "饸":"hé", "阂":"hé", "盍":"hé", "荷":"hé", "核":"hé", "𬌗":"hé", "盉":"hé", "菏":"hé", "龁":"hé", "盒":"hé", "涸":"hé", "颌":"hé", "貉":"hé", "阖":"hé", "鹖":"hé", "翮":"hé", "鞨":"hé", "龢":"hé",
        "吓":"hè", "和":"hè", "垎":"hè", "贺":"hè", "荷":"hè", "隺":"hè", "喝":"hè", "赫":"hè", "熇":"hè", "褐":"hè", "鹤":"hè", "翯":"hè", "壑":"hè",
        "黑":"hēi", "嘿":"hēi", "𬭶":"hēi","痕":"hén","𬣳":"hěn", "很":"hěn", "狠":"hěn","恨":"hèn","亨":"hēng", "哼":"hēng",
        "行":"héng", "恒":"héng", "姮":"héng", "珩":"héng", "桁":"héng", "鸻":"héng", "横":"héng", "衡":"héng", "蘅":"héng",
        "堼":"hèng", "横":"hèng","哼":"hng","吽":"hōng", "轰":"hōng", "哄":"hōng", "訇":"hōng", "烘":"hōng", "薨":"hōng",
        "弘":"hóng", "红":"hóng", "玒":"hóng", "闳":"hóng", "宏":"hóng", "纮":"hóng", "泓":"hóng", "荭":"hóng", "虹":"hóng", "竑":"hóng", "洪":"hóng", "翃":"hóng", "𫟹":"hóng", "鸿":"hóng", "𬭎":"hóng", "谼":"hóng", "蕻":"hóng", "黉":"hóng",
        "哄":"hǒng", "唝":"hǒng","讧":"hòng", "哄":"hòng","齁":"hōu",
        "侯":"hóu", "喉":"hóu", "猴":"hóu", "𬭤":"hóu", "瘊":"hóu", "骺":"hóu", "篌":"hóu", "糇":"hóu","吼":"hǒu",
        "后":"hòu", "郈":"hòu", "厚":"hòu", "侯":"hòu", "垕":"hòu", "逅":"hòu", "候":"hòu", "堠":"hòu", "鲎":"hòu", "鲘":"hòu",
        "乎":"hū", "昒":"hū", "呼":"hū", "忽":"hū", "轷":"hū", "烀":"hū", "唿":"hū", "淴":"hū", "惚":"hū", "滹":"hū", "糊":"hū",
        "囫":"hú", "和":"hú", "狐":"hú", "弧":"hú", "胡":"hú", "壶":"hú", "核":"hú", "斛":"hú", "葫":"hú", "鹄":"hú", "猢":"hú", "湖":"hú", "瑚":"hú", "煳":"hú", "鹕":"hú", "鹘":"hú", "槲":"hú", "蝴":"hú", "糊":"hú", "縠":"hú", "醐":"hú", "觳":"hú",
        "虎":"hǔ", "浒":"hǔ", "唬":"hǔ", "琥":"hǔ","互":"hù", "户":"hù", "冱":"hù", "护":"hù", "沪":"hù", "昈":"hù", "岵":"hù", "怙":"hù", "戽":"hù", "祜":"hù", "笏":"hù", "瓠":"hù", "扈":"hù", "鄠":"hù", "嫭":"hù", "糊":"hù", "鹱":"hù", "鳠":"hù",
        "花":"huā", "砉":"huā", "哗":"huā","划":"huá", "华":"huá", "哗":"huá", "骅":"huá", "铧":"huá", "猾":"huá", "滑":"huá",
        "化":"huà", "划":"huà", "华":"huà", "画":"huà", "话":"huà", "桦":"huà", "婳":"huà", "觟":"huà",
        "怀":"huái", "徊":"huái", "淮":"huái", "槐":"huái", "踝":"huái","坏":"huài","欢":"huān", "獾":"huān",
        "还":"huán", "环":"huán", "郇":"huán", "荁":"huán", "峘":"huán", "洹":"huán", "桓":"huán", "𬘫":"huán", "萑":"huán", "貆":"huán", "锾":"huán", "圜":"huán", "澴":"huán", "寰":"huán", "缳":"huán", "𤩽":"huán", "鹮":"huán", "镮":"huán", "鬟":"huán",
        "缓":"huǎn", "㬊":"huǎn","幻":"huàn", "奂":"huàn", "宦":"huàn", "换":"huàn", "唤":"huàn", "涣":"huàn", "浣":"huàn", "患":"huàn", "焕":"huàn", "逭":"huàn", "痪":"huàn", "豢":"huàn", "漶":"huàn", "鲩":"huàn", "擐":"huàn",
        "肓":"huāng", "荒":"huāng", "慌":"huāng","皇":"huáng", "黄":"huáng", "凰":"huáng", "隍":"huáng", "喤":"huáng", "遑":"huáng", "徨":"huáng", "湟":"huáng", "惶":"huáng", "媓":"huáng", "瑝":"huáng", "煌":"huáng", "锽":"huáng", "潢":"huáng", "璜":"huáng", "蝗":"huáng", "篁":"huáng", "艎":"huáng", "𨱑":"huáng", "癀":"huáng", "蟥":"huáng", "簧":"huáng", "鳇":"huáng",
        "恍":"huǎng", "晃":"huǎng", "谎":"huǎng", "幌":"huǎng","晃":"huàng", "㿠":"huàng", "滉":"huàng",
        "灰":"huī", "㧑":"huī", "诙":"huī", "挥":"huī", "咴":"huī", "恢":"huī", "袆":"huī", "晖":"huī", "辉":"huī", "翚":"huī", "麾":"huī", "徽":"huī", "隳":"huī",
        "回":"huí", "茴":"huí", "洄":"huí", "烠":"huí", "蛔":"huí","虺":"huǐ", "悔":"huǐ", "毁":"huǐ",
        "卉":"huì", "汇":"huì", "会":"huì", "讳":"huì", "荟":"huì", "哕":"huì", "浍":"huì", "诲":"huì", "绘":"huì", "恚":"huì", "桧":"huì", "贿":"huì", "烩":"huì", "彗":"huì", "硊":"huì", "晦":"huì", "秽":"huì", "惠":"huì", "喙":"huì", "翙":"huì", "溃":"huì", "𬤝":"huì", "慧":"huì", "蕙":"huì", "橞":"huì", "𬭬":"huì", "蟪":"huì",
        "昏":"hūn", "荤":"hūn", "阍":"hūn", "惛":"hūn", "婚":"hūn", "碈":"hūn","浑":"hún", "珲":"hún", "馄":"hún", "魂":"hún","诨":"hùn", "混":"hùn", "溷":"hùn",
        "耠":"huō", "𬴃":"huō", "锪":"huō", "劐":"huō", "嚄":"huō", "豁":"huō", "攉":"huō","和":"huó", "佸":"huó", "活":"huó",
        "火":"huǒ", "伙":"huǒ", "钬":"huǒ", "漷":"huǒ", "夥":"huǒ","或":"huò", "和":"huò", "货":"huò", "获":"huò", "祸":"huò", "惑":"huò", "霍":"huò", "濩":"huò", "豁":"huò", "镬":"huò", "藿":"huò", "嚯":"huò", "蠖":"huò", "㸌":"huò",
        "和":"huo","几":"jī", "讥":"jī", "击":"jī", "叽":"jī", "饥":"jī", "玑":"jī", "圾":"jī", "芨":"jī", "机":"jī", "乩":"jī", "肌":"jī", "矶":"jī", "鸡":"jī", "枅":"jī", "奇":"jī", "𬯀":"jī", "剞":"jī", "唧":"jī", "积":"jī", "笄":"jī", "屐":"jī", "姬":"jī", "基":"jī", "𫓯":"jī", "期":"jī", "赍":"jī", "犄":"jī", "嵇":"jī", "缉":"jī", "畸":"jī", "跻":"jī", "𫓹":"jī", "𫌀":"jī", "箕":"jī", "稽":"jī", "觭":"jī", "齑":"jī", "畿":"jī", "墼":"jī", "激":"jī", "羁":"jī",
        "及":"jí", "伋":"jí", "吉":"jí", "岌":"jí", "汲":"jí", "级":"jí", "极":"jí", "即":"jí", "佶":"jí", "亟":"jí", "笈":"jí", "急":"jí", "姞":"jí", "疾":"jí", "堲":"jí", "棘":"jí", "殛":"jí", "戢":"jí", "集":"jí", "㴔":"jí", "蒺":"jí", "楫":"jí", "辑":"jí", "嵴":"jí", "嫉":"jí", "耤":"jí", "蕺":"jí", "瘠":"jí", "鹡":"jí", "藉":"jí", "蹐":"jí", "籍":"jí",
        "几":"jǐ", "己":"jǐ", "纪":"jǐ", "虮":"jǐ", "挤":"jǐ", "济":"jǐ", "给":"jǐ", "脊":"jǐ", "掎":"jǐ", "鱾":"jǐ", "戟":"jǐ", "麂":"jǐ",
        "计":"jì", "记":"jì", "伎":"jì", "纪":"jì", "技":"jì", "芰":"jì", "系":"jì", "忌":"jì", "际":"jì", "妓":"jì", "季":"jì", "剂":"jì", "垍":"jì", "荠":"jì", "迹":"jì", "洎":"jì", "济":"jì", "既":"jì", "𪟝":"jì", "觊":"jì", "继":"jì", "偈":"jì", "徛":"jì", "祭":"jì", "悸":"jì", "寄":"jì", "寂":"jì", "绩":"jì", "惎":"jì", "蓟":"jì", "霁":"jì", "跽":"jì", "鲚":"jì", "漈":"jì", "暨":"jì", "稷":"jì", "鲫":"jì", "髻":"jì", "冀":"jì", "穄":"jì", "罽":"jì", "𬶨":"jì", "𬶭":"jì", "骥":"jì", "瀱":"jì",
        "加":"jiā", "夹":"jiā", "伽":"jiā", "茄":"jiā", "佳":"jiā", "泇":"jiā", "迦":"jiā", "珈":"jiā", "枷":"jiā", "浃":"jiā", "𬂩":"jiā", "痂":"jiā", "家":"jiā", "笳":"jiā", "袈":"jiā", "葭":"jiā", "跏":"jiā", "嘉":"jiā", "镓":"jiā",
        "夹":"jiá", "郏":"jiá", "荚":"jiá", "恝":"jiá", "戛":"jiá", "铗":"jiá", "颊":"jiá", "蛱":"jiá",
        "甲":"jiǎ", "岬":"jiǎ", "胛":"jiǎ", "贾":"jiǎ", "钾":"jiǎ", "假":"jiǎ", "斝":"jiǎ", "槚":"jiǎ", "瘕":"jiǎ",
        "价":"jià", "驾":"jià", "架":"jià", "假":"jià", "嫁":"jià", "稼":"jià","家":"jia",
        "戋":"jiān", "尖":"jiān", "奸":"jiān", "歼":"jiān", "坚":"jiān", "间":"jiān", "肩":"jiān", "艰":"jiān", "监":"jiān", "兼":"jiān", "菅":"jiān", "笺":"jiān", "犍":"jiān", "湔":"jiān", "缄":"jiān", "搛":"jiān", "蒹":"jiān", "煎":"jiān", "缣":"jiān", "鲣":"jiān", "鹣":"jiān", "篯":"jiān", "鞬":"jiān", "鞯":"jiān", "鳒":"jiān",
        "拣":"jiǎn", "枧":"jiǎn", "茧":"jiǎn", "柬":"jiǎn", "俭":"jiǎn", "捡":"jiǎn", "笕":"jiǎn", "检":"jiǎn", "趼":"jiǎn", "减":"jiǎn", "剪":"jiǎn", "睑":"jiǎn", "锏":"jiǎn", "裥":"jiǎn", "暕":"jiǎn", "简":"jiǎn", "谫":"jiǎn", "戬":"jiǎn", "碱":"jiǎn", "翦":"jiǎn", "蹇":"jiǎn", "謇":"jiǎn",
        "见":"jiàn", "件":"jiàn", "间":"jiàn", "𬣡":"jiàn", "饯":"jiàn", "建":"jiàn", "荐":"jiàn", "贱":"jiàn", "牮":"jiàn", "剑":"jiàn", "监":"jiàn", "健":"jiàn", "舰":"jiàn", "涧":"jiàn", "渐":"jiàn", "谏":"jiàn", "楗":"jiàn", "践":"jiàn", "毽":"jiàn", "腱":"jiàn", "溅":"jiàn", "鉴":"jiàn", "键":"jiàn", "槛":"jiàn", "僭":"jiàn", "踺":"jiàn", "箭":"jiàn",
        "江":"jiāng", "茳":"jiāng", "将":"jiāng", "姜":"jiāng", "豇":"jiāng", "浆":"jiāng", "僵":"jiāng", "缰":"jiāng", "鳉":"jiāng", "礓":"jiāng", "疆":"jiāng",
        "讲":"jiǎng", "奖":"jiǎng", "桨":"jiǎng", "蒋":"jiǎng", "耩":"jiǎng", "膙":"jiǎng",
        "匠":"jiàng", "降":"jiàng", "虹":"jiàng", "将":"jiàng", "洚":"jiàng", "绛":"jiàng", "浆":"jiàng", "弶":"jiàng", "强":"jiàng", "酱":"jiàng", "犟":"jiàng", "糨":"jiàng",
        "艽":"jiāo", "交":"jiāo", "郊":"jiāo", "茭":"jiāo", "峧":"jiāo", "浇":"jiāo", "娇":"jiāo", "姣":"jiāo", "骄":"jiāo", "胶":"jiāo", "教":"jiāo", "䴔":"jiāo", "椒":"jiāo", "蛟":"jiāo", "焦":"jiāo", "跤":"jiāo", "僬":"jiāo", "鲛":"jiāo", "蕉":"jiāo", "燋":"jiāo", "礁":"jiāo", "鹪":"jiāo",
        "矫":"jiáo", "嚼":"jiáo","角":"jiǎo", "侥":"jiǎo", "佼":"jiǎo", "狡":"jiǎo", "饺":"jiǎo", "恔":"jiǎo", "绞":"jiǎo", "铰":"jiǎo", "矫":"jiǎo", "皎":"jiǎo", "脚":"jiǎo", "搅":"jiǎo", "湫":"jiǎo", "敫":"jiǎo", "剿":"jiǎo", "缴":"jiǎo", "璬":"jiǎo", "皦":"jiǎo",
        "叫":"jiào", "峤":"jiào", "觉":"jiào", "校":"jiào", "轿":"jiào", "较":"jiào", "教":"jiào", "窖":"jiào", "滘":"jiào", "斠":"jiào", "酵":"jiào", "漖":"jiào", "噍":"jiào", "徼":"jiào", "藠":"jiào", "醮":"jiào", "嚼":"jiào", "皭":"jiào",
        "节":"jiē", "阶":"jiē", "疖":"jiē", "皆":"jiē", "结":"jiē", "接":"jiē", "秸":"jiē", "揭":"jiē", "喈":"jiē", "嗟":"jiē", "街":"jiē", "湝":"jiē", "楷":"jiē",
        "孑":"jié", "节":"jié", "讦":"jié", "劫":"jié", "岊":"jié", "劼":"jié", "杰":"jié", "诘":"jié", "㛃":"jié", "拮":"jié", "洁":"jié", "结":"jié", "桔":"jié", "桀":"jié", "捷":"jié", "婕":"jié", "絜":"jié", "颉":"jié", "睫":"jié", "蜐":"jié", "截":"jié", "碣":"jié", "鲒":"jié", "竭":"jié", "羯":"jié",
        "姐":"jiě", "解":"jiě", "檞":"jiě","介":"jiè", "戒":"jiè", "芥":"jiè", "玠":"jiè", "届":"jiè", "界":"jiè", "疥":"jiè", "诫":"jiè", "蚧":"jiè", "借":"jiè", "悈":"jiè", "骱":"jiè", "解":"jiè", "褯":"jiè", "藉":"jiè",
        "价":"jie","巾":"jīn", "斤":"jīn", "今":"jīn", "金":"jīn", "𬬱":"jīn", "津":"jīn", "衿":"jīn", "矜":"jīn", "珒":"jīn", "筋":"jīn", "禁":"jīn", "襟":"jīn",
        "仅":"jǐn", "尽":"jǐn", "卺":"jǐn", "紧":"jǐn", "堇":"jǐn", "锦":"jǐn", "谨":"jǐn", "馑":"jǐn", "廑":"jǐn", "瑾":"jǐn", "槿":"jǐn",
        "尽":"jìn", "进":"jìn", "近":"jìn", "妗":"jìn", "劲":"jìn", "荩":"jìn", "浕":"jìn", "晋":"jìn", "赆":"jìn", "烬":"jìn", "浸":"jìn", "琎":"jìn", "祲":"jìn", "靳":"jìn", "禁":"jìn", "溍":"jìn", "缙":"jìn", "瑨":"jìn", "墐":"jìn", "觐":"jìn", "殣":"jìn", "噤":"jìn",
        "茎":"jīng", "京":"jīng", "泾":"jīng", "经":"jīng", "荆":"jīng", "菁":"jīng", "猄":"jīng", "旌":"jīng", "惊":"jīng", "晶":"jīng", "腈":"jīng", "䴖":"jīng", "睛":"jīng", "粳":"jīng", "兢":"jīng", "精":"jīng", "鲸":"jīng", "麖":"jīng", "鼱":"jīng",
        "井":"jǐng", "阱":"jǐng", "汫":"jǐng", "刭":"jǐng", "肼":"jǐng", "颈":"jǐng", "景":"jǐng", "儆":"jǐng", "憬":"jǐng", "璥":"jǐng", "璟":"jǐng", "警":"jǐng",
        "劲":"jìng", "径":"jìng", "净":"jìng", "迳":"jìng", "经":"jìng", "胫":"jìng", "倞":"jìng", "痉":"jìng", "竞":"jìng", "竟":"jìng", "竫":"jìng", "婧":"jìng", "靓":"jìng", "敬":"jìng", "靖":"jìng", "静":"jìng", "境":"jìng", "獍":"jìng", "镜":"jìng",
        "坰":"jiōng", "𬳶":"jiōng", "扃":"jiōng","冏":"jiǒng", "炅":"jiǒng", "迥":"jiǒng", "泂":"jiǒng", "䌹":"jiǒng", "炯":"jiǒng", "颎":"jiǒng", "窘":"jiǒng",
        "纠":"jiū", "鸠":"jiū", "究":"jiū", "赳":"jiū", "阄":"jiū", "揪":"jiū", "啾":"jiū", "鬏":"jiū",
        "九":"jiǔ", "久":"jiǔ", "氿":"jiǔ", "玖":"jiǔ", "灸":"jiǔ", "韭":"jiǔ", "酒":"jiǔ",
        "旧":"jiù", "臼":"jiù", "咎":"jiù", "疚":"jiù", "柩":"jiù", "桕":"jiù", "救":"jiù", "厩":"jiù", "就":"jiù", "舅":"jiù", "僦":"jiù", "㠇":"jiù", "鹫":"jiù",
        "车":"jū", "拘":"jū", "苴":"jū", "岨":"jū", "狙":"jū", "泃":"jū", "居":"jū", "驹":"jū", "砠":"jū", "俱":"jū", "疽":"jū", "掬":"jū", "据":"jū", "崌":"jū", "娵":"jū", "琚":"jū", "趄":"jū", "椐":"jū", "锔":"jū", "腒":"jū", "雎":"jū", "𬶋":"jū", "裾":"jū", "鞠":"jū", "鞫":"jū",
        "局":"jú", "菊":"jú", "焗":"jú", "锔":"jú", "䴗":"jú", "橘":"jú",
        "弆":"jǔ", "柜":"jǔ", "咀":"jǔ", "沮":"jǔ", "莒":"jǔ", "枸":"jǔ", "矩":"jǔ", "举":"jǔ", "筥":"jǔ", "蒟":"jǔ", "榉":"jǔ", "龃":"jǔ", "踽":"jǔ",
        "巨":"jù", "句":"jù", "讵":"jù", "拒":"jù", "苣":"jù", "岠":"jù", "具":"jù", "炬":"jù", "钜":"jù", "秬":"jù", "俱":"jù", "倨":"jù", "剧":"jù", "据":"jù", "距":"jù", "惧":"jù", "犋":"jù", "飓":"jù", "锯":"jù", "聚":"jù", "窭":"jù", "踞":"jù", "屦":"jù", "遽":"jù", "澽":"jù", "醵":"jù",
        "捐":"juān", "涓":"juān", "娟":"juān", "圈":"juān", "焆":"juān", "鹃":"juān", "镌":"juān", "蠲":"juān",
        "卷":"juǎn", "锩":"juǎn","卷":"juàn", "隽":"juàn", "倦":"juàn", "狷":"juàn", "桊":"juàn", "绢":"juàn", "鄄":"juàn", "圈":"juàn", "眷":"juàn",
        "撅":"juē", "噘":"juē","孓":"jué", "决":"jué", "诀":"jué", "抉":"jué", "角":"jué", "𫘝":"jué", "玦":"jué", "珏":"jué", "砄":"jué", "觉":"jué", "绝":"jué", "倔":"jué", "掘":"jué", "桷":"jué", "崛":"jué", "觖":"jué", "厥":"jué", "傕":"jué", "劂":"jué", "谲":"jué", "蕨":"jué", "獗":"jué", "㵐":"jué", "橛":"jué", "镢":"jué", "𫔎":"jué", "爵":"jué", "蹶":"jué", "矍":"jué", "嚼":"jué", "爝":"jué", "攫":"jué", "玃":"jué",
        "蹶":"juě","倔":"juè","军":"jūn", "均":"jūn", "龟":"jūn", "君":"jūn", "钧":"jūn", "莙":"jūn", "菌":"jūn", "皲":"jūn", "筠":"jūn", "鲪":"jūn", "麇":"jūn",
        "俊":"jùn", "郡":"jùn", "捃":"jùn", "峻":"jùn", "浚":"jùn", "骏":"jùn", "珺":"jùn", "菌":"jùn", "晙":"jùn", "焌":"jùn", "葰":"jùn", "畯":"jùn", "䐃":"jùn", "竣":"jùn",
        "咔":"kā", "咖":"kā", "喀":"kā","卡":"kǎ", "咔":"kǎ", "咯":"kǎ", "胩":"kǎ","开":"kāi", "揩":"kāi", "锎":"kāi",
        "剀":"kǎi", "凯":"kǎi", "垲":"kǎi", "闿":"kǎi", "恺":"kǎi", "铠":"kǎi", "蒈":"kǎi", "慨":"kǎi", "楷":"kǎi", "锴":"kǎi",
        "忾":"kài", "炌":"kài","刊":"kān", "看":"kān", "勘":"kān", "龛":"kān", "堪":"kān", "嵁":"kān", "戡":"kān",
        "坎":"kǎn", "侃":"kǎn", "砍":"kǎn", "莰":"kǎn", "槛":"kǎn","看":"kàn", "衎":"kàn", "崁":"kàn", "墈":"kàn", "阚":"kàn", "磡":"kàn", "瞰":"kàn",
        "康":"kāng", "𡐓":"kāng", "慷":"kāng", "糠":"kāng", "𩾌":"kāng","扛":"káng",
        "亢":"kàng", "伉":"kàng", "抗":"kàng", "闶":"kàng", "炕":"kàng", "钪":"kàng","尻":"kāo",
        "考":"kǎo", "拷":"kǎo", "洘":"kǎo", "栲":"kǎo", "烤":"kǎo","铐":"kào", "犒":"kào", "靠":"kào", "㸆":"kào",
        "坷":"kē", "苛":"kē", "匼":"kē", "珂":"kē", "柯":"kē", "轲":"kē", "科":"kē", "牁":"kē", "疴":"kē", "棵":"kē", "颏":"kē", "嗑":"kē", "稞":"kē", "窠":"kē", "颗":"kē", "磕":"kē", "瞌":"kē", "蝌":"kē", "髁":"kē",
        "壳":"ké", "咳":"ké", "颏":"ké","可":"kě", "坷":"kě", "岢":"kě", "炣":"kě", "渴":"kě",
        "可":"kè", "克":"kè", "刻":"kè", "恪":"kè", "客":"kè", "课":"kè", "氪":"kè", "骒":"kè", "缂":"kè", "嗑":"kè", "锞":"kè", "溘":"kè",
        "剋":"kēi","肯":"kěn", "垦":"kěn", "恳":"kěn", "啃":"kěn","裉":"kèn","坑":"kēng", "吭":"kēng", "硁":"kēng", "铿":"kēng",
        "空":"kōng", "埪":"kōng", "崆":"kōng", "箜":"kōng","孔":"kǒng", "恐":"kǒng", "倥":"kǒng",
        "空":"kòng", "控":"kòng", "硿":"kòng","抠":"kōu", "芤":"kōu", "𫸩":"kōu", "眍":"kōu","口":"kǒu",
        "叩":"kòu", "扣":"kòu", "寇":"kòu", "筘":"kòu", "蔻":"kòu","矻":"kū", "刳":"kū", "枯":"kū", "哭":"kū", "圐":"kū", "窟":"kū", "骷":"kū","苦":"kǔ",
        "库":"kù", "绔":"kù", "喾":"kù", "裤":"kù", "酷":"kù","夸":"kuā", "姱":"kuā","侉":"kuǎ", "垮":"kuǎ",
        "挎":"kuà", "胯":"kuà", "跨":"kuà","㧟":"kuǎi", "蒯":"kuǎi",
        "会":"kuài", "块":"kuài", "快":"kuài", "侩":"kuài", "郐":"kuài", "哙":"kuài", "狯":"kuài", "脍":"kuài", "筷":"kuài", "鲙":"kuài",
        "宽":"kuān", "髋":"kuān","款":"kuǎn","匡":"kuāng", "诓":"kuāng", "哐":"kuāng", "洭":"kuāng", "筐":"kuāng",
        "狂":"kuáng", "诳":"kuáng", "𫛭":"kuáng","夼":"kuǎng",
        "邝":"kuàng", "圹":"kuàng", "纩":"kuàng", "旷":"kuàng", "况":"kuàng", "矿":"kuàng", "贶":"kuàng", "框":"kuàng", "眶":"kuàng",
        "亏":"kuī", "岿":"kuī", "悝":"kuī", "盔":"kuī", "窥":"kuī",
        "奎":"kuí", "逵":"kuí", "馗":"kuí", "揆":"kuí", "葵":"kuí", "喹":"kuí", "骙":"kuí", "暌":"kuí", "魁":"kuí", "戣":"kuí", "睽":"kuí", "蝰":"kuí", "櫆":"kuí", "夔":"kuí",
        "𫠆":"kuǐ", "傀":"kuǐ", "跬":"kuǐ", "煃":"kuǐ","匮":"kuì", "蒉":"kuì", "喟":"kuì", "馈":"kuì", "溃":"kuì", "愦":"kuì", "愧":"kuì", "聩":"kuì", "篑":"kuì",
        "坤":"kūn", "昆":"kūn", "堃":"kūn", "裈":"kūn", "婫":"kūn", "琨":"kūn", "焜":"kūn", "髡":"kūn", "鹍":"kūn", "锟":"kūn", "醌":"kūn", "鲲":"kūn",
        "捆":"kǔn", "阃":"kǔn", "悃":"kǔn", "壸":"kǔn","困":"kùn","扩":"kuò", "括":"kuò", "蛞":"kuò", "阔":"kuò", "廓":"kuò",
        "垃":"lā", "拉":"lā", "啦":"lā", "邋":"lā","旯":"lá", "拉":"lá", "砬":"lá","喇":"lǎ",
        "剌":"là", "落":"là", "腊":"là", "蜡":"là", "瘌":"là", "辣":"là", "蝲":"là", "𬶟":"là", "镴":"là","啦":"la", "鞡":"la",
        "来":"lái", "俫":"lái", "莱":"lái", "崃":"lái", "徕":"lái", "涞":"lái", "梾":"lái", "铼":"lái",
        "赉":"lài", "睐":"lài", "赖":"lài", "濑":"lài", "癞":"lài", "籁":"lài",
        "兰":"lán", "岚":"lán", "拦":"lán", "栏":"lán", "婪":"lán", "阑":"lán", "蓝":"lán", "𬒗":"lán", "谰":"lán", "澜":"lán", "褴":"lán", "篮":"lán", "斓":"lán", "镧":"lán", "襕":"lán",
        "览":"lǎn", "揽":"lǎn", "缆":"lǎn", "榄":"lǎn", "罱":"lǎn", "漤":"lǎn", "懒":"lǎn","烂":"làn", "滥":"làn","啷":"lāng",
        "郎":"láng", "狼":"láng", "琅":"láng", "桹":"láng", "廊":"láng", "榔":"láng", "锒":"láng", "稂":"láng", "筤":"láng", "螂":"láng",
        "朗":"lǎng", "烺":"lǎng", "蓢":"lǎng", "塱":"lǎng", "㮾":"lǎng","郎":"làng", "埌":"làng", "莨":"làng", "崀":"làng", "阆":"làng", "浪":"làng", "㫰":"làng", "蒗":"làng",
        "捞":"lāo","劳":"láo", "牢":"láo", "𫭼":"láo", "唠":"láo", "崂":"láo", "铹":"láo", "痨":"láo", "醪":"láo",
        "老":"lǎo", "佬":"lǎo", "荖":"lǎo", "姥":"lǎo", "栳":"lǎo", "铑":"lǎo",
        "络":"lào", "唠":"lào", "烙":"lào", "涝":"lào", "落":"lào", "耢":"lào", "酪":"lào", "嫪":"lào",
        "仂":"lè", "叻":"lè", "乐":"lè", "泐":"lè", "勒":"lè", "簕":"lè", "鳓":"lè","了":"le", "饹":"le","勒":"lēi",
        "累":"léi", "雷":"léi", "嫘":"léi", "缧":"léi", "擂":"léi", "檑":"léi", "礌":"léi", "镭":"léi", "羸":"léi", "罍":"léi",
        "耒":"lěi", "诔":"lěi", "垒":"lěi", "累":"lěi", "磊":"lěi", "蕾":"lěi", "儡":"lěi", "藟":"lěi", "癗":"lěi",
        "肋":"lèi", "泪":"lèi", "类":"lèi", "累":"lèi", "酹":"lèi", "擂":"lèi","嘞":"lei","棱":"lēng",
        "崚":"léng", "塄":"léng", "棱":"léng", "楞":"léng","冷":"lěng","堎":"lèng", "愣":"lèng","哩":"lī",
        "丽":"lí", "厘":"lí", "狸":"lí", "离":"lí", "骊":"lí", "梨":"lí", "犁":"lí", "鹂":"lí", "喱":"lí", "蓠":"lí", "蜊":"lí", "漓":"lí", "缡":"lí", "璃":"lí", "嫠":"lí", "黎":"lí", "鲡":"lí", "罹":"lí", "篱":"lí", "醨":"lí", "藜":"lí", "㰀":"lí", "黧":"lí", "蠡":"lí",
        "礼":"lǐ", "李":"lǐ", "里":"lǐ", "俚":"lǐ", "逦":"lǐ", "浬":"lǐ", "娌":"lǐ", "理":"lǐ", "锂":"lǐ", "鲤":"lǐ", "澧":"lǐ", "醴":"lǐ", "鳢":"lǐ", "蠡":"lǐ",
        "力":"lì", "历":"lì", "厉":"lì", "立":"lì", "朸":"lì", "吏":"lì", "坜":"lì", "苈":"lì", "丽":"lì", "励":"lì", "呖":"lì", "𫵷":"lì", "利":"lì", "沥":"lì", "枥":"lì", "例":"lì", "疠":"lì", "戾":"lì", "隶":"lì", "𬍛":"lì", "荔":"lì", "栎":"lì", "郦":"lì", "轹":"lì", "俪":"lì", "俐":"lì", "疬":"lì", "珕":"lì", "莉":"lì", "莅":"lì", "鬲":"lì", "栗":"lì", "砺":"lì", "砾":"lì", "猁":"lì", "浰":"lì", "蛎":"lì", "唳":"lì", "笠":"lì", "粝":"lì", "粒":"lì", "雳":"lì", "跞":"lì", "詈":"lì", "傈":"lì", "凓":"lì", "痢":"lì", "溧":"lì", "篥":"lì",
        "哩":"li","俩":"liǎ","奁":"lián", "连":"lián", "怜":"lián", "帘":"lián", "莲":"lián", "涟":"lián", "梿":"lián", "联":"lián", "裢":"lián", "廉":"lián", "鲢":"lián", "濂":"lián", "镰":"lián", "蠊":"lián",
        "琏":"liǎn", "敛":"liǎn", "脸":"liǎn", "裣":"liǎn", "蔹":"liǎn",
        "练":"liàn", "炼":"liàn", "恋":"liàn", "浰":"liàn", "殓":"liàn", "链":"liàn", "瑓":"liàn", "楝":"liàn", "潋":"liàn", "𬶠":"liàn",
        "良":"liáng", "俍":"liáng", "莨":"liáng", "凉":"liáng", "梁":"liáng", "𫟅":"liáng", "椋":"liáng", "辌":"liáng", "量":"liáng", "粮":"liáng", "粱":"liáng", "墚":"liáng",
        "两":"liǎng", "俩":"liǎng", "𬜯":"liǎng", "魉":"liǎng",
        "亮":"liàng", "凉":"liàng", "悢":"liàng", "谅":"liàng", "辆":"liàng", "靓":"liàng", "量":"liàng", "晾":"liàng", "踉":"liàng",
        "撩":"liāo", "蹽":"liāo","辽":"liáo", "疗":"liáo", "聊":"liáo", "僚":"liáo", "漻":"liáo", "寥":"liáo", "撩":"liáo", "嘹":"liáo", "獠":"liáo", "潦":"liáo", "寮":"liáo", "嫽":"liáo", "缭":"liáo", "橑":"liáo", "燎":"liáo", "鹩":"liáo", "簝":"liáo", "髎":"liáo",
        "了":"liǎo", "钌":"liǎo", "蓼":"liǎo", "憭":"liǎo", "燎":"liǎo",
        "尥":"liào", "钌":"liào", "料":"liào", "撂":"liào", "𪤗":"liào", "廖":"liào", "瞭":"liào", "镣":"liào","咧":"liē","咧":"liě",
        "列":"liè", "劣":"liè", "冽":"liè", "峛":"liè", "洌":"liè", "埒":"liè", "烈":"liè", "捩":"liè", "䴕":"liè", "脟":"liè", "猎":"liè", "裂":"liè", "趔":"liè", "躐":"liè", "𫚭":"liè", "鬣":"liè",
        "拎":"līn","邻":"lín", "林":"lín", "临":"lín", "啉":"lín", "淋":"lín", "琳":"lín", "箖":"lín", "粼":"lín", "嶙":"lín", "遴":"lín", "潾":"lín", "𬴊":"lín", "璘":"lín", "霖":"lín", "辚":"lín", "磷":"lín", "瞵":"lín", "𬭸":"lín", "翷":"lín", "鳞":"lín", "麟":"lín",
        "凛":"lǐn", "廪":"lǐn", "懔":"lǐn", "檩":"lǐn","吝":"lìn", "赁":"lìn", "淋":"lìn", "蔺":"lìn", "膦":"lìn", "躏":"lìn",
        "令":"líng", "伶":"líng", "灵":"líng", "坽":"líng", "苓":"líng", "囹":"líng", "泠":"líng", "姈":"líng", "玲":"líng", "柃":"líng", "昤":"líng", "瓴":"líng", "铃":"líng", "鸰":"líng", "凌":"líng", "陵":"líng", "聆":"líng", "菱":"líng", "棂":"líng", "蛉":"líng", "舲":"líng", "翎":"líng", "羚":"líng", "㥄":"líng", "绫":"líng", "棱":"líng", "祾":"líng", "零":"líng", "龄":"líng", "鲮":"líng", "澪":"líng", "酃":"líng",
        "令":"lǐng", "岭":"lǐng", "领":"lǐng","另":"lìng", "令":"lìng", "呤":"lìng","溜":"liū", "熘":"liū",
        "刘":"liú", "浏":"liú", "留":"liú", "流":"liú", "琉":"liú", "硫":"liú", "馏":"liú", "旒":"liú", "骝":"liú", "榴":"liú", "飗":"liú", "镏":"liú", "鹠":"liú", "瘤":"liú", "瑬":"liú", "疁":"liú", "镠":"liú", "鎏":"liú",
        "珋":"liǔ", "柳":"liǔ", "绺":"liǔ", "锍":"liǔ", "罶":"liǔ","六":"liù", "陆":"liù", "碌":"liù", "遛":"liù", "馏":"liù", "溜":"liù", "镏":"liù", "鹨":"liù",
        "咯":"lo","龙":"lóng", "茏":"lóng", "咙":"lóng", "泷":"lóng", "珑":"lóng", "栊":"lóng", "昽":"lóng", "胧":"lóng", "砻":"lóng", "眬":"lóng", "聋":"lóng", "笼":"lóng", "隆":"lóng", "漋":"lóng", "癃":"lóng", "窿":"lóng",
        "陇":"lǒng", "拢":"lǒng", "垄":"lǒng", "笼":"lǒng", "𬕂":"lǒng","弄":"lòng", "哢":"lòng","搂":"lōu", "䁖":"lōu",
        "剅":"lóu", "娄":"lóu", "偻":"lóu", "𪣻":"lóu", "蒌":"lóu", "喽":"lóu", "溇":"lóu", "楼":"lóu", "𦝼":"lóu", "耧":"lóu", "蝼":"lóu", "髅":"lóu",
        "搂":"lǒu", "嵝":"lǒu", "篓":"lǒu","陋":"lòu", "镂":"lòu", "瘘":"lòu", "漏":"lòu", "露":"lòu","喽":"lou","撸":"lū", "噜":"lū",
        "卢":"lú", "芦":"lú", "庐":"lú", "垆":"lú", "炉":"lú", "泸":"lú", "栌":"lú", "轳":"lú", "胪":"lú", "鸬":"lú", "𬬻":"lú", "颅":"lú", "舻":"lú", "鲈":"lú",
        "芦":"lǔ", "卤":"lǔ", "虏":"lǔ", "掳":"lǔ", "鲁":"lǔ", "澛":"lǔ", "橹":"lǔ", "镥":"lǔ",
        "甪":"lù", "陆":"lù", "录":"lù", "辂":"lù", "赂":"lù", "菉":"lù", "鹿":"lù", "渌":"lù", "逯":"lù", "𫘧":"lù", "绿":"lù", "琭":"lù", "禄":"lù", "碌":"lù", "路":"lù", "稑":"lù", "僇":"lù", "勠":"lù", "箓":"lù", "漉":"lù", "辘":"lù", "戮":"lù", "蕗":"lù", "潞":"lù", "璐":"lù", "簏":"lù", "鹭":"lù", "麓":"lù", "露":"lù",
        "氇":"lu","驴":"lǘ", "闾":"lǘ", "榈":"lǘ", "𦝼":"lǘ",
        "吕":"lǚ", "侣":"lǚ", "捋":"lǚ", "梠":"lǚ", "旅":"lǚ", "铝":"lǚ", "稆":"lǚ", "偻":"lǚ", "屡":"lǚ", "缕":"lǚ", "膂":"lǚ", "褛":"lǚ", "履":"lǚ",
        "垏":"lǜ", "律":"lǜ", "虑":"lǜ", "率":"lǜ", "绿":"lǜ", "葎":"lǜ", "氯":"lǜ", "滤":"lǜ",
        "峦":"luán", "孪":"luán", "娈":"luán", "栾":"luán", "挛":"luán", "鸾":"luán", "脔":"luán", "滦":"luán", "銮":"luán",
        "卵":"luǎn","乱":"luàn","䂮":"lüè", "掠":"lüè", "略":"lüè", "锊":"lüè", "圙":"lüè","抡":"lūn",
        "仑":"lún", "伦":"lún", "论":"lún", "囵":"lún", "沦":"lún", "纶":"lún", "轮":"lún", "𬬭":"lún",
        "𫭢":"lǔn","论":"lùn","捋":"luō", "啰":"luō","罗":"luó", "萝":"luó", "啰":"luó", "逻":"luó", "脶":"luó", "猡":"luó", "椤":"luó", "锣":"luó", "箩":"luó", "骡":"luó", "螺":"luó",
        "倮":"luǒ", "蓏":"luǒ", "裸":"luǒ", "瘰":"luǒ", "蠃":"luǒ",
        "泺":"luò", "荦":"luò", "咯":"luò", "洛":"luò", "骆":"luò", "络":"luò", "珞":"luò", "烙":"luò", "落":"luò", "摞":"luò", "雒":"luò", "漯":"luò",
        "啰":"luo","呒":"ḿ", "呣":"ḿ","呣":"m̀","妈":"mā", "抹":"mā", "摩":"mā","吗":"má", "麻":"má", "蟆":"má",
        "马":"mǎ", "吗":"mǎ", "犸":"mǎ", "玛":"mǎ", "码":"mǎ", "蚂":"mǎ","杩":"mà", "祃":"mà", "蚂":"mà", "骂":"mà",
        "吗":"ma", "嘛":"ma","埋":"mái", "霾":"mái","买":"mǎi", "荬":"mǎi",
        "劢":"mài", "迈":"mài", "麦":"mài", "卖":"mài", "脉":"mài", "唛":"mài", "鿏":"mài","嫚":"mān", "颟":"mān",
        "埋":"mán", "蛮":"mán", "蔓":"mán", "馒":"mán", "瞒":"mán", "鞔":"mán", "鳗":"mán", "鬘":"mán","满":"mǎn", "螨":"mǎn",
        "𬜬":"màn", "曼":"màn", "谩":"màn", "墁":"màn", "蔓":"màn", "幔":"màn", "漫":"màn", "慢":"màn", "嫚":"màn", "缦":"màn", "镘":"màn",
        "牤":"māng","邙":"máng", "芒":"máng", "忙":"máng", "杧":"máng", "尨":"máng", "盲":"máng", "氓":"máng", "茫":"máng", "厖":"máng", "硭":"máng", "牻":"máng",
        "莽":"mǎng", "漭":"mǎng", "蟒":"mǎng","猫":"māo","毛":"máo", "矛":"máo", "茆":"máo", "茅":"máo", "牦":"máo", "旄":"máo", "锚":"máo", "髦":"máo", "蝥":"máo", "蟊":"máo",
        "卯":"mǎo", "峁":"mǎo", "泖":"mǎo", "昴":"mǎo", "铆":"mǎo",
        "芼":"mào", "茂":"mào", "眊":"mào", "冒":"mào", "贸":"mào", "耄":"mào", "袤":"mào", "鄚":"mào", "帽":"mào", "瑁":"mào", "楙":"mào", "貌":"mào", "瞀":"mào", "懋":"mào",
        "么":"me","没":"méi", "玫":"méi", "枚":"méi", "眉":"méi", "莓":"méi", "梅":"méi", "郿":"méi", "嵋":"méi", "湄":"méi", "媒":"méi", "瑂":"méi", "楣":"méi", "煤":"méi", "酶":"méi", "镅":"méi", "鹛":"méi", "霉":"méi", "糜":"méi",
        "每":"měi", "美":"měi", "浼":"měi", "渼":"měi", "媄":"měi", "镁":"měi","妹":"mèi", "昧":"mèi", "袂":"mèi", "寐":"mèi", "媚":"mèi", "魅":"mèi","闷":"mēn",
        "门":"mén", "们":"mén", "扪":"mén", "钔":"mén", "𫞩":"mén","呇":"mèn", "闷":"mèn", "焖":"mèn", "懑":"mèn","们":"men","蒙":"mēng",
        "虻":"méng", "𫑡":"méng", "萌":"méng", "蒙":"méng", "盟":"méng", "甍":"méng", "瞢":"méng", "㠓":"méng", "幪":"méng", "檬":"méng", "朦":"méng", "鹲":"méng", "礞":"méng", "艨":"méng",
        "勐":"měng", "猛":"měng", "蒙":"měng", "锰":"měng", "蜢":"měng", "艋":"měng", "獴":"měng", "懵":"měng", "蠓":"měng",
        "孟":"mèng", "梦":"mèng","咪":"mī", "眯":"mī","弥":"mí", "迷":"mí", "祢":"mí", "眯":"mí", "猕":"mí", "谜":"mí", "醚":"mí", "糜":"mí", "縻":"mí", "麋":"mí", "靡":"mí", "蘼":"mí", "醾":"mí",
        "米":"mǐ", "芈":"mǐ", "咪":"mǐ", "洣":"mǐ", "弭":"mǐ", "脒":"mǐ", "敉":"mǐ", "靡":"mǐ",
        "汨":"mì", "觅":"mì", "泌":"mì", "宓":"mì", "祕":"mì", "秘":"mì", "密":"mì", "幂":"mì", "谧":"mì", "蓂":"mì", "嘧":"mì", "蜜":"mì",
        "眠":"mián", "绵":"mián", "棉":"mián","丏":"miǎn", "免":"miǎn", "沔":"miǎn", "勉":"miǎn", "娩":"miǎn", "勔":"miǎn", "冕":"miǎn", "偭":"miǎn", "渑":"miǎn", "湎":"miǎn", "愐":"miǎn", "缅":"miǎn", "腼":"miǎn", "𩾃":"miǎn",
        "面":"miàn", "眄":"miàn","喵":"miāo","苗":"miáo", "描":"miáo", "鹋":"miáo", "瞄":"miáo",
        "杪":"miǎo", "眇":"miǎo", "秒":"miǎo", "淼":"miǎo", "渺":"miǎo", "缈":"miǎo", "藐":"miǎo", "邈":"miǎo",
        "妙":"miào", "庙":"miào", "缪":"miào","乜":"miē", "咩":"miē","灭":"miè", "蔑":"miè", "篾":"miè",
        "民":"mín", "苠":"mín", "旻":"mín", "岷":"mín", "忞":"mín", "珉":"mín", "缗":"mín",
        "皿":"mǐn", "闵":"mǐn", "抿":"mǐn", "黾":"mǐn", "泯":"mǐn", "闽":"mǐn", "悯":"mǐn", "敏":"mǐn", "湣":"mǐn", "愍":"mǐn", "鳘":"mǐn",
        "名":"míng", "明":"míng", "鸣":"míng", "茗":"míng", "洺":"míng", "冥":"míng", "铭":"míng", "溟":"míng", "暝":"míng", "瞑":"míng", "螟":"míng",
        "酩":"mǐng","命":"mìng","谬":"miù", "缪":"miù","摸":"mō",
        "无":"mó", "谟":"mó", "馍":"mó", "嫫":"mó", "摹":"mó", "模":"mó", "膜":"mó", "麽":"mó", "摩":"mó", "磨":"mó", "嬷":"mó", "藦":"mó", "蘑":"mó", "魔":"mó",
        "抹":"mǒ","万":"mò", "末":"mò", "没":"mò", "抹":"mò", "茉":"mò", "殁":"mò", "沫":"mò", "陌":"mò", "脉":"mò", "莫":"mò", "秣":"mò", "蓦":"mò", "貊":"mò", "漠":"mò", "寞":"mò", "靺":"mò", "墨":"mò", "镆":"mò", "瘼":"mò", "默":"mò", "磨":"mò", "貘":"mò", "𬙊":"mò", "耱":"mò",
        "哞":"mōu","牟":"móu", "侔":"móu", "眸":"móu", "谋":"móu", "蛑":"móu", "缪":"móu", "鍪":"móu",
        "某":"mǒu","毪":"mú", "模":"mú","母":"mǔ", "牡":"mǔ", "亩":"mǔ", "拇":"mǔ", "姆":"mǔ", "𬭁":"mǔ", "𧿹":"mǔ",
        "木":"mù", "目":"mù", "仫":"mù", "牟":"mù", "沐":"mù", "苜":"mù", "牧":"mù", "钼":"mù", "募":"mù", "墓":"mù", "幕":"mù", "睦":"mù", "慕":"mù", "暮":"mù", "穆":"mù",
        "那":"nā", "南":"nā","拿":"ná", "镎":"ná","乸":"nǎ", "哪":"nǎ","那":"nà", "呐":"nà", "纳":"nà", "肭":"nà", "𦰡":"nà", "钠":"nà", "衲":"nà", "娜":"nà", "捺":"nà",
        "哪":"na","乃":"nǎi", "艿":"nǎi", "奶":"nǎi", "氖":"nǎi", "迺":"nǎi","奈":"nài", "佴":"nài", "柰":"nài", "耐":"nài", "耏":"nài", "萘":"nài", "鼐":"nài",
        "囡":"nān","男":"nán", "南":"nán", "难":"nán", "萳":"nán", "喃":"nán", "楠":"nán","赧":"nǎn", "腩":"nǎn", "蝻":"nǎn",
        "难":"nàn", "婻":"nàn","囊":"nāng", "囔":"nāng","囊":"náng", "馕":"náng","曩":"nǎng", "攮":"nǎng", "馕":"nǎng",
        "齉":"nàng","孬":"nāo","呶":"náo", "挠":"náo", "峱":"náo", "硇":"náo", "铙":"náo", "蛲":"náo", "猱":"náo",
        "垴":"nǎo", "恼":"nǎo", "脑":"nǎo", "瑙":"nǎo","闹":"nào", "淖":"nào", "臑":"nào","哪":"né","讷":"nè","呢":"ne","馁":"něi","内":"nèi",
        "恁":"nèn", "嫩":"nèn","能":"néng","嗯":"ńg","嗯":"ňg","嗯":"ǹg","妮":"nī",
        "尼":"ní", "伲":"ní", "坭":"ní", "呢":"ní", "泥":"ní", "怩":"ní", "铌":"ní", "倪":"ní", "猊":"ní", "𫐐":"ní", "霓":"ní", "𫠜":"ní", "鲵":"ní", "麑":"ní",
        "拟":"nǐ", "你":"nǐ", "旎":"nǐ", "薿":"nǐ","泥":"nì", "昵":"nì", "逆":"nì", "匿":"nì", "𨺙":"nì", "睨":"nì", "腻":"nì", "溺":"nì","拈":"niān", "蔫":"niān",
        "年":"nián", "粘":"nián", "鲇":"nián", "黏":"nián","捻":"niǎn", "辇":"niǎn", "撵":"niǎn", "碾":"niǎn",
        "廿":"niàn", "念":"niàn", "埝":"niàn","娘":"niáng","酿":"niàng","鸟":"niǎo", "茑":"niǎo", "袅":"niǎo",
        "尿":"niào", "脲":"niào","捏":"niē","乜":"niè", "陧":"niè", "聂":"niè", "臬":"niè", "涅":"niè", "菍":"niè", "啮":"niè", "嗫":"niè", "嵲":"niè", "𫔶":"niè", "镊":"niè", "镍":"niè", "颞":"niè", "蹑":"niè", "孽":"niè", "蘖":"niè", "糵":"niè",
        "您":"nín","宁":"níng", "拧":"níng", "苧":"níng", "咛":"níng", "狞":"níng", "柠":"níng", "聍":"níng", "凝":"níng",
        "拧":"nǐng","宁":"nìng", "佞":"nìng", "拧":"nìng", "泞":"nìng", "甯":"nìng",
        "妞":"niū","牛":"niú","扭":"niǔ", "狃":"niǔ", "忸":"niǔ", "纽":"niǔ", "杻":"niǔ", "钮":"niǔ",
        "拗":"niù","农":"nóng", "侬":"nóng", "哝":"nóng", "浓":"nóng", "脓":"nóng", "秾":"nóng", "𬪩":"nóng",
        "弄":"nòng","耨":"nòu","奴":"nú", "孥":"nú", "驽":"nú", "笯":"nú","努":"nǔ", "弩":"nǔ", "砮":"nǔ", "胬":"nǔ",
        "怒":"nù", "傉":"nù","女":"nǚ", "钕":"nǚ","恧":"nǜ", "衄":"nǜ","暖":"nuǎn","疟":"nüè", "虐":"nüè",
        "挪":"nuó", "𦰡":"nuó", "娜":"nuó", "傩":"nuó","诺":"nuò", "喏":"nuò", "搦":"nuò", "锘":"nuò", "懦":"nuò", "糯":"nuò",
        "噢":"ō","哦":"ó","哦":"ò","区":"ōu", "讴":"ōu", "𫭟":"ōu", "瓯":"ōu", "欧":"ōu", "殴":"ōu", "鸥":"ōu",
        "𠙶":"ǒu", "呕":"ǒu", "𬉼":"ǒu", "偶":"ǒu", "耦":"ǒu", "藕":"ǒu","沤":"òu", "怄":"òu",
        "趴":"pā", "舥":"pā", "啪":"pā", "葩":"pā","扒":"pá", "杷":"pá", "爬":"pá", "耙":"pá", "琶":"pá", "筢":"pá", "潖":"pá",
        "帕":"pà", "怕":"pà","拍":"pāi","俳":"pái", "排":"pái", "徘":"pái", "牌":"pái", "簰":"pái",
        "迫":"pǎi", "排":"pǎi","哌":"pài", "派":"pài", "蒎":"pài", "湃":"pài",
        "番":"pān", "潘":"pān", "攀":"pān","爿":"pán", "胖":"pán", "盘":"pán", "槃":"pán", "磐":"pán", "磻":"pán", "蹒":"pán", "蟠":"pán",
        "判":"pàn", "泮":"pàn", "盼":"pàn", "叛":"pàn", "畔":"pàn", "袢":"pàn", "襻":"pàn",
        "乓":"pāng", "雱":"pāng", "滂":"pāng", "膀":"pāng","彷":"páng", "庞":"páng", "逄":"páng", "旁":"páng", "膀":"páng", "磅":"páng", "螃":"páng", "鳑":"páng",
        "耪":"pǎng","胖":"pàng","抛":"pāo", "泡":"pāo", "脬":"pāo",
        "刨":"páo", "咆":"páo", "狍":"páo", "庖":"páo", "炮":"páo", "袍":"páo", "匏":"páo", "跑":"páo",
        "跑":"pǎo","泡":"pào", "炮":"pào", "疱":"pào","呸":"pēi", "胚":"pēi", "衃":"pēi", "醅":"pēi",
        "陪":"péi", "培":"péi", "赔":"péi", "锫":"péi", "裴":"péi","沛":"pèi", "帔":"pèi", "佩":"pèi", "配":"pèi", "旆":"pèi", "辔":"pèi", "霈":"pèi",
        "喷":"pēn","盆":"pén", "湓":"pén","喷":"pèn","抨":"pēng", "怦":"pēng", "砰":"pēng", "烹":"pēng", "嘭":"pēng",
        "芃":"péng", "朋":"péng", "堋":"péng", "淜":"péng", "弸":"péng", "彭":"péng", "棚":"péng", "搒":"péng", "蓬":"péng", "硼":"péng", "鹏":"péng", "澎":"péng", "篷":"péng", "膨":"péng", "蟛":"péng",
        "捧":"pěng","椪":"pèng", "碰":"pèng","丕":"pī", "批":"pī", "邳":"pī", "伾":"pī", "纰":"pī", "坯":"pī", "披":"pī", "狉":"pī", "𬳵":"pī", "砒":"pī", "劈":"pī", "噼":"pī", "霹":"pī",
        "皮":"pí", "陂":"pí", "枇":"pí", "毗":"pí", "蚍":"pí", "铍":"pí", "郫":"pí", "疲":"pí", "陴":"pí", "啤":"pí", "琵":"pí", "脾":"pí", "鲏":"pí", "蜱":"pí", "罴":"pí", "貔":"pí", "鼙":"pí",
        "匹":"pǐ", "圮":"pǐ", "仳":"pǐ", "苉":"pǐ", "否":"pǐ", "痞":"pǐ", "劈":"pǐ", "癖":"pǐ", "嚭":"pǐ",
        "屁":"pì", "埤":"pì", "淠":"pì", "睥":"pì", "辟":"pì", "媲":"pì", "僻":"pì", "澼":"pì", "甓":"pì", "䴙":"pì", "譬":"pì",
        "片":"piān", "扁":"piān", "偏":"piān", "犏":"piān", "篇":"piān", "翩":"piān",
        "便":"pián", "骈":"pián", "胼":"pián", "㛹":"pián", "楩":"pián", "蹁":"pián","谝":"piǎn", "𡎚":"piǎn","片":"piàn", "骗":"piàn",
        "剽":"piāo", "漂":"piāo", "缥":"piāo", "飘":"piāo", "螵":"piāo","朴":"piáo", "嫖":"piáo", "瓢":"piáo", "薸":"piáo",
        "殍":"piǎo", "漂":"piǎo", "瞟":"piǎo","票":"piào", "蔈":"piào", "嘌":"piào", "漂":"piào", "骠":"piào",
        "氕":"piē", "撇":"piē", "瞥":"piē","苤":"piě", "撇":"piě", "𬭯":"piě","拼":"pīn", "姘":"pīn",
        "玭":"pín", "贫":"pín", "频":"pín", "嫔":"pín", "𬞟":"pín", "颦":"pín","品":"pǐn","牝":"pìn", "聘":"pìn",
        "乒":"pīng", "俜":"pīng", "涄":"pīng", "娉":"pīng",
        "平":"píng", "评":"píng", "坪":"píng", "苹":"píng", "凭":"píng", "泙":"píng", "玶":"píng", "荓":"píng", "枰":"píng", "帡":"píng", "洴":"píng", "屏":"píng", "瓶":"píng", "萍":"píng", "蚲":"píng", "鲆":"píng",
        "钋":"pō", "坡":"pō", "泊":"pō", "泼":"pō", "䥽":"pō", "颇":"pō", "酦":"pō","婆":"pó", "鄱":"pó", "繁":"pó", "皤":"pó",
        "叵":"pǒ", "钷":"pǒ", "笸":"pǒ","朴":"pò", "迫":"pò", "珀":"pò", "破":"pò", "粕":"pò", "魄":"pò","桲":"po",
        "剖":"pōu","抔":"póu", "掊":"póu", "裒":"póu","掊":"pǒu","仆":"pū", "扑":"pū", "铺":"pū", "噗":"pū", "潽":"pū",
        "仆":"pú", "匍":"pú", "莆":"pú", "菩":"pú", "脯":"pú", "葡":"pú", "蒱":"pú", "蒲":"pú", "酺":"pú", "墣":"pú", "璞":"pú", "镤":"pú", "穙":"pú", "濮":"pú",
        "朴":"pǔ", "埔":"pǔ", "圃":"pǔ", "浦":"pǔ", "普":"pǔ", "溥":"pǔ", "谱":"pǔ", "氆":"pǔ", "镨":"pǔ", "蹼":"pǔ",
        "铺":"pù", "堡":"pù", "瀑":"pù", "曝":"pù",
        "七":"qī", "沏":"qī", "妻":"qī", "柒":"qī", "栖":"qī", "桤":"qī", "郪":"qī", "凄":"qī", "萋":"qī", "戚":"qī", "期":"qī", "欺":"qī", "欹":"qī", "缉":"qī", "嘁":"qī", "漆":"qī", "蹊":"qī",
        "亓":"qí", "𨙸":"qí", "齐":"qí", "祁":"qí", "圻":"qí", "芪":"qí", "岐":"qí", "其":"qí", "奇":"qí", "𬨂":"qí", "歧":"qí", "祈":"qí", "祇":"qí", "荠":"qí", "俟":"qí", "耆":"qí", "颀":"qí", "脐":"qí", "埼":"qí", "萁":"qí", "䓫":"qí", "畦":"qí", "跂":"qí", "崎":"qí", "淇":"qí", "骐":"qí", "骑":"qí", "琪":"qí", "琦":"qí", "棋":"qí", "蛴":"qí", "祺":"qí", "锜":"qí", "愭":"qí", "綦":"qí", "蜞":"qí", "旗":"qí", "蕲":"qí", "鲯":"qí", "鳍":"qí", "麒":"qí",
        "乞":"qǐ", "芑":"qǐ", "屺":"qǐ", "岂":"qǐ", "企":"qǐ", "玘":"qǐ", "杞":"qǐ", "启":"qǐ", "起":"qǐ", "婍":"qǐ", "绮":"qǐ", "棨":"qǐ",
        "气":"qì", "讫":"qì", "迄":"qì", "汔":"qì", "弃":"qì", "汽":"qì", "泣":"qì", "亟":"qì", "契":"qì", "砌":"qì", "洓":"qì", "葺":"qì", "碛":"qì", "碶":"qì", "槭":"qì", "磜":"qì", "器":"qì", "憩":"qì",
        "掐":"qiā", "袷":"qiā", "葜":"qiā","拤":"qiá","卡":"qiǎ","洽":"qià", "恰":"qià", "髂":"qià",
        "千":"qiān", "仟":"qiān", "阡":"qiān", "圲":"qiān", "扦":"qiān", "芊":"qiān", "迁":"qiān", "杄":"qiān", "岍":"qiān", "佥":"qiān", "汧":"qiān", "钎":"qiān", "牵":"qiān", "铅":"qiān", "悭":"qiān", "谦":"qiān", "签":"qiān", "愆":"qiān", "鹐":"qiān", "骞":"qiān", "搴":"qiān", "磏":"qiān", "褰":"qiān",
        "荨":"qián", "钤":"qián", "前":"qián", "虔":"qián", "钱":"qián", "钳":"qián", "掮":"qián", "乾":"qián", "靬":"qián", "犍":"qián", "墘":"qián", "潜":"qián", "黔":"qián",
        "肷":"qiǎn", "浅":"qiǎn", "遣":"qiǎn", "谴":"qiǎn", "缱":"qiǎn",
        "欠":"qiàn", "伣":"qiàn", "纤":"qiàn", "芡":"qiàn", "茜":"qiàn", "倩":"qiàn", "堑":"qiàn", "𬘬":"qiàn", "椠":"qiàn", "嵌":"qiàn", "蒨":"qiàn", "慊":"qiàn", "歉":"qiàn",
        "抢":"qiāng", "呛":"qiāng", "羌":"qiāng", "玱":"qiāng", "枪":"qiāng", "戗":"qiāng", "戕":"qiāng", "腔":"qiāng", "蜣":"qiāng", "锖":"qiāng", "锵":"qiāng", "镪":"qiāng",
        "强":"qiáng", "墙":"qiáng", "蔷":"qiáng", "嫱":"qiáng", "蔃":"qiáng", "樯":"qiáng",
        "抢":"qiǎng", "羟":"qiǎng", "强":"qiǎng", "襁":"qiǎng","呛":"qiàng", "戗":"qiàng", "炝":"qiàng", "跄":"qiàng",
        "悄":"qiāo", "硗":"qiāo", "雀":"qiāo", "跷":"qiāo", "锹":"qiāo", "劁":"qiāo", "敲":"qiāo", "橇":"qiāo", "缲":"qiāo",
        "乔":"qiáo", "侨":"qiáo", "荞":"qiáo", "峤":"qiáo", "桥":"qiáo", "硚":"qiáo", "翘":"qiáo", "谯":"qiáo", "鞒":"qiáo", "憔":"qiáo", "樵":"qiáo", "瞧":"qiáo",
        "巧":"qiǎo", "悄":"qiǎo", "雀":"qiǎo", "愀":"qiǎo",
        "壳":"qiào", "俏":"qiào", "诮":"qiào", "峭":"qiào", "窍":"qiào", "翘":"qiào", "撬":"qiào", "鞘":"qiào",
        "切":"qiē","伽":"qié", "茄":"qié","且":"qiě","切":"qiè", "郄":"qiè", "妾":"qiè", "怯":"qiè", "窃":"qiè", "挈":"qiè", "惬":"qiè", "趄":"qiè", "慊":"qiè", "锲":"qiè", "箧":"qiè",
        "钦":"qīn", "侵":"qīn", "亲":"qīn", "衾":"qīn", "骎":"qīn", "嵚":"qīn",
        "芹":"qín", "芩":"qín", "秦":"qín", "梣":"qín", "琴":"qín", "覃":"qín", "禽":"qín", "勤":"qín", "嗪":"qín", "溱":"qín", "慬":"qín", "擒":"qín", "噙":"qín", "檎":"qín",
        "锓":"qǐn", "寝":"qǐn","吣":"qìn", "沁":"qìn", "揿":"qìn",
        "青":"qīng", "轻":"qīng", "氢":"qīng", "倾":"qīng", "卿":"qīng", "圊":"qīng", "清":"qīng", "蜻":"qīng", "鲭":"qīng",
        "勍":"qíng", "情":"qíng", "晴":"qíng", "氰":"qíng", "檠":"qíng", "擎":"qíng", "黥":"qíng",
        "苘":"qǐng", "顷":"qǐng", "请":"qǐng", "庼":"qǐng","庆":"qìng", "亲":"qìng", "碃":"qìng", "箐":"qìng", "綮":"qìng", "磬":"qìng", "罄":"qìng",
        "邛":"qióng", "穷":"qióng", "茕":"qióng", "穹":"qióng", "䓖":"qióng", "筇":"qióng", "琼":"qióng", "蛩":"qióng", "銎":"qióng",
        "丘":"qiū", "邱":"qiū", "龟":"qiū", "秋":"qiū", "蚯":"qiū", "萩":"qiū", "湫":"qiū", "楸":"qiū", "鹙":"qiū", "鳅":"qiū", "鞧":"qiū",
        "仇":"qiú", "囚":"qiú", "犰":"qiú", "求":"qiú", "虬":"qiú", "泅":"qiú", "俅":"qiú", "訄":"qiú", "酋":"qiú", "逑":"qiú", "球":"qiú", "赇":"qiú", "𨱇":"qiú", "遒":"qiú", "巯":"qiú", "裘":"qiú", "璆":"qiú", "蝤":"qiú", "鼽":"qiú",
        "糗":"qiǔ","区":"qū", "曲":"qū", "𫭟":"qū", "岖":"qū", "诎":"qū", "驱":"qū", "坥":"qū", "岨":"qū", "屈":"qū", "㭕":"qū", "𪨰":"qū", "胠":"qū", "祛":"qū", "袪":"qū", "䓛":"qū", "蛆":"qū", "躯":"qū", "焌":"qū", "趋":"qū", "蛐":"qū", "麹":"qū", "黢":"qū",
        "劬":"qú", "朐":"qú", "鸲":"qú", "渠":"qú", "蕖":"qú", "磲":"qú", "璩":"qú", "瞿":"qú", "鼩":"qú", "蘧":"qú", "灈":"qú", "氍":"qú", "癯":"qú", "衢":"qú", "蠼":"qú",
        "曲":"qǔ", "苣":"qǔ", "取":"qǔ", "竘":"qǔ", "娶":"qǔ", "龋":"qǔ",
        "去":"qù", "阒":"qù", "趣":"qù", "觑":"qù","戌":"qu","悛":"quān", "圈":"quān", "棬":"quān", "𨟠":"quān",
        "权":"quán", "全":"quán", "佺":"quán", "诠":"quán", "荃":"quán", "泉":"quán", "辁":"quán", "拳":"quán", "铨":"quán", "痊":"quán", "婘":"quán", "筌":"quán", "瑔":"quán", "蜷":"quán", "醛":"quán", "鳈":"quán", "鬈":"quán", "颧":"quán",
        "犬":"quǎn", "畎":"quǎn", "绻":"quǎn","劝":"quàn", "券":"quàn","炔":"quē", "缺":"quē", "阙":"quē","瘸":"qué",
        "却":"què", "埆":"què", "𬒈":"què", "悫":"què", "雀":"què", "确":"què", "阕":"què", "鹊":"què", "碏":"què", "阙":"què", "榷":"què",
        "囷":"qūn", "逡":"qūn","裙":"qún", "群":"qún", "麇":"qún","蚺":"rán", "然":"rán", "髯":"rán", "燃":"rán",
        "冉":"rǎn", "苒":"rǎn", "染":"rǎn", "䎃":"rǎn","嚷":"rāng","儴":"ráng", "蘘":"ráng", "瀼":"ráng", "禳":"ráng", "穰":"ráng", "瓤":"ráng","壤":"rǎng", "攘":"rǎng", "嚷":"rǎng",
        "让":"ràng", "瀼":"ràng","荛":"ráo", "饶":"ráo", "娆":"ráo", "桡":"ráo","扰":"rǎo","绕":"rào","惹":"rě","热":"rè",
        "人":"rén", "壬":"rén", "仁":"rén", "任":"rén","忍":"rěn", "荏":"rěn", "稔":"rěn",
        "刃":"rèn", "认":"rèn", "仞":"rèn", "讱":"rèn", "任":"rèn", "纫":"rèn", "韧":"rèn", "轫":"rèn", "饪":"rèn", "妊":"rèn", "纴":"rèn", "衽":"rèn", "葚":"rèn",
        "扔":"rēng","仍":"réng","日":"rì", "驲":"rì","戎":"róng", "茸":"róng", "荣":"róng", "狨":"róng", "绒":"róng", "容":"róng", "嵘":"róng", "蓉":"róng", "溶":"róng", "瑢":"róng", "榕":"róng", "熔":"róng", "蝾":"róng", "镕":"róng", "融":"róng",
        "冗":"rǒng","柔":"róu", "揉":"róu", "𫐓":"róu", "糅":"róu", "蹂":"róu", "鞣":"róu","肉":"ròu",
        "如":"rú", "茹":"rú", "铷":"rú", "儒":"rú", "薷":"rú", "嚅":"rú", "濡":"rú", "孺":"rú", "嬬":"rú", "襦":"rú", "颥":"rú", "蠕":"rú",
        "汝":"rǔ", "乳":"rǔ", "辱":"rǔ","入":"rù", "洳":"rù", "蓐":"rù", "溽":"rù", "缛":"rù", "褥":"rù","堧":"ruán",
        "阮":"ruǎn", "软":"ruǎn", "媆":"ruǎn", "瓀":"ruǎn","蕤":"ruí","蕊":"ruǐ",
        "芮":"ruì", "汭":"ruì", "枘":"ruì", "蚋":"ruì", "锐":"ruì", "瑞":"ruì", "睿":"ruì","闰":"rùn", "润":"rùn",
        "若":"ruò", "鄀":"ruò", "偌":"ruò", "弱":"ruò", "婼":"ruò", "蒻":"ruò", "箬":"ruò", "爇":"ruò",
        "仨":"sā", "挲":"sā", "撒":"sā","洒":"sǎ", "靸":"sǎ", "撒":"sǎ", "潵":"sǎ","卅":"sà", "飒":"sà", "脎":"sà", "萨":"sà",
        "腮":"sāi", "塞":"sāi", "噻":"sāi", "鳃":"sāi","塞":"sài", "赛":"sài","三":"sān", "叁":"sān", "毵":"sān",
        "伞":"sǎn", "散":"sǎn", "糁":"sǎn", "馓":"sǎn","散":"sàn","丧":"sāng", "桑":"sāng",
        "搡":"sǎng", "嗓":"sǎng", "磉":"sǎng", "颡":"sǎng","丧":"sàng","搔":"sāo", "溞":"sāo", "骚":"sāo", "缫":"sāo", "臊":"sāo",
        "扫":"sǎo", "嫂":"sǎo","扫":"sào", "埽":"sào", "瘙":"sào", "臊":"sào","色":"sè", "涩":"sè", "啬":"sè", "铯":"sè", "瑟":"sè", "塞":"sè", "穑":"sè", "璱":"sè",
        "森":"sēn","僧":"sēng","杀":"shā", "杉":"shā", "沙":"shā", "纱":"shā", "刹":"shā", "砂":"shā", "莎":"shā", "铩":"shā", "痧":"shā", "煞":"shā", "裟":"shā", "鲨":"shā",
        "啥":"shá","傻":"shǎ","沙":"shà", "唼":"shà", "厦":"shà", "嗄":"shà", "歃":"shà", "煞":"shà", "霎":"shà","筛":"shāi","色":"shǎi","晒":"shài",
        "山":"shān", "芟":"shān", "杉":"shān", "删":"shān", "苫":"shān", "钐":"shān", "衫":"shān", "姗":"shān", "珊":"shān", "埏":"shān", "栅":"shān", "舢":"shān", "烻":"shān", "扇":"shān", "跚":"shān", "煽":"shān", "潸":"shān", "膻":"shān",
        "闪":"shǎn", "陕":"shǎn", "晱":"shǎn","讪":"shàn", "汕":"shàn", "苫":"shàn", "钐":"shàn", "疝":"shàn", "单":"shàn", "剡":"shàn", "扇":"shàn", "𫮃":"shàn", "善":"shàn", "禅":"shàn", "骟":"shàn", "鄯":"shàn", "墡":"shàn", "缮":"shàn", "擅":"shàn", "嶦":"shàn", "膳":"shàn", "嬗":"shàn", "赡":"shàn", "蟮":"shàn", "鳝":"shàn",
        "伤":"shāng", "殇":"shāng", "商":"shāng", "觞":"shāng", "墒":"shāng", "熵":"shāng",
        "上":"shǎng", "垧":"shǎng", "晌":"shǎng", "赏":"shǎng","上":"shàng", "尚":"shàng", "绱":"shàng",
        "裳":"shang","捎":"shāo", "烧":"shāo", "梢":"shāo", "稍":"shāo", "蛸":"shāo", "筲":"shāo", "艄":"shāo", "鞘":"shāo",
        "勺":"sháo", "芍":"sháo", "苕":"sháo", "玿":"sháo", "柖":"sháo", "韶":"sháo",
        "少":"shǎo","少":"shào", "召":"shào", "邵":"shào", "劭":"shào", "绍":"shào", "捎":"shào", "哨":"shào", "睄":"shào", "稍":"shào", "潲":"shào",
        "𪨶":"shē", "奢":"shē", "赊":"shē", "猞":"shē", "畲":"shē","舌":"shé", "折":"shé", "佘":"shé", "蛇":"shé", "阇":"shé",
        "舍":"shě","厍":"shè", "设":"shè", "社":"shè", "舍":"shè", "拾":"shè", "射":"shè", "涉":"shè", "赦":"shè", "摄":"shè", "滠":"shè", "慑":"shè", "歙":"shè", "麝":"shè",
        "谁":"shéi","申":"shēn", "屾":"shēn", "伸":"shēn", "身":"shēn", "呻":"shēn", "侁":"shēn", "诜":"shēn", "参":"shēn", "绅":"shēn", "珅":"shēn", "𬳽":"shēn", "莘":"shēn", "砷":"shēn", "甡":"shēn", "娠":"shēn", "深":"shēn", "棽":"shēn", "糁":"shēn", "鲹":"shēn", "燊":"shēn",
        "什":"shén", "神":"shén", "𬬹":"shén","沈":"shěn", "审":"shěn", "哂":"shěn", "矧":"shěn", "谂":"shěn", "婶":"shěn", "瞫":"shěn",
        "肾":"shèn", "甚":"shèn", "胂":"shèn", "渗":"shèn", "葚":"shèn", "椹":"shèn", "蜃":"shèn", "瘆":"shèn", "慎":"shèn",
        "升":"shēng", "生":"shēng", "声":"shēng", "昇":"shēng", "牲":"shēng", "陞":"shēng", "笙":"shēng", "甥":"shēng",
        "绳":"shéng","省":"shěng", "眚":"shěng","圣":"shèng", "胜":"shèng", "盛":"shèng", "剩":"shèng", "嵊":"shèng",
        "尸":"shī", "失":"shī", "师":"shī", "邿":"shī", "诗":"shī", "鸤":"shī", "虱":"shī", "䴓":"shī", "狮":"shī", "施":"shī", "浉":"shī", "湿":"shī", "蓍":"shī", "酾":"shī", "嘘":"shī", "𫚕":"shī", "鲺":"shī",
        "十":"shí", "什":"shí", "石":"shí", "时":"shí", "识":"shí", "实":"shí", "拾":"shí", "食":"shí", "蚀":"shí", "炻":"shí", "祏":"shí", "埘":"shí", "莳":"shí", "湜":"shí", "鲥":"shí", "鼫":"shí",
        "史":"shǐ", "矢":"shǐ", "豕":"shǐ", "使":"shǐ", "始":"shǐ", "驶":"shǐ", "屎":"shǐ",
        "士":"shì", "氏":"shì", "示":"shì", "世":"shì", "仕":"shì", "市":"shì", "式":"shì", "似":"shì", "势":"shì", "事":"shì", "侍":"shì", "饰":"shì", "试":"shì", "视":"shì", "拭":"shì", "贳":"shì", "柿":"shì", "是":"shì", "峙":"shì", "适":"shì", "䏡":"shì", "恃":"shì", "室":"shì", "逝":"shì", "莳":"shì", "栻":"shì", "轼":"shì", "铈":"shì", "舐":"shì", "𬤊":"shì", "弑":"shì", "释":"shì", "谥":"shì", "媞":"shì", "嗜":"shì", "筮":"shì", "誓":"shì", "奭":"shì", "噬":"shì", "螫":"shì", "襫":"shì",
        "匙":"shi", "殖":"shi","收":"shōu","熟":"shóu","手":"shǒu", "守":"shǒu", "首":"shǒu", "艏":"shǒu",
        "寿":"shòu", "受":"shòu", "狩":"shòu", "授":"shòu", "售":"shòu", "兽":"shòu", "绶":"shòu", "瘦":"shòu",
        "殳":"shū", "书":"shū", "抒":"shū", "纾":"shū", "枢":"shū", "叔":"shū", "陎":"shū", "姝":"shū", "殊":"shū", "倏":"shū", "菽":"shū", "梳":"shū", "鄃":"shū", "淑":"shū", "舒":"shū", "疏":"shū", "摅":"shū", "输":"shū", "毹":"shū", "蔬":"shū",
        "秫":"shú", "孰":"shú", "婌":"shú", "赎":"shú", "塾":"shú", "熟":"shú",
        "暑":"shǔ", "黍":"shǔ", "属":"shǔ", "署":"shǔ", "蜀":"shǔ", "鼠":"shǔ", "数":"shǔ", "薯":"shǔ", "曙":"shǔ",
        "术":"shù", "戍":"shù", "束":"shù", "述":"shù", "沭":"shù", "树":"shù", "竖":"shù", "𬬸":"shù", "恕":"shù", "庶":"shù", "隃":"shù", "腧":"shù", "数":"shù", "墅":"shù", "漱":"shù", "澍":"shù",
        "刷":"shuā", "唰":"shuā","耍":"shuǎ","刷":"shuà","衰":"shuāi", "摔":"shuāi",
        "甩":"shuǎi","帅":"shuài", "率":"shuài", "蟀":"shuài","闩":"shuān", "拴":"shuān", "栓":"shuān",
        "涮":"shuàn", "腨":"shuàn","双":"shuāng", "泷":"shuāng", "漴":"shuāng", "霜":"shuāng", "孀":"shuāng", "骦":"shuāng", "礵":"shuāng", "鹴":"shuāng",
        "爽":"shuǎng","谁":"shuí","水":"shuǐ","说":"shuì", "帨":"shuì", "税":"shuì", "睡":"shuì","吮":"shǔn", "楯":"shǔn","顺":"shùn", "舜":"shùn", "瞬":"shùn",
        "说":"shuō","妁":"shuò", "烁":"shuò", "铄":"shuò", "朔":"shuò", "硕":"shuò", "搠":"shuò", "蒴":"shuò", "数":"shuò", "槊":"shuò",
        "司":"sī", "丝":"sī", "私":"sī", "咝":"sī", "㟃":"sī", "思":"sī", "虒":"sī", "鸶":"sī", "斯":"sī", "蛳":"sī", "缌":"sī", "楒":"sī", "飔":"sī", "厮":"sī", "锶":"sī", "凘":"sī", "撕":"sī", "嘶":"sī", "澌":"sī",
        "死":"sǐ","巳":"sì", "四":"sì", "寺":"sì", "似":"sì", "汜":"sì", "兕":"sì", "伺":"sì", "祀":"sì", "姒":"sì", "饲":"sì", "泗":"sì", "驷":"sì", "俟":"sì", "涘":"sì", "耜":"sì", "笥":"sì", "肆":"sì", "嗣":"sì",
        "忪":"sōng", "松":"sōng", "娀":"sōng", "凇":"sōng", "菘":"sōng", "崧":"sōng", "淞":"sōng", "嵩":"sōng",
        "㧐":"sǒng", "怂":"sǒng", "耸":"sǒng", "悚":"sǒng", "竦":"sǒng","讼":"sòng", "宋":"sòng", "送":"sòng", "诵":"sòng", "颂":"sòng",
        "搜":"sōu", "蒐":"sōu", "嗖":"sōu", "馊":"sōu", "廋":"sōu", "溲":"sōu", "飕":"sōu", "锼":"sōu", "螋":"sōu", "艘":"sōu",
        "叟":"sǒu", "瞍":"sǒu", "嗾":"sǒu", "擞":"sǒu", "薮":"sǒu",
        "嗽":"sòu", "擞":"sòu","苏":"sū", "甦":"sū", "酥":"sū", "稣":"sū", "窣":"sū",
        "俗":"sú","夙":"sù", "诉":"sù", "肃":"sù", "素":"sù", "速":"sù", "𫗧":"sù", "涑":"sù", "宿":"sù", "骕":"sù", "粟":"sù", "傃":"sù", "谡":"sù", "嗉":"sù", "塑":"sù", "溯":"sù", "愫":"sù", "鹔":"sù", "蔌":"sù", "僳":"sù", "觫":"sù", "缩":"sù", "簌":"sù", "蹜":"sù",
        "狻":"suān", "酸":"suān","蒜":"suàn", "算":"suàn",
        "尿":"suī", "虽":"suī", "荽":"suī", "眭":"suī", "睢":"suī", "濉":"suī","绥":"suí", "隋":"suí", "随":"suí", "遂":"suí",
        "髓":"suǐ","岁":"suì", "谇":"suì", "祟":"suì", "遂":"suì", "碎":"suì", "隧":"suì", "璲":"suì", "𫟦":"suì", "燧":"suì", "𬭼":"suì", "穗":"suì", "穟":"suì", "邃":"suì", "襚":"suì", "旞":"suì",
        "孙":"sūn", "荪":"sūn", "狲":"sūn", "飧":"sūn","损":"sǔn", "笋":"sǔn", "隼":"sǔn", "榫":"sǔn",
        "莎":"suō", "唆":"suō", "娑":"suō", "桫":"suō", "梭":"suō", "挲":"suō", "睃":"suō", "蓑":"suō", "嗦":"suō", "嗍":"suō", "羧":"suō", "缩":"suō",
        "所":"suǒ", "索":"suǒ", "唢":"suǒ", "琐":"suǒ", "葰":"suǒ", "锁":"suǒ", "溹":"suǒ",
        "他":"tā", "它":"tā", "她":"tā", "趿":"tā", "铊":"tā", "塌":"tā", "遢":"tā", "溻":"tā", "踏":"tā", "褟":"tā",
        "鿎":"tǎ", "塔":"tǎ", "獭":"tǎ", "鳎":"tǎ",
        "拓":"tà", "沓":"tà", "挞":"tà", "闼":"tà", "阘":"tà", "榻":"tà", "踏":"tà", "蹋":"tà", "鞳":"tà",
        "台":"tāi", "苔":"tāi", "胎":"tāi","台":"tái", "邰":"tái", "抬":"tái", "苔":"tái", "骀":"tái", "炱":"tái", "跆":"tái", "鲐":"tái", "薹":"tái",
        "太":"tài", "汰":"tài", "态":"tài", "肽":"tài", "钛":"tài", "泰":"tài", "酞":"tài",
        "坍":"tān", "贪":"tān", "摊":"tān", "滩":"tān", "瘫":"tān",
        "坛":"tán", "昙":"tán", "倓":"tán", "郯":"tán", "谈":"tán", "惔":"tán", "弹":"tán", "覃":"tán", "榃":"tán", "锬":"tán", "痰":"tán", "谭":"tán", "潭":"tán", "澹":"tán", "檀":"tán", "磹":"tán", "镡":"tán",
        "忐":"tǎn", "坦":"tǎn", "钽":"tǎn", "袒":"tǎn", "菼":"tǎn", "毯":"tǎn", "璮":"tǎn","叹":"tàn", "炭":"tàn", "探":"tàn", "碳":"tàn",
        "汤":"tāng", "铴":"tāng", "耥":"tāng", "嘡":"tāng", "羰":"tāng", "镗":"tāng", "蹚":"tāng",
        "唐":"táng", "堂":"táng", "棠":"táng", "鄌":"táng", "塘":"táng", "搪":"táng", "䣘":"táng", "溏":"táng", "瑭":"táng", "樘":"táng", "膛":"táng", "螗":"táng", "镗":"táng", "糖":"táng", "螳":"táng",
        "帑":"tǎng", "倘":"tǎng", "埫":"tǎng", "淌":"tǎng", "傥":"tǎng", "镋":"tǎng", "躺":"tǎng",
        "烫":"tàng", "趟":"tàng","叨":"tāo", "弢":"tāo", "涛":"tāo", "绦":"tāo", "焘":"tāo", "掏":"tāo", "滔":"tāo", "慆":"tāo", "韬":"tāo", "饕":"tāo",
        "逃":"táo", "洮":"táo", "桃":"táo", "陶":"táo", "萄":"táo", "梼":"táo", "啕":"táo", "淘":"táo", "𫘦":"táo", "绹":"táo", "鼗":"táo",
        "讨":"tǎo","套":"tào","忑":"tè", "特":"tè", "铽":"tè", "慝":"tè",
        "熥":"tēng","疼":"téng", "腾":"téng", "誊":"téng", "滕":"téng", "螣":"téng", "縢":"téng", "藤":"téng", "䲢":"téng",
        "体":"tī", "剔":"tī", "梯":"tī", "䏲":"tī", "锑":"tī", "踢":"tī", "䴘":"tī", "擿":"tī",
        "荑":"tí", "提":"tí", "啼":"tí", "遆":"tí", "鹈":"tí", "𫘨":"tí", "缇":"tí", "瑅":"tí", "题":"tí", "醍":"tí", "蹄":"tí", "鳀":"tí",
        "体":"tǐ","屉":"tì", "剃":"tì", "倜":"tì", "逖":"tì", "涕":"tì", "悌":"tì", "绨":"tì", "惕":"tì", "替":"tì", "裼":"tì", "嚏":"tì", "趯":"tì",
        "天":"tiān", "添":"tiān", "黇":"tiān",
        "田":"tián", "沺":"tián", "盷":"tián", "畋":"tián", "恬":"tián", "甜":"tián", "湉":"tián", "填":"tián", "阗":"tián",
        "忝":"tiǎn", "殄":"tiǎn", "淟":"tiǎn", "晪":"tiǎn", "腆":"tiǎn", "舔":"tiǎn",
        "掭":"tiàn", "瑱":"tiàn","佻":"tiāo", "挑":"tiāo", "祧":"tiāo",
        "条":"tiáo", "迢":"tiáo", "调":"tiáo", "笤":"tiáo", "龆":"tiáo", "蜩":"tiáo", "髫":"tiáo", "鲦":"tiáo",
        "挑":"tiǎo", "朓":"tiǎo", "窕":"tiǎo", "嬥":"tiǎo",
        "眺":"tiào", "粜":"tiào", "跳":"tiào","帖":"tiē", "贴":"tiē", "萜":"tiē","帖":"tiě", "铁":"tiě","帖":"tiè", "餮":"tiè",
        "厅":"tīng", "汀":"tīng", "听":"tīng", "烃":"tīng", "𬘩":"tīng", "桯":"tīng",
        "廷":"tíng", "莛":"tíng", "亭":"tíng", "庭":"tíng", "停":"tíng", "葶":"tíng", "蜓":"tíng", "渟":"tíng", "婷":"tíng", "霆":"tíng", "䗴":"tíng",
        "圢":"tǐng", "侹":"tǐng", "挺":"tǐng", "珽":"tǐng", "梃":"tǐng", "烶":"tǐng", "铤":"tǐng", "颋":"tǐng", "艇":"tǐng",
        "梃":"tìng","通":"tōng", "嗵":"tōng",
        "仝":"tóng", "同":"tóng", "佟":"tóng", "彤":"tóng", "峂":"tóng", "𫍣":"tóng", "垌":"tóng", "茼":"tóng", "哃":"tóng", "峒":"tóng", "洞":"tóng", "桐":"tóng", "砼":"tóng", "烔":"tóng", "铜":"tóng", "童":"tóng", "酮":"tóng", "僮":"tóng", "鲖":"tóng", "潼":"tóng", "橦":"tóng", "曈":"tóng", "瞳":"tóng", "穜":"tóng", "𦒍":"tóng",
        "统":"tǒng", "捅":"tǒng", "㛚":"tǒng", "桶":"tǒng", "筒":"tǒng","同":"tòng", "恸":"tòng", "通":"tòng", "痛":"tòng",
        "偷":"tōu","头":"tóu", "投":"tóu", "骰":"tóu","透":"tòu","凸":"tū", "秃":"tū", "突":"tū", "葖":"tū", "㻬":"tū",
        "图":"tú", "荼":"tú", "徒":"tú", "途":"tú", "涂":"tú", "𬳿":"tú", "梌":"tú", "屠":"tú", "稌":"tú", "腯":"tú", "酴":"tú",
        "土":"tǔ", "吐":"tǔ", "钍":"tǔ","吐":"tù", "兔":"tù", "堍":"tù", "菟":"tù",
        "猯":"tuān", "湍":"tuān", "煓":"tuān","团":"tuán", "抟":"tuán","疃":"tuǎn","彖":"tuàn","忒":"tuī", "推":"tuī",
        "𬯎":"tuí", "颓":"tuí", "魋":"tuí","腿":"tuǐ","退":"tuì", "蜕":"tuì", "煺":"tuì", "褪":"tuì",
        "吞":"tūn", "焞":"tūn", "暾":"tūn","屯":"tún", "坉":"tún", "囤":"tún", "饨":"tún", "忳":"tún", "豚":"tún", "鲀":"tún", "臀":"tún",
        "褪":"tùn","圫":"tuō", "托":"tuō", "拖":"tuō", "侂":"tuō", "脱":"tuō",
        "驮":"tuó", "佗":"tuó", "陀":"tuó", "坨":"tuó", "沱":"tuó", "驼":"tuó", "柁":"tuó", "砣":"tuó", "铊":"tuó", "鸵":"tuó", "酡":"tuó", "跎":"tuó", "𬶍":"tuó", "橐":"tuó", "鼍":"tuó",
        "妥":"tuǒ", "庹":"tuǒ", "椭":"tuǒ","拓":"tuò", "柝":"tuò", "萚":"tuò", "唾":"tuò", "箨":"tuò",
        "坬":"wā", "挖":"wā", "哇":"wā", "洼":"wā", "畖":"wā", "窊":"wā", "娲":"wā", "蛙":"wā",
        "娃":"wá","瓦":"wǎ", "佤":"wǎ","瓦":"wà", "袜":"wà", "腽":"wà","哇":"wa","歪":"wāi","崴":"wǎi","外":"wài",
        "弯":"wān", "剜":"wān", "婠":"wān", "塆":"wān", "湾":"wān", "蜿":"wān", "豌":"wān",
        "丸":"wán", "芄":"wán", "纨":"wán", "完":"wán", "玩":"wán", "顽":"wán", "烷":"wán",
        "宛":"wǎn", "挽":"wǎn", "莞":"wǎn", "菀":"wǎn", "晚":"wǎn", "脘":"wǎn", "惋":"wǎn", "婉":"wǎn", "绾":"wǎn", "琬":"wǎn", "椀":"wǎn", "皖":"wǎn", "碗":"wǎn", "畹":"wǎn",
        "万":"wàn", "𬇕":"wàn", "腕":"wàn", "蔓":"wàn","尢":"wāng", "尪":"wāng", "汪":"wāng","亡":"wáng", "王":"wáng",
        "网":"wǎng", "枉":"wǎng", "罔":"wǎng", "往":"wǎng", "惘":"wǎng", "辋":"wǎng", "魍":"wǎng",
        "妄":"wàng", "忘":"wàng", "旺":"wàng", "望":"wàng",
        "危":"wēi", "威":"wēi", "逶":"wēi", "偎":"wēi", "隈":"wēi", "葳":"wēi", "微":"wēi", "煨":"wēi", "溦":"wēi", "薇":"wēi", "鳂":"wēi", "巍":"wēi",
        "韦":"wéi", "为":"wéi", "圩":"wéi", "违":"wéi", "围":"wéi", "帏":"wéi", "闱":"wéi", "𣲗":"wéi", "沩":"wéi", "峗":"wéi", "洈":"wéi", "桅":"wéi", "涠":"wéi", "唯":"wéi", "帷":"wéi", "惟":"wéi", "维":"wéi", "琟":"wéi", "嵬":"wéi", "𬶏":"wéi", "潍":"wéi",
        "伟":"wěi", "伪":"wěi", "苇":"wěi", "𫇭":"wěi", "尾":"wěi", "纬":"wěi", "玮":"wěi", "𬀩":"wěi", "委":"wěi", "炜":"wěi", "洧":"wěi", "诿":"wěi", "娓":"wěi", "萎":"wěi", "隗":"wěi", "𬱟":"wěi", "猥":"wěi", "廆":"wěi", "韪":"wěi", "艉":"wěi", "痿":"wěi", "鲔":"wěi", "薳":"wěi", "亹":"wěi",
        "卫":"wèi", "为":"wèi", "未":"wèi", "位":"wèi", "味":"wèi", "畏":"wèi", "胃":"wèi", "硙":"wèi", "谓":"wèi", "尉":"wèi", "喂":"wèi", "猬":"wèi", "渭":"wèi", "煟":"wèi", "蔚":"wèi", "碨":"wèi", "慰":"wèi", "魏":"wèi", "螱":"wèi", "霨":"wèi", "鳚":"wèi",
        "温":"wēn", "榅":"wēn", "辒":"wēn", "瘟":"wēn", "蕰":"wēn", "鳁":"wēn",
        "文":"wén", "芠":"wén", "𫘜":"wén", "纹":"wén", "玟":"wén", "炆":"wén", "闻":"wén", "蚊":"wén", "阌":"wén", "雯":"wén",
        "刎":"wěn", "吻":"wěn", "紊":"wěn", "稳":"wěn",
        "问":"wèn", "汶":"wèn", "璺":"wèn","翁":"wēng", "嗡":"wēng", "滃":"wēng", "𬭩":"wēng", "鹟":"wēng",
        "蓊":"wěng","瓮":"wèng", "蕹":"wèng","挝":"wō", "莴":"wō", "倭":"wō", "涡":"wō", "喔":"wō", "窝":"wō", "蜗":"wō", "踒":"wō",
        "我":"wǒ","肟":"wò", "沃":"wò", "卧":"wò", "偓":"wò", "握":"wò", "硪":"wò", "幄":"wò", "渥":"wò", "斡":"wò", "龌":"wò",
        "乌":"wū", "圬":"wū", "邬":"wū", "污":"wū", "巫":"wū", "呜":"wū", "钨":"wū", "洿":"wū", "诬":"wū", "屋":"wū",
        "无":"wú", "毋":"wú", "芜":"wú", "吾":"wú", "吴":"wú", "郚":"wú", "唔":"wú", "峿":"wú", "浯":"wú", "珸":"wú", "梧":"wú", "鹀":"wú", "铻":"wú", "蜈":"wú", "鼯":"wú",
        "五":"wǔ", "午":"wǔ", "伍":"wǔ", "仵":"wǔ", "迕":"wǔ", "庑":"wǔ", "𣲘":"wǔ", "怃":"wǔ", "忤":"wǔ", "妩":"wǔ", "武":"wǔ", "旿":"wǔ", "侮":"wǔ", "捂":"wǔ", "牾":"wǔ", "珷":"wǔ", "鹉":"wǔ", "舞":"wǔ",
        "兀":"wù", "勿":"wù", "戊":"wù", "务":"wù", "屼":"wù", "坞":"wù", "芴":"wù", "杌":"wù", "物":"wù", "误":"wù", "恶":"wù", "悟":"wù", "晤":"wù", "焐":"wù", "靰":"wù", "痦":"wù", "婺":"wù", "骛":"wù", "雾":"wù", "寤":"wù", "鹜":"wù", "鋈":"wù",
        "夕":"xī", "兮":"xī", "西":"xī", "吸":"xī", "汐":"xī", "希":"xī", "昔":"xī", "析":"xī", "肸":"xī", "穸":"xī", "茜":"xī", "俙":"xī", "郗":"xī", "饻":"xī", "恓":"xī", "唏":"xī", "牺":"xī", "息":"xī", "奚":"xī", "浠":"xī", "菥":"xī", "硒":"xī", "晞":"xī", "悉":"xī", "烯":"xī", "淅":"xī", "惜":"xī", "晰":"xī", "睎":"xī", "稀":"xī", "傒":"xī", "舾":"xī", "翕":"xī", "粞":"xī", "犀":"xī", "皙":"xī", "锡":"xī", "溪":"xī", "裼":"xī", "熙":"xī", "豨":"xī", "蜥":"xī", "僖":"xī", "熄":"xī", "嘻":"xī", "嶲":"xī", "膝":"xī", "嬉":"xī", "熹":"xī", "樨":"xī", "暿":"xī", "螅":"xī", "羲":"xī", "熻":"xī", "窸":"xī", "蹊":"xī", "蟋":"xī", "谿":"xī", "釐":"xī", "醯":"xī", "曦":"xī", "巇":"xī", "酅":"xī", "爔":"xī", "鼷":"xī", "觿":"xī",
        "习":"xí", "席":"xí", "觋":"xí", "袭":"xí", "𠅤":"xí", "媳":"xí", "𫘬":"xí", "嶍":"xí", "隰":"xí", "檄":"xí", "鳛":"xí",
        "洗":"xǐ", "枲":"xǐ", "玺":"xǐ", "铣":"xǐ", "徙":"xǐ", "喜":"xǐ", "葸":"xǐ", "蓰":"xǐ", "屣":"xǐ", "憙":"xǐ", "禧":"xǐ", "𬭳":"xǐ", "𬶮":"xǐ",
        "戏":"xì", "饩":"xì", "系":"xì", "屃":"xì", "细":"xì", "咥":"xì", "郤":"xì", "绤":"xì", "阋":"xì", "舄":"xì", "隙":"xì", "禊":"xì", "潟":"xì",
        "呷":"xiā", "虾":"xiā", "瞎":"xiā","匣":"xiá", "侠":"xiá", "狎":"xiá", "柙":"xiá", "峡":"xiá", "狭":"xiá", "叚":"xiá", "硖":"xiá", "翈":"xiá", "遐":"xiá", "瑕":"xiá", "暇":"xiá", "辖":"xiá", "霞":"xiá", "黠":"xiá",
        "下":"xià", "吓":"xià", "夏":"xià", "厦":"xià", "罅":"xià",
        "仙":"xiān", "先":"xiān", "纤":"xiān", "氙":"xiān", "忺":"xiān", "祆":"xiān", "籼":"xiān", "莶":"xiān", "掀":"xiān", "酰":"xiān", "跹":"xiān", "锨":"xiān", "鲜":"xiān", "暹":"xiān", "𬸣":"xiān", "孅":"xiān",
        "伭":"xián", "闲":"xián", "贤":"xián", "弦":"xián", "挦":"xián", "咸":"xián", "涎":"xián", "娴":"xián", "衔":"xián", "舷":"xián", "𫍯":"xián", "痫":"xián", "鹇":"xián", "嫌":"xián",
        "狝":"xiǎn", "冼":"xiǎn", "显":"xiǎn", "洗":"xiǎn", "险":"xiǎn", "蚬":"xiǎn", "崄":"xiǎn", "猃":"xiǎn", "筅":"xiǎn", "跣":"xiǎn", "禒":"xiǎn", "㬎":"xiǎn", "鲜":"xiǎn", "藓":"xiǎn", "燹":"xiǎn",
        "见":"xiàn", "苋":"xiàn", "县":"xiàn", "岘":"xiàn", "现":"xiàn", "𬀪":"xiàn", "限":"xiàn", "线":"xiàn", "𪾢":"xiàn", "宪":"xiàn", "陷":"xiàn", "馅":"xiàn", "羡":"xiàn", "缐":"xiàn", "献":"xiàn", "腺":"xiàn", "霰":"xiàn",
        "乡":"xiāng", "芗":"xiāng", "相":"xiāng", "香":"xiāng", "厢":"xiāng", "葙":"xiāng", "湘":"xiāng", "缃":"xiāng", "箱":"xiāng", "襄":"xiāng", "骧":"xiāng", "𬙋":"xiāng", "瓖":"xiāng", "镶":"xiāng",
        "详":"xiáng", "降":"xiáng", "庠":"xiáng", "祥":"xiáng", "翔":"xiáng",
        "享":"xiǎng", "响":"xiǎng", "饷":"xiǎng", "飨":"xiǎng", "想":"xiǎng", "鲞":"xiǎng",
        "向":"xiàng", "项":"xiàng", "巷":"xiàng", "相":"xiàng", "珦":"xiàng", "象":"xiàng", "像":"xiàng", "橡":"xiàng",
        "肖":"xiāo", "枭":"xiāo", "枵":"xiāo", "削":"xiāo", "哓":"xiāo", "骁":"xiāo", "逍":"xiāo", "鸮":"xiāo", "虓":"xiāo", "消":"xiāo", "宵":"xiāo", "绡":"xiāo", "萧":"xiāo", "猇":"xiāo", "硝":"xiāo", "销":"xiāo", "翛":"xiāo", "蛸":"xiāo", "箫":"xiāo", "潇":"xiāo", "霄":"xiāo", "魈":"xiāo", "蟏":"xiāo", "嚣":"xiāo",
        "洨":"xiáo", "崤":"xiáo", "淆":"xiáo","小":"xiǎo", "晓":"xiǎo", "𫍲":"xiǎo", "筱":"xiǎo", "皛":"xiǎo",
        "孝":"xiào", "肖":"xiào", "校":"xiào", "哮":"xiào", "笑":"xiào", "效":"xiào", "涍":"xiào", "啸":"xiào", "敩":"xiào", "滧":"xiào",
        "些":"xiē", "揳":"xiē", "楔":"xiē", "歇":"xiē", "蝎":"xiē",
        "叶":"xié", "协":"xié", "邪":"xié", "胁":"xié", "挟":"xié", "偕":"xié", "斜":"xié", "谐":"xié", "絜":"xié", "颉":"xié", "携":"xié", "㙦":"xié", "撷":"xié", "鞋":"xié", "勰":"xié", "缬":"xié",
        "写":"xiě", "血":"xiě","泄":"xiè", "泻":"xiè", "绁":"xiè", "卸":"xiè", "屑":"xiè", "械":"xiè", "偰":"xiè", "𬹼":"xiè", "亵":"xiè", "渫":"xiè", "谢":"xiè", "解":"xiè", "榭":"xiè", "榍":"xiè", "薤":"xiè", "薢":"xiè", "獬":"xiè", "邂":"xiè", "廨":"xiè", "澥":"xiè", "懈":"xiè", "燮":"xiè", "蟹":"xiè", "瀣":"xiè", "𤫉":"xiè", "躞":"xiè",
        "心":"xīn", "䜣":"xīn", "芯":"xīn", "辛":"xīn", "忻":"xīn", "昕":"xīn", "欣":"xīn", "炘":"xīn", "莘":"xīn", "锌":"xīn", "𫷷":"xīn", "新":"xīn", "歆":"xīn", "薪":"xīn", "馨":"xīn", "鑫":"xīn",
        "伈":"xǐn","囟":"xìn", "芯":"xìn", "信":"xìn", "衅":"xìn",
        "兴":"xīng", "星":"xīng", "骍":"xīng", "猩":"xīng", "惺":"xīng", "瑆":"xīng", "腥":"xīng", "煋":"xīng",
        "刑":"xíng", "邢":"xíng", "行":"xíng", "饧":"xíng", "形":"xíng", "陉":"xíng", "𫰛":"xíng", "型":"xíng", "荥":"xíng", "钘":"xíng", "硎":"xíng", "铏":"xíng",
        "省":"xǐng", "醒":"xǐng", "擤":"xǐng",
        "兴":"xìng", "杏":"xìng", "幸":"xìng", "性":"xìng", "姓":"xìng", "荇":"xìng", "悻":"xìng", "婞":"xìng",
        "凶":"xiōng", "兄":"xiōng", "芎":"xiōng", "匈":"xiōng", "讻":"xiōng", "汹":"xiōng", "胸":"xiōng",
        "雄":"xióng", "熊":"xióng","诇":"xiòng", "夐":"xiòng",
        "休":"xiū", "咻":"xiū", "修":"xiū", "庥":"xiū", "脩":"xiū", "羞":"xiū", "鸺":"xiū", "貅":"xiū", "馐":"xiū", "髹":"xiū", "䗛":"xiū",
        "朽":"xiǔ", "宿":"xiǔ", "滫":"xiǔ",
        "秀":"xiù", "岫":"xiù", "珛":"xiù", "臭":"xiù", "袖":"xiù", "绣":"xiù", "琇":"xiù", "宿":"xiù", "锈":"xiù", "嗅":"xiù", "溴":"xiù",
        "𬣙":"xū", "圩":"xū", "戌":"xū", "吁":"xū", "旴":"xū", "盱":"xū", "须":"xū", "胥":"xū", "顼":"xū", "虚":"xū", "谞":"xū", "媭":"xū", "欻":"xū", "墟":"xū", "需":"xū", "嘘":"xū", "魆":"xū", "𦈡":"xū",
        "徐":"xú","许":"xǔ", "诩":"xǔ", "浒":"xǔ", "珝":"xǔ", "栩":"xǔ", "冔":"xǔ", "糈":"xǔ", "醑":"xǔ",
        "旭":"xù", "序":"xù", "昫":"xù", "叙":"xù", "㳚":"xù", "洫":"xù", "恤":"xù", "垿":"xù", "畜":"xù", "酗":"xù", "勖":"xù", "绪":"xù", "续":"xù", "溆":"xù", "湑":"xù", "絮":"xù", "婿":"xù", "蓄":"xù", "煦":"xù",
        "蓿":"xu","轩":"xuān", "咺":"xuān", "宣":"xuān", "谖":"xuān", "萱":"xuān", "喧":"xuān", "𫓶":"xuān", "愃":"xuān", "瑄":"xuān", "暄":"xuān", "煊":"xuān", "儇":"xuān", "禤":"xuān", "𫍽":"xuān", "嬛":"xuān", "翾":"xuān",
        "玄":"xuán", "𫠊":"xuán", "玹":"xuán", "痃":"xuán", "悬":"xuán", "旋":"xuán", "漩":"xuán", "璇":"xuán", "暶":"xuán",
        "选":"xuǎn", "晅":"xuǎn", "烜":"xuǎn", "癣":"xuǎn",
        "券":"xuàn", "泫":"xuàn", "昡":"xuàn", "炫":"xuàn", "绚":"xuàn", "眩":"xuàn", "铉":"xuàn", "琄":"xuàn", "衒":"xuàn", "旋":"xuàn", "渲":"xuàn", "楦":"xuàn", "碹":"xuàn",
        "削":"xuē", "靴":"xuē", "薛":"xuē","穴":"xué", "茓":"xué", "峃":"xué", "学":"xué", "踅":"xué", "噱":"xué",
        "雪":"xuě", "鳕":"xuě","血":"xuè", "谑":"xuè",
        "勋":"xūn", "埙":"xūn", "熏":"xūn", "薰":"xūn", "獯":"xūn", "𫄸":"xūn", "曛":"xūn", "醺":"xūn",
        "旬":"xún", "寻":"xún", "𬘓":"xún", "巡":"xún", "郇":"xún", "询":"xún", "𬩽":"xún", "荀":"xún", "荨":"xún", "峋":"xún", "洵":"xún", "浔":"xún", "恂":"xún", "珣":"xún", "𬍤":"xún", "栒":"xún", "𬊈":"xún", "循":"xún", "鲟":"xún",
        "训":"xùn", "讯":"xùn", "汛":"xùn", "迅":"xùn", "驯":"xùn", "徇":"xùn", "逊":"xùn", "殉":"xùn", "浚":"xùn", "巽":"xùn", "蕈":"xùn", "噀":"xùn",
        "丫":"yā", "压":"yā", "呀":"yā", "押":"yā", "垭":"yā", "鸦":"yā", "哑":"yā", "桠":"yā", "鸭":"yā",
        "牙":"yá", "伢":"yá", "芽":"yá", "岈":"yá", "玡":"yá", "琊":"yá", "蚜":"yá", "堐":"yá", "崖":"yá", "涯":"yá", "睚":"yá", "衙":"yá",
        "哑":"yǎ", "雅":"yǎ","轧":"yà", "亚":"yà", "压":"yà", "讶":"yà", "迓":"yà", "砑":"yà", "娅":"yà", "氩":"yà", "揠":"yà", "猰":"yà",
        "呀":"ya","咽":"yān", "恹":"yān", "殷":"yān", "胭":"yān", "烟":"yān", "焉":"yān", "崦":"yān", "阉":"yān", "阏":"yān", "淹":"yān", "腌":"yān", "湮":"yān", "鄢":"yān", "墕":"yān", "漹":"yān", "嫣":"yān", "燕":"yān",
        "延":"yán", "闫":"yán", "芫":"yán", "严":"yán", "言":"yán", "妍":"yán", "岩":"yán", "炎":"yán", "沿":"yán", "研":"yán", "𫄧":"yán", "盐":"yán", "铅":"yán", "阎":"yán", "蜒":"yán", "筵":"yán", "颜":"yán", "虤":"yán", "檐":"yán",
        "沇":"yǎn", "奄":"yǎn", "兖":"yǎn", "䶮":"yǎn", "俨":"yǎn", "衍":"yǎn", "弇":"yǎn", "掩":"yǎn", "郾":"yǎn", "厣":"yǎn", "眼":"yǎn", "偃":"yǎn", "琰":"yǎn", "棪":"yǎn", "渰":"yǎn", "扊":"yǎn", "罨":"yǎn", "𬸘":"yǎn", "演":"yǎn", "𬙂":"yǎn", "魇":"yǎn", "蝘":"yǎn", "戭":"yǎn", "𪩘":"yǎn", "黡":"yǎn", "甗":"yǎn", "鼹":"yǎn",
        "厌":"yàn", "觃":"yàn", "砚":"yàn", "咽":"yàn", "彦":"yàn", "艳":"yàn", "晏":"yàn", "唁":"yàn", "宴":"yàn", "验":"yàn", "掞":"yàn", "谚":"yàn", "堰":"yàn", "雁":"yàn", "焰":"yàn", "焱":"yàn", "滟":"yàn", "酽":"yàn", "餍":"yàn", "谳":"yàn", "燕":"yàn", "赝":"yàn", "嬿":"yàn",
        "央":"yāng", "咉":"yāng", "泱":"yāng", "殃":"yāng", "鸯":"yāng", "秧":"yāng", "鞅":"yāng",
        "扬":"yáng", "羊":"yáng", "阳":"yáng", "玚":"yáng", "杨":"yáng", "旸":"yáng", "飏":"yáng", "炀":"yáng", "钖":"yáng", "佯":"yáng", "疡":"yáng", "垟":"yáng", "徉":"yáng", "洋":"yáng", "烊":"yáng", "蛘":"yáng",
        "仰":"yǎng", "养":"yǎng", "氧":"yǎng", "痒":"yǎng",
        "怏":"yàng", "样":"yàng", "恙":"yàng", "烊":"yàng", "羕":"yàng", "鞅":"yàng", "漾":"yàng",
        "幺":"yāo", "夭":"yāo", "吆":"yāo", "约":"yāo", "妖":"yāo", "要":"yāo", "㙘":"yāo", "腰":"yāo", "邀":"yāo",
        "爻":"yáo", "尧":"yáo", "侥":"yáo", "肴":"yáo", "垚":"yáo", "轺":"yáo", "峣":"yáo", "姚":"yáo", "珧":"yáo", "铫":"yáo", "窑":"yáo", "谣":"yáo", "摇":"yáo", "徭":"yáo", "遥":"yáo", "猺":"yáo", "媱":"yáo", "瑶":"yáo", "鳐":"yáo",
        "杳":"yǎo", "咬":"yǎo", "舀":"yǎo", "窅":"yǎo", "窈":"yǎo",
        "疟":"yào", "药":"yào", "要":"yào", "钥":"yào", "崾":"yào", "靿":"yào", "鹞":"yào", "曜":"yào", "耀":"yào",
        "耶":"yē", "倻":"yē", "掖":"yē", "椰":"yē", "噎":"yē","爷":"yé", "耶":"yé", "揶":"yé", "铘":"yé","也":"yě", "冶":"yě", "野":"yě",
        "业":"yè", "叶":"yè", "页":"yè", "曳":"yè", "邺":"yè", "夜":"yè", "咽":"yè", "晔":"yè", "烨":"yè", "掖":"yè", "液":"yè", "谒":"yè", "腋":"yè", "馌":"yè", "靥":"yè",
        "一":"yī", "伊":"yī", "衣":"yī", "医":"yī", "依":"yī", "祎":"yī", "咿":"yī", "洢":"yī", "铱":"yī", "猗":"yī", "揖":"yī", "壹":"yī", "椅":"yī", "漪":"yī", "噫":"yī", "繄":"yī", "黟":"yī",
        "匜":"yí", "仪":"yí", "圯":"yí", "夷":"yí", "沂":"yí", "诒":"yí", "迤":"yí", "饴":"yí", "怡":"yí", "宜":"yí", "荑":"yí", "咦":"yí", "贻":"yí", "姨":"yí", "眙":"yí", "胰":"yí", "宧":"yí", "扅":"yí", "移":"yí", "痍":"yí", "遗":"yí", "颐":"yí", "椸":"yí", "疑":"yí", "嶷":"yí", "簃":"yí", "彝":"yí",
        "乙":"yǐ", "已":"yǐ", "以":"yǐ", "钇":"yǐ", "苡":"yǐ", "佁":"yǐ", "尾":"yǐ", "矣":"yǐ", "迤":"yǐ", "蚁":"yǐ", "舣":"yǐ", "酏":"yǐ", "倚":"yǐ", "扆":"yǐ", "椅":"yǐ", "𫖮":"yǐ", "旖":"yǐ", "踦":"yǐ", "𬺈":"yǐ",
        "乂":"yì", "弋":"yì", "亿":"yì", "义":"yì", "艺":"yì", "刈":"yì", "忆":"yì", "艾":"yì", "议":"yì", "屹":"yì", "亦":"yì", "异":"yì", "抑":"yì", "杙":"yì", "呓":"yì", "邑":"yì", "佚":"yì", "役":"yì", "译":"yì", "枍":"yì", "易":"yì", "峄":"yì", "𬬩":"yì", "佾":"yì", "㑊":"yì", "怿":"yì", "诣":"yì", "驿":"yì", "绎":"yì", "轶":"yì", "弈":"yì", "奕":"yì", "疫":"yì", "羿":"yì", "挹":"yì", "益":"yì", "浥":"yì", "悒":"yì", "谊":"yì", "埸":"yì", "勚":"yì", "逸":"yì", "翊":"yì", "翌":"yì", "嗌":"yì", "肄":"yì", "裛":"yì", "裔":"yì", "意":"yì", "溢":"yì", "缢":"yì", "蜴":"yì", "廙":"yì", "瘗":"yì", "潩":"yì", "嫕":"yì", "鹝":"yì", "镒":"yì", "毅":"yì", "鹢":"yì", "熠":"yì", "薏":"yì", "殪":"yì", "螠":"yì", "劓":"yì", "燚":"yì", "𫄷":"yì", "翳":"yì", "臆":"yì", "翼":"yì", "𬟁":"yì", "镱":"yì", "癔":"yì", "懿":"yì",
        "因":"yīn", "阴":"yīn", "茵":"yīn", "荫":"yīn", "音":"yīn", "洇":"yīn", "姻":"yīn", "骃":"yīn", "𬘡":"yīn", "氤":"yīn", "殷":"yīn", "铟":"yīn", "𬤇":"yīn", "堙":"yīn", "喑":"yīn", "𬮱":"yīn", "愔":"yīn", "歅":"yīn", "溵":"yīn", "禋":"yīn",
        "吟":"yín", "垠":"yín", "珢":"yín", "狺":"yín", "訚":"yín", "硍":"yín", "崟":"yín", "银":"yín", "淫":"yín", "寅":"yín", "龂":"yín", "鄞":"yín", "龈":"yín", "夤":"yín", "蟫":"yín", "嚚":"yín", "霪":"yín",
        "尹":"yǐn", "引":"yǐn", "吲":"yǐn", "饮":"yǐn", "蚓":"yǐn", "隐":"yǐn", "瘾":"yǐn",
        "印":"yìn", "饮":"yìn", "茚":"yìn", "荫":"yìn", "胤":"yìn", "䲟":"yìn", "窨":"yìn", "慭":"yìn",
        "应":"yīng", "英":"yīng", "莺":"yīng", "䓨":"yīng", "婴":"yīng", "媖":"yīng", "瑛":"yīng", "锳":"yīng", "撄":"yīng", "嘤":"yīng", "罂":"yīng", "缨":"yīng", "璎":"yīng", "樱":"yīng", "鹦":"yīng", "膺":"yīng", "鹰":"yīng",
        "迎":"yíng", "茔":"yíng", "荥":"yíng", "荧":"yíng", "盈":"yíng", "莹":"yíng", "萤":"yíng", "营":"yíng", "萦":"yíng", "溁":"yíng", "蓥":"yíng", "楹":"yíng", "滢":"yíng", "蝇":"yíng", "潆":"yíng", "嬴":"yíng", "赢":"yíng", "瀛":"yíng",
        "郢":"yǐng", "颍":"yǐng", "颖":"yǐng", "影":"yǐng", "瘿":"yǐng","应":"yìng", "映":"yìng", "硬":"yìng", "媵":"yìng",
        "哟":"yō", "唷":"yō","哟":"yo","佣":"yōng", "拥":"yōng", "痈":"yōng", "邕":"yōng", "庸":"yōng", "鄘":"yōng", "雍":"yōng", "墉":"yōng", "慵":"yōng", "镛":"yōng", "壅":"yōng", "澭":"yōng", "臃":"yōng", "鳙":"yōng", "饔":"yōng",
        "喁":"yóng", "颙":"yóng","永":"yǒng", "甬":"yǒng", "咏":"yǒng", "泳":"yǒng", "栐":"yǒng", "俑":"yǒng", "勇":"yǒng", "埇":"yǒng", "涌":"yǒng", "恿":"yǒng", "蛹":"yǒng", "踊":"yǒng", "鲬":"yǒng",
        "用":"yòng", "佣":"yòng", "㶲":"yòng",
        "优":"yōu", "攸":"yōu", "忧":"yōu", "呦":"yōu", "幽":"yōu", "悠":"yōu", "麀":"yōu", "耰":"yōu",
        "尤":"yóu", "由":"yóu", "邮":"yóu", "犹":"yóu", "油":"yóu", "柚":"yóu", "疣":"yóu", "莜":"yóu", "莸":"yóu", "铀":"yóu", "浟":"yóu", "蚰":"yóu", "鱿":"yóu", "游":"yóu", "𬨎":"yóu", "鲉":"yóu", "猷":"yóu", "蝣":"yóu", "蝤":"yóu", "繇":"yóu",
        "友":"yǒu", "有":"yǒu", "酉":"yǒu", "卣":"yǒu", "羑":"yǒu", "莠":"yǒu", "铕":"yǒu", "槱":"yǒu", "牖":"yǒu", "黝":"yǒu",
        "又":"yòu", "右":"yòu", "幼":"yòu", "佑":"yòu", "侑":"yòu", "柚":"yòu", "囿":"yòu", "宥":"yòu", "祐":"yòu", "诱":"yòu", "蚴":"yòu", "釉":"yòu", "鼬":"yòu",
        "迂":"yū", "吁":"yū", "纡":"yū", "於":"yū", "淤":"yū", "瘀":"yū",
        "于":"yú", "予":"yú", "邘":"yú", "玙":"yú", "欤":"yú", "余":"yú", "妤":"yú", "盂":"yú", "臾":"yú", "鱼":"yú", "於":"yú", "禺":"yú", "竽":"yú", "舁":"yú", "俞":"yú", "狳":"yú", "谀":"yú", "娱":"yú", "萸":"yú", "雩":"yú", "渔":"yú", "隅":"yú", "揄":"yú", "喁":"yú", "嵎":"yú", "嵛":"yú", "畬":"yú", "逾":"yú", "腴":"yú", "渝":"yú", "愉":"yú", "瑜":"yú", "榆":"yú", "虞":"yú", "愚":"yú", "艅":"yú", "觎":"yú", "舆":"yú", "窬":"yú", "褕":"yú", "蝓":"yú", "髃":"yú",
        "与":"yǔ", "予":"yǔ", "屿":"yǔ", "伛":"yǔ", "宇":"yǔ", "羽":"yǔ", "雨":"yǔ", "俣":"yǔ", "禹":"yǔ", "语":"yǔ", "圄":"yǔ", "敔":"yǔ", "圉":"yǔ", "鄅":"yǔ", "庾":"yǔ", "㺄":"yǔ", "瑀":"yǔ", "瘐":"yǔ", "龉":"yǔ", "窳":"yǔ",
        "与":"yù", "玉":"yù", "驭":"yù", "芋":"yù", "吁":"yù", "聿":"yù", "饫":"yù", "妪":"yù", "郁":"yù", "育":"yù", "昱":"yù", "狱":"yù", "彧":"yù", "峪":"yù", "钰":"yù", "浴":"yù", "预":"yù", "域":"yù", "堉":"yù", "悆":"yù", "欲":"yù", "阈":"yù", "淯":"yù", "谕":"yù", "尉":"yù", "棫":"yù", "遇":"yù", "喻":"yù", "御":"yù", "鹆":"yù", "寓":"yù", "裕":"yù", "矞":"yù", "蓣":"yù", "愈":"yù", "煜":"yù", "滪":"yù", "誉":"yù", "蔚":"yù", "蜮":"yù", "毓":"yù", "潏":"yù", "熨":"yù", "遹":"yù", "豫":"yù", "燠":"yù", "燏":"yù", "鹬":"yù", "鬻":"yù",
        "鸢":"yuān", "眢":"yuān", "鸳":"yuān", "冤":"yuān", "渊":"yuān", "涴":"yuān", "蜎":"yuān", "箢":"yuān",
        "元":"yuán", "芫":"yuán", "园":"yuán", "员":"yuán", "沅":"yuán", "妧":"yuán", "垣":"yuán", "爰":"yuán", "袁":"yuán", "原":"yuán", "圆":"yuán", "鼋":"yuán", "援":"yuán", "湲":"yuán", "媛":"yuán", "缘":"yuán", "塬":"yuán", "猿":"yuán", "源":"yuán", "嫄":"yuán", "𫘪":"yuán", "辕":"yuán", "橼":"yuán", "螈":"yuán", "圜":"yuán", "羱":"yuán",
        "远":"yuǎn","苑":"yuàn", "怨":"yuàn", "院":"yuàn", "垸":"yuàn", "掾":"yuàn", "媛":"yuàn", "瑗":"yuàn", "愿":"yuàn",
        "曰":"yuē", "约":"yuē", "彟":"yuē","哕":"yuě",
        "月":"yuè", "乐":"yuè", "刖":"yuè", "𫐄":"yuè", "玥":"yuè", "岳":"yuè", "栎":"yuè", "钥":"yuè", "钺":"yuè", "阅":"yuè", "悦":"yuè", "跃":"yuè", "越":"yuè", "粤":"yuè", "𬸚":"yuè", "樾":"yuè", "龠":"yuè", "瀹":"yuè", "爚":"yuè", "籥":"yuè",
        "晕":"yūn", "氲":"yūn", "煴":"yūn", "𫖳":"yūn", "赟":"yūn", "馧":"yūn",
        "云":"yún", "匀":"yún", "芸":"yún", "沄":"yún", "妘":"yún", "纭":"yún", "昀":"yún", "郧":"yún", "耘":"yún", "涢":"yún", "筠":"yún", "筼":"yún", "鋆":"yún",
        "允":"yǔn", "狁":"yǔn", "陨":"yǔn", "殒":"yǔn",
        "孕":"yùn", "运":"yùn", "员":"yùn", "郓":"yùn", "恽":"yùn", "晕":"yùn", "酝":"yùn", "愠":"yùn", "缊":"yùn", "韫":"yùn", "韵":"yùn", "蕴":"yùn", "熨":"yùn",
        "扎":"zā", "匝":"zā", "咂":"zā", "拶":"zā", "臜":"zā","杂":"zá", "砸":"zá","咋":"zǎ",
        "灾":"zāi", "甾":"zāi", "哉":"zāi", "栽":"zāi","仔":"zǎi", "载":"zǎi", "宰":"zǎi", "崽":"zǎi",
        "再":"zài", "在":"zài", "载":"zài","糌":"zān", "簪":"zān","咱":"zán",
        "拶":"zǎn", "昝":"zǎn", "寁":"zǎn", "攒":"zǎn", "趱":"zǎn","暂":"zàn", "錾":"zàn", "赞":"zàn", "酂":"zàn", "瓒":"zàn",
        "赃":"zāng", "脏":"zāng", "牂":"zāng", "臧":"zāng","驵":"zǎng",
        "脏":"zàng", "奘":"zàng", "葬":"zàng", "藏":"zàng","遭":"zāo", "糟":"zāo","凿":"záo",
        "早":"zǎo", "枣":"zǎo", "蚤":"zǎo", "澡":"zǎo", "璪":"zǎo", "藻":"zǎo",
        "皂":"zào", "灶":"zào", "唣":"zào", "造":"zào", "慥":"zào", "噪":"zào", "簉":"zào", "燥":"zào", "𥖨":"zào", "躁":"zào",
        "则":"zé", "责":"zé", "择":"zé", "咋":"zé", "迮":"zé", "泽":"zé", "啧":"zé", "帻":"zé", "笮":"zé", "舴":"zé", "箦":"zé", "赜":"zé",
        "仄":"zè", "昃":"zè","贼":"zéi", "鲗":"zéi","怎":"zěn","谮":"zèn",
        "曾":"zēng", "鄫":"zēng", "增":"zēng", "憎":"zēng", "缯":"zēng", "罾":"zēng", "矰":"zēng", "䎖":"zēng",
        "综":"zèng", "锃":"zèng", "赠":"zèng", "甑":"zèng",
        "扎":"zhā", "吒":"zhā", "咋":"zhā", "挓":"zhā", "查":"zhā", "奓":"zhā", "哳":"zhā", "揸":"zhā", "喳":"zhā", "渣":"zhā", "楂":"zhā", "齇":"zhā",
        "扎":"zhá", "札":"zhá", "轧":"zhá", "闸":"zhá", "炸":"zhá", "铡":"zhá", "喋":"zhá", "劄":"zhá",
        "拃":"zhǎ", "眨":"zhǎ", "砟":"zhǎ", "鲊":"zhǎ", "鲝":"zhǎ",
        "乍":"zhà", "诈":"zhà", "柞":"zhà", "栅":"zhà", "咤":"zhà", "炸":"zhà", "痄":"zhà", "蚱":"zhà", "溠":"zhà", "榨":"zhà", "䃎":"zhà", "霅":"zhà",
        "馇":"zha","斋":"zhāi", "摘":"zhāi","宅":"zhái", "择":"zhái", "翟":"zhái","窄":"zhǎi",
        "豸":"zhài", "债":"zhài", "祭":"zhài", "寨":"zhài", "瘵":"zhài",
        "占":"zhān", "沾":"zhān", "毡":"zhān", "栴":"zhān", "旃":"zhān", "粘":"zhān", "詹":"zhān", "谵":"zhān", "𫗴":"zhān", "瞻":"zhān", "鹯":"zhān", "鳣":"zhān",
        "斩":"zhǎn", "飐":"zhǎn", "盏":"zhǎn", "展":"zhǎn", "崭":"zhǎn", "搌":"zhǎn", "辗":"zhǎn",
        "占":"zhàn", "栈":"zhàn", "战":"zhàn", "站":"zhàn", "偡":"zhàn", "绽":"zhàn", "湛":"zhàn", "蘸":"zhàn",
        "张":"zhāng", "章":"zhāng", "鄣":"zhāng", "獐":"zhāng", "彰":"zhāng", "漳":"zhāng", "嫜":"zhāng", "璋":"zhāng", "樟":"zhāng", "暲":"zhāng", "蟑":"zhāng",
        "长":"zhǎng", "仉":"zhǎng", "涨":"zhǎng", "掌":"zhǎng",
        "丈":"zhàng", "仗":"zhàng", "杖":"zhàng", "帐":"zhàng", "账":"zhàng", "胀":"zhàng", "涨":"zhàng", "障":"zhàng", "嶂":"zhàng", "幛":"zhàng", "瘴":"zhàng",
        "钊":"zhāo", "招":"zhāo", "昭":"zhāo", "𬬿":"zhāo", "啁":"zhāo", "着":"zhāo", "朝":"zhāo",
        "着":"zháo","爪":"zhǎo", "找":"zhǎo", "沼":"zhǎo",
        "召":"zhào", "兆":"zhào", "诏":"zhào", "赵":"zhào", "笊":"zhào", "棹":"zhào", "旐":"zhào", "照":"zhào", "罩":"zhào", "𬶐":"zhào", "肇":"zhào", "曌":"zhào",
        "折":"zhē", "蜇":"zhē", "遮":"zhē",
        "折":"zhé", "哲":"zhé", "晢":"zhé", "辄":"zhé", "喆":"zhé", "蛰":"zhé", "詟":"zhé", "蜇":"zhé", "谪":"zhé", "磔":"zhé", "辙":"zhé",
        "者":"zhě", "啫":"zhě", "锗":"zhě", "赭":"zhě", "褶":"zhě",
        "这":"zhè", "柘":"zhè", "浙":"zhè", "蔗":"zhè", "鹧":"zhè", "䗪":"zhè",
        "着":"zhe","贞":"zhēn", "针":"zhēn", "侦":"zhēn", "珍":"zhēn", "帧":"zhēn", "胗":"zhēn", "浈":"zhēn", "真":"zhēn", "桢":"zhēn", "砧":"zhēn", "祯":"zhēn", "葴":"zhēn", "蓁":"zhēn", "斟":"zhēn", "甄":"zhēn", "瑧":"zhēn", "榛":"zhēn", "禛":"zhēn", "箴":"zhēn", "臻":"zhēn",
        "诊":"zhěn", "枕":"zhěn", "轸":"zhěn", "昣":"zhěn", "畛":"zhěn", "疹":"zhěn", "袗":"zhěn", "缜":"zhěn", "稹":"zhěn", "鬒":"zhěn",
        "圳":"zhèn", "阵":"zhèn", "纼":"zhèn", "鸩":"zhèn", "振":"zhèn", "朕":"zhèn", "赈":"zhèn", "揕":"zhèn", "震":"zhèn", "镇":"zhèn",
        "正":"zhēng", "争":"zhēng", "征":"zhēng", "挣":"zhēng", "峥":"zhēng", "狰":"zhēng", "钲":"zhēng", "症":"zhēng", "烝":"zhēng", "睁":"zhēng", "铮":"zhēng", "筝":"zhēng", "蒸":"zhēng",
        "拯":"zhěng", "整":"zhěng","正":"zhèng", "证":"zhèng", "郑":"zhèng", "怔":"zhèng", "诤":"zhèng", "政":"zhèng", "挣":"zhèng", "症":"zhèng",
        "之":"zhī", "支":"zhī", "氏":"zhī", "只":"zhī", "卮":"zhī", "汁":"zhī", "芝":"zhī", "吱":"zhī", "𦭜":"zhī", "枝":"zhī", "知":"zhī", "肢":"zhī", "泜":"zhī", "织":"zhī", "栀":"zhī", "胝":"zhī", "祗":"zhī", "脂":"zhī", "稙":"zhī", "禔":"zhī", "榰":"zhī", "蜘":"zhī",
        "执":"zhí", "直":"zhí", "侄":"zhí", "值":"zhí", "埴":"zhí", "职":"zhí", "絷":"zhí", "植":"zhí", "殖":"zhí", "跖":"zhí", "摭":"zhí", "踯":"zhí",
        "止":"zhǐ", "只":"zhǐ", "旨":"zhǐ", "址":"zhǐ", "扺":"zhǐ", "芷":"zhǐ", "沚":"zhǐ", "纸":"zhǐ", "祉":"zhǐ", "指":"zhǐ", "枳":"zhǐ", "轵":"zhǐ", "咫":"zhǐ", "趾":"zhǐ", "黹":"zhǐ", "酯":"zhǐ", "徵":"zhǐ",
        "至":"zhì", "志":"zhì", "豸":"zhì", "忮":"zhì", "识":"zhì", "郅":"zhì", "帜":"zhì", "帙":"zhì", "制":"zhì", "质":"zhì", "炙":"zhì", "治":"zhì", "栉":"zhì", "峙":"zhì", "庤":"zhì", "陟":"zhì", "贽":"zhì", "挚":"zhì", "桎":"zhì", "轾":"zhì", "致":"zhì", "晊":"zhì", "秩":"zhì", "鸷":"zhì", "掷":"zhì", "梽":"zhì", "畤":"zhì", "铚":"zhì", "痔":"zhì", "窒":"zhì", "𬃊":"zhì", "蛭":"zhì", "智":"zhì", "痣":"zhì", "滞":"zhì", "骘":"zhì", "彘":"zhì", "跱":"zhì", "置":"zhì", "锧":"zhì", "雉":"zhì", "稚":"zhì", "滍":"zhì", "疐":"zhì", "踬":"zhì", "觯":"zhì",
        "中":"zhōng", "忠":"zhōng", "终":"zhōng", "柊":"zhōng", "盅":"zhōng", "钟":"zhōng", "舯":"zhōng", "衷":"zhōng", "锺":"zhōng", "螽":"zhōng",
        "肿":"zhǒng", "种":"zhǒng", "冢":"zhǒng", "踵":"zhǒng",
        "中":"zhòng", "仲":"zhòng", "众":"zhòng", "茽":"zhòng", "种":"zhòng", "重":"zhòng",
        "舟":"zhōu", "州":"zhōu", "诌":"zhōu", "周":"zhōu", "洲":"zhōu", "辀":"zhōu", "啁":"zhōu", "鸼":"zhōu", "婤":"zhōu", "赒":"zhōu", "粥":"zhōu",
        "妯":"zhóu", "轴":"zhóu", "碡":"zhóu","肘":"zhǒu", "帚":"zhǒu",
        "纣":"zhòu", "㑇":"zhòu", "咒":"zhòu", "㤘":"zhòu", "宙":"zhòu", "绉":"zhòu", "荮":"zhòu", "轴":"zhòu", "胄":"zhòu", "昼":"zhòu", "酎":"zhòu", "皱":"zhòu", "骤":"zhòu", "籀":"zhòu",
        "朱":"zhū", "邾":"zhū", "侏":"zhū", "诛":"zhū", "茱":"zhū", "洙":"zhū", "珠":"zhū", "株":"zhū", "诸":"zhū", "铢":"zhū", "猪":"zhū", "蛛":"zhū", "槠":"zhū", "潴":"zhū", "橥":"zhū",
        "术":"zhú", "竹":"zhú", "竺":"zhú", "逐":"zhú", "烛":"zhú", "舳":"zhú", "瘃":"zhú", "蠋":"zhú", "躅":"zhú",
        "主":"zhǔ", "𬣞":"zhǔ", "拄":"zhǔ", "渚":"zhǔ", "煮":"zhǔ", "嘱":"zhǔ", "麈":"zhǔ", "瞩":"zhǔ",
        "伫":"zhù", "苎":"zhù", "助":"zhù", "住":"zhù", "纻":"zhù", "杼":"zhù", "贮":"zhù", "注":"zhù", "驻":"zhù", "柷":"zhù", "柱":"zhù", "炷":"zhù", "祝":"zhù", "砫":"zhù", "疰":"zhù", "著":"zhù", "蛀":"zhù", "铸":"zhù", "筑":"zhù", "翥":"zhù", "箸":"zhù",
        "抓":"zhuā", "髽":"zhuā","爪":"zhuǎ","拽":"zhuài","专":"zhuān", "䏝":"zhuān", "砖":"zhuān", "颛":"zhuān",
        "转":"zhuǎn","传":"zhuàn", "沌":"zhuàn", "转":"zhuàn", "啭":"zhuàn", "瑑":"zhuàn", "赚":"zhuàn", "僎":"zhuàn", "撰":"zhuàn", "篆":"zhuàn", "馔":"zhuàn",
        "妆":"zhuāng", "庄":"zhuāng", "桩":"zhuāng", "装":"zhuāng","奘":"zhuǎng",
        "壮":"zhuàng", "状":"zhuàng", "撞":"zhuàng", "幢":"zhuàng", "戆":"zhuàng",
        "隹":"zhuī", "追":"zhuī", "骓":"zhuī", "椎":"zhuī", "锥":"zhuī","坠":"zhuì", "缀":"zhuì", "惴":"zhuì", "缒":"zhuì", "赘":"zhuì",
        "肫":"zhūn", "窀":"zhūn", "谆":"zhūn", "衠":"zhūn","准":"zhǔn", "𬘯":"zhǔn",
        "拙":"zhuō", "捉":"zhuō", "桌":"zhuō", "倬":"zhuō", "棁":"zhuō", "涿":"zhuō", "䦃":"zhuō",
        "汋":"zhuó", "灼":"zhuó", "茁":"zhuó", "卓":"zhuó", "叕":"zhuó", "斫":"zhuó", "浊":"zhuó", "酌":"zhuó", "浞":"zhuó", "诼":"zhuó", "著":"zhuó", "䓬":"zhuó", "啄":"zhuó", "着":"zhuó", "琢":"zhuó", "椓":"zhuó", "晫":"zhuó", "禚":"zhuó", "𬸦":"zhuó", "擢":"zhuó", "濯":"zhuó", "镯":"zhuó",
        "孖":"zī", "吱":"zī", "孜":"zī", "咨":"zī", "姿":"zī", "兹":"zī", "赀":"zī", "资":"zī", "淄":"zī", "缁":"zī", "鄑":"zī", "辎":"zī", "嗞":"zī", "嵫":"zī", "粢":"zī", "孳":"zī", "滋":"zī", "趑":"zī", "觜":"zī", "锱":"zī", "龇":"zī", "镃":"zī", "鼒":"zī", "髭":"zī", "鲻":"zī",
        "子":"zǐ", "仔":"zǐ", "姊":"zǐ", "耔":"zǐ", "茈":"zǐ", "虸":"zǐ", "秭":"zǐ", "籽":"zǐ", "笫":"zǐ", "梓":"zǐ", "紫":"zǐ", "訾":"zǐ", "滓":"zǐ",
        "自":"zì", "字":"zì", "恣":"zì", "眦":"zì", "渍":"zì",
        "枞":"zōng", "宗":"zōng", "倧":"zōng", "综":"zōng", "棕":"zōng", "腙":"zōng", "踪":"zōng", "鬃":"zōng", "鬷":"zōng",
        "总":"zǒng", "偬":"zǒng","纵":"zòng", "疭":"zòng", "粽":"zòng","邹":"zōu", "驺":"zōu", "诹":"zōu", "陬":"zōu", "鄹":"zōu", "鲰":"zōu",
        "走":"zǒu","奏":"zòu", "揍":"zòu","租":"zū", "菹":"zū","足":"zú", "卒":"zú", "崒":"zú", "族":"zú", "镞":"zú",
        "诅":"zǔ", "阻":"zǔ", "组":"zǔ", "珇":"zǔ", "俎":"zǔ", "祖":"zǔ","钻":"zuān", "躜":"zuān","缵":"zuǎn", "纂":"zuǎn","钻":"zuàn", "攥":"zuàn",
        "咀":"zuǐ", "嘴":"zuǐ","最":"zuì", "罪":"zuì", "槜":"zuì", "蕞":"zuì", "醉":"zuì",
        "尊":"zūn", "嶟":"zūn", "遵":"zūn", "樽":"zūn", "𨱔":"zūn", "鳟":"zūn","僔":"zǔn", "撙":"zǔn", "噂":"zǔn","作":"zuō", "嘬":"zuō",
        "昨":"zuó", "捽":"zuó", "笮":"zuó", "琢":"zuó","左":"zuǒ", "佐":"zuǒ", "撮":"zuǒ",
        "作":"zuò", "坐":"zuò", "阼":"zuò", "岞":"zuò", "怍":"zuò", "柞":"zuò", "胙":"zuò", "祚":"zuò", "唑":"zuò", "座":"zuò", "做":"zuò", "酢":"zuò"}
        self.strona_pierwsza()
        self.show_page(self.page1)

    def strona_pierwsza(self):
        self.page1 = ttk.Frame(self)

        self.tabGeneral = ttk.Notebook(self.page1)
        self.tabGeneral.grid()

        # Zakładka numer 1 JĘZYK ROSYJSKI

        self.tab1_rus = ttk.Frame(self.tabGeneral)
        self.tabGeneral.add(self.tab1_rus, text='JĘZYK ROSYJSKI')

        self.input_label_ru = ttk.Label(
            self.tab1_rus, text="Wprowadź tekst do transliteracji\n z języka rosyjskiego na alfabet łaciński", anchor='center')
        self.input_label_ru.grid(row=0, column=0, padx=5, pady=5, columnspan=3)

        self.input_text_ru = tk.Text(self.tab1_rus, height=4, width=50)
        self.input_text_ru.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

        self.translate_button = ttk.Button(
            self.tab1_rus, text="TRANSLITERACJA", command=self.transliteracja_ru)
        self.translate_button.grid(row=2, column=0, padx=5, pady=5)

        self.keyboard_button = ttk.Button(
            self.tab1_rus, text="KLAWIATURA ROSYJSKA", command=self.show_keyboard_ru)
        self.keyboard_button.grid(row=2, column=1, padx=5, pady=5)

        self.back_button = ttk.Button(
            self.tab1_rus, text="POWRÓT DO MENU", command=self.back_to_menu, compound="right")
        self.back_button.grid(row=2, column=2, padx=5, pady=5)

        self.output_text_ru = tk.Text(self.tab1_rus, height=4, width=50)
        self.output_text_ru.grid(row=4, column=0, padx=5, pady=5, columnspan=3)

        # Zakładka numer 2 JĘZYK UKRAIŃSKI

        self.tab2_ukr = ttk.Frame(self.tabGeneral)
        self.tabGeneral.add(self.tab2_ukr, text='JĘZYK UKRAIŃSKI')

        self.input_label_ukr = ttk.Label(
            self.tab2_ukr, text="Wprowadź tekst do transliteracji\n z języka ukraińskiego na alfabet łaciński", anchor='center')
        self.input_label_ukr.grid(
            row=0, column=0, padx=5, pady=5, columnspan=3)

        self.input_text_ukr = tk.Text(self.tab2_ukr, height=4, width=50)
        self.input_text_ukr.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

        self.translate_button = ttk.Button(
            self.tab2_ukr, text="TRANSLITERACJA", command=self.transliteracja_ukr)
        self.translate_button.grid(row=2, column=0, padx=5, pady=5)

        self.keyboard_button = ttk.Button(
            self.tab2_ukr, text="KLAWIATURA UKRAIŃSKA", command=self.show_keyboard_ukr)
        self.keyboard_button.grid(row=2, column=1, padx=5, pady=5)

        self.back_button = ttk.Button(
            self.tab2_ukr, text="POWRÓT DO MENU", command=self.back_to_menu, compound="right")
        self.back_button.grid(row=2, column=2, padx=5, pady=5)

        self.output_text_ukr = tk.Text(self.tab2_ukr, height=4, width=50)
        self.output_text_ukr.grid(
            row=4, column=0, padx=5, pady=5, columnspan=3)

        # Zakładka numer 3 JĘZYK BIAŁORUSKI

        self.tab3_bel = ttk.Frame(self.tabGeneral)
        self.tabGeneral.add(self.tab3_bel, text='JĘZYK BIAŁORUSKI')

        self.input_label_bel = ttk.Label(
            self.tab3_bel, text="Wprowadź tekst do transliteracji\n z języka białoruskiego na alfabet łaciński", anchor='center')
        self.input_label_bel.grid(
            row=0, column=0, padx=5, pady=5, columnspan=3)

        self.input_text_bel = tk.Text(self.tab3_bel, height=4, width=50)
        self.input_text_bel.grid(row=1, column=0, padx=5, pady=5, columnspan=3)

        self.translate_button = ttk.Button(
            self.tab3_bel, text="TRANSLITERACJA", command=self.transliteracja_bel)
        self.translate_button.grid(row=2, column=0, padx=5, pady=5)

        self.keyboard_button = ttk.Button(
            self.tab3_bel, text="KLAWIATURA BIAŁORUSKA", command=self.show_keyboard_bel)
        self.keyboard_button.grid(row=2, column=1, padx=5, pady=5)

        self.back_button = ttk.Button(
            self.tab3_bel, text="POWRÓT DO MENU", command=self.back_to_menu, compound="right")
        self.back_button.grid(row=2, column=2, padx=5, pady=5)

        self.output_text_bel = tk.Text(self.tab3_bel, height=4, width=50)
        self.output_text_bel.grid(
            row=4, column=0, padx=5, pady=5, columnspan=3)
        
        # Zakładka numer 4 JĘZYK CHIŃSKI

        self.tab4_china = ttk.Frame(self.tabGeneral)
        self.tabGeneral.add(self.tab4_china, text='JĘZYK CHIŃSKI')

        self.input_label_china = ttk.Label(
            self.tab4_china, text="Wprowadź tekst do transliteracji\n z języka chińskiego na alfabet łaciński", anchor='center')
        self.input_label_china.grid(
            row=0, column=0, padx=5, pady=5, columnspan=2)

        self.input_text_china = tk.Text(self.tab4_china, height=4, width=50)
        self.input_text_china.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

        self.translate_button = ttk.Button(
            self.tab4_china, text="TRANSLITERACJA", command=self.transliteracja_china)
        self.translate_button.grid(row=2, column=0, padx=5, pady=5)

        self.back_button = ttk.Button(
            self.tab4_china, text="POWRÓT DO MENU", command=self.back_to_menu, compound="right")
        self.back_button.grid(row=2, column=1, padx=5, pady=5)

        self.output_text_china = tk.Text(self.tab4_china, height=4, width=50)
        self.output_text_china.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

    def transliteracja_ru(self):
        text_to_translate = self.input_text_ru.get("1.0", "end-1c")
        self.translated_text = []

        for char in text_to_translate:
            translated_char = self.all_chars_rus.get(char, char)
            self.translated_text.append(translated_char)

        self.output_text_ru.delete("1.0", "end")
        self.output_text_ru.insert("end", ''.join(self.translated_text))

    def transliteracja_china(self):
        text_to_translate = self.input_text_china.get("1.0", "end-1c")
        self.translated_text = []

        for char in text_to_translate:
            translated_char = self.all_chars_china.get(char, char)
            self.translated_text.append(translated_char)

        self.output_text_china.delete("1.0", "end")
        self.output_text_china.insert("end", ''.join(self.translated_text))

    def transliteracja_ukr(self):
        text_to_translate = self.input_text_ukr.get("1.0", "end-1c")
        self.translated_text = []

        for i, char in enumerate(text_to_translate):
            if char.lower() == "г" and i > 0 and text_to_translate[i-1].lower() == "з":
                translated_char = "gh"
            elif char.lower() == "є" and (i == 0 or text_to_translate[i-1] == " "):
                translated_char = "ye"
            elif char.lower() == "є":
                translated_char = "ie"
            elif char.lower() == "ї" and (i == 0 or text_to_translate[i-1] == " "):
                translated_char = "yi"
            elif char.lower() == "ї":
                translated_char = "i"
            elif char.lower() == "й" and (i == 0 or text_to_translate[i-1] == " "):
                translated_char = "y"
            elif char.lower() == "й":
                translated_char = "i"
            elif char.lower() == "ю" and (i == 0 or text_to_translate[i-1] == " "):
                translated_char = "yu"
            elif char.lower() == "ю":
                translated_char = "iu"
            elif char.lower() == "я" and (i == 0 or text_to_translate[i-1] == " "):
                translated_char = "ya"
            elif char.lower() == "я":
                translated_char = "ia"
            else:
                translated_char = self.all_chars_ukr.get(char, char)
            self.translated_text.append(translated_char)

        self.output_text_ukr.delete("1.0", "end")
        self.output_text_ukr.insert("end", ''.join(self.translated_text))

    def transliteracja_bel(self):
        text_to_translate = self.input_text_bel.get("1.0", "end-1c")
        self.translated_text = []
        vowels = "АЕЁІЎЫЭЮЯаеёіўыэюя"

        for i, char in enumerate(text_to_translate):
            if char.lower() == "е" and (i == 0 or text_to_translate[i-1] in vowels or text_to_translate[i-1] == "'" or
                                        (i > 1 and text_to_translate[i-2:i] in {"ў", "ь"})):
                translated_char = "je"
            elif char.lower() == "ё" and (i == 0 or text_to_translate[i-1] in vowels or text_to_translate[i-1] == "'" or
                                          (i > 1 and text_to_translate[i-2:i] in {"ў", "ь"})):
                translated_char = "jo"
            elif char.lower() == "ю" and (i == 0 or text_to_translate[i-1] in vowels or text_to_translate[i-1] == "'" or
                                          (i > 1 and text_to_translate[i-2:i] in {"ў", "ь"})):
                translated_char = "ju"
            elif char.lower() == "я" and (i == 0 or text_to_translate[i-1] in vowels or text_to_translate[i-1] == "'" or
                                          (i > 1 and text_to_translate[i-2:i] in {"ў", "ь"})):
                translated_char = "ja"
            else:
                translated_char = self.all_chars_bel.get(char, char)
            self.translated_text.append(translated_char)

        self.output_text_bel.delete("1.0", "end")
        self.output_text_bel.insert("end", ''.join(self.translated_text))

    def show_keyboard_ru(self):
        self.keyboard_frame_ru = tk.Toplevel(self)
        self.keyboard_frame_ru.title("KLAWIATURA ROSYJSKA")
        self.create_keyboard_ru(self.keyboard_frame_ru)

    def show_keyboard_ukr(self):
        self.keyboard_frame_ukr = tk.Toplevel(self)
        self.keyboard_frame_ukr.title("KLAWIATURA UKRAIŃSKA")
        self.create_keyboard_ukr(self.keyboard_frame_ukr)

    def show_keyboard_bel(self):
        self.keyboard_frame_bel = tk.Toplevel(self)
        self.keyboard_frame_bel.title("KLAWIATURA BIAŁORUSKA")
        self.create_keyboard_bel(self.keyboard_frame_bel)

    def create_keyboard_ru(self, parent):
        self.rows_small = [
            ("й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "х", "ъ"),
            ("ф", "ы", "в", "а", "п", "р", "о", "л", "д", "ж", "э"),
            ("я", "ч", "с", "м", "и", "т", "ь", "б", "ю"),
        ]
        self.rows_big = [
            ("Й", "Ц", "У", "К", "Е", "Н", "Г", "Ш", "Щ", "З", "Х", "Ъ"),
            ("Ф", "Ы", "В", "А", "П", "Р", "О", "Л", "Д", "Ж", "Э"),
            ("Я", "Ч", "С", "М", "И", "Т", "Ь", "Б", "Ю"),
        ]

        self.rows = self.rows_small

        self.update_keyboard_ru(parent)

        self.toggle_case_button = tk.Button(
            parent, text="CAPS LOCK", command=self.toggle_case_ru)
        self.toggle_case_button.grid(row=len(self.rows_big), column=0, columnspan=len(
            self.rows_big[0]), padx=5, pady=5)

    def toggle_case_ru(self):
        self.rows = self.rows_big if self.rows == self.rows_small else self.rows_small
        self.update_keyboard_ru(self.keyboard_frame_ru)

    def update_keyboard_ru(self, parent):
        for widget in parent.winfo_children():
            widget.destroy()

        for i, row in enumerate(self.rows):
            for j, char in enumerate(row):
                button = tk.Button(
                    parent, text=char, command=lambda c=char: self.insert_char_ru(c))
                button.grid(row=i, column=j, padx=5, pady=5)

        self.toggle_case_button = tk.Button(
            parent, text="CAPS LOCK", command=self.toggle_case_ru)
        self.toggle_case_button.grid(row=len(self.rows_big), column=0, columnspan=len(
            self.rows_big[0]), padx=5, pady=5)

    def create_keyboard_ukr(self, parent):
        self.rows_small = [
            ("й", "ц", "у", "к", "е", "н", "г", "ш", "щ", "з", "х", "ї", "ґ"),
            ("ф", "і", "в", "а", "п", "р", "о", "л", "д", "ж", "є"),
            ("я", "ч", "с", "м", "и", "т", "ь", "б", "ю")
        ]

        self.rows_big = [
            ("Й", "Ц", "У", "К", "Е", "Н", "Г", "Ш", "Щ", "З", "Х", "Ї", "Ґ"),
            ("Ф", "І", "В", "А", "П", "Р", "О", "Л", "Д", "Ж", "Є"),
            ("Я", "Ч", "С", "М", "И", "Т", "Ь", "Б", "Ю")
        ]

        self.rows = self.rows_small

        self.update_keyboard_ukr(parent)

        self.toggle_case_button = tk.Button(
            parent, text="CAPS LOCK", command=self.toggle_case_ukr)
        self.toggle_case_button.grid(row=len(self.rows_big), column=0, columnspan=len(
            self.rows_big[0]), padx=5, pady=5)

    def toggle_case_ukr(self):
        self.rows = self.rows_big if self.rows == self.rows_small else self.rows_small
        self.update_keyboard_ukr(self.keyboard_frame_ukr)

    def update_keyboard_ukr(self, parent):
        for widget in parent.winfo_children():
            widget.destroy()

        for i, row in enumerate(self.rows):
            for j, char in enumerate(row):
                button = tk.Button(
                    parent, text=char, command=lambda c=char: self.insert_char_ukr(c))
                button.grid(row=i, column=j, padx=5, pady=5)

        self.toggle_case_button = tk.Button(
            parent, text="CAPS LOCK", command=self.toggle_case_ukr)
        self.toggle_case_button.grid(row=len(self.rows_big), column=0, columnspan=len(
            self.rows_big[0]), padx=5, pady=5)

    def create_keyboard_bel(self, parent):
        self.rows_small = [
            ("й", "ц", "у", "к", "е", "н", "г", "ш", "ў", "з", "х", "ї", "і"),
            ("ф", "ы", "в", "а", "п", "р", "о", "л", "д", "ж", "э"),
            ("я", "ч", "с", "м", "і", "т", "ь", "б", "ю")
        ]

        self.rows_big = [
            ("Й", "Ц", "У", "К", "Е", "Н", "Г", "Ш", "Ў", "З", "Х", "Ї", "І"),
            ("Ф", "Ы", "В", "А", "П", "Р", "О", "Л", "Д", "Ж", "Э"),
            ("Я", "Ч", "С", "М", "І", "Т", "Ь", "Б", "Ю")
        ]

        self.rows = self.rows_small

        self.update_keyboard_bel(parent)

        self.toggle_case_button = tk.Button(
            parent, text="CAPS LOCK", command=self.toggle_case_bel)
        self.toggle_case_button.grid(row=len(self.rows_big), column=0, columnspan=len(
            self.rows_big[0]), padx=5, pady=5)

    def toggle_case_bel(self):
        self.rows = self.rows_big if self.rows == self.rows_small else self.rows_small
        self.update_keyboard_bel(self.keyboard_frame_bel)

    def update_keyboard_bel(self, parent):
        for widget in parent.winfo_children():
            widget.destroy()

        for i, row in enumerate(self.rows):
            for j, char in enumerate(row):
                button = tk.Button(
                    parent, text=char, command=lambda c=char: self.insert_char_bel(c))
                button.grid(row=i, column=j, padx=5, pady=5)

        self.toggle_case_button = tk.Button(
            parent, text="CAPS LOCK", command=self.toggle_case_bel)
        self.toggle_case_button.grid(row=len(self.rows_big), column=0, columnspan=len(
            self.rows_big[0]), padx=5, pady=5)

    def insert_char_ru(self, char):
        current_text = self.input_text_ru.get("1.0", "end-1c")
        self.input_text_ru.delete("1.0", "end")
        self.input_text_ru.insert("end", current_text + char)

    def insert_char_ukr(self, char):
        current_text = self.input_text_ukr.get("1.0", "end-1c")
        self.input_text_ukr.delete("1.0", "end")
        self.input_text_ukr.insert("end", current_text + char)

    def insert_char_bel(self, char):
        current_text = self.input_text_bel.get("1.0", "end-1c")
        self.input_text_bel.delete("1.0", "end")
        self.input_text_bel.insert("end", current_text + char)

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
    
