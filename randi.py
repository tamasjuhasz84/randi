import PySimpleGUI as sg
import sqlite3
sg.theme("LightGrey3")

conn = sqlite3.connect("randi.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS tb(nev TEXT, telefonszam TEXT, eletkor INTEGER)")
conn.commit()

col1=[

    [sg.Text('Név:' )],
    [sg.Text('Telefonszám:' )],
    [sg.Text('Életkor:' )],
    [sg.Button('Keres')]
    ]

col2=[

    [sg.Input(key='Név')],
    [sg.Input(key='Telefonszám')],
    [sg.Input(key='Életkor')],
    [sg.Button('Ment')]
    ]

layout= [
    [sg.Column(col1),sg.Column(col2)]
    ]


window = sg.Window("Randi",layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (None, "Exit"):
        break
    
    if event in ("Ment"):
        nev = values['Név']
        telefonszam = values['Telefonszám']
        eletkor = values['Életkor']
        c.execute("INSERT INTO tb VALUES(?,?,?)",(nev,telefonszam,eletkor))
        conn.commit()
        
    if event in ("Keres"):
        nev = values['Név']
        telefonszam = values['Telefonszám']
        eletkor = values['Életkor']
        c.execute("SELECT * FROM tb WHERE nev LIKE ?",(nev,))
        eredmeny=c.fetchall()
        nev=eredmeny[0][0]
        telefonszam=eredmeny[0][1]
        eletkor=eredmeny[0][2]
        window['Név'].update(nev)
        window['Telefonszám'].update(telefonszam)
        window['Életkor'].update(eletkor)
        
        print(eredmeny)