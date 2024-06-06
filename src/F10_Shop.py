from src.Important_Function import *

# Mengecek Apakah Monster Ada di Inventory Agent
def isMonsterExistInInventory(userId:int,idMonster:str,dataMonsterInventory:list) -> bool:
    for monster in dataMonsterInventory:
        if monster[0] == str(userId):
            if monster[1] == idMonster:
                return True
    return False

# Mengecek Apakah Potion Ada di Inventory Agent
def isPotionExistInInventory(userId:int,namePotion:str,dataItemInventory:list) -> bool:
    for potion in dataItemInventory:
        if potion[0] == str(userId):
            if potion[1] == namePotion:
                return True
    return False

# F10 - SHOP
def shop(dataMonster:list,dataMonsterShop:list,dataItemShop:list,dataMonsterInventory:list,dataItemInventory:list,coin:int,userId:int):
    print('\n===========================================================================================================')
    print('''
                                    ░█▀▀▀█ ░█─░█ ░█▀▀▀█ ░█▀▀█ 
                                    ─▀▀▀▄▄ ░█▀▀█ ░█──░█ ░█▄▄█ 
                                    ░█▄▄▄█ ░█─░█ ░█▄▄▄█ ░█───''')
    print('\n===========================================================================================================')
    print('\nSelamat datang di Mr. Yanto SHOP !!!')

    while True:
        action = input('\n>>> Pilih aksi (LIHAT/BELI/KELUAR): ').upper()
        if action == 'LIHAT':
            while True:
                option = input('\n>>> Mau lihat apa? (MONSTER/POTION): ').upper()
                if option == 'MONSTER':
                    displayMonsterShop(dataMonsterShop,dataMonster)
                    break
                elif option == 'POTION':
                    displayPotionShop(dataItemShop)
                    break
                else:
                    print('Pilihan tidak valid!')

        elif action == 'BELI':
            print(f'\nJumlah O.W.C.A. Coin-mu sekarang {coin} OC.')
            while True:
                option = input('\n>>> Mau beli apa? (MONSTER/POTION): ').upper()
                if option == 'MONSTER':
                    displayMonsterShop(dataMonsterShop,dataMonster)

                    if len(dataMonsterShop)-1>0:
                        # Validasi input id monster
                        while True:
                            idMonster = input('\n>>> Masukkan id monster: ')
                            isValid = False
                            for monster in dataMonsterShop:
                                if monster[0] == idMonster:
                                    isValid = True
                                    break
                            if isValid == True:
                                break
                            else:
                                print('Id Monster tidak valid!')

                        nameMonster:str = getDataById(idMonster,dataMonster)[1]
                        price:int = int(getDataById(idMonster,dataMonsterShop)[2])
                        stock:int = int(getDataById(idMonster,dataMonsterShop)[1])
                        

                        # Cek apakah monster yang akan dibeli ada pada inventory
                        if isMonsterExistInInventory(userId,idMonster,dataMonsterInventory) == True:
                            print(f'\nMonster {nameMonster} sudah ada dalam inventory-mu! Pembelian dibatalkan.')
                        else:
                            if coin<price:
                                print(f'\nO.W.C.A Coin Anda tidak cukup untuk membeli {nameMonster}.')
                            else:
                                if stock>0:
                                    print(f'\nBerhasil membeli item: {nameMonster}. Item sudah masuk ke inventory-mu!')
                                    coin-=price
                                    stock-=1
                                    # Ubah Stok Monster Pada Shop
                                    for monster in dataMonsterShop:
                                        if monster[0] == idMonster:
                                            monster[1] = stock
                                    # Menambahkan monster baru ke data monster inventory
                                    dataMonsterInventory.append([str(userId),idMonster,'1'])

                                else:
                                    print(f'\nYahh stok {nameMonster} pada shop sudah habis..')
                    else:
                        print('\nTidak ada monster yang dapat dibeli...')
                    break
                elif option == 'POTION':
                    displayPotionShop(dataItemShop)

                    if len(dataItemShop)-1>0:
                        # Validasi input id potion
                        while True:
                            idPotion:str = input('\n>>> Masukkan id potion: ')
                            if isNum(idPotion)==False:
                                print('Id Potion tidak valid!')
                            else:
                                if 1<=int(idPotion)<=len(dataItemShop)-1:
                                    break
                                else:
                                    print('Id Potion tidak valid!')

                        namePotion = dataItemShop[int(idPotion)][0]
                        stock = int(dataItemShop[int(idPotion)][1])
                        price = int(dataItemShop[int(idPotion)][2])

                        # Validasi kuantitas pembelian
                        while True:
                            quantity = input('\n>>> Masukkan jumlah: ')
                            if isNum(quantity)==False:
                                print('Jumlah tidak valid!')
                            else:
                                quantity = int(quantity)
                                if 1<=quantity<=stock:
                                    break
                                elif quantity>stock:
                                    if stock == 0:
                                        break
                                    else:
                                        print(f'Stok {namePotion} Potion pada shop tidak mencukupi')
                                else:
                                    print('Jumlah tidak valid!')
                        
                        # Cek apakah potion yang akan dibeli ada pada inventory
                        if coin<quantity*price:
                            print(f'\nO.W.C.A Coin Anda tidak cukup untuk membeli {quantity} {namePotion} Potion.')
                        else:
                            if stock>0:
                                print(f'\nBerhasil membeli item: {quantity} {namePotion} Potion. Item sudah masuk ke inventory-mu!')
                                coin-=quantity*price
                                stock-=quantity
                                # Ubah Stok Potion Pada Shop
                                for potion in dataItemShop:
                                    if potion[0] == namePotion:
                                        potion[1] = stock
                                # Memperbarui jumlah potion ke data item inventory
                                if isPotionExistInInventory(userId,namePotion,dataItemInventory)==True: # Jika sudah ada
                                    for potionInvent in dataItemInventory:
                                        if potionInvent[0] == str(userId) and potionInvent[1] == namePotion:
                                            potionInvent[2] = str(int(potionInvent[2])+quantity)
                                else:
                                    dataItemInventory.append([str(userId),namePotion,str(quantity)])
                            else:
                                print(f'\nYahh stok {namePotion} Potion pada shop sudah habis..')
                    else:
                        print('\nTidak ada potion yang dapat dibeli...')
                    break
                else:
                    print('Pilihan tidak valid!')
        elif action == 'KELUAR':
            print('\nTerima kasih telah berkunjung di Mr. Yanto SHOP, sering-sering ya belanja disini !!! ')
            break
        else:
            print('\nAksi tidak valid!')
    
    return coin