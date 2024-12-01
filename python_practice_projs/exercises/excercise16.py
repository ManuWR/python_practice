import FreeSimpleGUI as sg

label1 = sg.Text("Enter feet")
feet_box = sg.Input()

label2 = sg.Text("Enter inches")
inches_box = sg.Input()

button = sg.Button("Convert")

window = sg.Window("Convertor", 
                   layout=[[label1, feet_box],
                           [label2, inches_box],
                           [button]])
window.read()
window.close()