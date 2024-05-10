from CSV_Handler import *

dataItemShop = readCSV('data/item_shop.csv')
dataMonsterShop = readCSV('data/monster_shop.csv')
dataMonster = readCSV('data/monster.csv')
dataPotion = ['strength','resilience','healing']
updateDataMonster = []
updateDataItem = []
deleteDataMonster = []
deleteDataItem = []

def isNum(x):
    if not x: # Kasus string kosong
        return False
    for char in x:
        if ord(char)<48 or ord(char)>57:
            return False
    return True

def getInfoMonsterFromIdMonster(i,dataMonsterShop,dataMonster):
    monsterId = dataMonsterShop[i][0]
    for j in range(len(dataMonster)):
        if dataMonster[j][0] == monsterId:
            infoMonster = dataMonster[j]
    return infoMonster

def getMonsterNotInShop(dataMonsterShop,dataMonster):
    monsterNotInShop = []
    for i in range(1,len(dataMonster)):
        isFound = False
        for j in range(1,len(dataMonsterShop)):
            if dataMonster[i][0] == dataMonsterShop[j][0]:
                isFound = True
                break
        # Jika tidak ditemukan id monster pada monster_shop, maka akan ditambahkan ke dalam list monsterNotInShop
        if isFound == False:
            monsterNotInShop.append(dataMonster[i])
    return monsterNotInShop

def getPotionNotInShop(dataPotion):
    potionNotInShop = []
    for i in range(len(dataPotion)):
        isFound = False
        for j in range(1,len(dataItemShop)):
            if dataPotion[i] == dataItemShop[j][0]:
                isFound = True
                break
         # Jika tidak ditemukan potion pada item_shop, maka akan ditambahkan ke dalam list potionNotInShop
        if isFound == False:
            potionNotInShop.append(dataPotion[i])
    return potionNotInShop

def displayMonsterShop(dataMonsterShop,dataMonster):
    print(f"{'ID':<3} | {'Type':<15} | {'ATK Power':<9} | {'DEF Power':<9} | {'HP':<5} | {'Stok':<5} | Harga")
    for i in range(1,len(dataMonsterShop)):
        infoMonster = getInfoMonsterFromIdMonster(i,dataMonsterShop,dataMonster)
        print(f"{dataMonsterShop[i][0]:<3} | {infoMonster[1]:<15} | {infoMonster[2]:<9} | {infoMonster[3]:<9} | {infoMonster[4]:<5} | {dataMonsterShop[i][1]:<5} | {dataMonsterShop[i][2]}")

def displayPotionShop(dataItemShop):
    print(f"{'ID':<3} | {'Type':<20} | {'Stok':<5} | Harga")
    for i in range(1,len(dataItemShop)):
        print(f"{i:<3} | {f'{dataItemShop[i][0]} Potion':<20} | {dataItemShop[i][1]:<5} | {dataItemShop[i][2]}")

