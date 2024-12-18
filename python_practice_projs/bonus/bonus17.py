import FreeSimpleGUI as sg
from converters14 import convert

feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input(key="feet")

inch_label = sg.Text("Enter inches: ")
inch_input = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text(key="output")

window = sg.Window("Convertor", 
                   layout=[[feet_label, feet_input],
                           [inch_label, inch_input],
                           [convert_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    feet = float(values["feet"])
    inches = float(values["inches"])
    result = convert(feet, inches)
    window["output"].update(value=f"{result} m", text_color="orange")

window.close()