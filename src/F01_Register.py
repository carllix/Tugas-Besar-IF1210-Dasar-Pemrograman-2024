from src.Important_Function import *

# Validasi Username
def username_valid(username:str)->bool:
    for char in username:
        if not(97<=ord(char)<=122 or 65<=ord(char)<=90 or 48<=ord(char)<=57 or ord(char)==95 or ord(char)==45):
            return False
    return True

# Validasi Keunikan Username
def username_unik(username:str,dataUser:list)->bool:
    for user in dataUser:
        if user[1] == username:
            return False
    return True

# Validasi Id Monster
def isIdExist(monster_pilihan:str,dataMonster:list)->bool:
    for monster in dataMonster:
        if monster[0] == monster_pilihan:
            return True
    return False

# F01 - REGISTER
def register(dataUser:list,isLogin:bool,username:str,dataMonster:list,dataMonsterInventory:list):
    if isLogin==True:
        print('\nRegister gagal')
        print(f'Anda telah login dengan username {username} silakan lakukan "LOGOUT" sebelum melakukan register.\n')
    else:
        print('\n============================================================================================================')
        print('''
                            ░█▀▀█ ░█▀▀▀ ░█▀▀█ ▀█▀ ░█▀▀▀█ ▀▀█▀▀ ░█▀▀▀ ░█▀▀█ 
                            ░█▄▄▀ ░█▀▀▀ ░█─▄▄ ░█─ ─▀▀▀▄▄ ─░█── ░█▀▀▀ ░█▄▄▀ 
                            ░█─░█ ░█▄▄▄ ░█▄▄█ ▄█▄ ░█▄▄▄█ ─░█── ░█▄▄▄ ░█─░█''')
        print('\n============================================================================================================')
        # Validasi Username dan Password
        while True:
            # Input Username & Password
            username:str = input('\nMasukan Username: ')
            password:str = input('Masukan Password: ')

            if not username:
                print('\nUsername tidak boleh kosong!\n')
            elif not password:
                print('\nPassword tidak boleh kosong!\n')
            elif username_valid(username) == False:
                print('\nUsername hanya boleh berisi alfabet, angka, underscore, dan strip!\n')
            elif username_unik(username,dataUser) == False:
                print(f'\nUsername {username} sudah terpakai, silakan gunakan username lain!\n')
            else:
                break
        
        # Pilih Monster
        print('\nSilakan pilih salah satu monster sebagai monster awalmu!')
        # Menampilkan List Monster
        for monster in dataMonster[1:]:
            print(f'{monster[0]}. {monster[1]}')

        # Validasi Input pilihan monster
        while True:
            monster_pilihan = input('\nMonster pilihanmu: ')
            if isIdExist(monster_pilihan,dataMonster) == True:
                
                # Menambahkan data user baru
                userId:int = newId(dataUser)
                newUser:list = [str(userId),username,password,'agent','0']
                dataUser.append(newUser)

                # Menambahkan data monster inventory user
                dataMonsterInventory.append([str(userId),monster_pilihan,'1'])
                
                print(f'\nSelamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {getDataById(monster_pilihan,dataMonster)[1]}!')
                break
            else:
                print('Pilihan Tidak Valid')