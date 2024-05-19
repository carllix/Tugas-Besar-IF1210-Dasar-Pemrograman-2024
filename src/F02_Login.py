# Get Data User By Username
def getDataByUsername(newUsername:str,dataUser:list) -> list:
    for user in dataUser:
        if user[1] == newUsername:
            return user
        
# Cek Keberadaan Username Pada Database
def isUsernameExist(newUsername:str,dataUser:list) -> bool:
    for user in dataUser:
        if user[1] == newUsername:
            return True
    return False

# Cek Apakah Password Sesuai Dengan Database
def isValidPassword(newUsername:str,password:str,dataUser:list) -> bool:
    for user in dataUser:
        if user[1] == newUsername:
            if user[2] == password:
                return True
            else:
                return False
                
# F02 - LOGIN
def login(isLogin:bool,dataUser:list,userId:int,username:str,coin:int,role:str):
    if isLogin == False:
        print('\n============================================================================================================')
        print('''
                                    ░█─── ░█▀▀▀█ ░█▀▀█ ▀█▀ ░█▄─░█ 
                                    ░█─── ░█──░█ ░█─▄▄ ░█─ ░█░█░█ 
                                    ░█▄▄█ ░█▄▄▄█ ░█▄▄█ ▄█▄ ░█──▀█''')
        print('\n============================================================================================================')

        # Validasi Username dan Password
        while True:
            newUsername:str = input("\nUsername: ")
            password:str = input("Password: ")

            if isUsernameExist(newUsername,dataUser) == False:
                print('\nUsername tidak terdaftar!')
            else:
                if isValidPassword(newUsername,password,dataUser) == False:
                    print('\nPassword salah!')
                else:
                    isLogin:bool = True
                    userNow:list = getDataByUsername(newUsername,dataUser)
                    userId:int = int(userNow[0])
                    username:str = userNow[1]
                    role:str = userNow[3]
                    coin:int = int(userNow[4])

                    print(f'\nSelamat datang kembali, {role.capitalize()} {username}. Mari lanjutkan petualangan kita!')
                    print('Masukkan command "HELP" untuk daftar command yang dapat kamu panggil.')
                    return isLogin,userId,username,coin,role
    else:
        print('\nLogin gagal!')
        print(f'Anda telah login dengan username {username}, silahkan lakukan "LOGOUT" sebelum melakukan login kembali.')
    return isLogin,userId,username,coin,role