# F12 - SHOP MANAGEMENT
def shopManagement(dataItemShop,dataMonsterShop,dataMonster):
    print('Welkamm!\n')

    action = input('>>> Pilih aksi (lihat/tambah/ubah/hapus/keluar): ')
    
    while action != 'keluar':
        if action == 'lihat':
            option = ''
            while option!='monster' and option!='potion':
                option = input('>>> Mau lihat apa? (monster/potion): ')

                if option == 'monster': # Melihat monster yang terdaftar di Shop
                    displayMonsterShop(dataMonsterShop,dataMonster)
                elif option == 'potion': # Melihat potion yang terdaftar di Shop
                    displayPotionShop(dataItemShop)
                else:
                    print('Input tidak valid!')

        elif action == 'tambah':
            option = ''
            while option!='monster' and option!='potion':
                option = input('>>> Mau nambahin apa? (monster/potion): ')

                # Menambah monster yang akan di jual
                if option == 'monster':
                    # Menampilkan seluruh monster yang ada di database tetapi belum ada pada shop
                    monsterNotInShop = getMonsterNotInShop(dataMonsterShop,dataMonster)
                    print(f"{'ID':<3} | {'Type':<15} | {'ATK Power':<9} | {'DEF Power':<9} | {'HP':<5}")
                    for i in range(len(monsterNotInShop)):
                        print(f"{monsterNotInShop[i][0]:<3} | {monsterNotInShop[i][1]:<15} | {monsterNotInShop[i][2]:<9} | {monsterNotInShop[i][3]:<9} | {monsterNotInShop[i][4]:<5}")
                    # Validasi input id monster
                    while True:
                        newIdMonster = input('>>> Masukkan id monster: ')
                        isValid = False
                        for monster in monsterNotInShop:
                            if monster[0] == newIdMonster:
                                isValid = True
                                break
                        if isValid == True:
                            break
                        else:
                            print('Id Monster tidak valid!')
                    # Validasi stok awal
                    while True:
                        stock = input('>>> Masukkan stok awal: ')
                        if isNum(stock) == True:
                            break
                        else:
                            print('Stok tidak valid')
                    # Validasi harga
                    while True:
                        price = input('>>> Masukkan harga: ')
                        if isNum(price) == True:
                            break
                        else:
                            print('Harga tidak valid')
                            
                    # Tambah data baru ke dataMonsterShop
                    newMonsterShop = [newIdMonster,stock,price]
                    dataMonsterShop.append(newMonsterShop)
                    print(f'{dataMonster[int(newIdMonster)][1]} telah berhasil ditambahkan ke dalam shop!')


                # Menambah potion yang akan di jual
                elif option == 'potion':
                    # Menampilkan seluruh potion yang ada di database tetapi belum ada pada shop
                    potionNotInShop = getPotionNotInShop(dataPotion)
                    print(f"{'ID':<3} | {'Type':<20}")
                    for i in range(len(potionNotInShop)):
                        print(f"{len(dataItemShop)+i:<3} | {f'{potionNotInShop[i]} Potion':<20}")
                    # Validasi input id potion
                    while True:
                        newIdPotion = input('>>> Masukkan id potion: ')
                        if isNum(newIdPotion)==False:
                            print('Id Potion tidak valid!')
                        else:
                            if len(dataItemShop)<=int(newIdPotion)<=len(dataItemShop)+len(potionNotInShop)-1:
                                break
                            else:
                                print('Id Potion tidak valid!')
                    # Validasi stok awal
                    while True:
                        stock = input('>>> Masukkan stok awal: ')
                        if isNum(stock) == True:
                            break
                        else:
                            print('Stok tidak valid')
                    # Validasi harga
                    while True:
                        price = input('>>> Masukkan harga: ')
                        if isNum(price) == True:
                            break
                        else:
                            print('Harga tidak valid')

                    # Tambah data baru ke dataItemShop
                    newItemShop = [potionNotInShop[int(newIdPotion)-len(dataItemShop)],stock,price]
                    dataItemShop.append(newItemShop)
                    print(f'{potionNotInShop[int(newIdPotion)-len(dataItemShop)]} Potion telah berhasil ditambahkan ke dalam shop!')
                else:
                    print('Input tidak valid!')

        elif action == 'ubah':
            option = ''
            while option!='monster' and option!='potion':
                option = input('>>> Mau ubah apa? (monster/potion): ')
                if option == 'monster':
                    # Menampilkan seluruh monster yang ada di shop
                    displayMonsterShop(dataMonsterShop,dataMonster)
                    # Validasi input id monster
                    while True:
                        updateIdMonster = input('>>> Masukkan id monster: ')
                        isValid = False
                        for monster in dataMonsterShop:
                            if monster[0] == updateIdMonster:
                                isValid = True
                                break
                        if isValid == True:
                            break
                        else:
                            print('Id Monster tidak valid!')
                    # Validasi stok baru
                    while True:
                        stock = input('>>> Masukkan stok baru: ')
                        if isNum(stock) == True or not stock:
                            break
                        else:
                            print('Stok tidak valid')
                    # Validasi harga baru
                    while True:
                        price = input('>>> Masukkan harga baru: ')
                        if isNum(price) == True or not price:
                            break
                        else:
                            print('Harga tidak valid')

                    # Menyimpan data yang ingin diupdate ke dalam list sementara
                    changeDataMonster = [updateIdMonster,stock,price]
                    updateDataMonster.append(changeDataMonster)

                    for i in range(len(dataMonster)):
                        if dataMonster[i][0] == updateIdMonster:
                            nameMonster = dataMonster[i][1]

                    if not stock and not price:
                        print(f'Tidak ada data {nameMonster} yang diubah.')
                    elif not stock:
                        print(f'{nameMonster} telah berhasil diubah dengan harga baru {price}')
                    elif not price:
                        print(f'{nameMonster} telah berhasil diubah dengan stok baru sejumlah {stock}')
                    else:
                        print(f'{nameMonster} telah berhasil diubah dengan stok baru sejumlah {stock} dan dengan harga baru {price}')

                elif option == 'potion':
                    # Menampilkan seluruh potion yang ada di shop 
                    displayPotionShop(dataItemShop)
                    # Validasi input id potion
                    while True:
                        updateIdPotion = input('>>> Masukkan id potion: ')
                        if isNum(updateIdPotion)==False:
                            print('Id Potion tidak valid!')
                        else:
                            if 1<=int(updateIdPotion)<=len(dataItemShop)-1:
                                break
                            else:
                                print('Id Potion tidak valid!')
                    # Validasi stok baru
                    while True:
                        stock = input('>>> Masukkan stok baru: ')
                        if isNum(stock) == True or not stock:
                            break
                        else:
                            print('Stok tidak valid')
                    # Validasi harga baru
                    while True:
                        price = input('>>> Masukkan harga baru: ')
                        if isNum(price) == True or not price:
                            break
                        else:
                            print('Harga tidak valid')
                    # Ubah data ke item_shop.csv
                    namePotion = dataItemShop[int(updateIdPotion)][0]
                    changeDataItem = [namePotion,stock,price]
                    updateDataItem.append(changeDataItem)

                    if not stock and not price:
                        print(f'Tidak ada data {namePotion} Potion yang diubah.')
                    elif not stock:
                        print(f'{namePotion} Potion telah berhasil diubah dengan harga baru {price}')
                    elif not price:
                        print(f'{namePotion} Potion telah berhasil diubah dengan stok baru sejumlah {stock}')
                    else:
                        print(f'{namePotion} Potion telah berhasil diubah dengan stok baru sejumlah {stock} dan dengan harga baru {price}')
                else:
                    print('Input tidak valid!')
            
        elif action == 'hapus':
            option = ''
            while option!='monster' and option!='potion':
                option = input('>>> Mau hapus apa? (monster/potion): ')
                if option == 'monster':
                    # Menampilkan seluruh monster yang ada di shop
                    displayMonsterShop(dataMonsterShop,dataMonster)
                    # Validasi input id monster
                    while True:
                        delIdMonster = input('>>> Masukkan id monster: ')
                        isValid = False
                        for monster in dataMonsterShop:
                            if monster[0] == delIdMonster:
                                isValid = True
                                break
                        if isValid == True:
                            break
                        else:
                            print('Id Monster tidak valid!')
                    for i in range(len(dataMonster)):
                        if dataMonster[i][0] == delIdMonster:
                            nameMonster = dataMonster[i][1]
                    # Validasi y/n delete
                    while True:
                        delete = input(f'>>> Apakah anda yakin ingin menghapus {nameMonster} dari shop (y/n)? ')
                        if delete == 'y':
                            # Menambahkan id monster yang dihapus ke deleteDataMonster
                            deleteDataMonster.append(delIdMonster)
                            print(f'{nameMonster} telah berhasil dihapus dari shop!')
                            break
                        elif delete == 'n':
                            print(f'{nameMonster} tidak jadi Anda hapus.')
                            break
                        else:
                            print('Input tidak valid!')

                elif option == 'potion':
                    # Menampilkan seluruh potion yang ada di shop 
                    displayPotionShop(dataItemShop)
                    # Validasi input id potion
                    while True:
                        delIdPotion = input('>>> Masukkan id potion: ')
                        if isNum(delIdPotion)==False:
                            print('Id Potion tidak valid!')
                        else:
                            if 1<=int(delIdPotion)<=len(dataItemShop)-1:
                                break
                            else:
                                print('Id Potion tidak valid!')
                    # Validasi y/n delete
                    namePotion = dataItemShop[int(delIdPotion)][0]
                    while True:
                        delete = input(f'>>> Apakah anda yakin ingin menghapus {namePotion} Potion dari shop (y/n)? ')
                        if delete == 'y':
                            print(f'{namePotion} Potion telah berhasil dihapus dari shop!')
                            # Menambahkan id monster yang dihapus ke deleteDataItem
                            deleteDataItem.append(namePotion)
                            break
                        elif delete == 'n':
                            print(f'{namePotion} Potion tidak jadi Anda hapus.')
                            break
                        else:
                            print('Input tidak valid!')
                else:
                    print('Input tidak valid!')
        else:
            print('Aksi tidak valid!')

        action = input('>>> Pilih aksi (lihat/tambah/ubah/hapus/keluar): ')
    
    print('Dadahh!')

    # TES
    print(f'Add Monster:\n{dataMonsterShop}')
    print(f'Add Potion:\n{dataItemShop}')
    print(f'Update Monster:\n{updateDataMonster}')
    print(f'Update Item:\n{updateDataItem}')
    print(f'Delete Monster:\n{deleteDataMonster}')
    print(f'Delete Item:\n{deleteDataItem}')

shopManagement(dataItemShop,dataMonsterShop,dataMonster)