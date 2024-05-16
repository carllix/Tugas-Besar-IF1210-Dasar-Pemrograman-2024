# from . import F04_Help
# from src import F01,F02,F03
# from src import Important_Function

# # LOAD DATA
# dataUser, dataMonster, dataMonsterInventory, dataItemInventory, dataMonsterShop, dataItemShop = Important_Function.load()
# isLogin = False
# username = ''
# userId = 0
# coin = 0
# role = ''

# # if dataUser and dataMonster and dataMonsterInventory and dataItemInventory and dataMonsterShop and dataItemShop:

# print('''
# ██████████████████████████████████████████████████████████████████████████████████████████████████████████
# █▄─█▀▀▀█─▄█▄─▄▄─█▄─▄███─▄▄▄─█─▄▄─█▄─▀█▀─▄█▄─▄▄─███─▄─▄─█─▄▄─███─▄▄─█████▄─█▀▀▀█─▄█████─▄▄▄─██████▀▄─██████
# ██─█─█─█─███─▄█▀██─██▀█─███▀█─██─██─█▄█─███─▄█▀█████─███─██─███─██─█░░███─█─█─█─██░░██─███▀█░░███─▀─██░░██
# ▀▀▄▄▄▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▀▀▀▄▄▄▀▀▄▄▄▄▀▀▀▄▄▄▄▀▄▄▀▀▀▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▄▄▀▄▄▀▀▄▄▀▄▄▀▄▄▀▀''')
# print('===========================================================================================================')
# print('Masukkan Command')
# command = input('>>> ').upper
# if command == 'REGISTER':
#     F01.register(dataUser,isLogin,username)
# elif command == 'LOGIN':
#     F02.login(isLogin,dataUser,userId,username,coin,role)
# elif command == 'LOGOUT':
#     F03.logout(isLogin,userId,username,coin,role)
# elif command == 'HELP':
#     F04_Help.help(isLogin, role, username)
# elif command == '':