from Important_Function import *

# Get Data User By Username
def getDataByUsername(newUsername,dataUser):
    for user in dataUser:
        if user[1] == newUsername:
            return user
        
# Cek Keberadaan Username Pada Database
def isUsernameExist(newUsername,dataUser):
    for user in dataUser:
        if user[1] == newUsername:
            return True
    return False

# Cek Apakah Password Sesuai Dengan Database
def isValidPassword(newUsername,password,dataUser):
    for user in dataUser:
        if user[1] == newUsername:
            if user[2] == password:
                return True
            else:
                return False
                

# F02 - LOGIN
def login(isLogin,dataUser,userId,username,coin,role):
    if isLogin == False:
        print('===========================================================================================================')
        print('''
█░░ █▀█ █▀▀ █ █▄░█
█▄▄ █▄█ █▄█ █ █░▀█ ''')
        print('\n===========================================================================================================')

        # Validasi Username dan Password
        while True:
            newUsername = input("Username: ")
            password = input("Password: ")

            if isUsernameExist(newUsername,dataUser) == False:
                print('\nUsername tidak terdaftar!\n')
            else:
                if isValidPassword(newUsername,password,dataUser) == False:
                    print('\nPassword salah!\n')
                else:
                    isLogin = True
                    userNow = getDataByUsername(newUsername,dataUser)
                    userId = int(userNow[0])
                    username = userNow[1]
                    role = userNow[3]
                    coin = int(userNow[4])

                    print(f'\nSelamat datang kembali, {role.capitalize()} {username}. Mari lanjutkan petualangan kita!')
                    print('Masukkan command "help" untuk daftar command yang dapat kamu panggil.\n')
                    return isLogin,userId,username,coin,role
    else:
        print('Login gagal!')
        print(f'Anda telah login dengan username {username}, silahkan lakukan "LOGOUT" sebelum melakukan login kembali.\n')
    return isLogin,userId,username,coin,role