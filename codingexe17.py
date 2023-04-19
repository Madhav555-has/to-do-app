import PySimpleGUI as sg

def feet_inches(feet,inches):
    return 0.3048 * feet + 0.0254 * inches


label1 = sg.Text("Enter Foot:")
input_box1 = sg.InputText(tooltip="Enter the feet you want to convert", key="feet")

label2 = sg.Text("Enter inches:")
input_box2 = sg.InputText(tooltip="Enter the inches you want to convert", key="inches")

output_label = sg.Text("", key="output")

convert_button = sg.Button("convert")

windows = sg.Window('Convertor', layout=[[label1, input_box1],
                                         [label2, input_box2,],
                                         [convert_button, output_label]])
while True:
    event,value = windows.read()
    print(event,value)
    match event:
        case 'convert':
            feet = float(value["feet"])
            inches = float(value["inches"])
            result = feet_inches(feet, inches)
            windows['output'].update(value=f"{result} m", text_color="white")

        case sg.WIN_CLOSED:
            break

windows.close()