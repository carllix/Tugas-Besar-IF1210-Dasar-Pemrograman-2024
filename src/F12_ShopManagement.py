from Important_Function import *

dataItemShop = readCSV('data/item_shop.csv')
dataMonsterShop = readCSV('data/monster_shop.csv')
dataMonster = readCSV('data/monster.csv')
dataPotion = ['strength','resilience','healing']

# Mendapatkan data monster yang tidak terdapat di shop
def getMonsterNotInShop(dataMonsterShop:list,dataMonster:list) -> list:
    monsterNotInShop:list = []
    for i in range(1,len(dataMonster)):
        isFound:bool = False
        for j in range(1,len(dataMonsterShop)):
            if dataMonster[i][0] == dataMonsterShop[j][0]:
                isFound = True
                break
        # Jika tidak ditemukan id monster pada monster_shop, maka akan ditambahkan ke dalam list monsterNotInShop
        if isFound == False:
            monsterNotInShop.append(dataMonster[i])
    return monsterNotInShop

# Mendapatkan data potion yang tidak terdapat di shop
def getPotionNotInShop(dataItemShop:list,dataPotion:list) -> list:
    potionNotInShop:list = []
    for i in range(len(dataPotion)):
        isFound:bool = False
        for j in range(1,len(dataItemShop)):
            if dataPotion[i] == dataItemShop[j][0]:
                isFound = True
                break
         # Jika tidak ditemukan potion pada item_shop, maka akan ditambahkan ke dalam list potionNotInShop
        if isFound == False:
            potionNotInShop.append(dataPotion[i])
    return potionNotInShop

# Menampilkan monster yang terdaftar di Shop
def displayMonsterShop(dataMonsterShop:list,dataMonster:list):
    if len(dataMonsterShop)-1>0:
        print(f"{'ID':<3} | {'Type':<15} | {'ATK Power':<9} | {'DEF Power':<9} | {'HP':<5} | {'Stok':<5} | Harga")
        for monster in dataMonsterShop[1:]:
            idMonster:str = monster[0]
            infoMonster:list = getDataById(idMonster,dataMonster)
            print(f"{infoMonster[0]:<3} | {infoMonster[1]:<15} | {infoMonster[2]:<9} | {infoMonster[3]:<9} | {infoMonster[4]:<5} | {monster[1]:<5} | {monster[2]}")
    else:
        print('Tidak ada data monster pada shop...')

# Menampilkan potion yang terdaftar di Shop
def displayPotionShop(dataItemShop:list):
    if len(dataItemShop)-1>0:
        print(f"{'ID':<3} | {'Type':<20} | {'Stok':<5} | Harga")
        i = 1
        for potion in dataItemShop[1:]:
            print(f"{i:<3} | {f'{potion[0].capitalize()} Potion':<20} | {potion[1]:<5} | {potion[2]}")
            i+=1
    else:
        print('Tidak ada data potion pada shop...')

