# READ CSV FILE
def readCSV(path:str):
    data = []
    with open(path,'r') as file:
        for line in file:
            elmt = ''
            row = []
            for char in line:
                if char == ';' or char == '\n':
                    row.append(elmt)
                    elmt = ''
                else:
                    elmt = elmt + char 
            data.append(row)
    return data
# # CONTOH APLIKASI
# readCSV('data/monster.csv')

# WRITE DATA TO CSV FILE
def writeCSV(path: str, data: list):
    with open(path, 'a') as file:
        row = ''
        for i, elmt in enumerate(data):
            row += str(elmt)
            if i < len(data) - 1:
                row += ';'
        file.write(row + '\n')
# # CONTOH APLIKASI
# writeCSV('data/item_shop.csv',['healing',3,20])

# UPDATE DATA CSV
def updateCSV(path:str,dataId:int,newData:list):
    data = readCSV(path)
    updated_data = []
    for row in data:
        if row[0] == str(dataId):
            for i in range(1, len(newData)):  
                if newData[i] != '': 
                    row[i] = str(newData[i])
        updated_data.append(row)

    with open(path, 'w') as file:
        for row in updated_data:
            writeCSV(path, row)
# # CONTOH APLIKASI
# updateCSV('data/monster_shop.csv', 3, [3,'',101])

# DELETE DATA CSV
def deleteData(path:str,dataId:int):
    data = readCSV(path)
    updated_data = []
    for row in data:
        if row[0] != str(dataId):
            updated_data.append(row)
    
    with open(path, 'w') as file:
        for row in updated_data:
            writeCSV(path, row)
# CONTOH APLIKASI
# deleteData('data/monster_shop.csv',3)