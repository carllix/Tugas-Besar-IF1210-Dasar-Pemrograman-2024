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

# Menampilkan monster yang terdaftar di Shop
def displayMonsterShop(dataMonsterShop:list,dataMonster:list):
    if len(dataMonsterShop)-1>0:
        print(f"\n{'ID':<3} | {'Type':<15} | {'ATK Power':<9} | {'DEF Power':<9} | {'HP':<5} | {'Stok':<5} | Harga")
        for monster in dataMonsterShop[1:]:
            idMonster:str = monster[0]
            infoMonster:list = getDataById(idMonster,dataMonster)
            print(f"{infoMonster[0]:<3} | {infoMonster[1]:<15} | {infoMonster[2]:<9} | {infoMonster[3]:<9} | {infoMonster[4]:<5} | {monster[1]:<5} | {monster[2]}")
    else:
        print('\nTidak ada data monster pada shop...')

# Menampilkan potion yang terdaftar di Shop
def displayPotionShop(dataItemShop:list):
    if len(dataItemShop)-1>0:
        print(f"\n{'ID':<3} | {'Type':<20} | {'Stok':<5} | Harga")
        i = 1
        for potion in dataItemShop[1:]:
            print(f"{i:<3} | {f'{potion[0].capitalize()} Potion':<20} | {potion[1]:<5} | {potion[2]}")
            i+=1
    else:
        print('\nTidak ada data potion pada shop...')