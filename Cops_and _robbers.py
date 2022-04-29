import PySimpleGUI as sg
TURNS_NUMBER=15
MAX_ROWS = MAX_COL = 8
theif='C:\\Users\TEMP\Pictures\\theif.png'

def cop_move(cop_location,robber_location):
    new_location=[cop_location[0],cop_location[1]]
    if abs(cop_location[0]-robber_location[0])>abs(cop_location[1]-robber_location[1]):
        new_location[0]= new_location[0]+(robber_location[0]-cop_location[0])//abs(robber_location[0]-cop_location[0])
    else:
        new_location[1]= new_location[1]+(robber_location[1]-cop_location[1])//abs(cop_location[1]-robber_location[1])
    return (new_location[0],new_location[1])

color={0:"White",1:"Black"}
layout =  [sg.Text("Please choose the place of the robber",color,key="-INSTRUCTIONS-",text_color="Black",font='Any 20',	justification="center")],[[sg.Button('',button_color=(color[(i+j)%2],color[(i+j+1)%2]), size=(8, 4), key=(i,j), pad=(0,0)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]
window = sg.Window('Cops and robbers', layout)
while True:
    event, values = window.read()
    robber_location=event
    window[event].update("R")
    window["-INSTRUCTIONS-"].update("Please choose the place of the cop")
    event, values = window.read()
    cop_location=event
    window[event].update("C")

    for k in range(TURNS_NUMBER,0,-1):
        window["-INSTRUCTIONS-"].update(f"{k} turns left",text_color="Black")
        # Robbers turn
        event, values = window.read()
        while abs(robber_location[0]-event[0])+abs(robber_location[1]-event[1])!=1  or cop_location == event:
            window["-INSTRUCTIONS-"].update("Iligal move",text_color="Red")
            event, values = window.read()
        window[robber_location].update("")
        robber_location = event
        window[robber_location].update("R")
        # Cops turn
        event, values = window.read(timeout=500)
        window[cop_location].update("")
        cop_location=cop_move(cop_location,robber_location)
        window[cop_location].update("C")
        # Check winning of the cop
        if cop_location == robber_location:
            window["-INSTRUCTIONS-"].update("Cop win! click anywhere to restart",text_color="Black")
            break
    # Check winning of the robber
    if cop_location != robber_location:
        window["-INSTRUCTIONS-"].update("Robber win! click anywhere to restart",text_color="Black")
    window[cop_location].update("")
    window[robber_location].update("")
    event, values = window.read()
    window["-INSTRUCTIONS-"].update("Please choose the place of the robber")


    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    # window[(row, col)].update('New text')   # To change a button's text, use this pattern
    # For this example, change the text of the button to the board's value and turn color black
window.close()