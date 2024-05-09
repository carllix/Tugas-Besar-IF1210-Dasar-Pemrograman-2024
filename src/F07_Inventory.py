def inventory(dataUser,dataMonster,dataItemInventory,dataMonsterInventory,userId):
    print(f'============ INVENTORY LIST (User ID: {userId})============')
    print(f'Jumlah O.W.C.A Coin-mu sekarang {dataUser[int(userId)][4]}.')
    
    listInventory = []

    # MENAMPILKAN LIST INVENTORY MONSTER, POTION, DAN MONSTER BALL
    x = 1
    # LIST MONSTER
    for i in range(1,len(dataMonsterInventory)):
        if dataMonsterInventory[i][0] == userId:
            jenis = 'Monster'
            monsterId = int(dataMonsterInventory[i][1])
            listInventory.append([jenis, monsterId, dataMonsterInventory[i][2]])

            print(f'{x}. {jenis}\t (Name: {dataMonster[monsterId][1]}, Lvl: {dataMonsterInventory[i][2]}, HP: {dataMonster[monsterId][4]})')
            x+=1

    # LIST POTION
    for i in range(1, len(dataItemInventory)):
        if dataItemInventory[i][0] == userId:
            if dataItemInventory[i][1] != 'monster_ball':
                jenis = 'Potion'
                listInventory.append([jenis,[dataItemInventory[i][1],dataItemInventory[i][2]]])

                print(f'{x}. {jenis}\t (Type: {dataItemInventory[i][1]}, Qty: {dataItemInventory[i][2]})')
                x+=1

    # LIST MONSTER BALL
    for i in range(1, len(dataItemInventory)):
        if dataItemInventory[i][0] == userId:
            if dataItemInventory[i][1] == 'monster_ball':
                jenis = 'Monster Ball'
                listInventory.append([jenis,dataItemInventory[i][2]])

                print(f'{x}. {jenis}\t (Qty: {dataItemInventory[i][2]})')
                x+=1

    while True:
        # Input id untuk menampilkan detail item
        print('\nKetikkan id untuk menampilkan detail item:')
        id = input('>>> ')
        
        # Mekanisme untuk keluar dari inventory
        if id == 'KELUAR':
            break
        
        # Cek apakah id merupakan angka
        isNumber = True
        for char in id:
            if ord(char)<48 or ord(char)>57:
                isNumber = False
                break

        # Validasi input id
        if isNumber==False:
            print('id tidak valid!')
        else: # isNumber == True
            if int(id)<1 or int(id)>len(listInventory):
                print('id tidak valid!')
            else:
                detailItem = listInventory[int(id)-1]
                print(detailItem[0])
                if detailItem[0] == 'Monster':
                    idMonster = detailItem[1]
                    print(f'Name\t\t: {dataMonster[idMonster][1]}')
                    print(f'ATK Power\t: {dataMonster[idMonster][2]}')
                    print(f'DEF Power\t: {dataMonster[idMonster][3]}')
                    print(f'HP\t\t: {dataMonster[idMonster][4]}')
                    print(f'Level\t\t: {detailItem[2]}')
                elif detailItem[0] == 'Potion':
                    print(f'Type\t\t: {detailItem[1][0]}')
                    print(f'Quantity\t: {detailItem[1][1]}')
                else:
                    print(f'Quantity\t: {detailItem[1]}')