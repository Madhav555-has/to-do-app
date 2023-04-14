import PySimpleGUI as sg
label1 = sg.Text("Select Files to compress")
input_box1 = sg.InputText(tooltip="Select the file")
add_button1 = sg.FileBrowse("Choose")

label2 = sg.Text("Select destination folder")
input_box2 = sg.InputText(tooltip="destination folder")
add_button2 = sg.FileBrowse("Choose")

windows = sg.Window('File Zipper', layout=[[label1, input_box1, add_button1],[label2, input_box2, add_button2]])
windows.read()
windows.close()