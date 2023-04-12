import functions
new_data = []
fresh_data = []
def temperature():
    with open('temperature','r') as file:
        data = file.readlines()
        for i in data:
            i=i.replace("\n","")
            new_data.append(i)
        return new_data
average= temperature()
length = len(average[1:])
for j in average[1:]:
    j = int(j)
    fresh_data.append(j)
total = sum(fresh_data)
print('average temperature is:', total/length)

