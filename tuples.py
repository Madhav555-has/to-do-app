filename = ["Rawdata.txt", "Reports.txt", "presentation.txt"]
newfilename = []
for files in filename:
    files = files.replace('.' , '-')
    newfilename.append(files)
print(newfilename)
