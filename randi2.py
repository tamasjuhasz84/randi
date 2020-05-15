import PySimpleGUI as sg
sg.theme("LightGrey3")

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
        with open('randi.csv', 'a') as f:
            print(f'{nev}; {telefonszam}; {eletkor}', file=f)
        
    if event in ("Keres"):
        nev = values['Név']
        telefonszam = values['Telefonszám']
        eletkor = values['Életkor']
        with open('randi.csv', 'r') as f:
            for sor in f:
                fnev, ftelefon, fkor=sor.strip().split(';')
                
                if nev == fnev:
                    window['Telefonszám'].update(ftelefon)
                    window['Életkor'].update(fkor)
        