# Membaca CSV File sebagai matriks
def readCSV(path:str) -> list:
    data:list = []
    with open(path,'r') as file:
        for line in file:
            elmt:str = ''
            row:list = []
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

# Menulis matriks ke CSV file
def writeCSV(path:str,data:list):
    with open(path, 'a') as file:
        row:str = ''
        for i, elmt in enumerate(data):
            row += str(elmt)
            if i < len(data) - 1:
                row += ';'
        file.write(row + '\n')
# # CONTOH APLIKASI
# writeCSV('data/item_shop.csv',['healing',3,20])

# Memperbarui CSV
def updateCSV(path:str,dataId:str,newData:list):
    data:list = readCSV(path)
    updated_data:str = []
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
# def deleteData(path:str,dataId:int):
#     data = readCSV(path)
#     updated_data = []
#     for row in data:
#         if row[0] != str(dataId):
#             updated_data.append(row)
    
#     with open(path, 'w') as file:
#         for row in updated_data:
#             writeCSV(path, row)
# CONTOH APLIKASI
# deleteData('data/monster_shop.csv',3)

# Mengecek apakah angka
def isNum(x:str) -> bool:
    if not x: # Kasus string kosong
        return False
    for char in x:
        if ord(char)<48 or ord(char)>57:
            return False
    return True

# Mendapatkan data monster berdasarkan id monster
def getInfoMonsterByIdMonster(idMonster:str,dataMonster:list) -> list: 
    for monster in dataMonster:
        if monster[0] == idMonster:
            return monster

# Menghapus data
def deleteData(dataX:list,delId:str) -> list:
    newData:list = []
    for data in dataX:
        if data[0] != delId:
            newData.append(data)
    return newData

# Memperbarui data
def updateData(dataX:list,updateIdX:str,newData:list) -> list:
    updateData = []
    for data in dataX:
        if data[0] == str(updateIdX):
            for i in range(1, len(newData)):  
                if newData[i] != '': 
                    data[i] = str(newData[i])
        updateData.append(data)
    return updateData