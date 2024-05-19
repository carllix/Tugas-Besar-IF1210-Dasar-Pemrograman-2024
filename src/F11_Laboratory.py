from src.Important_Function import *
from src.F08_Battle import *

# F11 - LABORATORY
def laboratory(dataMonsterInventory:list,dataMonster:list,userId:int,coin:int) -> int:
    print('\n===========================================================================================================')
    print('''
                    ░█─── ─█▀▀█ ░█▀▀█ ░█▀▀▀█ ░█▀▀█ ─█▀▀█ ▀▀█▀▀ ░█▀▀▀█ ░█▀▀█ ░█──░█ 
                    ░█─── ░█▄▄█ ░█▀▀▄ ░█──░█ ░█▄▄▀ ░█▄▄█ ─░█── ░█──░█ ░█▄▄▀ ░█▄▄▄█ 
                    ░█▄▄█ ░█─░█ ░█▄▄█ ░█▄▄▄█ ░█─░█ ░█─░█ ─░█── ░█▄▄▄█ ░█─░█ ──░█──''')
    print('\n===========================================================================================================')
    print('\nSelamat Datang di Laboratory O.W.C.A!')
    print(f'\nJumlah O.W.C.A. Coin-mu sekarang: {coin} OC')

    # Menampilkan Upgrade Price
    print('\n============ UPGRADE PRICE ============')
    print('1. Level 1 -> Level 2: 200 OC')
    print('2. Level 2 -> Level 3: 400 OC')
    print('3. Level 3 -> Level 4: 600 OC')
    print('4. Level 4 -> Level 5: 800 OC')

    # Menampilkan Monster pada Inventory
    print('\n============ MONSTER LIST ============')
    allMonsterAgent = getMonsterAgent(dataMonsterInventory,dataMonster,userId)
    x = 1
    for monster in allMonsterAgent:
        print(f'{x}. {monster[0]} (Level: {monster[4]})')
        x+=1

    # Validasi Pilihan Monster
    while True:
        pilihMonster = input('\nPilih monster: ')
        if isNum(pilihMonster) == False:
            print('Pilihan tidak valid!')
        else:
            if 1<=int(pilihMonster)<=len(allMonsterAgent):
                break
            else:
                print('Pilihan nomor tidak tersedia!')

    monster = allMonsterAgent[int(pilihMonster)-1]
    nameMonster = monster[0]
    level = int(monster[4])
    if level == 5:
        print('\nMaaf, monster yang Anda pilih sudah memiliki level maksimum')
    else:
        print(f'\n{nameMonster} akan di-upgrade ke level {level+1}.')

        # Menampilkan Harga Upgrade Berdasarkan Level
        if level == 1:
            price = 200
        elif level == 2:
            price = 400
        elif level == 3:
            price = 600
        else: # level == 4:
            price = 800
        print(f'Harga untuk melakukan upgrade {nameMonster} adalah {price} OC.')

        # Konfirmasi Upgrade
        while True:
            confirm = input('\nLanjutkan upgrade (Y/N): ').upper()
            if confirm == 'Y':
                if coin<price:
                    print(f'\nMaaf OC Anda tidak cukup untuk melakukan upgrade {nameMonster}.')
                else:
                    coin -= price
                    level+=1
                    allMonsterAgent[int(pilihMonster)-1][4] = level
                    print(f'\nSelamat, {nameMonster} berhasil di-upgrade ke level {level} !')
                break
            elif confirm == 'N':
                print(f'\nYah sayang sekali Anda tidak jadi melakukan upgrade terhadap {nameMonster}:(')
                break
            else:
                print('Konfirmasi tidak valid !')
    
    
    # Merubah level monster pada data monster inventory
    for row in dataMonsterInventory:
        if row[0] == str(userId):
            nameMonster = getDataById(row[1],dataMonster)[1]
            for monster in allMonsterAgent:
                if monster[0] == nameMonster:
                    row[2] = monster[4]
            
    return coin