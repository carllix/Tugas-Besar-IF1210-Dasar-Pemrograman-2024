from src.Important_Function import *

# F07 - INVENTORY
def inventory(dataMonster:list,dataItemInventory:list,dataMonsterInventory:list,userId:int,coin:int,username:str):
    print('\n=================================================================================================================')
    print('''
                        ▀█▀ ░█▄─░█ ░█──░█ ░█▀▀▀ ░█▄─░█ ▀▀█▀▀ ░█▀▀▀█ ░█▀▀█ ░█──░█ 
                        ░█─ ░█░█░█ ─░█░█─ ░█▀▀▀ ░█░█░█ ─░█── ░█──░█ ░█▄▄▀ ░█▄▄▄█ 
                        ▄█▄ ░█──▀█ ──▀▄▀─ ░█▄▄▄ ░█──▀█ ─░█── ░█▄▄▄█ ░█─░█ ──░█──''')
    print('\n=================================================================================================================')
    print(f'\n============ INVENTORY LIST (User ID: {userId}) ============')
    print(f'Jumlah O.W.C.A Coin-mu sekarang {coin} OC.')
    
    listInventory:list = []

    # MENAMPILKAN LIST INVENTORY MONSTER, POTION, DAN MONSTER BALL
    idx:int = 1
    # LIST MONSTER
    for monster in dataMonsterInventory:
        if monster[0] == str(userId):
            idMonster:str = monster[1]
            level:str = monster[2]
            listInventory.append(['Monster',idMonster,level])

            # Display
            infoMonster:list = getDataById(idMonster,dataMonster)
            print(f'{idx}.{"":<2}{"Monster":<14} (Name: {infoMonster[1]}, Lvl: {level}, HP: {infoMonster[4]})')
            idx+=1

    # LIST POTION
    for item in dataItemInventory:
        if item[0] == str(userId) and item[1]!='monster_ball':
            listInventory.append(['Potion',item[1],item[2]])

            # Display
            print(f'{idx}.{"":<2}{"Potion":<14} (Type: {item[1].capitalize()}, Qty: {item[2]})')
            idx+=1

    # LIST MONSTER BALL
    for item in dataItemInventory[1:]:
        if item[0] == str(userId) and item[1]=='monster_ball':
            listInventory.append(['Monster Ball',item[1],item[2]])

            # Display
            print(f'{idx}.{"":<2}{"Monster Ball":<14} (Qty: {item[2]})')
            idx+=1

    while True:
        # Input id untuk menampilkan detail item
        print('\nKetikkan id untuk menampilkan detail item :')
        print('(Ketik "KELUAR" jika ingin keluar dari INVENTORY)')
        id:str = input('\n>>> ').upper()
        
        # Mekanisme untuk keluar dari inventory
        if id == 'KELUAR':
            print(f'\nSampai Jumpa Lagi Agent {username} !!!')
            break
        else:
            # Validasi input id
            if isNum(id)==False:
                print('id tidak valid!')
            else:
                if int(id)<1 or int(id)>len(listInventory):
                    print('id tidak valid!')
                else:
                    detailItem:list = listInventory[int(id)-1]
                    print(f'\n{detailItem[0]}')
                    if detailItem[0] == 'Monster':
                        idMonster:str = detailItem[1]
                        infoMonster:list = getDataById(idMonster,dataMonster)
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