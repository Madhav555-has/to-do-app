import PySimpleGUI as sg
import zip_creator as zp
label1 = sg.Text("Select Files to compress")
input_box1 = sg.InputText(tooltip="Select the file", key="Files")
add_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder")
input_box2 = sg.InputText(tooltip="destination folder", key="Folder")
add_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

windows = sg.Window('File Zipper', layout=[[label1, input_box1, add_button1],
                                           [label2, input_box2, add_button2],
                                           [compress_button]])

while True:
    event,value = windows.read()
    print(event,value)
    filepath = value["Files"].split(";")
    folderpath = value["Folder"]
    zp.make_archive(filepath, folderpath)
windows.close()