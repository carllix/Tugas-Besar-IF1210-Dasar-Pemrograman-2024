from CSV_Handler import *

# READ CSV
dataMonster = readCSV('data/monster.csv')
dataItemInventory = readCSV('data/item_inventory.csv')
dataMonsterInventory = readCSV('data/monster_inventory.csv')

# Nanti userId dan oc ambil dari login (return dataUser)
userId = '2'
oc = '9999'

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

# F07 - Inventory
def inventory(dataMonster:list,dataItemInventory:list,dataMonsterInventory:list,userId:str):
    print(f'============ INVENTORY LIST (User ID: {userId}) ============')
    print(f'Jumlah O.W.C.A Coin-mu sekarang {oc}.')
    
    listInventory:list = []

    # MENAMPILKAN LIST INVENTORY MONSTER, POTION, DAN MONSTER BALL
    idx:int = 1
    # LIST MONSTER
    for monster in dataMonsterInventory:
        if monster[0] == userId:
            idMonster:str = monster[1]
            level:str = monster[2]
            listInventory.append(['Monster',idMonster,level])

            # Display
            infoMonster:list = getInfoMonsterByIdMonster(idMonster,dataMonster)
            print(f'{idx}.{"":<2}{"Monster":<14} (Name: {infoMonster[1]}, Lvl: {level}, HP: {infoMonster[4]})')
            idx+=1

    # LIST POTION
    for item in dataItemInventory:
        if item[0] == userId and item[1]!='monster_ball':
            listInventory.append(['Potion',item[1],item[2]])

            # Display
            print(f'{idx}.{"":<2}{"Potion":<14} (Type: {item[1].capitalize()}, Qty: {item[2]})')
            idx+=1

    # LIST MONSTER BALL
    for item in dataItemInventory[1:]:
        if item[0] == userId and item[1]=='monster_ball':
            listInventory.append(['Monster Ball',item[1],item[2]])

            # Display
            print(f'{idx}.{"":<2}{"Monster Ball":<14} (Qty: {item[2]})')
            idx+=1

    while True:
        # Input id untuk menampilkan detail item
        print('\nKetikkan id untuk menampilkan detail item:')
        id:str = input('>>> ').upper()
        
        # Mekanisme untuk keluar dari inventory
        if id == 'KELUAR':
            break

        # Validasi input id
        if isNum(id)==False:
            print('id tidak valid!')
        else:
            if int(id)<1 or int(id)>len(listInventory):
                print('id tidak valid!')
            else:
                detailItem:list = listInventory[int(id)-1]
                if detailItem[0] == 'Monster':
                    idMonster:str = detailItem[1]
                    infoMonster:list = getInfoMonsterByIdMonster(idMonster,dataMonster)
                    print(f'{"Name":<11}: {infoMonster[1]}')
                    print(f'{"ATK Power":<11}: {infoMonster[2]}')
                    print(f'{"DEF Power":<11}: {infoMonster[3]}')
                    print(f'{"HP":<11}: {infoMonster[4]}')
                    print(f'{"Level":<11}: {detailItem[2]}')
                elif detailItem[0] == 'Potion':
                    print(f'{"Type":<11}: {detailItem[1].capitalize()}')
                    print(f'{"Quantitiy":<11}: {detailItem[2]}')
                else:
                    print(f'{"Quantitiy":<11}: {detailItem[2]}')

inventory(dataMonster,dataItemInventory,dataMonsterInventory,userId)