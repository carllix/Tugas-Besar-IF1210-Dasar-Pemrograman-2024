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

# Mendapatkan data berdasarkan ID
def getDataById(id:str,data:str) -> list:
    for row in data:
        if row[0] == id:
            return row

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

# get New Id
def newId(data:list) -> int:
    maxID:int = 0
    for row in data[1:]:
        if int(row[0])>maxID:
            maxID = int(row[0])
    return maxID+1

# Load bayangan
def load():
    dataUser = readCSV('data/user.csv')
    dataMonster = readCSV('data/monster.csv')
    dataMonsterInventory = readCSV('data/monster_inventory.csv')
    dataItemInventory = readCSV('data/item_inventory.csv')
    dataMonsterShop = readCSV('data/monster_shop.csv')
    dataItemShop = readCSV('data/item_shop.csv')
    return dataUser, dataMonster, dataMonsterInventory, dataItemInventory, dataMonsterShop, dataItemShop
