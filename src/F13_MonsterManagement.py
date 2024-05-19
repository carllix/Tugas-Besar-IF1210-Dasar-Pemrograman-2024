from src.Important_Function import *

def foundMonster(dataMonster:list, newMonster:str) -> bool:
    for monster in dataMonster:
        if monster[1] == newMonster:
            return True
    return False

def displayMonster(dataMonster:list):
    if len(dataMonster)-1>0:
        print(f"\n{'ID':<3} | {'Type':<15} | {'ATK Power':<9} | {'DEF Power':<9} | {'HP':<8} |")
        for i in range(1,len(dataMonster)):
            print(f"{dataMonster[i][0]:<3} | {dataMonster[i][1]:<15} | {dataMonster[i][2]:<9} | {dataMonster[i][3]:<9} | {dataMonster[i][4]:<8} |")
    else:
        print('\nTidak ada data yang dapat ditampilkan...')

def addMonster(dataMonster:list):
    print('\nMemulai pembuatan monster baru')

    # Validasi input monster type
    while True:
        newType:str = input('\n>>> Masukkan Type / Nama : ').title()
        if isNum(newType) == True:
            print('Nama harus string, coba lagi!')
        elif foundMonster(dataMonster, newType) == False:
            break
        else:
            print('Nama sudah terdaftar, coba lagi!')
    
    # Validasi ATK Power
    while True:
        newATKPower:str = input('\n>>> Masukkan ATK Power : ')
        if isNum(newATKPower) == True:
            break
        else:
            print('Masukkan input bertipe Integer, coba lagi!')

    # Validasi DEF Power
    while True:
        newDEFPower:str = input('\n>>> Masukkan DEF Power (0-50) : ')
        if isNum(newDEFPower) == True:
            if 0<=int(newDEFPower)<=50:
                break
            else:
                print('DEF Power harus bernilai 0-50, coba lagi!')
        else:
            print('Masukkan input bertipe Integer, coba lagi!')
    
    # Validasi HP
    while True:
        newHP:str = input('\n>>> Masukkan HP : ')
        if isNum(newHP) == True:
            break
        else:
            print('Masukkan input bertipe Integer, coba lagi!')

    # Menampilkan Data Monster Baru
    print('\nMonster baru berhasil dibuat!')
    print(f'Type\t\t: {newType}')
    print(f'ATK Power\t: {newATKPower}')
    print(f'DEF Power\t: {newDEFPower}')
    print(f'HP\t\t: {newHP}')

    # Konfirmasi tambah data ke dalam database
    while True:
        confirm:str = input('\n>>> Tambahkan Monster ke database (Y/N) : ').upper()
        if confirm == 'Y':
            newMonster:list = [str(newId(dataMonster)),newType,newATKPower,newDEFPower,newHP]
            dataMonster.append(newMonster)
            print('\nMonster baru telah ditambahkan!')
            break
        elif confirm =='N':
            print('\nMonster gagal ditambahkan!')
            break
        else:
            print('\nKonfirmasi tidak valid!')

# F13 - MONSTER MANAGEMENT
def monsterManagement(dataMonster:list,username:str):
    print('\n=================================================================================================================')
    print('''
░█▀▄▀█ ░█▀▀▀█ ░█▄─░█ ░█▀▀▀█ ▀▀█▀▀ ░█▀▀▀ ░█▀▀█ 　 ░█▀▄▀█ ─█▀▀█ ░█▄─░█ ─█▀▀█ ░█▀▀█ ░█▀▀▀ ░█▀▄▀█ ░█▀▀▀ ░█▄─░█ ▀▀█▀▀ 
░█░█░█ ░█──░█ ░█░█░█ ─▀▀▀▄▄ ─░█── ░█▀▀▀ ░█▄▄▀ 　 ░█░█░█ ░█▄▄█ ░█░█░█ ░█▄▄█ ░█─▄▄ ░█▀▀▀ ░█░█░█ ░█▀▀▀ ░█░█░█ ─░█── 
░█──░█ ░█▄▄▄█ ░█──▀█ ░█▄▄▄█ ─░█── ░█▄▄▄ ░█─░█ 　 ░█──░█ ░█─░█ ░█──▀█ ░█─░█ ░█▄▄█ ░█▄▄▄ ░█──░█ ░█▄▄▄ ░█──▀█ ─░█──''')
    print('\n=================================================================================================================')
    print(f'\nSELAMAT DATANG DI DATABASE PARA MONSTER {username} !!!')
    print('\n1. Tampilkan Semua Monster')
    print('2. Tambah Monster baru')
    print('3. Keluar')

    while True:
        action:str = input('\n>>> Pilih Aksi (1/2/3): ')
        if action == '1':
            displayMonster(dataMonster)
        elif action == '2':
            addMonster(dataMonster)
        elif action == '3':
            print(f'\nSampai Jumpa Lagi {username} !!!')
            break
        else:
            print('Aksi tidak valid!')