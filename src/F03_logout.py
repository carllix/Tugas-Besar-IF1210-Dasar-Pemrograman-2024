# F03 - LOGOUT
def logout(isLogin:bool,userId:int,username:str,coin:int,role:str):
    # Periksa Apakah Pengguna Sudah Login
    if isLogin == True:
        print(f'\nAnda Berhasil Logout dari Akun dengan username {username}.\n')
        isLogin:bool = False
        userId:int = 0
        username:str = ''
        coin:int = 0
        role:str = ''
        return isLogin,userId,username,coin,role
    else:
        print('\nLogout gagal!')
        print('Anda belum login, silahkan lakukan "LOGIN" terlebih dahulu sebelum melakukan logout.\n')
        return isLogin,userId,username,coin,role