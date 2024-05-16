from Important_Function import *

# READ CSV FILE
dataMonster = readCSV('data/monster.csv')

def isNum(x:str) -> bool:
    if not x: # Kasus string kosong
        return False
    for char in x:
        if ord(char)<48 or ord(char)>57:
            return False
    return True

def maxIDMonster(dataMonster:list) -> int:
    maxID:int = 0
    for monster in dataMonster[1:]:
        if int(monster[0])>maxID:
            maxID = int(monster[0])
    return maxID

def foundMonster(dataMonster:list, newMonster:str) -> bool:
    for monster in dataMonster:
        if monster[1] == newMonster:
            return True
    return False

def displayMonster(dataMonster:list):
    if len(dataMonster)-1>0:
        print(f"{'ID':<3} | {'Type':<15} | {'ATK Power':<9} | {'DEF Power':<9} | HP")
        for i in range(1,len(dataMonster)):
            print(f"{dataMonster[i][0]:<3} | {dataMonster[i][1]:<15} | {dataMonster[i][2]:<9} | {dataMonster[i][3]:<9} | {dataMonster[i][4]}")
    else:
        print('Tidak ada data yang dapat ditampilkan...')

def addMonster(dataMonster:list):
    print('Memulai pembuatan monster baru\n')

    # Validasi input monster type
    while True:
        newType:str = input('>>> Masukkan Type / Nama : ').title()
        if isNum(newType) == True:
            print('Nama harus string, coba lagi!')
        elif foundMonster(dataMonster, newType) == False:
            break
        else:
            print('Nama sudah terdaftar, coba lagi!')
    
    # Validasi ATK Power
    while True:
        newATKPower:str = input('>>> Masukkan ATK Power : ')
        if isNum(newATKPower) == True:
            break
        else:
            print('Masukkan input bertipe Integer, coba lagi!')

    # Validasi DEF Power
    while True:
        newDEFPower:str = input('>>> Masukkan DEF Power (0-50) : ')
        if isNum(newDEFPower) == True:
            if 0<=int(newDEFPower)<=50:
                break
            else:
                print('DEF Power harus bernilai 0-50, coba lagi!')
        else:
            print('Masukkan input bertipe Integer, coba lagi!')
    
    # Validasi HP
    while True:
        newHP:str = input('>>> Masukkan HP : ')
        if isNum(newHP) == True:
            break
        else:
            print('Masukkan input bertipe Integer, coba lagi!')

    # Menampilkan Data Monster Baru
    print('Monster baru berhasil dibuat!')
    print(f'Type\t\t: {newType}')
    print(f'ATK Power\t: {newATKPower}')
    print(f'DEF Power\t: {newDEFPower}')
    print(f'HP\t\t: {newHP}')

    # Konfirmasi tambah data ke dalam database
    while True:
        confirm:str = input('>>> Tambahkan Monster ke database (Y/N) : ').upper()
        if confirm == 'Y':
            newMonster:list = [maxIDMonster(dataMonster)+1,newType,newATKPower,newDEFPower,newHP]
            dataMonster.append(newMonster)
            print('Monster baru telah ditambahkan!')
            break
        elif confirm =='N':
            print('Monster gagal ditambahkan!')
            break
        else:
            print('Konfirmasi tidak valid!')

# F13 - Monster Management
def monsterManagement(dataMonster:list):
    print('SELAMAT DATANG DI DATABASE PARA MONSTER !!!')
    print('1. Tampilkan semua Monster')
    print('2. Tambah Monster baru')
    print('3. Keluar')

    while True:
        action:str = input('>>> Pilih Aksi (1/2/3): ')
        if action == '1':
            displayMonster(dataMonster)
        elif action == '2':
            addMonster(dataMonster)
        elif action == '3':
            print('Dadahhhh!')
            break
        else:
            print('Aksi tidak valid!')

monsterManagement(dataMonster)