# F12 - SHOP MANAGEMENT
def shopManagement(dataItemShop:list,dataMonsterShop:list,dataMonster:list):
    print('Welkamm!\n')

    while True:
        action:str = input('>>> Pilih aksi (lihat/tambah/ubah/hapus/keluar): ').lower()
        if action == 'lihat':
            while True:
                option:str = input('>>> Mau lihat apa? (monster/potion): ').lower()
                if option == 'monster': # Melihat monster yang terdaftar di Shop
                    displayMonsterShop(dataMonsterShop,dataMonster)
                    break
                elif option == 'potion': # Melihat potion yang terdaftar di Shop
                    displayPotionShop(dataItemShop)
                    break
                else:
                    print('Input tidak valid!')

        elif action == 'tambah':
            while True:
                option:str = input('>>> Mau nambahin apa? (monster/potion): ').lower()

                # Menambah monster yang akan di jual
                if option == 'monster':
                    # Menampilkan seluruh monster yang ada di database tetapi belum ada pada shop
                    monsterNotInShop:list = getMonsterNotInShop(dataMonsterShop,dataMonster)
                    if len(monsterNotInShop)-1>=0:
                        print(f"{'ID':<3} | {'Type':<15} | {'ATK Power':<9} | {'DEF Power':<9} | {'HP':<5}")
                        for i in range(len(monsterNotInShop)):
                            print(f"{monsterNotInShop[i][0]:<3} | {monsterNotInShop[i][1]:<15} | {monsterNotInShop[i][2]:<9} | {monsterNotInShop[i][3]:<9} | {monsterNotInShop[i][4]:<5}")
                        # Validasi input id monster
                        while True:
                            newIdMonster:str = input('>>> Masukkan id monster: ')
                            isValid:bool = False
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
                            stock:str = input('>>> Masukkan stok awal: ')
                            if isNum(stock) == True:
                                break
                            else:
                                print('Stok tidak valid')
                        # Validasi harga
                        while True:
                            price:str = input('>>> Masukkan harga: ')
                            if isNum(price) == True:
                                break
                            else:
                                print('Harga tidak valid')
                        # Tambah data baru ke dataMonsterShop
                        newMonsterShop:list = [newIdMonster,stock,price]
                        dataMonsterShop.append(newMonsterShop)
                        print(f'{dataMonster[int(newIdMonster)][1]} telah berhasil ditambahkan ke dalam shop!')
                    else:
                        print('Seluruh monster pada database telah ditambahkan pada shop...')
                    break

                # Menambah potion yang akan di jual
                elif option == 'potion':
                    # Menampilkan seluruh potion yang ada di database tetapi belum ada pada shop
                    potionNotInShop:list = getPotionNotInShop(dataItemShop,dataPotion)
                    if len(potionNotInShop)-1>=0:
                        print(f"{'ID':<3} | {'Type':<20}")
                        for i in range(len(potionNotInShop)):
                            print(f"{len(dataItemShop)+i:<3} | {f'{potionNotInShop[i].capitalize()} Potion':<20}")
                        # Validasi input id potion
                        while True:
                            newIdPotion:str = input('>>> Masukkan id potion: ')
                            if isNum(newIdPotion)==False:
                                print('Id Potion tidak valid!')
                            else:
                                if len(dataItemShop)<=int(newIdPotion)<=len(dataItemShop)+len(potionNotInShop)-1:
                                    break
                                else:
                                    print('Id Potion tidak valid!')
                        # Validasi stok awal
                        while True:
                            stock:str = input('>>> Masukkan stok awal: ')
                            if isNum(stock) == True:
                                break
                            else:
                                print('Stok tidak valid')
                        # Validasi harga
                        while True:
                            price:str = input('>>> Masukkan harga: ')
                            if isNum(price) == True:
                                break
                            else:
                                print('Harga tidak valid')
                        # Tambah data baru ke dataItemShop
                        newItemShop:list = [potionNotInShop[int(newIdPotion)-len(dataItemShop)],stock,price]
                        print(f'{potionNotInShop[int(newIdPotion)-len(dataItemShop)].capitalize()} Potion telah berhasil ditambahkan ke dalam shop!')
                        dataItemShop.append(newItemShop)
                    else:
                        print('Seluruh potion pada database telah ditambahkan pada shop...')
                    break
                else:
                    print('Input tidak valid!')

        elif action == 'ubah':
            while True:
                option:str = input('>>> Mau ubah apa? (monster/potion): ').lower()
                if option == 'monster':
                    # Menampilkan seluruh monster yang ada di shop
                    displayMonsterShop(dataMonsterShop,dataMonster)
                    
                    if len(dataMonsterShop)-1>0:
                        # Validasi input id monster
                        while True:
                            updateIdMonster = input('>>> Masukkan id monster: ')
                            isValid:bool = False
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
                            stock:str = input('>>> Masukkan stok baru: ')
                            if isNum(stock) == True or not stock:
                                break
                            else:
                                print('Stok tidak valid')
                        # Validasi harga baru
                        while True:
                            price:str = input('>>> Masukkan harga baru: ')
                            if isNum(price) == True or not price:
                                break
                            else:
                                print('Harga tidak valid')

                        # Update dataMonsterShop dengan data yang baru
                        dataMonsterShop:list = updateData(dataMonsterShop,updateIdMonster,[updateIdMonster,stock,price])

                        nameMonster:str = getDataById(updateIdMonster,dataMonster)[1]
                        if not stock and not price:
                            print(f'Tidak ada data {nameMonster} yang diubah.')
                        elif not stock:
                            print(f'{nameMonster} telah berhasil diubah dengan harga baru {price}')
                        elif not price:
                            print(f'{nameMonster} telah berhasil diubah dengan stok baru sejumlah {stock}')
                        else:
                            print(f'{nameMonster} telah berhasil diubah dengan stok baru sejumlah {stock} dan dengan harga baru {price}')
                    else:
                        print('Tidak ada data monster yang dapat diubah...')
                    break
                elif option == 'potion':
                    # Menampilkan seluruh potion yang ada di shop 
                    displayPotionShop(dataItemShop)

                    if len(dataItemShop)-1>0:
                        # Validasi input id potion
                        while True:
                            updateIdPotion:str = input('>>> Masukkan id potion: ')
                            if isNum(updateIdPotion)==False:
                                print('Id Potion tidak valid!')
                            else:
                                if 1<=int(updateIdPotion)<=len(dataItemShop)-1:
                                    break
                                else:
                                    print('Id Potion tidak valid!')
                        # Validasi stok baru
                        while True:
                            stock:str = input('>>> Masukkan stok baru: ')
                            if isNum(stock) == True or not stock:
                                break
                            else:
                                print('Stok tidak valid')
                        # Validasi harga baru
                        while True:
                            price:str = input('>>> Masukkan harga baru: ')
                            if isNum(price) == True or not price:
                                break
                            else:
                                print('Harga tidak valid')

                        # Update dataItemShop dengan data yang baru
                        namePotion:str = dataItemShop[int(updateIdPotion)][0]
                        dataItemShop:list = updateData(dataItemShop,namePotion,[namePotion,stock,price])
                        if not stock and not price:
                            print(f'Tidak ada data {namePotion.capitalize()} Potion yang diubah.')
                        elif not stock:
                            print(f'{namePotion.capitalize()} Potion telah berhasil diubah dengan harga baru {price}')
                        elif not price:
                            print(f'{namePotion.capitalize()} Potion telah berhasil diubah dengan stok baru sejumlah {stock}')
                        else:
                            print(f'{namePotion.capitalize()} Potion telah berhasil diubah dengan stok baru sejumlah {stock} dan dengan harga baru {price}')
                    else:
                        print('Tidak ada data potion yang dapat diubah...')
                    break
                else:
                    print('Input tidak valid!')
            
        elif action == 'hapus':
            while True:
                option:str = input('>>> Mau hapus apa? (monster/potion): ').lower()
                if option == 'monster':
                    # Menampilkan seluruh monster yang ada di shop
                    displayMonsterShop(dataMonsterShop,dataMonster)

                    if len(dataMonsterShop)-1>0:
                        # Validasi input id monster
                        while True:
                            delIdMonster:str = input('>>> Masukkan id monster: ')
                            isValid:bool = False
                            for monster in dataMonsterShop:
                                if monster[0] == delIdMonster:
                                    isValid = True
                                    break
                            if isValid == True:
                                break
                            else:
                                print('Id Monster tidak valid!')
                        nameMonster:str = getDataById(delIdMonster,dataMonster)[1]

                        # Validasi y/n delete
                        while True:
                            delete:str = input(f'>>> Apakah anda yakin ingin menghapus {nameMonster} dari shop (y/n)? ').lower()
                            if delete == 'y':
                                # Menghapus data monster pada shop yang memiliki delIdMonster
                                dataMonsterShop = deleteData(dataMonsterShop,delIdMonster)
                                print(f'{nameMonster} telah berhasil dihapus dari shop!')
                                break
                            elif delete == 'n':
                                print(f'{nameMonster} tidak jadi Anda hapus.')
                                break
                            else:
                                print('Input tidak valid!')
                    else:
                        print('Tidak ada data monster yang dapat dihapus...')
                    break
                elif option == 'potion':
                    # Menampilkan seluruh potion yang ada di shop 
                    displayPotionShop(dataItemShop)

                    if len(dataItemShop)-1>0:
                        # Validasi input id potion
                        while True:
                            delIdPotion:str = input('>>> Masukkan id potion: ')
                            if isNum(delIdPotion)==False:
                                print('Id Potion tidak valid!')
                            else:
                                if 1<=int(delIdPotion)<=len(dataItemShop)-1:
                                    break
                                else:
                                    print('Id Potion tidak valid!')
                        # Validasi y/n delete
                        delNamePotion:str = dataItemShop[int(delIdPotion)][0]
                        while True:
                            delete:str = input(f'>>> Apakah anda yakin ingin menghapus {delNamePotion.capitalize()} Potion dari shop (y/n)? ').lower()
                            if delete == 'y':
                                print(f'{delNamePotion.capitalize()} Potion telah berhasil dihapus dari shop!')

                                # Menghapus data potion pada shop yang memiliki delIdMonster
                                dataItemShop:list = deleteData(dataItemShop,delNamePotion)
                                break
                            elif delete == 'n':
                                print(f'{delNamePotion.capitalize()} Potion tidak jadi Anda hapus.')
                                break
                            else:
                                print('Input tidak valid!')
                    else:
                        print('Tidak ada data potion yang dapat dihapus...')
                    break
                else:
                    print('Input tidak valid!')
        elif action == 'keluar':
            print('Dadahh!')
            break
        else:
            print('Aksi tidak valid!')

shopManagement(dataItemShop,dataMonsterShop,dataMonster)