from src.F01_Register import *
from src.F02_Login import *
from src.F03_logout import *
from src.F04_Help import *
from src.F07_Inventory import *
from src.F08_Battle import *
from src.F09_Arena import *
from src.F10_Shop import *
from src.F11_Laboratory import *
from src.F12_ShopManagement import *
from src.F13_MonsterManagement import *
from src.F14_Load import *
from src.F15_Save import *
from src.F16_Exit import *


# LOAD DATA
dataUser, dataMonster, dataMonsterInventory, dataItemInventory, dataMonsterShop, dataItemShop = main_load()

# Inisialisasi variabel
dataPotion:list = ['strength','resilience','healing']
isLogin:bool = False
username:str = ''
userId:int = 0
coin:int = 0
role:str = ''

print('\n===========================================================================================================')
print('''
    ░█──░█ ░█▀▀▀ ░█─── ░█▀▀█ ░█▀▀▀█ ░█▀▄▀█ ░█▀▀▀ 　 ▀▀█▀▀ ░█▀▀▀█ 　 ░█▀▀▀█ ─ ░█──░█ ─ ░█▀▀█ ─ ─█▀▀█ 　 █ 
    ░█░█░█ ░█▀▀▀ ░█─── ░█─── ░█──░█ ░█░█░█ ░█▀▀▀ 　 ─░█── ░█──░█ 　 ░█──░█ ▄ ░█░█░█ ▄ ░█─── ▄ ░█▄▄█ 　 ▀ 
    ░█▄▀▄█ ░█▄▄▄ ░█▄▄█ ░█▄▄█ ░█▄▄▄█ ░█──░█ ░█▄▄▄ 　 ─░█── ░█▄▄▄█ 　 ░█▄▄▄█ █ ░█▄▀▄█ █ ░█▄▄█ █ ░█─░█ 　 ▄''')
print('\n===========================================================================================================')
while True:
    print('\nMasukkan Command : ')
    command = input('>>> ').upper()
    if command == 'REGISTER':
        register(dataUser,isLogin,username,dataMonster,dataMonsterInventory)
    elif command == 'LOGIN':
        isLogin,userId,username,coin,role = login(isLogin,dataUser,userId,username,coin,role)
    elif command == 'LOGOUT':
        isLogin,userId,username,coin,role = logout(isLogin,userId,username,coin,role)
    elif command == 'HELP':
        help(isLogin, role, username)
    elif command == 'INVENTORY':
        if isLogin == True:
            if role == 'admin':
                print('\nAnda bukanlah Agent. Silahkan login sebagai Agent untuk menjalankan command INVENTORY !')
            else:
                inventory(dataMonster,dataItemInventory,dataMonsterInventory,userId,coin,username)
        else:
            print('\nAnda harus login terlebih dahulu untuk menjalankan command INVENTORY !')
    elif command == 'BATTLE':
        if isLogin == True:
            if role == 'admin':
                print('\nAnda bukanlah Agent. Silahkan login sebagai Agent untuk menjalankan command BATTLE !')
            else:
                coin = battle(userId,username,dataMonster,dataMonsterInventory,dataItemInventory,coin)
        else:
            print('\nAnda harus login terlebih dahulu untuk menjalankan command BATTLE !')
    elif command == 'ARENA':
        if isLogin == True:
            if role == 'admin':
                print('\nAnda bukanlah Agent. Silahkan login sebagai Agent untuk menjalankan command ARENA !')
            else:
                coin = arena(userId,username,dataMonster,dataMonsterInventory,dataItemInventory,coin)
        else:
            print('\nAnda harus login terlebih dahulu untuk menjalankan command ARENA !')
    elif command == 'SHOP':
        if isLogin == True:
            if role == 'admin':
                shopManagement(dataPotion,dataItemShop,dataMonsterShop,dataMonster,username)
            else:
                shop(dataMonster,dataMonsterShop,dataItemShop,dataMonsterInventory,dataItemInventory,coin,userId)
        else:
            print('\nAnda harus login terlebih dahulu untuk menjalankan command SHOP !')
    elif command == 'LABORATORY':
        if isLogin == True:
            if role == 'admin':
                print('\nAnda bukanlah Agent. Silahkan login sebagai Agent untuk menjalankan command LABORATORY !')
            else:
                coin = laboratory(dataMonsterInventory,dataMonster,userId,coin)
        else:
            print('\nAnda harus login terlebih dahulu untuk menjalankan command LABORATORY !')
    elif command == 'MONSTER':
        if isLogin == True:
            if role == 'admin':
                monsterManagement(dataMonster,username)
            else:
                print('\nAnda bukanlah Admin. Silahkan login sebagai Admin untuk menjalankan command MONSTER !')
        else:
            print('\nAnda harus login terlebih dahulu untuk menjalankan command LABORATORY !')
    elif command == 'SAVE':
        save(dataUser,dataMonster,dataMonsterInventory, dataItemInventory, dataMonsterShop, dataItemShop)
    elif command == 'EXIT':
        exit(dataUser, dataMonster, dataMonsterInventory, dataItemInventory, dataMonsterShop, dataItemShop)
    else:
        print('Command tidak valid. Silahkan masukkan command "HELP" untuk daftar command yang dapat kamu panggil.')
    
    # Ubah coin user pada dataUser
    for data in dataUser:
        if data[0] == str(userId):
            data[4] = coin